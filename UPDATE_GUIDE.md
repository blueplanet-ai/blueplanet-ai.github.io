# Update guide

These are the rules every scheduled research run follows when checking a report on this site. A scheduled run researches and reports its findings (change table, proposed edits, flags); it does not edit the repository. The author then has the findings applied as a pull request, and reviews and merges it before publication.

## Process

1. Re-check every entry in the report against its sources, then search for newer official announcements since the report's "data as of" date.
2. Propose (in the report) or, when applying a report, edit the report's `index.html`:
   - update data, scores and text;
   - update the "data as of" date in the byline and stamp;
   - add a dated entry to the on-page change log.
3. Add the same entry to `CHANGELOG.md`.
4. Report the findings; when they are applied, open a pull request titled `<Report> refresh — <YYYY-MM-DD>`. The report and the pull request description must include:
   - a change report table: entry, what changed, old → new, source;
   - new entries and removals;
   - corrections;
   - open flags and doubts for the author to decide.
5. Scheduled runs never edit the repository, merge or push to `main`. Applied changes always go through a pull request. The author merges after review, and the site then updates automatically.

## Working rules

- **Sources:** official manufacturer or supplier domains first, then recognized benchmark studies (e.g. J.D. Power), then specialist trade press. Avoid aggregator and SEO sites. Check publication dates and prefer the newest.
- **No invented facts.** Quote example requests word for word only when the source publishes them. Where a company publishes none, say so and leave its evidence-grid row empty.
- **Neutrality.** Write for any automaker or interested reader. Make no recommendations to a specific company.
- **Flag, don't resolve.** Raise doubts and judgement calls in the pull request for the author to decide.
- **Quality.** Proofread and check the page renders at desktop and phone widths, in light and dark themes. Keep the existing styling. Every claim needs a source in the `SRC` registry.

## In-Car AI Assistant Benchmark — data map

All data lives in `incar-ai-benchmark/index.html`, in the `<script>` block near the end of the file.

| Object | Contents |
|---|---|
| `SRC` | Source registry, `key: [label, url, type]`. Type is `official`, `benchmark`, `trade` or `press`. |
| `DATA` | One matrix row per entry: `s` = seven scores (conversation, agentic, vehicle control, navigation, ecosystem, personalization, edge), plus `own` (OEM control), `a` (archetype), `st` (status), `stack`, `status`, `note`, optional `flag`, and `src` keys. |
| `UC_ROWS` | Use-case highlights per company: `feat`, `uc`, `lim`, `src`, evidence label `conf`, and evidence-grid marks in `grid`. |
| `UC_COLS` | The 11 use-case types in the evidence grid. |

## Schedule

- **Full refresh each quarter:**
  - mid-January (after CES)
  - mid-May (after Auto Shanghai in odd years, and Google I/O)
  - mid-July (after summer software updates)
  - mid-October (after IAA in odd years, and Q3 earnings)
- **Monthly scan of the watch list** in between; report (and have a pull request opened) only if something material changed.
- **First scheduled run:** mid-January 2027. The page shows "Next scheduled refresh: mid-January 2027"; update it on every run.

## Watch list (as of 11 October 2026)

| When | Item |
|---|---|
| H2 2026 | Volkswagen Group China's CEA agents confirmed in customer cars (ID. AURA T6 launched 20 Sep 2026; agent at launch unconfirmed) |
| H2 2026 | BMW's Alexa+-based assistant spreads beyond the iX3 to OS 9 / OS X models; US availability confirmed |
| Late 2026 | GM's own assistant arrives alongside Gemini |
| Late 2026 | SoundHound OASYS Edge (fully embedded agentic voice AI) first deployments |
| Early 2027 | Amazon's Alexa Custom Assistant on NVIDIA DRIVE AGX opens for automaker evaluation |
| Q1 2027 | Huawei HarmonySpace "Active Suggestion 2.0" (OTA roadmap) |
| H1 2027 | Mercedes' three-model C-Class reaches US dealers |
| 2027 | Ford assistant goes in-vehicle; Volkswagen's Qualcomm-based SSP cockpit starts |
| Open | Whether Rivian licenses its assistant beyond its own vehicles |

## Known caveats (carry forward until resolved)

- **BMW:** use-case examples come from a CES demo drive. Production use is confirmed in Germany; Alexa+ in US-delivered cars is not yet confirmed.
- **VW Group China:** whether the agent shipped on the ID. AURA T6 at launch is not confirmed.

- **Mercedes:** the three-model C-Class detail rests on a press report (How-To Geek); Mercedes' own release could not be retrieved.
- **VW Group China:** scored provisionally on announced specification. Partners come from AI Business, not from VW.
- **Volkswagen, Audi, VW Group China:** no published use-case examples, so their evidence-grid rows stay empty.
- **Tesla:** the 116-of-170 figure is a test compiled by owners. Grok is in beta.
- **Honda:** "free, no dealer visit" comes from Kelley Blue Book; Honda's release doesn't state terms.
- **Huawei:** the product page cited for MoLA 2.0 is undated.
- **Chinese-market rows:** they rest mainly on trade press. Xiaomi has no official English source.

## Mega Trends Outlook 2040 — refresh rules

**Schedule.** Full refresh at least once a year, in October, after the IMF October World Economic Outlook is published. The page shows "Next scheduled refresh: October 2027"; update it on every run. Between editions, report and open a pull request only for a material shock (for example a major war, pandemic or financial crisis) that changes a trend score or the 2026 scenario marker.

**Sources.** Official statistics and international institutions first (UN, IMF, World Bank, OECD, IEA, WMO, SIPRI, WTO), then peer-reviewed research, then recognized foresight and consulting reports, then reputable press. Prefer the newest edition and record its date.

**What to re-check each edition.**
- Every KPI tile, chart value and dated milestone against its source; replace with newer editions (UN WPP, IMF WEO and Fiscal Monitor, IEA WEO / EV / Critical Minerals outlooks, WEF Global Risks, SIPRI, UNEP Emissions Gap, Global Carbon Budget).
- Re-score the seven trends (1–5 on impact, certainty, speed, breadth). Scores are the author's judgement: propose changes in the pull request with the evidence; do not change them silently.
- Re-assess the 2026 scenario marker against the signposts listed on the page and propose a new position for the author to decide.
- Re-run the headline-figure verification table and update its date.
- Keep sector implications neutral: observations for the industry as a whole, never advice to a specific company.
- Claims about laws, regulations, treaties and government policy must cite the official text (legislation, official journal, government or intergovernmental release). If no official source can be retrieved, leave the claim out and say so in the pull request.

**Data map.** All data lives in `mega-trends-2040/index.html`, in the `<script>` block near the end of the file.

| Object | Contents |
|---|---|
| `T` | The seven trends: id, short name, full name, colour token and scores `s` = [impact, certainty, speed, breadth]. |
| `D` | One dossier per trend: `thesis`, `kpis` (value, label, source label, URL, re-checked flag, derived flag), `charts` (title, tag, source note), `h` (near/mid/far outlook), `unc`, `imp`, `mob` (sector note or null). |
| Chart calls | Chart values sit in the calls after `/* --- T1 charts --- */` and onward (one block per trend). |
| `E` | The 25 directed interaction links: from, to, sign, note, basis, loop id. |
| `M` | Dated milestones for the roadmap: year, trend number, text. |
| `WC` | Wildcard cards. |
| `V` | Headline-figure verification table. |
| HTML | Executive summary, scenarios, implications, known limitations, about, change log, research flags and the reference list are static HTML in the page body. |
