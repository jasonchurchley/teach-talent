# Teach Talent – website (pitch build)

Education recruitment agency site for TAs, SEN TAs, HLTAs and 1:1 support across the East of England.
Design: "Quiet Prestige" (Flatline-inspired). Competitor benchmark: educate-east.co.uk.

## Preview
```
python3 tools/build_pages.py
cd site && python3 -m http.server 8802 --bind 127.0.0.1
```
Edit content in `tools/build_pages.py` (never the HTML in `site/` directly), then rebuild.

## Folder map
- `tools/build_pages.py` – all content, data, schema; writes `site/`
- `tools/icons/` – Phosphor icons (inlined at build)
- `site/` – deployable static site (Netlify Forms ready)
- `brand/logo-source.jpg` – the only logo we have (low-res)

## Pages (25)
Home, For Schools (+ request form), For Candidates (+ register form with CV upload), Jobs (empty state + job alerts),
Roles hub + 4 role pages, Areas hub + 6 county pages, About, Guides hub + 3 guides, Contact, Privacy, Thanks (noindex), 404.

## Adding jobs
Add dicts to `JOBS` in the generator (example in the comment above it) and rebuild. Each job gets its own page
at `/jobs/<slug>/` plus Google JobPosting schema automatically, so roles can appear in Google for Jobs.

## SEO vs Educate East
Competitor has ~7 pages, one H1 with no location pages, no role pages, no guides.
This build adds: 6 county landing pages, 4 role landing pages, 3 guides, EmploymentAgency + FAQPage + BreadcrumbList
+ Service + Article + JobPosting schema, sitemap.xml, robots.txt, llms.txt (AI search), unique titles/descriptions,
canonical + OG/Twitter tags, 1200x630 share image. Ranking above them in 2 months also needs, off-site:
1. Google Business Profile at the real address (biggest local factor), with the same NAP as the site
2. Search Console + submit sitemap on launch day
3. Real reviews on GBP; REC / framework membership links
4. 1 to 2 new guides a month and live jobs posted regularly
5. Local citations (Yell, Bing Places, Apple Business Connect, Indeed company page)

## Before this could go live
- Real domain (SITE constant), phone, email, office address, company number
- Vector logo (SVG/PDF) from the client; current mark is extracted from a 359px JPG
- Replace the 3 testimonials on the home page (placeholders, no Review schema added)
- Confirm claims: "open from 7am", weekly PAYE pay, "same day" shortlists
- Full privacy notice (placeholder), cookie policy if analytics added
- Real photos to replace Unsplash
- Netlify: forms notifications to the client's inbox

## Photo credits (Unsplash, free licence)
| File | Unsplash ID |
|---|---|
| hero-reading.webp | photo-1583468982228-19f19164aee2 |
| classroom.webp | photo-1577896851231-70ef18881754 |
| workbook.webp | photo-1589206946274-929e4da3996b |
| sen-support.webp | photo-1771765767087-ce71e4a7916a |
| one-to-one.webp | photo-1583468991267-3f068b607ae1 |
| students.webp | photo-1571260899304-425eee4c7efc |

