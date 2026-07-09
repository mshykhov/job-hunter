#!/usr/bin/env python3
"""Block git commits carrying AI/attribution trailers (project rule: commits read as human-written)."""
import json
import re
import sys

FORBIDDEN = [
    r"co-authored-by",
    r"signed-off-by",
    r"generated with",
    r"noreply@anthropic",
    "\N{ROBOT FACE}",
]


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0
    if data.get("tool_name") != "Bash":
        return 0
    command = data.get("tool_input", {}).get("command", "")
    if not re.search(r"\bgit\b[\s\S]*\bcommit\b", command):
        return 0
    hits = [p for p in FORBIDDEN if re.search(p, command, re.IGNORECASE)]
    if hits:
        sys.stderr.write(
            "Commit blocked: message contains a forbidden trailer ("
            + ", ".join(hits)
            + "). Project rule: no Co-Authored-By, Signed-off-by, or Claude/AI "
            "attribution in commits. Remove it and commit again.\n"
        )
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
