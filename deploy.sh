#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
MSG="${1:-更新官网设计稿}"
SITE="https://nancity11521-ai.github.io/lucky-infinite-website/"
MAIN="index.html"

git add -A
git diff --cached --quiet || { git commit -q -m "$MSG"; git log --oneline -1; }
git push -q origin main

LOCAL_H=$(shasum -a 256 "$MAIN" | cut -d' ' -f1)
TMP=$(mktemp)
ok=0
for i in $(seq 1 20); do
  curl -s -o "$TMP" "${SITE}${MAIN}?cb=$RANDOM"
  ONLINE_H=$(shasum -a 256 "$TMP" | cut -d' ' -f1)
  if [ "$ONLINE_H" = "$LOCAL_H" ]; then echo "  ✓ 线上已更新（$(wc -c < "$TMP" | tr -d ' ') 字节）"; ok=1; break; fi
  echo "  [$i] 仍是旧内容，等待中…"; sleep 8
done
rm -f "$TMP"
[ "$ok" = "1" ] || { echo "⚠ 轮询后线上仍未更新"; exit 1; }
