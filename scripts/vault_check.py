#!/usr/bin/env python3
"""Read-only health check of the Obsidian vault, for the kinz-vault job.

Usage:
  python3 scripts/vault_check.py /home/user/kinz-obsidian-vault          # report
  python3 scripts/vault_check.py /home/user/kinz-obsidian-vault --json   # machine-readable
  ... --ignore-source "MOCs/Atlas — Index du Vault.md"                   # see --help

Reports what the job is allowed to act on and nothing else:
  missing_type   notes whose frontmatter has no `type`
  orphans        notes no other note links to (templates excluded)
  unwritten      wikilink targets with no note, counted by distinct linking notes
It never writes. Links resolve by file name, as Obsidian does: `[[Note]]`, `[[Note|x]]`,
`[[Note#h]]` all point at `Note.md` anywhere in the vault.
"""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

SKIP_DIRS = {".git", ".obsidian", ".claude", ".claudian", ".trash"}
TEMPLATE_DIRS = {"Templates"}
WIKILINK = re.compile(r"(?<!!)\[\[([^\]|#^]+)(?:[#^][^\]|]*)?(?:\|[^\]]*)?\]\]")
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def notes(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.md")
                  if not SKIP_DIRS.intersection(p.relative_to(root).parts))


def check(root: Path, ignore_sources: tuple = ()) -> dict:
    files = notes(root)
    by_name = {p.stem: p for p in files}
    inbound: Counter = Counter()
    unwritten: dict[str, set] = {}
    missing_type = []
    for p in files:
        rel = p.relative_to(root).as_posix()
        text = p.read_text(encoding="utf-8")
        fm = FRONTMATTER.match(text)
        is_template = p.relative_to(root).parts[0] in TEMPLATE_DIRS
        if not is_template and not (fm and re.search(r"^type:\s*\S", fm.group(1), re.M)):
            missing_type.append(rel)
        for target in {t.strip() for t in WIKILINK.findall(text)}:
            if target in by_name:
                if by_name[target] != p:
                    inbound[target] += 1
            elif rel not in ignore_sources:
                unwritten.setdefault(target, set()).add(rel)
    orphans = [p.relative_to(root).as_posix() for p in files
               if inbound[p.stem] == 0 and p.relative_to(root).parts[0] not in TEMPLATE_DIRS]
    ranked = sorted(((t, len(s)) for t, s in unwritten.items()), key=lambda x: (-x[1], x[0]))
    return {"notes": len(files), "missing_type": missing_type, "orphans": orphans,
            "unwritten": [{"target": t, "linked_from": n} for t, n in ranked]}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("vault")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--ignore-source", action="append", default=[], metavar="NOTE",
                    help="vault-relative note whose links are left out of the unwritten counts, "
                         "e.g. the Atlas, whose leads table would otherwise count itself")
    args = ap.parse_args()
    root = Path(args.vault)
    if not root.is_dir():
        sys.exit(f"no such vault: {root}")
    r = check(root, tuple(args.ignore_source))
    if args.json:
        print(json.dumps(r, ensure_ascii=False, indent=1))
        return
    print(f"{r['notes']} notes | missing type {len(r['missing_type'])} | "
          f"orphans {len(r['orphans'])} | unwritten targets {len(r['unwritten'])}")
    for k in ("missing_type", "orphans"):
        for f in r[k]:
            print(f"  {k}: {f}")
    for u in r["unwritten"][:12]:
        print(f"  unwritten: {u['target']} ({u['linked_from']} notes)")


if __name__ == "__main__":
    main()
