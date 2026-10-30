#!/bin/bash
# Netlify build: regenerate pages from content/, then (preview only) block indexing in place.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 tools/build_pages.py
if [ "${TT_PREVIEW:-}" = "1" ]; then
  find site -name "*.html" -print0 | xargs -0 sed -i \
    -e 's|<meta name="robots" content="[^"]*">|<meta name="robots" content="noindex, nofollow">|'
  printf 'User-agent: *\nDisallow: /\n' > site/robots.txt
  printf '/*\n  X-Robots-Tag: noindex, nofollow\n' > site/_headers
fi
