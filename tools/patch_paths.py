#!/usr/bin/env python3
"""Rewrite common local paths in the submitted notebooks.

This utility only changes string occurrences in notebook JSON. It is intended to
make the retained server-oriented notebooks easier to run on another machine.
"""

import argparse
import shutil
from pathlib import Path


def replace_in_file(path, replacements, make_backup=True):
    text = path.read_text(encoding="utf-8")
    new = text
    changed = []
    for old, repl in replacements:
        if old in new:
            new = new.replace(old, repl)
            changed.append((old, repl))
    if new != text:
        if make_backup:
            backup = path.with_suffix(path.suffix + ".bak")
            if not backup.exists():
                shutil.copy2(str(path), str(backup))
        path.write_text(new, encoding="utf-8")
    return changed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", required=True, help="Root used for result/cache directories")
    parser.add_argument("--data-root", required=True, help="Root containing benchmark datasets")
    parser.add_argument("--tslib-root", required=True, help="Time-Series-Library checkout")
    parser.add_argument("--package-root", default=None, help="Repository root (default: parent of tools/)")
    parser.add_argument("--no-backup", action="store_true")
    args = parser.parse_args()

    package_root = Path(args.package_root).resolve() if args.package_root else Path(__file__).resolve().parents[1]
    project_root = str(Path(args.project_root).resolve())
    data_root = str(Path(args.data_root).resolve())
    tslib_root = str(Path(args.tslib_root).resolve())

    replacements = [
        ("/data/time-series-foundation-model/Time-Series-Library", tslib_root),
        ("/data/time-series_foundation_model/Time-Series-Library", tslib_root),
        ("/data/Time-Series-Library_v2", tslib_root),
        ("/data/Time-Series-Library", tslib_root),
        ("/data/code/2026_08", project_root),
        ("/data/results_", project_root.rstrip("/") + "/results_"),
        ("/data/dataset", data_root),
    ]

    notebooks = sorted((package_root / "notebooks").rglob("*.ipynb"))
    n_changed = 0
    for notebook in notebooks:
        changes = replace_in_file(notebook, replacements, make_backup=not args.no_backup)
        if changes:
            n_changed += 1
            print("patched:", notebook.relative_to(package_root))

    print("notebooks scanned:", len(notebooks))
    print("notebooks changed:", n_changed)


if __name__ == "__main__":
    main()
