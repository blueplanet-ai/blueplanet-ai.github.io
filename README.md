# Chuhee Lee — Independent Research

Source for **https://blueplanet-ai.github.io/**: benchmarks, comparisons and research reports on topics chosen from a strategic perspective.

## Publications

| Report | Edition | Path |
|---|---|---|
| [Physical AI and the Rider’s Cabin](https://blueplanet-ai.github.io/physical-ai-cabin/) | October 2026 (data as of 13 Oct 2026; next refresh to be confirmed) | `physical-ai-cabin/` |
| [Agentic AI and the Consumer: 2027 Outlook](https://blueplanet-ai.github.io/agentic-consumer-2027/) | October 2026 (data as of 11 Oct 2026; next refresh to be confirmed) | `agentic-consumer-2027/` |
| [Mobility Product Outlook 2026–2036](https://blueplanet-ai.github.io/mobility-product-outlook/) | October 2026 (data as of 11 Oct 2026; next refresh Oct 2027) | `mobility-product-outlook/` |
| [Mega Trends Outlook 2040](https://blueplanet-ai.github.io/mega-trends-2040/) | October 2026 (data as of 1 Oct 2026; next refresh Oct 2027) | `mega-trends-2040/` |
| [In-Car AI Assistant Benchmark](https://blueplanet-ai.github.io/incar-ai-benchmark/) | October 2026 (data as of 11 Oct 2026; next refresh mid-Jan 2027) | `incar-ai-benchmark/` |

Each report is a single self-contained `index.html` in its own folder. To add a report, create a new folder, add a card on the home page (`index.html`) tagged with its layer and domain, and link it from the matching cell in the map.

Also add the report to `feed.xml` (new `<item>`, and update `<lastBuildDate>`) and to `sitemap.xml`, and update `<lastmod>` there when a report is refreshed. Site-wide files at the repository root: `favicon.svg`, `apple-touch-icon.png`, `og-image.png` (1200×630 social preview), `feed.xml`, `sitemap.xml`, `robots.txt`.

## How reports are updated

Updates arrive as pull requests. A scheduled research run re-checks each report against its sources and reports what changed. The author then has the findings applied as a pull request containing:

- the updated page,
- a dated entry in `CHANGELOG.md`, and
- a change report in the pull request description, covering rescores, new entries, corrections and open flags.

Nothing goes live until the author reviews and merges the pull request.

## Licence

© 2026 Chuhee Lee. Report content is licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). See [`LICENSE.md`](LICENSE.md).

Research, source verification and drafting are carried out with several AI models, including Claude (Anthropic), Gemini (Google) and ChatGPT (OpenAI); topic selection, scores and conclusions are the author's.

These are personal research projects. The views are the author's own and do not represent any employer or organization. No company named sponsors, reviews or endorses these reports, and product names and trademarks belong to their owners.
