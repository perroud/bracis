#!/usr/bin/env python3
"""
Validate compliance framework YAML files against JSON Schema definitions.

Usage:
    python validate.py                    # Validate all frameworks
    python validate.py frameworks/lgpd    # Validate specific framework
    python validate.py --schema-only      # Validate schemas only
"""

import json
import sys
from pathlib import Path

try:
    import jsonschema
    from jsonschema import validate, ValidationError
except ImportError:
    print("ERROR: jsonschema not installed. Run: pip install jsonschema")
    sys.exit(1)

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed. Run: pip install pyyaml")
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = ROOT / "schema"
FRAMEWORKS_DIR = ROOT / "frameworks"
MAPPINGS_DIR = ROOT / "mappings"


def load_schema(schema_name: str) -> dict:
    schema_path = SCHEMA_DIR / f"{schema_name}.schema.json"
    if not schema_path.exists():
        raise FileNotFoundError(f"Schema not found: {schema_path}")
    with open(schema_path) as f:
        return json.load(f)


def load_yaml(path: Path) -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def validate_file(yaml_path: Path, schema: dict) -> list[str]:
    errors = []
    try:
        data = load_yaml(yaml_path)
        if data is None:
            errors.append(f"{yaml_path}: File is empty or invalid YAML")
            return errors
        validate(instance=data, schema=schema)
    except ValidationError as e:
        errors.append(f"{yaml_path}: {e.message} (at {'.'.join(str(p) for p in e.absolute_path)})")
    except yaml.YAMLError as e:
        errors.append(f"{yaml_path}: YAML parse error: {e}")
    except Exception as e:
        errors.append(f"{yaml_path}: Unexpected error: {e}")
    return errors


def validate_frameworks(target: Path | None = None) -> list[str]:
    framework_schema = load_schema("framework")
    control_schema = load_schema("control")
    errors = []

    if target and target.is_dir():
        framework_dirs = [target]
    else:
        framework_dirs = sorted(FRAMEWORKS_DIR.iterdir()) if FRAMEWORKS_DIR.exists() else []

    for fw_dir in framework_dirs:
        if not fw_dir.is_dir() or fw_dir.name.startswith("."):
            continue

        # Validate framework.yaml
        fw_yaml = fw_dir / "framework.yaml"
        if fw_yaml.exists():
            errors.extend(validate_file(fw_yaml, framework_schema))
        else:
            errors.append(f"{fw_dir}: Missing framework.yaml")

        # Validate controls
        controls_dir = fw_dir / "controls"
        if controls_dir.exists():
            for control_file in sorted(controls_dir.rglob("*.yaml")):
                if control_file.name.startswith("_"):
                    continue
                errors.extend(validate_file(control_file, control_schema))

        # Validate i18n framework.yaml
        i18n_dir = fw_dir / "i18n"
        if i18n_dir.exists():
            for lang_dir in sorted(i18n_dir.iterdir()):
                if not lang_dir.is_dir():
                    continue
                i18n_fw = lang_dir / "framework.yaml"
                if i18n_fw.exists():
                    errors.extend(validate_file(i18n_fw, framework_schema))
                i18n_controls = lang_dir / "controls"
                if i18n_controls.exists():
                    for control_file in sorted(i18n_controls.rglob("*.yaml")):
                        if control_file.name.startswith("_"):
                            continue
                        errors.extend(validate_file(control_file, control_schema))

    return errors


def validate_mappings() -> list[str]:
    mapping_schema = load_schema("mapping")
    errors = []

    if not MAPPINGS_DIR.exists():
        return errors

    for mapping_file in sorted(MAPPINGS_DIR.glob("*.yaml")):
        if mapping_file.name.startswith("_"):
            continue
        errors.extend(validate_file(mapping_file, mapping_schema))

    return errors


def check_translation_completeness() -> list[str]:
    warnings = []

    if not FRAMEWORKS_DIR.exists():
        return warnings

    for fw_dir in sorted(FRAMEWORKS_DIR.iterdir()):
        if not fw_dir.is_dir() or fw_dir.name.startswith("."):
            continue

        controls_dir = fw_dir / "controls"
        i18n_dir = fw_dir / "i18n"

        if not controls_dir.exists() or not i18n_dir.exists():
            continue

        original_controls = set(
            str(p.relative_to(controls_dir))
            for p in controls_dir.rglob("*.yaml")
            if not p.name.startswith("_")
        )

        for lang_dir in sorted(i18n_dir.iterdir()):
            if not lang_dir.is_dir():
                continue
            lang = lang_dir.name
            translated_controls_dir = lang_dir / "controls"
            if not translated_controls_dir.exists():
                warnings.append(f"{fw_dir.name}/{lang}: No controls/ directory in translation")
                continue

            translated = set(
                str(p.relative_to(translated_controls_dir))
                for p in translated_controls_dir.rglob("*.yaml")
                if not p.name.startswith("_")
            )

            missing = original_controls - translated
            if missing:
                pct = len(translated) / len(original_controls) * 100 if original_controls else 0
                warnings.append(
                    f"{fw_dir.name}/{lang}: {len(translated)}/{len(original_controls)} "
                    f"controls translated ({pct:.0f}%) — missing: {', '.join(sorted(missing)[:5])}"
                    + (f" (+{len(missing) - 5} more)" if len(missing) > 5 else "")
                )

    return warnings


def main():
    target = None
    schema_only = False

    if len(sys.argv) > 1:
        if sys.argv[1] == "--schema-only":
            schema_only = True
        else:
            target = Path(sys.argv[1])
            if not target.is_absolute():
                target = ROOT / target

    print("=" * 60)
    print("Compliance Framework Validator")
    print("=" * 60)

    # Validate schemas exist
    print("\n[1/4] Checking schemas...")
    schema_files = ["framework", "control", "mapping"]
    for s in schema_files:
        path = SCHEMA_DIR / f"{s}.schema.json"
        if path.exists():
            print(f"  OK  {path.name}")
        else:
            print(f"  MISSING  {path.name}")

    if schema_only:
        return 0

    # Validate frameworks
    print("\n[2/4] Validating frameworks...")
    fw_errors = validate_frameworks(target)
    if fw_errors:
        for e in fw_errors:
            print(f"  ERROR  {e}")
    else:
        print("  All frameworks valid.")

    # Validate mappings
    print("\n[3/4] Validating mappings...")
    map_errors = validate_mappings()
    if map_errors:
        for e in map_errors:
            print(f"  ERROR  {e}")
    else:
        print("  All mappings valid.")

    # Check translations
    print("\n[4/4] Checking translation completeness...")
    warnings = check_translation_completeness()
    if warnings:
        for w in warnings:
            print(f"  WARN  {w}")
    else:
        print("  All translations complete (or no translations found).")

    # Summary
    total_errors = len(fw_errors) + len(map_errors)
    print("\n" + "=" * 60)
    print(f"Results: {total_errors} errors, {len(warnings)} warnings")
    print("=" * 60)

    return 1 if total_errors > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
