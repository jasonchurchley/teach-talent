"""Generate the Teach Talent site into ../site.

All content and data live here; the output is plain HTML with a shared
header, menu and footer. Run: python3 tools/build_pages.py
"""
import json
import os
import re
import sys
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_DIR = os.environ.get("TT_OUT", os.path.join(ROOT, "..", "site"))
ICONS = os.path.join(ROOT, "icons")

# ---------------------------------------------------------------- business
SITE = "https://www.teachtalent.co.uk"          # placeholder domain
NAME = "Teach Talent"
TAGLINE = "Education Recruitment Agency"
PHONE = "01223 000000"                           # placeholder
PHONE_INTL = "+441223000000"
EMAIL = "hello@teachtalent.co.uk"                # placeholder
ADDRESS = {"street": "Office 1, Example House, Hills Road",  # placeholder
           "town": "Cambridge", "region": "Cambridgeshire", "postcode": "CB2 1AA"}
HOURS_TEXT = "Monday to Friday, 7am to 6pm"
HIRE = ("Hire staff", "/for-schools/#request")
FIND = ("Find a role", "/for-candidates/#register")
TODAY = date.today().isoformat()

ROLES = [
    {
        "slug": "teaching-assistant", "name": "Teaching Assistants", "single": "Teaching Assistant",
        "short": "Classroom support across EYFS, KS1 and KS2, from daily cover to permanent posts.",
        "img": "workbook", "alt": "Teaching assistant guiding a pupil through a colourful workbook",
        "lead": "Teaching assistants keep lessons moving. They run small-group interventions, support pupils who need a second explanation and give the class teacher time to teach. We place TAs in primary and secondary schools across the East of England on daily, long-term and permanent contracts.",
        "does": ["Supporting small groups and individual pupils during lessons",
                 "Delivering phonics, reading and maths interventions",
                 "Preparing resources and helping with classroom routines",
                 "Supervising pupils at break, lunch and on trips",
                 "Feeding back progress to the class teacher"],
        "need": ["Experience with children, in school or elsewhere",
                 "A Level 2 or 3 Teaching Assistant qualification is welcome but not essential for every role",
                 "An enhanced DBS on the Update Service, or willingness to apply",
                 "Two professional references covering the last two years"],
        "faq": [("Do I need a qualification to work as a teaching assistant?",
                 "Not always. Many schools take on TAs with strong experience working with children. A Level 2 or Level 3 Certificate in Supporting Teaching and Learning opens more doors and can be completed while you work."),
                ("Can I work as a TA on a supply basis?",
                 "Yes. Day-to-day supply suits people who want flexibility. Many of our TAs start on supply and move into long-term or permanent roles with a school they enjoy."),
                ("How quickly can I start?",
                 "Once your registration, references and DBS are cleared, you can be offered work straight away. We aim to complete compliance within a few working days.")],
    },
    {
        "slug": "sen-teaching-assistant", "name": "SEN Teaching Assistants", "single": "SEN Teaching Assistant",
        "short": "Specialist support for pupils with SEND in mainstream and specialist settings.",
        "img": "sen-support", "alt": "SEN teaching assistant working one to one with a young pupil",
        "lead": "SEN teaching assistants support pupils with special educational needs and disabilities to learn, communicate and feel safe at school. We recruit SEN TAs for mainstream schools, resource bases, special schools and alternative provision across the East of England.",
        "does": ["Supporting pupils with autism, ADHD, speech and language needs, SEMH and physical needs",
                 "Following EHCP targets and individual support plans",
                 "Using visual timetables, Makaton or PECS where needed",
                 "De-escalating and supporting emotional regulation",
                 "Working closely with the SENCO, therapists and families"],
        "need": ["Experience supporting children or young people with SEND",
                 "Patience, consistency and calm under pressure",
                 "Team Teach, PBS or similar training is an advantage",
                 "An enhanced DBS and two professional references"],
        "faq": [("What is the difference between a TA and an SEN TA?",
                 "A teaching assistant usually supports the whole class or small groups. An SEN TA focuses on pupils with special educational needs, often working towards targets in an Education, Health and Care Plan (EHCP)."),
                ("Do you place SEN TAs in special schools?",
                 "Yes. We work with mainstream schools, specialist schools, resource bases and alternative provision across Cambridgeshire, Norfolk, Suffolk, Essex, Hertfordshire and Bedfordshire."),
                ("Will I get training?",
                 "We can point you towards safeguarding, autism awareness and behaviour support training so you feel ready for each placement.")],
    },
    {
        "slug": "higher-level-teaching-assistant", "name": "HLTAs", "single": "Higher Level Teaching Assistant",
        "short": "Experienced HLTAs for PPA cover, interventions and whole-class teaching.",
        "img": "students", "alt": "Higher level teaching assistant leading a class of older pupils",
        "lead": "Higher level teaching assistants take on more of the teaching load, covering PPA time, leading interventions and teaching whole classes under the direction of a teacher. We recruit HLTAs who can step in confidently and keep learning on track.",
        "does": ["Covering planned teacher absence and PPA time",
                 "Planning and leading targeted interventions",
                 "Teaching whole classes using the school's plans",
                 "Assessing and recording pupil progress",
                 "Mentoring and guiding other support staff"],
        "need": ["HLTA status, or significant experience at Level 3 and above",
                 "Strong behaviour management with whole classes",
                 "Good subject knowledge in English and maths",
                 "An enhanced DBS and two professional references"],
        "faq": [("How do I get HLTA status?",
                 "HLTA status is awarded through an assessment against the national HLTA standards, usually arranged through a regional provider and supported by your school."),
                ("Do HLTAs earn more than teaching assistants?",
                 "Yes. HLTA roles carry more responsibility and are usually paid at a higher rate. We will always share the rate before you accept a role."),
                ("Can HLTAs work on supply?",
                 "Yes. Schools often book HLTAs for planned absence, PPA cover and longer-term cover where a supply teacher is not needed.")],
    },
    {
        "slug": "one-to-one-support", "name": "1:1 Support & LSAs", "single": "1:1 Support Assistant",
        "short": "Dedicated one-to-one learning support assistants matched to a single pupil.",
        "img": "one-to-one", "alt": "Learning support assistant reading one to one with a pupil",
        "lead": "A one-to-one learning support assistant works with a single pupil, often funded through an EHCP. The match matters more than anything, so we take time to understand the pupil's needs, the school's approach and the person who will fit.",
        "does": ["Supporting one pupil throughout the school day",
                 "Adapting work and resources to the pupil's needs",
                 "Supporting personal care where required",
                 "Recording progress against EHCP outcomes",
                 "Building a trusting, consistent relationship"],
        "need": ["Experience with SEND, ideally the specific need involved",
                 "Reliability: consistency is vital for the pupil",
                 "Willingness to complete role-specific training",
                 "An enhanced DBS and two professional references"],
        "faq": [("How do you match a 1:1 to a pupil?",
                 "We ask the school about the pupil's needs, triggers, strengths and routines, then shortlist people with relevant experience. Schools can meet candidates before a start date."),
                ("Are 1:1 roles long term?",
                 "Most are. Many run for a full academic year or longer because consistency is so important for the pupil."),
                ("What if the placement is not working?",
                 "Talk to us early. We review placements with both the school and the assistant and will find a better fit if needed.")],
    },
]

COUNTIES = [
    {
        "slug": "cambridgeshire", "name": "Cambridgeshire",
        "towns": ["Cambridge", "Peterborough", "Huntingdon", "St Neots", "Ely", "St Ives", "Wisbech", "March"],
        "intro": "From Cambridge city primaries to rural schools around Ely and the Fens, Cambridgeshire schools need support staff who can adapt quickly. Our office is based in Cambridge, so we know the county's schools, trusts and travel routes well.",
        "note": "Peterborough and the Fenland towns have a growing need for SEN support staff, and we prioritise candidates who live locally so travel never gets in the way.",
    },
    {
        "slug": "norfolk", "name": "Norfolk",
        "towns": ["Norwich", "King's Lynn", "Great Yarmouth", "Thetford", "Dereham", "Wymondham", "Cromer", "Attleborough"],
        "intro": "Norfolk covers large distances, from Norwich to King's Lynn and the coast. We recruit teaching assistants and SEN support staff who live close to the schools they work in, so cover is dependable even in rural areas.",
        "note": "We support primary, secondary and specialist settings across Norwich, Breckland and West Norfolk.",
    },
    {
        "slug": "suffolk", "name": "Suffolk",
        "towns": ["Ipswich", "Bury St Edmunds", "Lowestoft", "Newmarket", "Stowmarket", "Sudbury", "Haverhill", "Felixstowe"],
        "intro": "Suffolk schools, from Ipswich and Bury St Edmunds to Lowestoft and Haverhill, rely on steady, skilled support staff. We match TAs and SEN assistants to schools across the county for daily, long-term and permanent roles.",
        "note": "Haverhill and Newmarket sit close to our Cambridge base, and we are building a dedicated pool of Suffolk candidates on the coast.",
    },
    {
        "slug": "essex", "name": "Essex",
        "towns": ["Chelmsford", "Colchester", "Harlow", "Braintree", "Saffron Walden", "Basildon", "Witham", "Southend-on-Sea"],
        "intro": "Essex is one of the largest education areas in the region. We help schools in Chelmsford, Colchester, Harlow, Braintree and beyond find teaching assistants and SEN support staff who are ready to start.",
        "note": "North and west Essex, including Saffron Walden and Harlow, are a short journey from our Cambridge office.",
    },
    {
        "slug": "hertfordshire", "name": "Hertfordshire",
        "towns": ["Stevenage", "Hitchin", "Letchworth", "St Albans", "Watford", "Hertford", "Royston", "Hemel Hempstead"],
        "intro": "Hertfordshire schools expect high standards. We supply experienced teaching assistants, HLTAs and SEN support staff to schools in Stevenage, Hitchin, St Albans, Royston and across the county.",
        "note": "North Hertfordshire towns like Royston, Letchworth and Hitchin are core areas for our candidate pool.",
    },
    {
        "slug": "bedfordshire", "name": "Bedfordshire",
        "towns": ["Bedford", "Luton", "Biggleswade", "Sandy", "Leighton Buzzard", "Dunstable", "Flitwick", "Ampthill"],
        "intro": "Bedfordshire has a strong mix of lower, middle and upper schools alongside primary and secondary academies. We recruit support staff who understand both systems, for schools in Bedford, Luton, Biggleswade and Central Bedfordshire.",
        "note": "We cover Bedford Borough, Central Bedfordshire and Luton, with candidates spread along the A1 and M1 corridors.",
    },
]

# Jobs board. Add dicts here and rebuild; JobPosting schema is generated for each.
# Example:
# {"slug": "sen-ta-cambridge", "title": "SEN Teaching Assistant", "town": "Cambridge",
#  "county": "Cambridgeshire", "type": "Long term", "employment": "FULL_TIME",
#  "pay": "£95 to £105 per day", "pay_min": 95, "pay_max": 105, "pay_unit": "DAY",
#  "start": "January 2027", "posted": "2026-11-01", "closes": "2026-12-01",
#  "summary": "...", "details": ["...", "..."]}
JOBS = []

GUIDES = [
    {
        "slug": "how-to-become-a-teaching-assistant",
        "title": "How to become a teaching assistant in the East of England",
        "desc": "Qualifications, experience, DBS checks and how to find your first teaching assistant role in Cambridgeshire, Norfolk, Suffolk, Essex, Hertfordshire or Bedfordshire.",
        "img": "classroom", "alt": "Primary classroom with pupils raising hands",
        "body": [
            ("h2", "Do you need qualifications?"),
            ("p", "You do not always need a formal qualification to start as a teaching assistant. Schools look for people who are good with children, reliable and willing to learn. Good GCSEs in English and maths (or equivalent) help, and many schools value a Level 2 or Level 3 Certificate in Supporting Teaching and Learning."),
            ("h2", "Get relevant experience"),
            ("p", "Volunteering in a school, running a youth group, coaching sport or working in childcare all count. If you are a parent, helping with reading at your child's school is a good start. Write down what you did, the ages involved and what you learned."),
            ("h2", "Your DBS and references"),
            ("p", "Every school role needs an enhanced DBS check with a barred list check. If you already have one, joining the DBS Update Service lets schools and agencies check it instantly. You will also need two references, ideally covering the last two years."),
            ("h2", "Start with supply"),
            ("p", "Day-to-day supply through an agency is one of the fastest ways in. You see different schools, build experience across year groups and often get offered longer placements by schools that like your work."),
            ("h2", "Register with Teach Talent"),
            ("p", "We help new and experienced teaching assistants find work across the East of England. Register once and we will match you to schools near you."),
        ],
    },
    {
        "slug": "what-does-an-sen-teaching-assistant-do",
        "title": "What does an SEN teaching assistant do?",
        "desc": "A clear guide to the SEN teaching assistant role: daily duties, the needs you might support, useful training and how it differs from a general TA role.",
        "img": "sen-support", "alt": "SEN teaching assistant using hand signs with a pupil",
        "body": [
            ("h2", "The short answer"),
            ("p", "An SEN teaching assistant supports pupils with special educational needs and disabilities so they can take part in learning and school life. The role can be one-to-one, small group or across a specialist class."),
            ("h2", "A typical day"),
            ("p", "Days usually start by preparing resources and checking the plan with the class teacher or SENCO. Through the day you might adapt tasks, use visual supports, help a pupil regulate their emotions, support personal care and record progress against EHCP outcomes."),
            ("h2", "Needs you might support"),
            ("p", "Common needs include autism, ADHD, speech, language and communication needs, social, emotional and mental health needs, moderate learning difficulties and physical or sensory needs. Every pupil is different, which is why the right match matters."),
            ("h2", "Useful training"),
            ("p", "Safeguarding, autism awareness, Makaton, Team Teach or other positive behaviour support training, and first aid all make you a stronger candidate."),
            ("h2", "SEN TA roles near you"),
            ("p", "We recruit SEN teaching assistants for mainstream and specialist schools across the East of England. Register and tell us the needs you have experience with."),
        ],
    },
    {
        "slug": "teaching-assistant-vs-hlta",
        "title": "Teaching assistant vs HLTA: what is the difference?",
        "desc": "How the teaching assistant and higher level teaching assistant roles compare on responsibility, qualifications and pay, and how to progress from TA to HLTA.",
        "img": "students", "alt": "HLTA teaching a group of secondary pupils",
        "body": [
            ("h2", "Responsibility"),
            ("p", "A teaching assistant supports the teacher and pupils during lessons. A higher level teaching assistant (HLTA) can lead whole classes, cover planned absence and run interventions with more independence."),
            ("h2", "Qualifications"),
            ("p", "TAs may hold Level 2 or 3 qualifications. HLTAs are usually assessed against the national HLTA standards, building on several years of classroom experience."),
            ("h2", "Pay"),
            ("p", "HLTA roles are paid at a higher rate than general TA roles because of the extra responsibility. Rates vary by school and contract, and we confirm them before you accept any role."),
            ("h2", "Moving up"),
            ("p", "Ask your school about HLTA assessment, take on intervention groups and keep a record of whole-class cover. Tell us you are working towards HLTA and we will look for roles that build that experience."),
        ],
    },
]

HOME_FAQ = [
    ("What roles does Teach Talent recruit for?",
     "We specialise in school support staff: teaching assistants, SEN teaching assistants, higher level teaching assistants (HLTAs) and one-to-one learning support assistants."),
    ("Which areas do you cover?",
     "We cover the East of England: Cambridgeshire, Norfolk, Suffolk, Essex, Hertfordshire and Bedfordshire, including Cambridge, Peterborough, Norwich, Ipswich, Chelmsford, Stevenage and Bedford."),
    ("How quickly can you provide cover?",
     "Call us from 7am for same-day cover. For long-term and permanent roles we usually share a shortlist within a few working days."),
    ("Are your candidates safeguarding checked?",
     "Yes. Every candidate has an enhanced DBS with barred list check, two verified references, right to work checks and a face-to-face or video interview before they are put forward, in line with Keeping Children Safe in Education."),
    ("Is it free to register as a candidate?",
     "Yes. Registering with Teach Talent is free for teaching assistants and support staff."),
]

SCHOOL_FAQ = [
    ("What does it cost to book a teaching assistant?",
     "Daily and long-term rates depend on the role, experience and length of booking. Call us or send a request and we will give you a clear rate with no hidden fees."),
    ("Can we meet a candidate before they start?",
     "Yes. For long-term, 1:1 and permanent roles we encourage a visit or trial day so you can see the fit."),
    ("What happens if someone is not the right fit?",
     "Tell us and we will replace them as quickly as possible. We would rather get the match right than fill a gap."),
    ("Can a temporary TA become permanent?",
     "Yes. If you want to make a placement permanent, we agree a fair transfer arrangement up front."),
]

CAND_FAQ = [
    ("How do I get paid?",
     "Weekly, through PAYE. You will receive a clear payslip and there are no umbrella company deductions."),
    ("Do I need a DBS already?",
     "No. If you do not have an enhanced DBS on the Update Service we will help you apply."),
    ("Can I choose where I work?",
     "Yes. Tell us how far you can travel and which days you are free. We only offer roles that suit you."),
    ("What documents do I need?",
     "Photo ID, proof of address, right to work documents, your CV and contact details for two referees."),
]

# ---------------------------------------------------------------- helpers
def icon(name, cls="ic"):
    with open(os.path.join(ICONS, name + ".svg")) as f:
        svg = f.read().strip()
    return svg.replace("<svg ", '<svg class="%s" aria-hidden="true" focusable="false" ' % cls, 1)


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def btn(label, href, kind="solid", extra=""):
    return '<a class="btn btn--%s" href="%s"%s><span>%s</span>%s</a>' % (kind, href, extra, label, icon("arrow-right"))


def ld(obj):
    return '<script type="application/ld+json">%s</script>' % json.dumps(obj, ensure_ascii=False)


ORG_ID = SITE + "/#organisation"
AREA = [{"@type": "AdministrativeArea", "name": c["name"]} for c in COUNTIES]

ORG = {
    "@context": "https://schema.org",
    "@type": "EmploymentAgency",
    "@id": ORG_ID,
    "name": NAME,
    "description": "Education recruitment agency for teaching assistants, SEN teaching assistants, HLTAs and 1:1 support staff across the East of England.",
    "url": SITE + "/",
    "logo": SITE + "/images/mark.png",
    "image": SITE + "/share.jpg",
    "telephone": PHONE_INTL,
    "email": EMAIL,
    "priceRange": "££",
    "address": {"@type": "PostalAddress", "streetAddress": ADDRESS["street"], "addressLocality": ADDRESS["town"],
                "addressRegion": ADDRESS["region"], "postalCode": ADDRESS["postcode"], "addressCountry": "GB"},
    "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
                                   "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                                   "opens": "07:00", "closes": "18:00"}],
    "areaServed": AREA,
    "knowsAbout": ["Teaching assistant recruitment", "SEN teaching assistant recruitment", "HLTA recruitment",
                   "1:1 learning support assistants", "Education supply cover", "Safer recruitment"],
    "potentialAction": {"@type": "ReserveAction", "name": "Request support staff",
                        "target": SITE + "/for-schools/#request"},
}


def faq_ld(items):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}


def crumbs_ld(trail):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + p}
                                for i, (n, p) in enumerate(trail)]}


def crumbs(trail):
    parts = []
    for i, (n, p) in enumerate(trail):
        if i == len(trail) - 1:
            parts.append('<span aria-current="page">%s</span>' % esc(n))
        else:
            parts.append('<a href="%s">%s</a>' % (p, esc(n)))
    return '<nav class="crumbs" aria-label="Breadcrumb">%s</nav>' % '<span class="sep">/</span>'.join(parts)


NAV = [("For Schools", "/for-schools/"), ("For Candidates", "/for-candidates/"), ("Jobs", "/jobs/"),
       ("Roles", "/roles/"), ("Areas", "/areas/"), ("About", "/about/"), ("Guides", "/guides/"),
       ("Contact", "/contact/")]


def logo():
    return ('<a class="logo" href="/" aria-label="Teach Talent home">'
            '<img src="/images/mark.png" alt="" width="36" height="38">'
            '<span class="logo__word"><span class="logo__name"><b>Teach</b> <i>Talent</i></span>'
            '<span class="logo__tag">Education Recruitment Agency</span></span></a>')


def header(path):
    links = []
    for n, p in NAV:
        cur = ' aria-current="page"' if path.startswith(p) else ""
        links.append('<li><a href="%s"%s>%s</a></li>' % (p, cur, n))
    nav = "".join(links)
    return (
        '<a class="skip" href="#main">Skip to content</a>'
        '<header class="site-head"><div class="wrap site-head__in">' + logo() +
        '<nav class="nav" aria-label="Main"><ul>' + nav + '</ul></nav>'
        '<div class="site-head__cta">' + btn(HIRE[0], HIRE[1], "ghost") + btn(FIND[0], FIND[1], "solid") + '</div>'
        '<button class="burger" type="button" aria-expanded="false" aria-controls="menu" aria-label="Open menu">'
        '<span></span><span></span></button></div></header>'
        '<div class="menu" id="menu" hidden><div class="menu__in wrap">'
        '<nav aria-label="Mobile"><ol>' +
        "".join('<li><a href="%s"><small>(%02d)</small>%s</a></li>' % (p, i + 1, n) for i, (n, p) in enumerate(NAV)) +
        '</ol></nav><div class="menu__cta">' + btn(HIRE[0], HIRE[1], "ghost") + btn(FIND[0], FIND[1], "solid") +
        '</div><p class="menu__contact"><a href="tel:%s">%s</a><a href="mailto:%s">%s</a></p></div></div>' % (
            PHONE_INTL, PHONE, EMAIL, EMAIL)
    )


def footer():
    roles = "".join('<li><a href="/roles/%s/">%s</a></li>' % (r["slug"], r["name"]) for r in ROLES)
    areas = "".join('<li><a href="/areas/%s/">%s</a></li>' % (c["slug"], c["name"]) for c in COUNTIES)
    return (
        '<aside class="float-card" aria-label="Quick contact"><p>Need cover this week?</p>'
        '<div><a class="btn btn--solid btn--sm" href="%s"><span>%s</span>%s</a>'
        '<a class="btn btn--line btn--sm" href="tel:%s"><span>Call us</span>%s</a></div></aside>' % (
            HIRE[1], HIRE[0], icon("arrow-right"), PHONE_INTL, icon("phone")) +
        '<footer class="site-foot"><div class="wrap">'
        '<div class="site-foot__big"><p class="display">Better support.<br><em>Stronger classrooms.</em></p>'
        '<div class="site-foot__cta">' + btn(HIRE[0], HIRE[1], "gold") + btn(FIND[0], FIND[1], "line-light") + '</div></div>'
        '<div class="site-foot__cols">'
        '<div>' + logo() + '<p>Specialist recruitment for teaching assistants, SEN support staff and HLTAs across the East of England.</p></div>'
        '<div><h2>Roles</h2><ul>' + roles + '</ul></div>'
        '<div><h2>Areas</h2><ul>' + areas + '</ul></div>'
        '<div><h2>Contact</h2><ul class="contact-list">'
        '<li>%s<a href="tel:%s">%s</a></li><li>%s<a href="mailto:%s">%s</a></li>'
        '<li>%s<span>%s, %s, %s</span></li><li>%s<span>%s</span></li></ul></div>' % (
            icon("phone"), PHONE_INTL, PHONE, icon("envelope-simple"), EMAIL, EMAIL,
            icon("map-pin"), ADDRESS["street"], ADDRESS["town"], ADDRESS["postcode"], icon("clock"), HOURS_TEXT) +
        '</div><div class="site-foot__base"><p>&copy; %d Teach Talent Ltd. Registered in England and Wales.</p>'
        '<ul><li><a href="/jobs/">Jobs</a></li><li><a href="/guides/">Guides</a></li><li><a href="/privacy/">Privacy</a></li>'
        '<li><a href="/sitemap.xml">Sitemap</a></li></ul></div></div></footer>' % date.today().year
    )


def page(path, title, desc, body, schema=(), noindex=False, og_img="/share.jpg"):
    url = SITE + path
    full_title = title if NAME in title else "%s | %s" % (title, NAME)
    robots = '<meta name="robots" content="noindex, follow">' if noindex else '<meta name="robots" content="index, follow, max-image-preview:large">'
    head = (
        '<!doctype html><html lang="en-GB"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<title>%s</title><meta name="description" content="%s">%s'
        '<link rel="canonical" href="%s">'
        '<meta property="og:type" content="website"><meta property="og:site_name" content="%s">'
        '<meta property="og:title" content="%s"><meta property="og:description" content="%s">'
        '<meta property="og:url" content="%s"><meta property="og:image" content="%s%s">'
        '<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">'
        '<meta property="og:locale" content="en_GB">'
        '<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="%s">'
        '<meta name="twitter:description" content="%s"><meta name="twitter:image" content="%s%s">'
        '<meta name="theme-color" content="#F6F3EC">'
        '<meta name="geo.region" content="GB-CAM"><meta name="geo.placename" content="East of England">'
        '<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon.png" type="image/png">'
        '<link rel="preload" href="/fonts/CormorantGaramond.woff2" as="font" type="font/woff2" crossorigin>'
        '<link rel="preload" href="/fonts/Manrope.woff2" as="font" type="font/woff2" crossorigin>'
        '<link rel="stylesheet" href="/css/style.css">'
        '<script>document.documentElement.classList.add("js")</script>'
        '<script src="/js/main.js" defer></script>'
    ) % (esc(full_title), esc(desc), robots, url, NAME, esc(full_title), esc(desc), url, SITE, og_img,
         esc(full_title), esc(desc), SITE, og_img)
    head += "".join(ld(s) for s in schema)
    html = head + '</head><body>' + header(path) + '<main id="main">' + body + '</main>' + footer() + '</body></html>'
    for bad in ("—", "–"):
        assert bad not in html, "dash found on %s" % path
    out = os.path.join(SITE_DIR, path.lstrip("/"))
    if path.endswith("/"):
        out = os.path.join(out, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        f.write(html)
    PAGES.append((path, noindex))


PAGES = []

# ---------------------------------------------------------------- sections
def faq_block(items, title="Questions, answered"):
    rows = "".join(
        '<details class="faq__item"><summary><span>%s</span>%s</summary><div class="faq__a"><p>%s</p></div></details>' % (
            esc(q), icon("plus", "ic faq__ic"), esc(a)) for q, a in items)
    return ('<section class="section faq"><div class="wrap faq__grid"><div class="reveal">'
            '<p class="eyebrow">FAQ</p><h2 class="h2">%s</h2></div><div class="faq__list reveal">%s</div></div></section>') % (title, rows)


def roles_list(heading="Who we place", intro=""):
    rows = "".join(
        '<li class="reveal"><a href="/roles/%s/"><span class="idx">(%02d)</span><span class="t">%s</span>'
        '<span class="d">%s</span>%s</a></li>' % (r["slug"], i + 1, r["name"], r["short"], icon("arrow-up-right", "ic arr"))
        for i, r in enumerate(ROLES))
    return ('<section class="section roles" id="roles"><div class="wrap"><div class="sec-head reveal"><p class="eyebrow">%s</p>'
            '<p class="lede">%s</p></div><ol class="roles__list">%s</ol></div></section>') % (heading, intro, rows)


def steps(items, heading):
    li = "".join('<li class="reveal"><span class="step__n">%02d</span><h3>%s</h3><p>%s</p></li>' % (i + 1, t, d)
                 for i, (t, d) in enumerate(items))
    return ('<section class="section steps"><div class="wrap"><h2 class="h2 reveal">%s</h2>'
            '<ol class="steps__list">%s</ol></div></section>') % (heading, li)


def areas_strip(heading="Across the East of England"):
    li = "".join('<li><a href="/areas/%s/"><span>%s</span><small>%s</small></a></li>' % (
        c["slug"], c["name"], ", ".join(c["towns"][:3])) for c in COUNTIES)
    return ('<section class="section areas"><div class="wrap"><div class="areas__head reveal"><p class="eyebrow">Where we work</p>'
            '<h2 class="h2">%s</h2><a class="link" href="/areas/">All areas %s</a></div>'
            '<ul class="areas__list reveal">%s</ul></div></section>') % (heading, icon("arrow-right"), li)


def cta_band(title, text):
    return ('<section class="cta-band"><div class="wrap cta-band__in reveal"><h2 class="display">%s</h2><p>%s</p>'
            '<div class="cta-band__btns">%s%s</div></div></section>') % (title, text, btn(HIRE[0], HIRE[1], "gold"),
                                                                          btn(FIND[0], FIND[1], "line-light"))


def page_hero(eyebrow, title, lede, trail, img=None, alt="", ctas=True):
    cta = '<div class="cta-row">%s%s</div>' % (btn(HIRE[0], HIRE[1], "solid"), btn(FIND[0], FIND[1], "line")) if ctas else ""
    pic = ""
    if img:
        pic = '<figure class="phero__img reveal"><img src="/images/%s.webp" alt="%s" width="1000" height="1200" fetchpriority="high"></figure>' % (img, esc(alt))
    return ('<section class="phero%s"><div class="wrap phero__in"><div class="phero__txt">%s<p class="eyebrow">%s</p>'
            '<h1 class="h1">%s</h1><p class="lede">%s</p>%s</div>%s</div></section>') % (
        " phero--img" if img else "", crumbs(trail), eyebrow, title, lede, cta, pic)


def field(name, label, kind="text", req=True, auto="", opts=None, full=False, hint=""):
    r = " required" if req else ""
    star = "" if req else ' <span class="opt">(optional)</span>'
    a = ' autocomplete="%s"' % auto if auto else ""
    cls = "field field--full" if full else "field"
    fid = "f-" + name
    hint_html = '<span class="hint">%s</span>' % hint if hint else ""
    if kind == "select":
        o = '<option value="">Choose one</option>' + "".join('<option>%s</option>' % x for x in opts)
        inp = '<select id="%s" name="%s"%s>%s</select>' % (fid, name, r, o)
    elif kind == "textarea":
        inp = '<textarea id="%s" name="%s" rows="4"%s></textarea>' % (fid, name, r)
    else:
        inp = '<input id="%s" name="%s" type="%s"%s%s>' % (fid, name, kind, a, r)
    return '<div class="%s"><label for="%s">%s%s</label>%s%s<span class="err" aria-live="polite"></span></div>' % (
        cls, fid, label, star, hint_html, inp)


def form(name, fields, submit, multipart=False):
    enc = ' enctype="multipart/form-data"' if multipart else ""
    return ('<form class="form" name="%s" method="POST" action="/thanks/" data-netlify="true" netlify-honeypot="company_url" novalidate%s>'
            '<input type="hidden" name="form-name" value="%s"><p class="hp"><label>Leave this empty <input name="company_url"></label></p>'
            '<div class="form__grid">%s</div><button class="btn btn--solid" type="submit"><span>%s</span>%s</button>'
            '<p class="form__note">We reply within one working day. See our <a href="/privacy/">privacy notice</a>.</p></form>') % (
        name, enc, name, "".join(fields), submit, icon("arrow-right"))


COUNTY_NAMES = [c["name"] for c in COUNTIES]
ROLE_NAMES = [r["single"] for r in ROLES]

# ---------------------------------------------------------------- pages
def build_home():
    hero = (
        '<section class="hero" aria-labelledby="hero-title"><div class="hero__stage">'
        '<figure class="hero__img"><img src="/images/hero-reading.webp" alt="Teaching assistant reading a book with a young pupil in a school library" width="900" height="1100" fetchpriority="high"></figure>'
        '<h1 class="hero__title" id="hero-title"><span class="sr">Teach Talent: teaching assistant and SEN recruitment across the East of England. </span>'
        '<span aria-hidden="true" class="hero__lines"><span class="l"><span>The talent</span></span><span class="l"><span>behind every</span></span><span class="l"><span>classroom</span></span></span></h1>'
        '<div class="hero__clip" aria-hidden="true"><span class="hero__lines"><span class="l"><span>The talent</span></span><span class="l"><span>behind every</span></span><span class="l"><span>classroom</span></span></span></div>'
        '</div><div class="wrap hero__foot"><p class="hero__sub">Teaching assistants, SEN support and HLTAs for schools across Cambridgeshire, Norfolk, Suffolk, Essex, Hertfordshire and Bedfordshire.</p>'
        '<div class="hero__btns">' + btn(HIRE[0], HIRE[1], "solid") + btn(FIND[0], FIND[1], "line") + '</div>'
        '<ul class="hero__meta"><li>East of England specialists</li><li>Enhanced DBS on every candidate</li></ul></div></section>'
    )
    statement = (
        '<section class="section statement"><div class="wrap"><p class="statement__txt reveal">'
        'Teach Talent is an education recruitment agency built for one job: finding the <em>teaching assistants</em> and '
        '<em>SEN support staff</em> that schools in the East of England depend on, and treating them well enough that they stay.</p></div></section>'
    )
    paths = (
        '<section class="section paths"><div class="wrap paths__grid">'
        '<article class="path reveal"><figure><img src="/images/classroom.webp" alt="Pupils raising hands in a primary classroom" width="1400" height="900" loading="lazy"></figure>'
        '<p class="eyebrow">For schools</p><h2 class="h2">Support staff you can rely on from the first morning</h2>'
        '<ul class="ticks"><li>%s Same-day, long-term and permanent</li><li>%s Safer recruitment on every candidate</li><li>%s One consultant who knows your school</li></ul>%s</article>'
        '<article class="path reveal"><figure><img src="/images/workbook.webp" alt="Teaching assistant helping a pupil with a workbook" width="1000" height="1200" loading="lazy"></figure>'
        '<p class="eyebrow">For candidates</p><h2 class="h2">Work that fits your life, in schools near you</h2>'
        '<ul class="ticks"><li>%s Weekly PAYE pay, no umbrella fees</li><li>%s Roles matched to your experience</li><li>%s Free to register, help with your DBS</li></ul>%s</article>'
        '</div></section>'
    ) % (icon("check"), icon("check"), icon("check"), btn(HIRE[0], HIRE[1], "solid"),
         icon("check"), icon("check"), icon("check"), btn(FIND[0], FIND[1], "solid"))
    problem = (
        '<section class="section problem"><div class="wrap problem__grid"><div class="reveal"><p class="eyebrow">The problem</p>'
        '<h2 class="h2">A missing TA is never just one missing person</h2></div><div class="problem__txt reveal">'
        '<p>When support staff are absent, interventions stop, 1:1 pupils lose the adult they trust and teachers lose the help that makes the lesson work. '
        'Generalist agencies treat support roles as an afterthought. We do the opposite.</p>'
        '<p>Support staff are our specialism, so we know what a good SEN match looks like, which candidates can handle a Year 6 class and who lives close enough to be reliable every day.</p></div></div></section>'
    )
    how = steps([
        ("Tell us what you need", "Call from 7am or send a request. We ask about the role, the pupils and how your school works."),
        ("Meet your shortlist", "We send fully checked candidates who fit, with clear rates. For long-term roles you can meet them first."),
        ("We stay in touch", "Your consultant checks in after day one and through the placement, and replaces anyone who is not right."),
    ], "How it works")
    quotes = (
        '<section class="section voices"><div class="wrap"><p class="eyebrow reveal">What schools and staff say</p>'
        '<div class="voices__grid">'
        '<figure class="voice reveal"><blockquote>&ldquo;They listened to what our SEN pupil needed and sent someone who was a perfect match within the week.&rdquo;</blockquote><figcaption>SENCO, primary school, Cambridgeshire</figcaption></figure>'
        '<figure class="voice reveal"><blockquote>&ldquo;The first agency that asked what hours I could actually do. Paid every week, no surprises.&rdquo;</blockquote><figcaption>Teaching assistant, Suffolk</figcaption></figure>'
        '<figure class="voice reveal"><blockquote>&ldquo;Reliable at 7am on a Monday, which is all a headteacher really wants.&rdquo;</blockquote><figcaption>Headteacher, Hertfordshire</figcaption></figure>'
        '</div></div></section>'
    )
    trust = (
        '<section class="section trust"><div class="wrap trust__grid">' +
        "".join('<div class="trust__item reveal">%s<h3>%s</h3><p>%s</p></div>' % (icon(i, "ic ic--lg"), t, d) for i, t, d in [
            ("shield-check", "Safer recruitment", "Enhanced DBS, barred list, two references and right to work checks, in line with KCSIE."),
            ("clock", "Open from 7am", "Early-morning cover line so your day starts staffed."),
            ("handshake", "One consultant", "A named person who knows your school and your pupils."),
            ("heart", "Staff who stay", "Fair weekly pay and real support mean fewer gaps for you."),
        ]) + '</div></section>'
    )
    body = hero + statement + paths + roles_list("Who we place", "Specialists in school support staff. Nothing else.") + problem + how + trust + areas_strip() + quotes + faq_block(HOME_FAQ) + cta_band(
        "Ready when <em>you</em> are", "Tell us about the role, or tell us about you. Either way, we will be in touch within one working day.")
    web = {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": NAME,
           "publisher": {"@id": ORG_ID}, "inLanguage": "en-GB"}
    page("/", "Teaching Assistant & SEN Recruitment Agency East of England | Teach Talent",
         "Teach Talent recruits teaching assistants, SEN TAs, HLTAs and 1:1 support staff for schools across Cambridgeshire, Norfolk, Suffolk, Essex, Hertfordshire and Bedfordshire.",
         body, [ORG, web, faq_ld(HOME_FAQ)])


def build_schools():
    trail = [("Home", "/"), ("For Schools", "/for-schools/")]
    services = (
        '<section class="section services"><div class="wrap"><h2 class="h2 reveal">How we can help</h2><div class="services__grid">' +
        "".join('<article class="svc reveal"><span class="idx">(%02d)</span><h3>%s</h3><p>%s</p></article>' % (i + 1, t, d) for i, (t, d) in enumerate([
            ("Day-to-day cover", "Short-notice TA and SEN cover for sickness, trips and training days. Call from 7am."),
            ("Long-term placements", "Half-term, term or full-year cover for maternity leave, vacancies and extra support."),
            ("Permanent recruitment", "We advertise, screen and shortlist so you only interview people worth meeting."),
            ("1:1 and EHCP support", "Carefully matched one-to-one assistants for pupils with specific needs."),
        ])) + '</div></div></section>'
    )
    compliance = (
        '<section class="section compliance"><div class="wrap compliance__grid"><div class="reveal"><p class="eyebrow">Safer recruitment</p>'
        '<h2 class="h2">Every candidate checked before they reach your door</h2><p>Our process follows Keeping Children Safe in Education. You can request a full compliance summary for anyone we put forward.</p></div>'
        '<ul class="checks reveal">' + "".join('<li>%s<span>%s</span></li>' % (icon("check"), x) for x in [
            "Enhanced DBS with barred list check", "Two verified professional references", "Right to work in the UK confirmed",
            "Photo ID and proof of address", "Face-to-face or video interview", "Safeguarding training confirmed",
            "Qualifications verified", "Overseas police checks where needed"]) + '</ul></div></section>'
    )
    req = (
        '<section class="section request" id="request"><div class="wrap request__grid"><div class="reveal"><p class="eyebrow">Staffing request</p>'
        '<h2 class="h2">Tell us who you need</h2><p>Send the basics and your consultant will call you back, usually the same day. For cover tomorrow morning, call <a href="tel:%s">%s</a>.</p></div>' % (PHONE_INTL, PHONE) +
        form("school-request", [
            field("school", "School name", auto="organization"),
            field("name", "Your name", auto="name"),
            field("email", "Email", "email", auto="email"),
            field("phone", "Phone", "tel", auto="tel"),
            field("role", "Role needed", "select", opts=ROLE_NAMES + ["Not sure yet"]),
            field("type", "Type of booking", "select", opts=["Day-to-day", "Long term", "Permanent", "1:1 / EHCP"]),
            field("county", "County", "select", opts=COUNTY_NAMES),
            field("start", "Start date", "date", req=False),
            field("details", "Anything we should know?", "textarea", req=False, full=True),
        ], "Send request") + '</div></section>'
    )
    body = page_hero("For schools", "Teaching assistant and SEN supply for East of England schools",
                     "Reliable teaching assistants, SEN TAs, HLTAs and 1:1 support for primary, secondary and specialist schools, from same-day cover to permanent hires.",
                     trail, "classroom", "Pupils raising hands in a primary classroom") + services + compliance + steps([
                         ("Request", "Call or send the form with the role, dates and any pupil needs."),
                         ("Shortlist", "We send checked candidates with clear rates, often the same day."),
                         ("Start and review", "Your consultant follows up after day one and through the placement."),
                     ], "Three steps to a staffed classroom") + req + faq_block(SCHOOL_FAQ) + areas_strip("Schools we support")
    page("/for-schools/", "Teaching Assistant Supply for Schools in the East of England",
         "Book teaching assistants, SEN TAs, HLTAs and 1:1 support staff for your school. Same-day cover from 7am, long-term and permanent recruitment across the East of England.",
         body, [ORG, faq_ld(SCHOOL_FAQ), crumbs_ld(trail),
                {"@context": "https://schema.org", "@type": "Service", "serviceType": "Education support staff recruitment",
                 "provider": {"@id": ORG_ID}, "areaServed": AREA}])


def build_candidates():
    trail = [("Home", "/"), ("For Candidates", "/for-candidates/")]
    perks = (
        '<section class="section services"><div class="wrap"><h2 class="h2 reveal">Why register with us</h2><div class="services__grid">' +
        "".join('<article class="svc reveal"><span class="idx">(%02d)</span><h3>%s</h3><p>%s</p></article>' % (i + 1, t, d) for i, (t, d) in enumerate([
            ("Weekly PAYE pay", "Paid every week with a clear payslip. No umbrella company fees."),
            ("Work near home", "We match you to schools within the distance you choose."),
            ("Flexible or permanent", "Pick the days you want on supply, or let us find a permanent post."),
            ("Training and support", "Help with your DBS plus guidance on safeguarding and SEN training."),
        ])) + '</div></div></section>'
    )
    reg = (
        '<section class="section request" id="register"><div class="wrap request__grid"><div class="reveal"><p class="eyebrow">Register</p>'
        '<h2 class="h2">Register in two minutes</h2><p>Tell us a little about you. A consultant will call to talk through roles and next steps. Registering is free.</p></div>' +
        form("candidate-register", [
            field("name", "Full name", auto="name"),
            field("email", "Email", "email", auto="email"),
            field("phone", "Phone", "tel", auto="tel"),
            field("postcode", "Postcode", auto="postal-code"),
            field("role", "Role you want", "select", opts=ROLE_NAMES),
            field("availability", "Availability", "select", opts=["Day-to-day supply", "Long term", "Permanent", "Open to anything"]),
            field("cv", "Upload your CV", "file", req=False, hint="PDF or Word, up to 8MB"),
            field("experience", "Your experience in a sentence or two", "textarea", req=False, full=True),
        ], "Register now", multipart=True) + '</div></section>'
    )
    body = page_hero("For candidates", "Teaching assistant and SEN jobs near you",
                     "Whether you are new to schools or an experienced HLTA, we find TA and SEN roles across the East of England that suit your skills, your hours and your journey.",
                     trail, "workbook", "Teaching assistant helping a pupil with a workbook") + perks + roles_list("Roles you can register for", "") + steps([
                         ("Register", "Fill in the form and upload your CV if you have one."),
                         ("Chat and checks", "A short call, then we complete your DBS, references and right to work."),
                         ("Start work", "We offer roles that match your preferences. You choose what to accept."),
                     ], "From sign-up to first day") + reg + faq_block(CAND_FAQ)
    page("/for-candidates/", "Teaching Assistant & SEN TA Jobs East of England",
         "Register free for teaching assistant, SEN TA, HLTA and 1:1 support jobs in Cambridgeshire, Norfolk, Suffolk, Essex, Hertfordshire and Bedfordshire. Weekly PAYE pay.",
         body, [ORG, faq_ld(CAND_FAQ), crumbs_ld(trail)])


def job_ld(j):
    return {"@context": "https://schema.org", "@type": "JobPosting", "title": j["title"], "description": "<p>%s</p><ul>%s</ul>" % (
        j["summary"], "".join("<li>%s</li>" % d for d in j["details"])), "datePosted": j["posted"], "validThrough": j["closes"],
        "employmentType": j["employment"], "hiringOrganization": {"@type": "Organization", "name": NAME, "sameAs": SITE},
        "jobLocation": {"@type": "Place", "address": {"@type": "PostalAddress", "addressLocality": j["town"],
                                                       "addressRegion": j["county"], "addressCountry": "GB"}},
        "baseSalary": {"@type": "MonetaryAmount", "currency": "GBP", "value": {"@type": "QuantitativeValue", "minValue": j["pay_min"],
                                                                                "maxValue": j["pay_max"], "unitText": j["pay_unit"]}}}


def build_jobs():
    trail = [("Home", "/"), ("Jobs", "/jobs/")]
    if JOBS:
        cards = "".join(
            '<li class="job reveal"><a href="/jobs/%s/"><h2>%s</h2><p class="job__meta"><span>%s, %s</span><span>%s</span><span>%s</span></p>'
            '<p>%s</p>%s</a></li>' % (j["slug"], esc(j["title"]), j["town"], j["county"], j["type"], j["pay"], esc(j["summary"]),
                                       icon("arrow-up-right", "ic arr")) for j in JOBS)
        listing = '<ul class="jobs__list">%s</ul>' % cards
    else:
        listing = (
            '<div class="jobs__empty reveal"><p class="display">New roles are on their way.</p>'
            '<p>We are adding live teaching assistant and SEN vacancies across the East of England. Register now and we will contact you about roles before they are posted here.</p>'
            '<div class="cta-row">' + btn(FIND[0], FIND[1], "solid") + '</div></div>')
    filt = (
        '<div class="jobs__filter reveal" aria-label="Browse by area and role"><div><p class="eyebrow">By area</p><ul class="chips">' +
        "".join('<li><a href="/areas/%s/">%s</a></li>' % (c["slug"], c["name"]) for c in COUNTIES) +
        '</ul></div><div><p class="eyebrow">By role</p><ul class="chips">' +
        "".join('<li><a href="/roles/%s/">%s</a></li>' % (r["slug"], r["name"]) for r in ROLES) + '</ul></div></div>'
    )
    alert = (
        '<section class="section request" id="alerts"><div class="wrap request__grid"><div class="reveal"><p class="eyebrow">Job alerts</p>'
        '<h2 class="h2">Hear about new roles first</h2><p>Leave your email, role and county. We will only email you about matching vacancies.</p></div>' +
        form("job-alerts", [
            field("email", "Email", "email", auto="email"),
            field("role", "Role", "select", opts=ROLE_NAMES),
            field("county", "County", "select", opts=COUNTY_NAMES),
        ], "Get job alerts") + '</div></section>'
    )
    body = page_hero("Jobs", "Teaching assistant and SEN jobs in the East of England",
                     "Live vacancies for teaching assistants, SEN TAs, HLTAs and 1:1 support staff across Cambridgeshire, Norfolk, Suffolk, Essex, Hertfordshire and Bedfordshire.", trail) + \
        '<section class="section jobs"><div class="wrap">' + listing + filt + '</div></section>' + alert
    page("/jobs/", "Teaching Assistant & SEN Jobs | East of England Vacancies",
         "Browse teaching assistant, SEN TA, HLTA and 1:1 support jobs in schools across the East of England, or set up job alerts for new vacancies near you.",
         body, [ORG, crumbs_ld(trail)] + [job_ld(j) for j in JOBS])
    for j in JOBS:
        jt = trail + [(j["title"], "/jobs/%s/" % j["slug"])]
        jb = page_hero("%s, %s" % (j["town"], j["county"]), esc(j["title"]), esc(j["summary"]), jt) + \
            '<section class="section prose-sec"><div class="wrap prose"><p><strong>Contract:</strong> %s<br><strong>Pay:</strong> %s<br><strong>Start:</strong> %s</p><ul>%s</ul>%s</div></section>' % (
                j["type"], j["pay"], j["start"], "".join("<li>%s</li>" % esc(d) for d in j["details"]), btn("Apply for this role", FIND[1], "solid"))
        page("/jobs/%s/" % j["slug"], "%s in %s" % (j["title"], j["town"]), j["summary"][:155], jb, [job_ld(j), crumbs_ld(jt)])


def build_roles():
    trail = [("Home", "/"), ("Roles", "/roles/")]
    body = page_hero("Roles", "The support staff we recruit",
                     "We specialise in the people who support learning: teaching assistants, SEN teaching assistants, HLTAs and one-to-one learning support assistants.", trail) + \
        roles_list("Four specialisms", "") + cta_band("Need one of <em>these</em>?", "Tell us the role and we will start your shortlist today.")
    page("/roles/", "Teaching Assistant, SEN, HLTA & 1:1 Support Roles",
         "The school support roles Teach Talent recruits for across the East of England: teaching assistants, SEN TAs, HLTAs and one-to-one learning support assistants.",
         body, [ORG, crumbs_ld(trail)])
    for r in ROLES:
        rt = trail + [(r["single"], "/roles/%s/" % r["slug"])]
        lst = lambda xs: "".join('<li>%s<span>%s</span></li>' % (icon("check"), x) for x in xs)
        town_links = ", ".join('<a href="/areas/%s/">%s</a>' % (c["slug"], c["name"]) for c in COUNTIES)
        body = page_hero(r["name"], "%s recruitment in the East of England" % r["single"], r["lead"], rt, r["img"], r["alt"]) + (
            '<section class="section split"><div class="wrap split__grid"><div class="reveal"><h2 class="h3">What the role involves</h2><ul class="checks checks--one">%s</ul></div>'
            '<div class="reveal"><h2 class="h3">What schools look for</h2><ul class="checks checks--one">%s</ul></div></div></section>'
            '<section class="section duo"><div class="wrap duo__grid">'
            '<div class="duo__card reveal"><p class="eyebrow">Schools</p><h2 class="h3">Need a %s?</h2><p>Same-day, long-term and permanent %s placements, fully checked.</p>%s</div>'
            '<div class="duo__card duo__card--navy reveal"><p class="eyebrow">Candidates</p><h2 class="h3">Looking for %s work?</h2><p>Register once and we will match you with schools near you.</p>%s</div></div></section>'
            '<section class="section prose-sec"><div class="wrap prose reveal"><h2 class="h3">Where we place %ss</h2><p>We recruit %ss for schools in %s, including %s.</p></div></section>'
        ) % (lst(r["does"]), lst(r["need"]), r["single"].lower(), r["single"].lower(), btn(HIRE[0], HIRE[1], "solid"),
             r["single"].lower(), btn(FIND[0], FIND[1], "gold"), r["single"].lower(), r["single"].lower(), town_links,
             ", ".join(c["towns"][0] for c in COUNTIES)) + faq_block(r["faq"])
        page("/roles/%s/" % r["slug"], "%s Recruitment Agency | East of England" % r["single"],
             ("%s jobs and %s supply for schools in Cambridgeshire, Norfolk, Suffolk, Essex, Hertfordshire and Bedfordshire. " % (r["single"], r["single"].lower()) +
              "Specialist recruitment by Teach Talent.")[:160],
             body, [ORG, faq_ld(r["faq"]), crumbs_ld(rt),
                    {"@context": "https://schema.org", "@type": "Service", "serviceType": "%s recruitment" % r["single"],
                     "provider": {"@id": ORG_ID}, "areaServed": AREA}])


def build_areas():
    trail = [("Home", "/"), ("Areas", "/areas/")]
    cards = "".join(
        '<li class="reveal"><a href="/areas/%s/"><span class="idx">(%02d)</span><span class="t">%s</span><span class="d">%s</span>%s</a></li>' % (
            c["slug"], i + 1, c["name"], ", ".join(c["towns"][:5]), icon("arrow-up-right", "ic arr")) for i, c in enumerate(COUNTIES))
    body = page_hero("Areas we cover", "Education recruitment across the East of England",
                     "Teach Talent places teaching assistants and SEN support staff in schools across six counties. Choose your county to see the towns we cover.", trail) + \
        '<section class="section roles"><div class="wrap"><ol class="roles__list">%s</ol></div></section>' % cards + \
        cta_band("Your school, <em>staffed</em>", "Wherever you are in the East of England, tell us what you need.")
    page("/areas/", "Education Recruitment Agency East of England | Areas Covered",
         "Teaching assistant and SEN recruitment in Cambridgeshire, Norfolk, Suffolk, Essex, Hertfordshire and Bedfordshire. See the towns and schools Teach Talent covers.",
         body, [ORG, crumbs_ld(trail)])
    for c in COUNTIES:
        ct = trail + [(c["name"], "/areas/%s/" % c["slug"])]
        faq = [
            ("Do you recruit teaching assistants in %s?" % c["name"],
             "Yes. We place teaching assistants, SEN TAs, HLTAs and 1:1 support staff in schools across %s, including %s." % (c["name"], ", ".join(c["towns"][:5]))),
            ("Can you provide same-day TA cover in %s?" % c["name"],
             "Call us from 7am. We keep a pool of checked support staff who live in and around %s so we can respond quickly." % ", ".join(c["towns"][:3])),
            ("How do I find TA jobs in %s?" % c["name"],
             "Register with Teach Talent, tell us how far you can travel, and we will match you with schools in %s that suit you." % c["name"]),
        ]
        towns = "".join("<li>%s</li>" % t for t in c["towns"])
        others = "".join('<li><a href="/areas/%s/">%s</a></li>' % (o["slug"], o["name"]) for o in COUNTIES if o is not c)
        role_links = "".join('<li><a href="/roles/%s/">%s in %s</a></li>' % (r["slug"], r["name"], c["name"]) for r in ROLES)
        body = page_hero(c["name"], "Teaching assistant and SEN recruitment in %s" % c["name"], c["intro"], ct) + (
            '<section class="section split"><div class="wrap split__grid"><div class="reveal"><h2 class="h3">Towns we cover in %s</h2><ul class="towns">%s</ul><p class="muted">%s</p></div>'
            '<div class="reveal"><h2 class="h3">Roles we fill in %s</h2><ul class="links">%s</ul></div></div></section>'
            '<section class="section duo"><div class="wrap duo__grid">'
            '<div class="duo__card reveal"><p class="eyebrow">%s schools</p><h2 class="h3">Book support staff</h2><p>Same-day cover from 7am, plus long-term and permanent recruitment.</p>%s</div>'
            '<div class="duo__card duo__card--navy reveal"><p class="eyebrow">%s candidates</p><h2 class="h3">Find TA work near you</h2><p>Weekly PAYE pay and roles within your travel distance.</p>%s</div></div></section>'
        ) % (c["name"], towns, c["note"], c["name"], role_links, c["name"], btn(HIRE[0], HIRE[1], "solid"), c["name"], btn(FIND[0], FIND[1], "gold")) + \
            faq_block(faq) + '<section class="section"><div class="wrap"><p class="eyebrow">Other areas</p><ul class="chips">%s</ul></div></section>' % others
        page("/areas/%s/" % c["slug"], "Teaching Assistant Recruitment Agency %s | SEN & TA Jobs" % c["name"],
             ("Teaching assistant and SEN recruitment in %s: %s. Same-day cover, long-term and permanent roles." % (c["name"], ", ".join(c["towns"][:4])))[:160],
             body, [dict(ORG, areaServed={"@type": "AdministrativeArea", "name": c["name"]}), faq_ld(faq), crumbs_ld(ct)])


def build_about():
    trail = [("Home", "/"), ("About", "/about/")]
    values = "".join('<article class="svc reveal"><span class="idx">(%02d)</span><h3>%s</h3><p>%s</p></article>' % (i + 1, t, d) for i, (t, d) in enumerate([
        ("Specialist", "We recruit support staff only, so we understand the roles in depth."),
        ("Local", "Based in Cambridge and focused on the East of England, not the whole country."),
        ("Careful", "Safer recruitment on every candidate, every time."),
        ("Fair", "Clear rates for schools, weekly pay for staff, no hidden fees for anyone."),
    ]))
    body = page_hero("About Teach Talent", "An education recruitment agency built around support staff",
                     "Teaching assistants and SEN support staff hold classrooms together, yet they are often an afterthought for recruitment agencies. Teach Talent was set up to change that in the East of England.",
                     trail, "one-to-one", "Learning support assistant reading with a pupil") + \
        '<section class="section statement"><div class="wrap"><p class="statement__txt reveal">We believe the right support assistant can change a pupil\'s year. So we take time to understand each school, each pupil\'s needs and each candidate, and we only make a match when it is <em>genuinely right</em>.</p></div></section>' + \
        '<section class="section services"><div class="wrap"><h2 class="h2 reveal">What we stand for</h2><div class="services__grid">%s</div></div></section>' % values + \
        areas_strip("Rooted in the East of England") + cta_band("Let\'s <em>talk</em>", "Whether you run a school or work in one, we would love to hear from you.")
    page("/about/", "About Us | Education Recruitment Specialists East of England",
         "Teach Talent is a Cambridge-based education recruitment agency specialising in teaching assistants and SEN support staff for schools across the East of England.",
         body, [ORG, crumbs_ld(trail), {"@context": "https://schema.org", "@type": "AboutPage", "about": {"@id": ORG_ID}}])


def build_guides():
    trail = [("Home", "/"), ("Guides", "/guides/")]
    cards = "".join(
        '<li class="guide reveal"><a href="/guides/%s/"><figure><img src="/images/%s.webp" alt="%s" width="1000" height="800" loading="lazy"></figure>'
        '<h2 class="h3">%s</h2><p>%s</p><span class="link">Read guide %s</span></a></li>' % (
            g["slug"], g["img"], esc(g["alt"]), g["title"], g["desc"], icon("arrow-right")) for g in GUIDES)
    body = page_hero("Guides", "Guides for teaching assistants and schools",
                     "Practical advice on teaching assistant careers, SEN support and school staffing in the East of England.", trail) + \
        '<section class="section"><div class="wrap"><ul class="guides">%s</ul></div></section>' % cards
    page("/guides/", "Teaching Assistant Career Guides & Advice",
         "Guides on becoming a teaching assistant, SEN TA duties and the TA to HLTA path, written for support staff and schools in the East of England.",
         body, [ORG, crumbs_ld(trail)])
    for g in GUIDES:
        gt = trail + [(g["title"], "/guides/%s/" % g["slug"])]
        prose = "".join("<%s>%s</%s>" % (t, esc(x), t) for t, x in g["body"])
        body = page_hero("Guide", g["title"], g["desc"], gt, g["img"], g["alt"], ctas=False) + \
            '<section class="section prose-sec"><article class="wrap prose">%s<div class="cta-row">%s%s</div></article></section>' % (
                prose, btn(FIND[0], FIND[1], "solid"), btn(HIRE[0], HIRE[1], "line"))
        art = {"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["desc"],
               "image": SITE + "/images/%s.webp" % g["img"], "datePublished": TODAY, "dateModified": TODAY,
               "author": {"@type": "Organization", "name": NAME, "url": SITE}, "publisher": {"@id": ORG_ID},
               "mainEntityOfPage": SITE + "/guides/%s/" % g["slug"]}
        page("/guides/%s/" % g["slug"], g["title"], g["desc"][:160], body, [art, crumbs_ld(gt)])


def build_contact():
    trail = [("Home", "/"), ("Contact", "/contact/")]
    body = page_hero("Contact", "Talk to Teach Talent",
                     "Call, email or send a message. For same-day cover, phone us from 7am.", trail) + (
        '<section class="section request"><div class="wrap request__grid"><div class="reveal"><ul class="contact-big">'
        '<li><small>Phone</small><a href="tel:%s">%s</a></li><li><small>Email</small><a href="mailto:%s">%s</a></li>'
        '<li><small>Office</small><span>%s<br>%s, %s</span></li><li><small>Hours</small><span>%s</span></li></ul></div>' % (
            PHONE_INTL, PHONE, EMAIL, EMAIL, ADDRESS["street"], ADDRESS["town"], ADDRESS["postcode"], HOURS_TEXT) +
        form("contact", [
            field("name", "Your name", auto="name"),
            field("email", "Email", "email", auto="email"),
            field("phone", "Phone", "tel", req=False, auto="tel"),
            field("about", "I am a", "select", opts=["School", "Candidate", "Other"]),
            field("message", "Message", "textarea", full=True),
        ], "Send message") + '</div></section>')
    page("/contact/", "Contact Teach Talent | Education Recruitment Cambridge",
         "Contact Teach Talent for teaching assistant and SEN cover or to register for work. Phone from 7am, Monday to Friday. Covering the East of England.",
         body, [ORG, crumbs_ld(trail), {"@context": "https://schema.org", "@type": "ContactPage", "about": {"@id": ORG_ID}}])


def build_misc():
    page("/privacy/", "Privacy Notice", "How Teach Talent collects, uses and protects personal data from schools and candidates.",
         page_hero("Legal", "Privacy notice", "Placeholder: the client's full UK GDPR privacy notice goes here before launch.", [("Home", "/"), ("Privacy", "/privacy/")], ctas=False) +
         '<section class="section prose-sec"><div class="wrap prose"><h2>Who we are</h2><p>Teach Talent Ltd is the data controller for information you send us through this website.</p>'
         '<h2>What we collect</h2><p>Contact details, CV information and the details you provide in our forms, used only to respond to you and to find suitable roles or candidates.</p>'
         '<h2>Your rights</h2><p>You can ask to see, correct or delete your data at any time by emailing <a href="mailto:%s">%s</a>.</p></div></section>' % (EMAIL, EMAIL))
    page("/thanks/", "Thank you", "Thanks for getting in touch with Teach Talent.",
         '<section class="phero"><div class="wrap phero__in"><div class="phero__txt"><p class="eyebrow">Received</p><h1 class="h1">Thank you. We will be in touch within one working day.</h1>'
         '<p class="lede">Need us sooner? Call <a href="tel:%s">%s</a>.</p><div class="cta-row">%s</div></div></div></section>' % (PHONE_INTL, PHONE, btn("Back to home", "/", "solid")),
         noindex=True)
    page("/404.html", "Page not found", "This page could not be found.",
         '<section class="phero"><div class="wrap phero__in"><div class="phero__txt"><p class="eyebrow">404</p><h1 class="h1">This page has moved or never existed.</h1>'
         '<div class="cta-row">%s%s</div></div></div></section>' % (btn("Home", "/", "solid"), btn("See jobs", "/jobs/", "line")), noindex=True)


def build_seo_files():
    urls = "".join("<url><loc>%s%s</loc><lastmod>%s</lastmod></url>" % (SITE, p, TODAY) for p, ni in PAGES if not ni)
    with open(os.path.join(SITE_DIR, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">%s</urlset>' % urls)
    with open(os.path.join(SITE_DIR, "robots.txt"), "w") as f:
        f.write("User-agent: *\nAllow: /\nDisallow: /thanks/\n\nSitemap: %s/sitemap.xml\n" % SITE)
    lines = ["# Teach Talent", "", "> Education recruitment agency for teaching assistants, SEN teaching assistants, HLTAs and 1:1 support staff across the East of England (Cambridgeshire, Norfolk, Suffolk, Essex, Hertfordshire, Bedfordshire).", "",
             "Phone: %s. Email: %s. Office: %s, %s. Hours: %s." % (PHONE, EMAIL, ADDRESS["street"], ADDRESS["town"], HOURS_TEXT), "", "## Key pages"]
    for p, ni in PAGES:
        if not ni:
            lines.append("- %s%s" % (SITE, p))
    with open(os.path.join(SITE_DIR, "llms.txt"), "w") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    build_home(); build_schools(); build_candidates(); build_jobs(); build_roles(); build_areas()
    build_about(); build_guides(); build_contact(); build_misc(); build_seo_files()
    print("%d pages written to %s" % (len(PAGES), os.path.abspath(SITE_DIR)))
