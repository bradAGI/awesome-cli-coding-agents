#!/usr/bin/env python3
"""Fetch current GitHub star counts and update README.md.

Updates the `⭐ Xk` badge on every entry that links to github.com and
re-sorts entries within each configured section by star count (desc).

Run locally with a PAT:
    GITHUB_TOKEN=ghp_... python3 scripts/update-stars.py
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"
TOKEN = os.environ.get("GITHUB_TOKEN")

ENTRY_RE = re.compile(
    r"^- \*\*\[([^\]]+)\]\((https://github\.com/([^/\s]+)/([^)\s]+))\)\*\*"
)
STAR_RE = re.compile(r"`⭐ [^`]+`")
EXISTING_STAR_RE = re.compile(r"`⭐ ([^`]+)`")

SORTED_SECTIONS = {
    "Open Source",
    "OpenClaw ecosystem",
    "Closed Source",
    "Session managers & parallel runners",
    "Orchestrators & autonomous loops",
    "Agent infrastructure",
}


def fetch_stars(owner: str, repo: str) -> int | None:
    url = f"https://api.github.com/repos/{owner}/{repo}"
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "awesome-cli-coding-agents-updater")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.load(resp).get("stargazers_count")
    except urllib.error.HTTPError as e:
        print(f"  WARN {owner}/{repo}: HTTP {e.code}", file=sys.stderr)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
        print(f"  WARN {owner}/{repo}: {e}", file=sys.stderr)
    return None


def format_stars(count: int) -> str:
    if count >= 100_000:
        return f"{round(count / 1000)}k"
    if count >= 1_000:
        s = f"{count / 1000:.1f}"
        return f"{s[:-2] if s.endswith('.0') else s}k"
    return str(count)


def parse_entry(line: str) -> tuple[str, str] | None:
    m = ENTRY_RE.match(line)
    return (m.group(3), m.group(4)) if m else None


def parse_existing_stars(line: str) -> int | None:
    m = EXISTING_STAR_RE.search(line)
    if not m:
        return None
    raw = m.group(1).strip().lower()
    try:
        if raw.endswith("k"):
            return int(float(raw[:-1]) * 1000)
        return int(raw)
    except ValueError:
        return None


def apply_star_badge(line: str, stars: int) -> str:
    badge = f"`⭐ {format_stars(stars)}`"
    if STAR_RE.search(line):
        return STAR_RE.sub(badge, line, count=1)
    return re.sub(
        r"(\*\*\[[^\]]+\]\([^)]+\)\*\*)", rf"\1 {badge}", line, count=1
    )


def main() -> int:
    if not TOKEN:
        print(
            "NOTE: GITHUB_TOKEN not set — unauthenticated requests are "
            "limited to 60/hour and will likely be rate-limited.",
            file=sys.stderr,
        )

    text = README.read_text()
    lines = text.split("\n")

    repos: dict[tuple[str, str], int | None] = {}
    for line in lines:
        parsed = parse_entry(line)
        if parsed and parsed not in repos:
            repos[parsed] = None

    print(f"Fetching stars for {len(repos)} repos…", file=sys.stderr)
    for owner, repo in list(repos.keys()):
        stars = fetch_stars(owner, repo)
        repos[(owner, repo)] = stars
        print(
            f"  {owner}/{repo}: "
            f"{format_stars(stars) if stars is not None else 'N/A'}",
            file=sys.stderr,
        )

    out: list[str] = []
    i = 0
    current_section: str | None = None
    while i < len(lines):
        line = lines[i]

        m = re.match(r"^### (.+)$", line)
        if m:
            current_section = m.group(1).strip()
            out.append(line)
            i += 1
            continue

        if line == "---" or line.startswith("## "):
            current_section = None
            out.append(line)
            i += 1
            continue

        if current_section in SORTED_SECTIONS and line.startswith("- **"):
            block: list[str] = []
            while i < len(lines) and (
                lines[i].startswith("- **") or lines[i] == ""
            ):
                block.append(lines[i])
                i += 1

            entries: list[list[str]] = []
            buf: list[str] = []
            for bl in block:
                if bl == "":
                    if buf:
                        entries.append(buf)
                        buf = []
                else:
                    buf.append(bl)
            if buf:
                entries.append(buf)

            for entry in entries:
                parsed = parse_entry(entry[0])
                if parsed and repos.get(parsed) is not None:
                    entry[0] = apply_star_badge(entry[0], repos[parsed])

            def key(entry: list[str]) -> tuple[int, int]:
                parsed = parse_entry(entry[0])
                stars = repos.get(parsed) if parsed else None
                if stars is None and parsed is not None:
                    stars = parse_existing_stars(entry[0])
                return (0, -stars) if stars is not None else (1, 0)

            entries.sort(key=key)

            for idx, entry in enumerate(entries):
                out.extend(entry)
                if idx < len(entries) - 1:
                    out.append("")
            out.append("")
            continue

        out.append(line)
        i += 1

    new_text = re.sub(r"\n{3,}", "\n\n", "\n".join(out))
    if not new_text.endswith("\n"):
        new_text += "\n"
    README.write_text(new_text)
    print("README.md updated.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
