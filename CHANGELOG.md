# Change log

## Site-wide

### 17 October 2026 — editorial home page, icon set and report covers (visual refresh, part 1 of 3)
- Home page redesigned as an editorial front page. Titles and section headings now use Newsreader; Saira stays for labels, navigation and data. No copy was rewritten except the map's empty cells ("Coming" is now "Planned"; the Mobility opportunity cell reads "First brief in progress").
- New top bar with section links and a Follow link.
- New hero illustration, the "journey line": car, rail, robotaxi and plane, with a shaded band for attention that is free to spend as people move from driving to riding. It is labelled as illustrative, not to scale. It replaces the "route" pictogram.
- A "Latest" strip under the hero, built from the first publication card.
- One icon set (24 × 24 grid, 1.6 stroke) for domains, layers, lenses and reader actions, used in the map, filters, tags and lenses.
- Map: layer icons on each row; pointing to a report shows a preview (cover, description, data-as-of date) beside the map on wide screens; on phones the map becomes a stacked list by layer, with the same domain filter.
- Publications: lead story plus a list, each with cover art. Reading time is shown for the four research reports (estimated from rendered text at 230 words a minute, excluding tables and references); none is shown for the benchmark.
- Cover art for every report (`<report>/cover.svg`, `<report>/cover-wide.svg`), drawn by `tools/make-covers.py` from each report's own structure: Mega Trends' seven arcs are sized by each trend's score out of 20; the Mobility Product Outlook has twelve spokes for its twelve dimensions; the benchmark has 21 dots in 7 columns. The Agentic AI and Physical AI covers are abstract. Re-run the script if a score or count changes.
- New "Follow new editions" band (RSS and LinkedIn, with each report's next refresh) and a three-column footer. No email sign-up.
- Report pages are unchanged in this update; they follow in parts 2 and 3.

### 15 October 2026 — at-a-glance infographics, report previews and home page visuals
- Every report now opens with an **At a glance** section: a one-page infographic built in the page from the report's own data, so it follows light and dark themes and fits a phone. Each has a downloadable PNG (`<report>/<report>-at-a-glance.png`). No figures were added or changed; every number is read from data or text already in the report and links back to its source or reference.
- Every report has its own 1200×630 social preview (`<report>/og-image.png`) with matching Open Graph and Twitter tags. The site-wide `og-image.png` stays for the home page.
- Home page: a "route" pictogram in the masthead showing how many reports sit in each layer (counted from the map), domain icons in the map header, lens icons, and a preview image on each report card.
- The infographic PNGs and preview images are static renders. Re-export them whenever a report's data changes: `python3 tools/export-infographics.py [report-folder ...]` (needs Python with Playwright and Chromium). Card figures for the previews live in `tools/og-cards.json`.

### 13 October 2026 — print styles, feed, sitemap and social preview
- Print styles on the home page and all four reports: the page prints as a clean light copy whatever the reader's colour theme, without navigation or filter controls, with wide tables fitted to the page and collapsed sections opened. Source URLs are printed after the links in each reference list. Use the browser's Print → Save as PDF.
- Added an RSS feed (`feed.xml`), `sitemap.xml` and `robots.txt`, linked from the head of every page, with an RSS link in the home page About text.
- Added a favicon (`favicon.svg`, `apple-touch-icon.png`) and a 1200×630 social preview image (`og-image.png`) with Open Graph and Twitter large-image tags on every page.
- Feed items use each report's data-as-of date as the item date. Add an item to `feed.xml` and a URL to `sitemap.xml` whenever a report is added or refreshed.

## Home page

### October 2026 — restructured around "Time and attention on the move"
- New thesis headline: mobility, travel and what people do with their time on the way are treated as one connected space.
- Eyebrow changed to "Independent research · Technology, Mobility, Travel".
- A "so what" line under the thesis for readers who want the point first.
- New map (layers × domains) as primary navigation: Forces, Shifts, Signals and Opportunities against Shared, Mobility, Travel and Entertainment. Existing reports placed; empty cells marked "Coming".
- Report cards tagged by layer and domain, with a domain filter.
- Opportunities section shows the brief template, including a potential-versus-complexity score; no briefs published yet.
- "How topics are found": six lenses (time, attention, state of mind, social context, space, transitions), placed after the reports and opportunities.
- Short author bio added to About.

## Physical AI and the Rider’s Cabin

### 15 October 2026 — at-a-glance infographic
- New At a glance section at the top (Tesla, Waymo, Baidu and humanoid anchors, the Waymo growth bars, the adoption ranking, Apollo Go, humanoid and venture charts and the three cabin stages, all read from the sections below), with a PNG download and a per-report social preview. No figures changed.

### 14 October 2026 — additions after cross-checking a second draft
- Added Google DeepMind Gemini 4 Argon (13 Oct 2026), Wayve GAIA-3, Winverse AI, ITU-T Recommendation F.748.66, BMW Virtual Factory figures and Qualcomm automotive figures, each with a dated source.
- Added a "traditional automation" row to the related-terms table and a table on ISO 26262 and ISO 21448 (SOTIF) for cabin agents.
- Claims from an AI-generated draft that could not be confirmed (a 2,000 TOPS Snapdragon Ride Flex figure, a BCG definition, "GAIA-4", Winverse as DeepSeek's robotics arm) are not used; this is stated in the page's flags.
- London added to the player map. No existing figures changed.
- Research-assistance credit updated to name Gemini (Google) alongside Claude (Anthropic), consistent with the home page.

### October 2026 edition — first release (data as of 13 October 2026)
- New report under Shifts / Mobility: a definition of physical AI (published definitions plus the author's working definition and a stack diagram), the main players across the stack globally, a ranking of the most-used products by measurable adoption, and applications in the car with the cabin and rider experience as the main lens.
- Cabin section covers who is already there, the separated-versus-unified agent choice, EU and Euro NCAP occupant-sensing rules, a "why not just the phone?" comparison and neutral opportunity angles. Driving and factory uses are covered more briefly.
- Baidu's H1 2026 driverless rides (2026 Interim Report) and Euro NCAP's occupant-monitoring points (protocol v1.2) re-checked against primary documents on 13 October 2026.
- Open flags are listed on the page, including conflicting humanoid shipment counts and an unset refresh date.

## Agentic AI and the Consumer: 2027 Outlook

### 15 October 2026 — at-a-glance infographic
- New At a glance section at the top (the autonomy cliff, AI-referred traffic by sector, car-buyer intent versus action, the 2027 read and the watch list, all read from the sections below), with a PNG download and a per-report social preview. No figures changed.

### 14 October 2026 — research credit
- Research-assistance credit updated to name Gemini (Google) alongside Claude (Anthropic), in the byline, the About text and the credit flag. No figures or conclusions changed.

### October 2026 edition — first release (data as of 11 October 2026)
- New report on how agentic AI changes what consumers trust, delegate, buy and feel through 2027. General-consumer lens, with automotive and mobility as a dedicated section and a US, EU and China comparison.
- Four enterprise-side figures carried over from earlier working research were not confirmed against primary sources and are not used; this is stated on the page.
- Open flags are listed on the page for the author to decide, including the next refresh date.

## Mobility Product Outlook 2026–2036

### 15 October 2026 — at-a-glance infographic
- New At a glance section at the top (headline tiles, the product-definition shift, the top eight of the fifteen-technology ranking, who leads by region, OTA and data-concern by market, and the milestone timeline, all computed from the page's own data), with a PNG download and a per-report social preview. No figures changed.

### October 2026 edition — first public release (data as of 11 October 2026)
- Published as an independent public report on how consumer electronics and customer expectations are redefining the car, for a general audience.
- Part 1: seven lessons from consumer electronics, customer expectations in six markets (US, Germany, China, Japan, South Korea, India; Deloitte 2026), and the wider context linked to the Mega Trends Outlook 2040.
- Part 2: a twelve-dimension product-definition framework, eight real vehicles and platforms that preview it, three clearly labelled illustrative concepts, and a robotaxi and shared-cabin section.
- Part 3: the ranking of fifteen technologies (data as of 3 October 2026), eight deep dives, a US/Europe/China comparison, charts and a schematic map.
- No company-specific recommendations; observations are written for the industry as a whole. Research flags list source conflicts and unverified items.
- Added author, research-assistance credit (several AI models, mainly Claude), licence (CC BY-NC 4.0), disclaimer and next scheduled refresh (October 2027).

## Mega Trends Outlook 2040

### 15 October 2026 — at-a-glance infographic
- New At a glance section at the top: seven trend cards (sourced anchor figure plus the four 1–5 scores), links per trend from the 25 mapped interactions, the four scenarios with the 2026 marker, and near, mid and far milestones, all computed from the page's own data. PNG download and a per-report social preview added. No figures changed.

### 13 October 2026 — method clarification
- Section 02 now defines what each of the four scoring criteria (impact, certainty, speed, breadth) measures. No scores, figures or conclusions changed.

### October 2026 edition — first public release (data as of 1 October 2026)
- Published as an independent public report: seven mega trends for 2026–2040 across society, economy, technology, climate and geopolitics, scored on impact, certainty, speed and breadth.
- Includes near/mid/far horizon outlooks, a 25-link interaction map, a dated milestone roadmap, four scenarios, wildcards, methods and caveats, and 130 references.
- AI-regulation details (EU AI Act timing, US executive order, China labelling rules) omitted because no official source was retrieved; the public page carries a short Known limitations list instead of the working research flags.
- Seventeen headline figures re-checked against official sources on 1 and 11 October 2026. McKinsey adoption figures re-attributed to its *State of AI* survey (25 Aug 2026); Swiss Re wording changed to its stated 49% insured share; IEA export-control exposure stated as per year and outside China.
- Added author, research-assistance credit (Claude, Anthropic), licence (CC BY-NC 4.0), disclaimer and next scheduled refresh (October 2027). Sector implications are written for the industry as a whole, not for any company.
- Research-assistance credit names several AI models (Claude, Gemini, ChatGPT) on this page, the other reports and the home page.

## In-Car AI Assistant Benchmark

### 15 October 2026 — at-a-glance infographic
- New At a glance section at the top: headline tiles, the capability index for all entries with the median, average capability by architecture and mean score per dimension, all computed from the benchmark data. PNG download and a per-report social preview added. No scores changed.

### October 2026 edition — first public release (data as of 11 October 2026)
- Published as an independent public report. Added author, research-assistance credit (Claude, Anthropic), licence (CC BY-NC 4.0), disclaimer and next scheduled refresh (mid-January 2027).
- Removed company-specific recommendations; findings are written for the industry as a whole.
- Research-assistance credit updated to name several AI models (Claude, Gemini, ChatGPT).
- The summary chart now ranks all 21 entries, and the routes table covers four architectures.
- Refreshed to 11 October 2026:
  - BMW Launching → Shipping. The assistant has been live in iX3s in Germany since spring 2026, and US deliveries began in September.
  - Rivian Assistant is now on R2 (software 2026.36).
  - Grok extended to Israel and the UAE.
  - VW's ID. AURA T6, the first CEA model, launched on 20 September.
  - The Kia Sorento (India) assistant is powered by SoundHound.
  - Huawei's OTA roadmap and SoundHound OASYS Edge added to the watch list.
  - Toyota re-sourced to its 2022 in-house assistant release.
- No scores changed.

### 27 September 2026 — refresh
- Added use-case highlights: per-company features, verbatim example requests where published, limits, an evidence label, an evidence grid and a shared Google built-in card.
- Added Volkswagen Group China (CEA agentic AI) as the 21st entry, scored provisionally on announced specification.
- Added a fifth archetype, "In-house, pre-generative", and moved Toyota/Lexus into it after official sources confirmed its agent is built in-house and no LLM cockpit assistant has shipped.
- Rescored Ford (no GenAI → shipping), Rivian edge 2→4, Li Auto vehicle control and personalization 4→5, Lucid edge 2→3, Tesla OEM control 4→3 and Toyota OEM control 3→4.
- Corrected NIO personalization 5→4. Removed the Stellantis "brand personalities" claim. Dropped Li Auto "MindGPT 3.0". Restored Huawei "MoLA 2.0" with Huawei's own page as the source.
- Re-sourced to official domains first, with sources labelled by type.

### 12 September 2026 — first compilation
- Assessed 20 assistants across seven capability dimensions plus OEM control of the stack.
