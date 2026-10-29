# Impeccable critique and audit (2026-10-29)
⚠️ DEGRADED: single-context. Context loading did not run; PRODUCT.md and DIRECTION.md read directly.

| Area | Score /10 | Notes |
|---|---|---|
| First impression / hero | 8 | Flatline clip headline is distinctive; cream text over photo needed more contrast |
| Hierarchy | 7 | Inner pages had no action above the fold |
| Layout | 7 | Home statement too narrow at 1440; inner heroes without photo left-heavy |
| Typography | 8 | Cormorant/Manrope pairing on brand; long words could break grids |
| Colour / contrast | 8 | gold-ink was 4.51:1, now 5.2:1 |
| Conversion | 7 | Floating card could cover form submit buttons |
| Accessibility | 9 | One H1, no heading skips, alt text, focus states, 44px tap targets |

## Fixed
1. Page heroes now carry Hire staff / Find a role buttons (not on guides or privacy).
2. Hero photo darkened (brightness .66) for the cream headline.
3. Statement width 28ch to 34ch.
4. Floating card hides while a form or CTA band is on screen.
5. Long unbroken words wrap (overflow-wrap:anywhere, grid children min-width:0).
6. No-photo page heroes widened to 900px text column.

## Still open (needs client)
Real testimonials, real stats/proof, vector logo.
