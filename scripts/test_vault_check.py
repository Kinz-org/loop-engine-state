#!/usr/bin/env python3
"""Tests for vault_check.py. Run: python3 scripts/test_vault_check.py"""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from vault_check import check  # noqa: E402

failures = 0


def expect(name, got, want):
    global failures
    if got != want:
        failures += 1
        print(f"FAIL {name}: got {got!r}, want {want!r}")


with tempfile.TemporaryDirectory() as d:
    root = Path(d)
    (root / "MOCs").mkdir()
    (root / "Concepts").mkdir()
    (root / "Templates").mkdir()
    (root / ".obsidian").mkdir()
    (root / "MOCs/Hub.md").write_text(
        "---\ntype: moc\n---\n[[Alpha]] [[Alpha|alias]] [[Beta#Section]] [[Ghost]] ![[img.png]]\n",
        encoding="utf-8")
    (root / "Concepts/Alpha.md").write_text("---\ntype: concept\n---\n[[Ghost]] [[Hub]]\n",
                                            encoding="utf-8")
    (root / "Concepts/Beta.md").write_text("no frontmatter, links to [[Beta]] only\n",
                                           encoding="utf-8")
    (root / "Concepts/Lonely.md").write_text("---\ntype: note\n---\nnothing\n", encoding="utf-8")
    (root / "Templates/T.md").write_text("{{title}}\n", encoding="utf-8")
    (root / ".obsidian/ignored.md").write_text("[[Nowhere]]\n", encoding="utf-8")

    r = check(root)
    expect("note count skips .obsidian", r["notes"], 5)
    expect("missing type excludes templates", r["missing_type"], ["Concepts/Beta.md"])
    # Beta links only to itself but Hub links to Beta#Section, so Beta is not an orphan.
    expect("orphans: self-links ignored, heading links count, templates excluded",
           r["orphans"], ["Concepts/Lonely.md"])
    expect("unwritten counted per distinct note, embeds ignored",
           r["unwritten"], [{"target": "Ghost", "linked_from": 2}])
    r = check(root, ("MOCs/Hub.md",))
    expect("ignored source not counted", r["unwritten"], [{"target": "Ghost", "linked_from": 1}])

if failures:
    sys.exit(f"{failures} failure(s)")
print("0 failure(s)")
