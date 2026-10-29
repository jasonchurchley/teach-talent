# Test loop (2026-10-29)
Pass 1: gold-ink text on cream measured 4.51:1 (borderline) -> darkened to #7F6133.
Pass 2 (all 25 pages at 320/375/1440): 0 sideways scroll, 0 off-screen elements, 0 tap targets < 24px, 0 missing alt, one H1 per page, no heading skips, 29/29 internal links 200, 0 console errors.
Menu: focus moves in, Escape closes, focus returns to burger. Empty form submit: 7 inline errors, focus on first. Valid test submit posts to /thanks/ (local server returns 501 on POST; Netlify handles it).
Not yet run: Impeccable critique/audit, Emil motion review, break-ui worst-case data pass.

## Review round (2026-10-29)
break-ui copy (long unbroken role/job names, 13 long town names, 77-char email, £8.50 to £1,250 pay, empty role description, 1,000-char FAQ answer) on a spare port:
Pass 1: overflow on home FAQ, jobs, job detail, role page at 320/375 and role page at 1440.
Fix: overflow-wrap:anywhere on text, min-width:0 on grid children. Pass 2: 0 issues. Copy deleted.
Final pass, real site, 25 pages at 320/375/1440: 0 overflow, 0 off-screen, 0 small tap targets, 0 heading issues.
