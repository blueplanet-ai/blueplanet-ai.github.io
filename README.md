# Chuhee Lee — Independent Research

Source for **https://blueplanet-ai.github.io/**: benchmarks, comparisons and research reports on topics chosen from a strategic perspective.

## Publications

| Report | Edition | Path |
|---|---|---|
| [The terminal benchmark](https://blueplanet-ai.github.io/terminal-benchmark/) | October 2026 (data as of 23 Oct 2026; one-time edition) | `terminal-benchmark/` |
| [What people do on the move](https://blueplanet-ai.github.io/on-the-move/) | October 2026 (data as of 21 Oct 2026; one-time edition) | `on-the-move/` |
| [One cabin, several people](https://blueplanet-ai.github.io/shared-cabin/) (opportunity brief) | October 2026 (data as of 17 Oct 2026; one-time brief, not refreshed) | `shared-cabin/` |
| [Physical AI and the Rider’s Cabin](https://blueplanet-ai.github.io/physical-ai-cabin/) | October 2026 (data as of 13 Oct 2026, updated 14 Oct; next refresh Oct 2027) | `physical-ai-cabin/` |
| [Agentic AI and the Consumer: 2027 Outlook](https://blueplanet-ai.github.io/agentic-consumer-2027/) | October 2026 (data as of 11 Oct 2026; next refresh Oct 2027) | `agentic-consumer-2027/` |
| [Mobility Product Outlook 2026–2031](https://blueplanet-ai.github.io/mobility-product-outlook/) | October 2026 (data as of 11 Oct 2026; next refresh Oct 2027) | `mobility-product-outlook/` |
| [Mega Trends Outlook 2040](https://blueplanet-ai.github.io/mega-trends-2040/) | October 2026 (data as of 1 Oct 2026; next refresh Oct 2027) | `mega-trends-2040/` |
| [In-Car AI Assistant Benchmark](https://blueplanet-ai.github.io/incar-ai-benchmark/) | October 2026 (data as of 11 Oct 2026; next refresh mid-Jan 2027) | `incar-ai-benchmark/` |

Each report is a single self-contained `index.html` in its own folder, with an **At a glance** infographic at the top (built in the page from the report's own data), a downloadable `<report>-at-a-glance.png` and a 1200×630 `og-image.png` used as its social preview and as its card image on the home page. To add a report, create a new folder, add a card on the home page (`index.html`) tagged with its layer and domain, and link it from the matching cell in the map.

Also add the report to `feed.xml` (new `<item>`, and update `<lastBuildDate>`) and to `sitemap.xml`, and update `<lastmod>` there when a report is refreshed. Site-wide files at the repository root: `favicon.svg`, `apple-touch-icon.png`, `og-image.png` (1200×630 social preview), `feed.xml`, `sitemap.xml`, `robots.txt`.

## Infographic and preview images

The infographic in each page updates itself from the page's data. The PNG downloads and social previews are static renders, so after a refresh re-export them:

```
python3 tools/export-infographics.py                    # all reports
python3 tools/export-infographics.py mega-trends-2040   # one report
```

This needs Python with Playwright and Chromium (`pip install playwright && playwright install chromium`). The three figures printed on each social preview are set in `tools/og-cards.json`; update them if the headline figures change.

## Cover art

Each report has a drawn cover (`<report>/cover.svg`, 3:4, and `<report>/cover-wide.svg`, 16:9) used on the home page. The motifs come from each report's structure (for example, Mega Trends' arcs are sized by the trend scores). If a score or count changes, update the numbers at the top of the script and re-run:

```
python3 tools/make-covers.py
```

A new report needs a motif function and an entry in `REPORTS` in that script.

## Report opener

Every report opens with the same block: top bar, cover, layer and domain tags, Newsreader title, dek, research question, scope, byline, reading time, data-as-of date, next refresh, change-log link, Cite / Share / Infographic / References buttons, a "Cite as" line, and **The report in 60 seconds** (three takeaways). The three shorter reports also get an "In this report" contents list; Mega Trends and the Mobility Product Outlook keep their own sticky section bars.

The markup lives in each `index.html`; the styles and the Cite and Share behavior are shared in `assets/report-opener.css` and `assets/report-opener.js`. The light/dark toggle is `assets/theme.js` and `assets/theme.css`, linked on every page. `404.html` is the not-found page.

Rules for the 60-second takeaways:

- Each takeaway restates text already in the report's summary; no new figures. Its source line links to the report's own reference entry (or, for the benchmark, the source page).
- Each carries one label for the status of its main claim: **Fact** (stated by the cited source), **Interpretation** (the author's reading of the cited evidence) or **Hypothesis** (expected from the evidence but not yet observed). Figures inside a takeaway are always sourced facts.
- The labels are defined on `/method/`. Keep that page in step if a scoring scale or the source order changes.
- At each refresh, check the takeaways, the data-as-of date, the next-refresh date and the citation line against the updated report.

## Reading time

Reading times on the home page cards and in each report opener are estimates (rendered text at 230 words a minute, excluding tables and references). Update the card's `data-read` value, its meta line and the report opener when a report's length changes substantially.

## Chapter openers and the end-of-report block

Each numbered chapter starts with a `header.co` block (numeral, title, one-sentence thesis, progress bar). When adding or renaming a chapter, update the `Chapter n of N` text and the progress segments in every opener of that report. The thesis restates the chapter's own text; no new figures. On Mega Trends the openers are generated in the page script from the trend data (the headline figure is the first key figure of each trend).

The "Continue down the map" block and follow band sit just before each report's footer. Cards link to sibling reports with their cover and research question. Refresh dates are not repeated there; they live on the home page (`#follow`).

## How reports are updated

Updates arrive as pull requests. A scheduled research run re-checks each report against its sources and reports what changed. The author then has the findings applied as a pull request containing:

- the updated page,
- a dated entry in `CHANGELOG.md`, and
- a change report in the pull request description, covering rescores, new entries, corrections and open flags.

Nothing goes live until the author reviews and merges the pull request.

## License

© 2026 Chuhee Lee. Report content is licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). See [`LICENSE.md`](LICENSE.md).

Research, source verification and drafting are carried out with several AI models, including Claude (Anthropic), Gemini (Google) and ChatGPT (OpenAI); topic selection, scores and conclusions are the author's.

These are personal research projects. The views are the author's own and do not represent any employer or organization. No company named sponsors, reviews or endorses these reports, and product names and trademarks belong to their owners.
