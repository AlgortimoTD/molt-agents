#!/usr/bin/env bash
# check.sh: the gates every push to this repository must pass (METHODOLOGY.md, section 14).
#   1. LF endings only (tracked text files)
#   2. no em dash (U+2014) or en dash (U+2013)
#   3. no secrets (token, key and credential patterns)
#   4. no personal data: no email addresses, no international phone numbers; plus an optional
#      local denylist (scripts/privacy-denylist.local.txt, gitignored) of real names to reject
#   5. valid JSON manifests; every marketplace plugin folder exists and has plugin.json
#   6. every <agent>/skills/<slug> has SKILL.md and a matching entry in skills/RELEASE.json
# Runs on tracked files (git ls-files) so it behaves the same locally and in CI. Exit 1 on any hit.
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"; cd "$ROOT"
PY="$(command -v python3 || command -v python)"
fail=0; hit() { echo "check: FAIL [$1] $2"; fail=1; }

mapfile -t FILES < <(git ls-files | grep -vE '\.(png|jpg|jpeg|gif|webp|pdf|woff2?|ttf|zip|skill)$')

# 1. LF
for f in "${FILES[@]}"; do grep -qI $'\r' "$f" 2>/dev/null && hit lf "$f has CRLF"; done

# 2. dashes (built from bytes so this script never contains the glyphs it rejects)
EM="$(printf '\xe2\x80\x94')"; EN="$(printf '\xe2\x80\x93')"
for f in "${FILES[@]}"; do
  grep -nI "$EM" "$f" 2>/dev/null | head -3 | sed "s|^|check: FAIL [em-dash] $f:|" && grep -qI "$EM" "$f" && fail=1
  grep -nI "$EN" "$f" 2>/dev/null | head -3 | sed "s|^|check: FAIL [en-dash] $f:|" && grep -qI "$EN" "$f" && fail=1
done

# 3. secrets
SECRET_RE='gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY|eyJ[A-Za-z0-9_-]{30,}\.[A-Za-z0-9_-]{10,}|(password|passwd|secret|api[_-]?key)\s*[:=]\s*["'"'"'][^"'"'"']{6,}'
for f in "${FILES[@]}"; do grep -nEI "$SECRET_RE" "$f" 2>/dev/null | head -3 | sed "s|^|check: FAIL [secret] $f:|" && grep -qEI "$SECRET_RE" "$f" && fail=1; done

# 4. personal data
EMAIL_RE='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
PHONE_RE='\+[0-9]{1,3}[ .-]?[0-9]{2,4}[ .-]?[0-9]{3,4}[ .-]?[0-9]{3,4}'
for f in "${FILES[@]}"; do
  grep -nEI "$EMAIL_RE" "$f" 2>/dev/null | grep -vE 'example\.(com|org)|<[^>]*@[^>]*>' | head -3 | sed "s|^|check: FAIL [email] $f:|" && grep -EI "$EMAIL_RE" "$f" | grep -qvE 'example\.(com|org)|<[^>]*@[^>]*>' && fail=1
  grep -nEI "$PHONE_RE" "$f" 2>/dev/null | head -3 | sed "s|^|check: FAIL [phone] $f:|" && grep -qEI "$PHONE_RE" "$f" && fail=1
done
if [ -f scripts/privacy-denylist.local.txt ]; then
  while IFS= read -r term; do
    term="${term%%#*}"; term="$(echo "$term" | sed 's/^ *//;s/ *$//')"; [ -n "$term" ] || continue
    for f in "${FILES[@]}"; do grep -qiI -- "$term" "$f" 2>/dev/null && hit privacy "$f mentions a denylisted term"; done
  done < scripts/privacy-denylist.local.txt
fi

# 5. manifests
for f in "${FILES[@]}"; do
  case "$f" in *.json) "$PY" -c "import json,sys;json.load(open(sys.argv[1],encoding='utf-8'))" "$f" 2>/dev/null || hit json "$f is not valid JSON" ;; esac
done
if [ -f .claude-plugin/marketplace.json ]; then
  while IFS= read -r src; do
    d="${src#./}"; [ -d "$d" ] || hit marketplace "plugin source $src does not exist"
    [ -f "$d/.claude-plugin/plugin.json" ] || hit marketplace "$d has no .claude-plugin/plugin.json"
  done < <("$PY" -c "import json;[print(p['source']) for p in json.load(open('.claude-plugin/marketplace.json',encoding='utf-8'))['plugins']]" | tr -d '\r')
fi

# 6. stamped skills
for skills_dir in */skills; do
  agent="${skills_dir%/skills}"; [ -d "$skills_dir" ] || continue
  [ "$agent" = "template" ] && continue
  for s in "$skills_dir"/*/; do
    [ -d "$s" ] || continue; slug="$(basename "$s")"
    [ -f "$s/SKILL.md" ] || hit skill "$s has no SKILL.md"
    [ -f "$skills_dir/RELEASE.json" ] || { hit skill "$agent has skills but no skills/RELEASE.json (run scripts/release.sh)"; continue; }
    "$PY" -c "import json,sys;sys.exit(0 if sys.argv[2] in json.load(open(sys.argv[1],encoding='utf-8'))['skills'] else 1)" "$skills_dir/RELEASE.json" "$slug" || hit skill "$slug is not stamped in $agent/skills/RELEASE.json (hand-copied?)"
  done
done

if [ $fail -eq 0 ]; then echo "check: all gates passed (${#FILES[@]} tracked files)"; fi
exit $fail
