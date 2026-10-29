#!/bin/bash
# Deploy a search-engine-blocked copy of site/ to the Netlify preview.
# site/ stays launch-ready; the preview copy is noindex everywhere so the
# netlify.app link never gets indexed ahead of the real domain.
set -euo pipefail
cd "$(dirname "$0")/.."
export PATH="$HOME/.local/node/bin:$PATH"

SITE_ID="dd7ba31d-34ea-4f0f-94c7-031fb6e1fd34"   # teachtalent-preview-jcandco.netlify.app
OUT="preview-build"

python3 tools/build_pages.py
rm -rf "$OUT" && cp -R site "$OUT"
find "$OUT" -name "*.html" -print0 | xargs -0 sed -i '' \
  -e 's|<meta name="robots" content="[^"]*">|<meta name="robots" content="noindex, nofollow">|'
printf 'User-agent: *\nDisallow: /\n' > "$OUT/robots.txt"
printf '/*\n  X-Robots-Tag: noindex, nofollow\n' > "$OUT/_headers"

if find "$OUT" -name "*.html" -exec grep -L 'content="noindex, nofollow"' {} + | grep -q .; then
  echo "Some pages are missing noindex, not deploying" >&2
  exit 1
fi

netlify deploy --dir "$OUT" --prod --site "$SITE_ID" --no-build --message "Teach Talent preview $(date +%Y-%m-%d)"
