#!/usr/bin/env python3
"""
Generate statistics about the compliance framework repository.
"""

import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed. Run: pip install pyyaml")
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent
FRAMEWORKS_DIR = ROOT / "frameworks"
MAPPINGS_DIR = ROOT / "mappings"
INDUSTRIES_DIR = ROOT / "industries"
REGIONS_DIR = ROOT / "regions"


def count_controls(fw_dir: Path) -> int:
    controls_dir = fw_dir / "controls"
    if not controls_dir.exists():
        return 0
    return len([
        p for p in controls_dir.rglob("*.yaml")
        if not p.name.startswith("_")
    ])


def count_translations(fw_dir: Path) -> dict:
    i18n_dir = fw_dir / "i18n"
    if not i18n_dir.exists():
        return {}
    result = {}
    for lang_dir in i18n_dir.iterdir():
        if not lang_dir.is_dir():
            continue
        controls = lang_dir / "controls"
        if controls.exists():
            result[lang_dir.name] = len([
                p for p in controls.rglob("*.yaml")
                if not p.name.startswith("_")
            ])
        else:
            result[lang_dir.name] = 0
    return result


def main():
    print("=" * 60)
    print("Compliance Framework Repository Statistics")
    print("=" * 60)

    if not FRAMEWORKS_DIR.exists():
        print("No frameworks directory found.")
        return

    frameworks = []
    total_controls = 0
    total_translations = 0
    types = {}
    regions_set = set()
    industries_set = set()

    for fw_dir in sorted(FRAMEWORKS_DIR.iterdir()):
        if not fw_dir.is_dir() or fw_dir.name.startswith("."):
            continue

        fw_yaml = fw_dir / "framework.yaml"
        if not fw_yaml.exists():
            continue

        try:
            with open(fw_yaml) as f:
                data = yaml.safe_load(f)
        except Exception:
            continue

        controls = count_controls(fw_dir)
        translations = count_translations(fw_dir)
        trans_total = sum(translations.values())

        total_controls += controls
        total_translations += trans_total

        fw_type = data.get("type", "unknown")
        types[fw_type] = types.get(fw_type, 0) + 1

        for r in data.get("regions", []):
            regions_set.add(r)
        for i in data.get("industries", []):
            industries_set.add(i)

        frameworks.append({
            "id": data.get("id", fw_dir.name),
            "title": data.get("short_title", data.get("title", "?")),
            "type": fw_type,
            "controls": controls,
            "translations": translations,
        })

    # Print summary
    print(f"\nFrameworks: {len(frameworks)}")
    print(f"Total controls: {total_controls}")
    print(f"Total translated controls: {total_translations}")
    print(f"Regions covered: {len(regions_set)}")
    print(f"Industries covered: {len(industries_set)}")

    print(f"\nBy type:")
    for t, count in sorted(types.items(), key=lambda x: -x[1]):
        print(f"  {t}: {count}")

    print(f"\nFrameworks detail:")
    print(f"  {'ID':<25} {'Type':<12} {'Controls':>8}  Translations")
    print(f"  {'-'*25} {'-'*12} {'-'*8}  {'-'*20}")
    for fw in frameworks:
        trans_str = ", ".join(f"{k}:{v}" for k, v in fw["translations"].items()) or "none"
        print(f"  {fw['id']:<25} {fw['type']:<12} {fw['controls']:>8}  {trans_str}")

    # Mappings
    mapping_count = 0
    if MAPPINGS_DIR.exists():
        mapping_count = len(list(MAPPINGS_DIR.glob("*.yaml")))
        print(f"\nCross-framework mappings: {mapping_count}")

    # Legal matrices
    legal_dir = ROOT / "legal"
    legal_count = len(list(legal_dir.glob("*.yaml"))) if legal_dir.exists() else 0
    if legal_count:
        print(f"Legal matrices: {legal_count}")


    # Export as JSON
    stats_file = ROOT / "stats.json"
    stats = {
        "framework_count": len(frameworks),
        "total_controls": total_controls,
        "total_translations": total_translations,
        "mappings_count": mapping_count,
        "legal_matrices_count": legal_count,
        "types": types,
        "regions": sorted(regions_set),
        "industries": sorted(industries_set),
        "frameworks": [
            {"id": fw["id"], "type": fw["type"], "controls": fw["controls"]}
            for fw in frameworks
        ],
    }
    with open(stats_file, "w") as f:
        json.dump(stats, f, indent=2)
    print(f"\nStats exported to: {stats_file}")


if __name__ == "__main__":
    main()
