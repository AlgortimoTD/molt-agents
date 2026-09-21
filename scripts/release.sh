#!/usr/bin/env bash
# release.sh: stamp an agent's skills from the Molt skill registry source and bump the plugin version.
#
# Usage:
#   scripts/release.sh <agent> [--bump patch|minor|major] [--monorepo <path>]
#
# The source of truth of every skill is catalogs/global/<slug>/skill/ in the platform monorepo
# (METHODOLOGY.md, section 7). This script is the ONLY way <agent>/skills/ gets written:
#   1. reads <agent>/skills.manifest (one slug per line, # comments allowed);
#   2. for each slug, replaces <agent>/skills/<slug>/ with a copy of catalogs/global/<slug>/skill/;
#   3. records slug, version (from the [vX.Y.Z] tag of the SKILL.md description) and the sha256 of
#      SKILL.md in <agent>/skills/RELEASE.json;
#   4. bumps <agent>/.claude-plugin/plugin.json (default: patch) unless --bump none.
# The monorepo path comes from --monorepo, then $MOLT_MONOREPO, then ../molt-agentic-plaform.
set -euo pipefail

usage() { sed -n '2,15p' "$0"; exit 2; }

AGENT="${1:-}"; [ -n "$AGENT" ] || usage; shift
BUMP="patch"; MONOREPO="${MOLT_MONOREPO:-}"
while [ $# -gt 0 ]; do
  case "$1" in
    --bump) BUMP="$2"; shift 2 ;;
    --monorepo) MONOREPO="$2"; shift 2 ;;
    *) usage ;;
  esac
done

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
[ -n "$MONOREPO" ] || MONOREPO="$ROOT/../molt-agentic-plaform"
[ -d "$MONOREPO/catalogs/global" ] || { echo "release: monorepo not found at $MONOREPO (pass --monorepo or set MOLT_MONOREPO)" >&2; exit 1; }
[ -d "$ROOT/$AGENT" ] || { echo "release: agent folder $AGENT not found" >&2; exit 1; }
MANIFEST="$ROOT/$AGENT/skills.manifest"
[ -f "$MANIFEST" ] || { echo "release: $AGENT/skills.manifest not found" >&2; exit 1; }
PY="$(command -v python3 || command -v python)"; [ -n "$PY" ] || { echo "release: python not found" >&2; exit 1; }

mkdir -p "$ROOT/$AGENT/skills"
ENTRIES=()
while IFS= read -r slug; do
  slug="${slug%%#*}"; slug="$(echo "$slug" | tr -d '[:space:]')"; [ -n "$slug" ] || continue
  SRC="$MONOREPO/catalogs/global/$slug/skill"
  [ -f "$SRC/SKILL.md" ] || { echo "release: $SRC/SKILL.md not found (is $slug vendored and published?)" >&2; exit 1; }
  version="$(grep -oE '\[v[0-9]+\.[0-9]+\.[0-9]+\]' "$SRC/SKILL.md" | head -1 | tr -d '[]v')"
  [ -n "$version" ] || { echo "release: $slug has no [vX.Y.Z] tag in SKILL.md; bump it in the monorepo first" >&2; exit 1; }
  DST="$ROOT/$AGENT/skills/$slug"
  rm -rf "$DST"; mkdir -p "$DST"
  ( cd "$SRC" && tar cf - --exclude='.git' . ) | ( cd "$DST" && tar xf - )
  sha="$("$PY" -c "import hashlib,sys;print(hashlib.sha256(open(sys.argv[1],'rb').read()).hexdigest())" "$SRC/SKILL.md")"
  ENTRIES+=("$slug|$version|$sha")
  echo "release: $slug v$version stamped"
done < "$MANIFEST"
[ ${#ENTRIES[@]} -gt 0 ] || { echo "release: manifest is empty" >&2; exit 1; }

printf '%s\n' "${ENTRIES[@]}" | "$PY" - "$ROOT/$AGENT/skills/RELEASE.json" <<'PYEOF'
import json, sys, datetime
rows = [l.strip().split("|") for l in sys.stdin if l.strip()]
out = {"stamped_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
       "source": "catalogs/global/<slug>/skill in the platform monorepo",
       "skills": {slug: {"version": v, "skill_md_sha256": s} for slug, v, s in rows}}
json.dump(out, open(sys.argv[1], "w", newline="\n"), indent=2, ensure_ascii=False); open(sys.argv[1], "a", newline="\n").write("\n")
PYEOF

if [ "$BUMP" != "none" ]; then
  "$PY" - "$ROOT/$AGENT/.claude-plugin/plugin.json" "$BUMP" <<'PYEOF'
import json, sys
p, part = sys.argv[1], sys.argv[2]
d = json.load(open(p, encoding="utf-8"))
major, minor, patch = (int(x) for x in d["version"].split("."))
major, minor, patch = {"major": (major+1, 0, 0), "minor": (major, minor+1, 0), "patch": (major, minor, patch+1)}[part]
d["version"] = f"{major}.{minor}.{patch}"
json.dump(d, open(p, "w", encoding="utf-8", newline="\n"), indent=2, ensure_ascii=False); open(p, "a", newline="\n").write("\n")
print(f"release: plugin version -> {d['version']}")
PYEOF
fi
echo "release: done. Run scripts/check.sh, then commit."
