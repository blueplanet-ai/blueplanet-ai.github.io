# Change log

## Site-wide

### 18 October 2026 — site polish: spelling, type, contrast, theme toggle
- **Spelling and typography:** American spelling throughout (about 140 changes); straight quotes became curly on four pages; money in prose is spelled out ("3 billion dollars") while tables, charts and labels keep bn/m/tn; report `<title>`s end with the author name; the home `og:title` is plain and `og:type` is set; footers say "any company or organization named"; full report names are used in cards, lists, references and the Method table. "U.S." in official study names is left as published. No findings or figures changed.
- **Type scale:** Mega Trends rem sizes and the 14.5 px, 12.5 px and sub-12 px sizes on Mega Trends, Mobility and Physical AI moved onto the 12-24 px scale.
- **Contrast (light mode only):** `ink-2` is now #344145 and `ink-3` #4E5B5F; small teal labels and numerals use the new `--signal-text`. Other light-mode text fixes: `--warn` is #9A4A1F, `--s4-ink` is dark on the mid-teal score cells, Mobility's Europe and China text and Mega Trends' flag, T1 and T2 colors reach 4.5:1. Dark mode is unchanged.
- **Infographics:** the six at-a-glance PNGs and social previews were re-exported to match the text changes.
- **Structure and accessibility:** `<main>` added to four reports; Method gets a visible keyboard focus ring.
- **New:** theme toggle (`assets/theme.js`, `assets/theme.css`), branded `404.html`, JSON-LD on every page, and a "Headline finding" line under each at-a-glance infographic (existing summary text, not new claims).

### 18 October 2026 — first opportunity brief: One cabin, several people
- **New page** `shared-cabin/`: the first Opportunities brief, built on the report template (opener, 60-second takeaways, at-a-glance infographic, seven chapters, method and references). It answers the eight template questions, sizes the shared-cabin problem in the US against congestion, distraction, phone integration, EV charging and in-flight entertainment, and lists concepts from the US, Europe, China, Korea and Japan.
- **Home page:** the brief is the new lead publication and "Latest"; added as 06 in Start here; the Mobility / Opportunities map cell now links to it; the Opportunities section shows the filled eight-question card instead of the placeholder; not added to the follow list because it is a one-time brief and will not be refreshed.
- **Shared code:** `assets/report-opener.js` gains the `opp` (Opportunities) icon, the same drawing as on the home page. `tools/make-covers.py` gains a `shared` motif drawn from the brief's comparison (hours a year per person: passenger, congestion, flying); other covers are unchanged. `tools/og-cards.json` gains the brief's social-card figures.
- **Cross-checked before release:** the brief was fact-checked against primary sources. Corrections: occupancy is worded as average vehicle occupancy (DOE words it per trip; FHWA tables the same figures as mileage-weighted), the AFEELA 1 is marked cancelled (March 2026), the Hyundai 20 million target is attributed to Pleos Connect, the USDOT $21.80 is labelled all-purpose with the $20.10 personal rate shown, the unverifiable AirConsole four-million claim was removed, the Li Auto voice figures were corrected to the Chinese-language source (front passengers above 72%, rear above 44%; the English trade report had attributed the 72% to the driver), and two US examples were added (Apple Vehicle Motion Cues, Chrysler Pacifica rear screens). The credit line now mentions the cross-checks. Absolute claims ("nobody counts its cost", "the whole answer does not exist") were bounded to the sources reviewed, the dollar value of passenger time is labelled illustrative, the average-speed flag no longer claims NHTS implies about 20 mph, the passenger-hours range was widened to 70 to 104 (speeds of 25 to 37 mph), and the congestion comparison now says comparable in scale rather than larger. Added: evidence labels (Shipped, Reported, Company claim, Announced, Patent, Cancelled) on the concept table; the 35% passenger-screen finding and the University of Michigan one-in-three estimate are worded as narrowly as their sources allow; and an "Illustrations to spark your own ideas" block with three author's illustrations and six questions for any solver, labelled as not validated. The brief is now about 14 minutes. A further pass added a note that the time value is unlike congestion's measured cost, a "who may ask for what" rule and question, a gentler-drive-modes pairing in the family wedge, and a labelled idea for content-platform payments.
- **Author's framing added after a further review:** a labelled coordination-problem framing in the Summary, a list of hypotheses on why no whole answer exists yet, a table of tests that would weaken the case, a user/buyer/distributor question, and a line that passenger hours are exposure, not unmet need. The $0.47 to $0.69 trillion value-of-time figure was moved from the size table to the arithmetic note, labelled illustrative. Reading time is now about 16 minutes.
- Feed, sitemap and README updated. Infographic PNG and social preview exported with `tools/export-infographics.py shared-cabin`.

### 17 October 2026 — infographics re-exported on the Sage ground
- The five "at a glance" PNG infographics were re-exported with the Sage paper ground and the 12 px type floor, so they match the pages. They are taller than before (roughly 50 to 190 px at 2x) because of the type-scale change. The social preview images are unchanged: they use the dark design, which did not change.

### 17 October 2026 — design system document
- Added `DESIGN.md` at the repository root: tokens, type scale, accessibility rules, page furniture, map method and the pre-PR checklist. No site files changed.

### 17 October 2026 — sage paper tone, readability and polish
- **Paper tone (light mode).** The page ground changes from the near-white grey-green to a soft sage paper: ground #EBF0E6, cards and bars #F4F7F0, second surface #E0E7DA, rules #CDD6C6 and #B3BFAB. Colour tokens only, on all seven pages and in `assets/report-opener.css`. Dark mode and the print stylesheet are unchanged.
- **Small grey text** (`--ink-3`, `--muted`, `--ro-ink-3`) darkens from #6B787C to #5A676B so it keeps at least 4.5:1 on the new surfaces. In a local scan the home page went from 59 to 5 text nodes under 4.5:1, and the report pages from 166–441 to 8–81. The remaining ones are mostly small teal and orange accent labels and numerals, left as designed.
- **Home page map** no longer makes the page scroll sideways at tablet widths (it overflowed at 712 and 768 px). The map now scrolls inside its own frame.
- **Type scale.** Page text and labels set in CSS no longer go below 12 px, and sizes snap to 12, 13, 14, 15, 16, 18, 20, 22 and 24 px. Chart labels drawn by script, SVG text and `em` sizes are unchanged.
- **Skip link and browser theme colour** on every page (`theme-color` follows light and dark).
- **Polish.** A very faint paper grain behind the light-mode ground; a quiet fade between pages in browsers that support cross-page view transitions; a thin reading-progress bar on the five reports; the "How topics are found" figure draws once when it scrolls into view. Grain is off in dark mode and in print, and the figure animation and page fade are off with reduced motion.
- Physical AI cabin: the "Where the players are based" panels now sit on a simplified inline basemap (land and country borders, Natural Earth public domain, about 60 KB, no external requests) projected with the same function as the pins; follows light and dark tokens.
- Static PNG infographics and social previews were not re-exported and still show the previous ground colour. Re-run `tools/export-infographics.py` to update them.

### 17 October 2026 — home page eyebrow
- The line above the headline now reads "Independent research · AI, Mobility, Experience" (was "Technology, Mobility, Travel").
- Matching wording in the home page's search description and social-card description, the audience line under the intro ("For people building products in AI, mobility and experience") and the RSS feed description. The headline, intro paragraph, map domains and method-page thesis are unchanged.

### 17 October 2026 — Mobility Product Outlook: Zoox diagram legend
- The "seat touchscreen" legend overlapped the vehicle outline in the Zoox cabin diagram. It now sits in its own row below the diagram. No data changed.

### 17 October 2026 — Mobility Product Outlook retitled 2026–2031
- The title and horizon label change from 2026–2036 to 2026–2031, matching the Shifts layer (one to five years). Updated on the report, home page, feed, README, social card and infographic, in the Physical AI reference list and in the "Continue down the map" cards on the other reports.
- The report text is unchanged. Passages that look beyond 2031 (the framework's 2030–2036 view, the 2031–2036 technology timings, adoption by 2036) are to be reviewed at the October 2027 refresh. The page URL is unchanged.

### 17 October 2026 — chapter openers, "Continue down the map", refreshed images (visual refresh, part 3 of 3)
- Every numbered chapter now opens the same way: an outlined numeral, the title in Newsreader, a one-sentence thesis and a "Chapter n of N" progress bar. Agentic AI (8 chapters), Physical AI (6), the benchmark (5) and the three Parts of the Mobility Product Outlook use it; the Mobility Part intro sentences are the theses.
- Mega Trends: each trend header now shows the numeral in the trend's colour, the existing thesis, the author's four scores and total, and one headline figure. The headline figure is the trend's first key figure moved up, so no figure was added or changed.
- The other chapter theses restate each chapter's own text and add no new figures. Chapters keep their previous headings (numbering moved into the numeral); anchors and ids are unchanged.
- New **Continue down the map** block at the end of every report: three related reports with cover, layer and research question, plus a "Follow new editions" band (RSS, LinkedIn). Next refresh dates stay on the home page only, so they are updated in one place.
- Infographic PNGs and 1200×630 social previews re-exported for all five reports (`tools/export-infographics.py`).
- Styles are in `assets/report-opener.css` (`.co`, `.rn`, `.rn-follow`). Printing hides the follow band.

### 17 October 2026 — "How this research is made" page
- New page at `/method/`: independence, how topics are chosen, source order, how AI is used, the Fact / Interpretation / Hypothesis labels used in each report's 60-second summary, scoring scales, refreshes and corrections, licence and citation. Written only from practice already stated on the site.
- Linked from the home page About section and footer, and from every report's footer. Added to `sitemap.xml`.

### 17 October 2026 — home page: Start here, research questions, compact Opportunities
- New **Start here** section under the hero: the five reports in reading order (forces, then shifts, then signals), each with its layer and its scope as stated in the report. Also linked from the top bar and footer.
- Each publication card now shows the report's one-line research question, the same wording as in the report opener.
- Screen readers now hear which report a "Read the report" link opens (map preview and Latest strip); the card-level duplicate is hidden from them because the whole card is already the link.
- Opportunities is compacted while no briefs are published: one short block listing the questions every brief will answer. The full template returns once briefs are published.
- New section order: hero and Latest, Start here, the map, publications, how topics are found, Opportunities, About, Follow.
- Headline and intro unchanged.

### 17 October 2026 — report openers and 60-second summaries (visual refresh, part 2 of 3)
- Every report now opens with the same block: the site's top bar (replacing the "All publications" strip), the report's cover, layer and domain tags, the title in Newsreader, the existing standfirst, a one-line research question, a scope list (taken from each report's former "stamp" box), byline, reading time (not shown for the benchmark), data-as-of date, next refresh and a link to the change log, plus **Cite** (copies the citation), **Share**, **Infographic (PNG)** and **References** buttons and a "Cite as" line.
- New **The report in 60 seconds** band on every report: three takeaways, each restating text already in the report's summary with its source linked, and labelled **Fact**, **Interpretation** or **Hypothesis**. No figures were added or changed.
- An "In this report" contents list on the Agentic AI, Physical AI and benchmark pages. Mega Trends and the Mobility Product Outlook keep their sticky section bars; on Mega Trends the ranking panel moves from the hero to just below the 60-second band.
- Report titles and section headings now use Newsreader, matching the home page; small headings, labels and data stay in Saira and Plex Mono.
- Anchors added for linking: each report's change log (`#changelog`) and references (`#refs`); Mega Trends and Mobility Product Outlook references are numbered anchors (`#ref-N`); five benchmark sections now have ids.
- The Agentic AI and Physical AI pages had no suggested citation; their "Cite as" lines follow the format used on the other three reports.
- Shared styles and script: `assets/report-opener.css`, `assets/report-opener.js`. Printing hides the top bar and buttons and prints the 60-second band in light colours.

### 17 October 2026 — editorial home page, icon set and report covers (visual refresh, part 1 of 3)
- Home page redesigned as an editorial front page. Titles and section headings now use Newsreader; Saira stays for labels, navigation and data. No copy was rewritten except the map's empty cells ("Coming" is now "Planned"; the Mobility opportunity cell reads "First brief in progress").
- New top bar with section links and a Follow link.
- New hero image: an editorial illustration of a rider on a train, generated with Gemini and labelled "AI-generated illustration (Gemini)". It replaces the "route" pictogram. Its request and settings are recorded in `media/prompts.md`, which will list every AI-generated item on the site.
- The home page social preview (`og-image.png`) now uses the same image, with the title and the same label.
- New drawn figure, the "journey line": car, rail, robotaxi and plane, with a shaded band for attention that is free to spend as people move from driving to riding, labelled as illustrative, not to scale. It opens "How topics are found".
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
