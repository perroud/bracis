#!/usr/bin/env python3
"""
Check translation completeness and staleness across all frameworks.

Compares original control files with their i18n counterparts.
Reports missing translations and potentially stale translations
(where the original has been updated after the translation).
"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed. Run: pip install pyyaml")
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent
FRAMEWORKS_DIR = ROOT / "frameworks"


def check_framework(fw_dir: Path) -> dict:
    result = {
        "framework": fw_dir.name,
        "languages": {},
        "original_count": 0,
    }

    controls_dir = fw_dir / "controls"
    i18n_dir = fw_dir / "i18n"

    if not controls_dir.exists():
        return result

    originals = sorted(
        p for p in controls_dir.rglob("*.yaml")
        if not p.name.startswith("_")
    )
    result["original_count"] = len(originals)

    if not i18n_dir.exists():
        return result

    for lang_dir in sorted(i18n_dir.iterdir()):
        if not lang_dir.is_dir():
            continue

        lang = lang_dir.name
        translated_dir = lang_dir / "controls"
        lang_result = {
            "translated": 0,
            "missing": [],
            "stale": [],
        }

        if not translated_dir.exists():
            lang_result["missing"] = [
                str(p.relative_to(controls_dir)) for p in originals
            ]
            result["languages"][lang] = lang_result
            continue

        for orig in originals:
            rel = orig.relative_to(controls_dir)
            translated = translated_dir / rel

            if not translated.exists():
                lang_result["missing"].append(str(rel))
            else:
                lang_result["translated"] += 1

                # Check staleness via _translation.source_version
                try:
                    with open(translated) as f:
                        data = yaml.safe_load(f)
                    if data and "_translation" in data:
                        with open(orig) as f:
                            orig_data = yaml.safe_load(f)
                        if orig_data and "version" in orig_data:
                            src_ver = data["_translation"].get("source_version", "")
                            if src_ver and src_ver != str(orig_data.get("version", "")):
                                lang_result["stale"].append(str(rel))
                except Exception:
                    pass

        result["languages"][lang] = lang_result

    return result


def main():
    print("=" * 60)
    print("Translation Completeness Report")
    print("=" * 60)

    if not FRAMEWORKS_DIR.exists():
        print("No frameworks directory found.")
        return 0

    total_missing = 0
    total_stale = 0

    for fw_dir in sorted(FRAMEWORKS_DIR.iterdir()):
        if not fw_dir.is_dir() or fw_dir.name.startswith("."):
            continue

        result = check_framework(fw_dir)
        if not result["languages"]:
            continue

        print(f"\n{result['framework']} ({result['original_count']} controls)")

        for lang, data in result["languages"].items():
            total = result["original_count"]
            done = data["translated"]
            pct = (done / total * 100) if total > 0 else 0
            missing = len(data["missing"])
            stale = len(data["stale"])

            total_missing += missing
            total_stale += stale

            status = "COMPLETE" if missing == 0 else f"{pct:.0f}%"
            print(f"  [{lang}] {done}/{total} ({status})")

            if data["missing"]:
                for m in data["missing"][:10]:
                    print(f"    MISSING: {m}")
                if len(data["missing"]) > 10:
                    print(f"    ... and {len(data['missing']) - 10} more")

            if data["stale"]:
                for s in data["stale"][:5]:
                    print(f"    STALE: {s}")
                if len(data["stale"]) > 5:
                    print(f"    ... and {len(data['stale']) - 5} more")

    print("\n" + "=" * 60)
    print(f"Total missing: {total_missing}, Total stale: {total_stale}")
    print("=" * 60)

    return 1 if total_missing > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
