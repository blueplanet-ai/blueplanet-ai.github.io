# Design system: blueplanet-ai.github.io

How the site looks and how to change it safely. Read this and `CHANGELOG.md` before touching styles. Report content and research findings are out of scope here; this file covers look, feel and code only.

Last updated 17 October 2026, after the Sage paper tone (PR #15).

## Direction

Editorial and calm, not corporate. Type does most of the work. Color is restrained: ink on paper, with teal for the main subject and one burnt-orange accent per view.

- **Newsreader** (serif): titles, body, quotes.
- **Saira** (sans): labels, navigation, UI.
- **IBM Plex Mono**: data, numbers, small captions. (Mega Trends also uses IBM Plex Sans.)
- Dark mode is a first-class theme. Don't change it unless asked.

## Color tokens

Each page carries an inline `<style>` token block: bare `:root` for light, then dark twice, once in `@media (prefers-color-scheme: dark)` guarded by `:root:not([data-theme="light"])` and once in `:root[data-theme="dark"]`. The shared `assets/report-opener.css` uses the same values with a `--ro-` prefix. Mega Trends names a few tokens differently (`--bg`, `--muted`, `--rule`). If you change a token, change it on all seven pages and in the opener CSS.

| Token | Light (Sage paper) | Dark | Use |
|---|---|---|---|
| ground | #EBF0E6 | #0D1213 | Page background |
| surface | #F4F7F0 | #151D1F | Cards, bars |
| surface-2 | #E0E7DA | #1D2729 | Second surface, wells |
| line | #CDD6C6 | #283436 | Hairlines |
| line-strong | #B3BFAB | #3C4B4E | Stronger rules |
| ink | #0F1719 | #E7EDEE | Main text |
| ink-2 | #344145 | #AFBDBF | Secondary text |
| ink-3 | #4E5B5F | see note | Small gray text, captions |
| signal | #0892A5 | #2BB3C6 | Main subject, links, data |
| signal-deep | #066A79 | #5FCCDB | Text on light, emphasis |
| opp | #C2622D | #DB8A4F | The single accent |
| opp-ink | #9A4A1F | #DB8A4F | Accent as text on light |

Note: dark `ink-3` is #8C9A9D on every page (it was #7F8D90 on the home page and Mega Trends before the 18 October polish; that gave only 4.45:1 on surface-2).

The print stylesheet forces a white ground with `!important`. That is intentional.

### Rules

- Light-mode ground is never white. If it looks white, check the surfaces too: ground and cards need a visible tint difference.
- Normal text must reach WCAG 2.2 AA, 4.5:1, on the surface it sits on. `ink-3` #4E5B5F gives 6.08:1 on ground and 5.56:1 on surface-2; `ink-2` #344145 gives 9.12:1 on ground.
- Small teal text uses `--signal-text` (light: `signal-deep`, 5.42:1 on ground; dark: `signal`). `--signal` itself is for fills, rules and large display type, not for text under 18 px.
- Remaining known gaps: outlined chapter numerals, decorative dashes and some chart fills are not text and are exempt; fix any small orange text with `opp-ink`.
- Use tokens, never raw hex, in page CSS and SVG (`var(--ink)`, `fill:var(--surface-2)`), so dark mode follows.

## Type scale

Sizes in page CSS snap to 12, 13, 14, 15, 16, 18, 20, 22 and 24 px. Use px, not rem, for text sizes. Body copy is 15-16 px sans on reports; the Method page is a serif essay at 18 px; leads (`.ro-dek`, `.co-thesis`) are 18-21 px. Nothing in page text or labels goes below 12 px. Chart labels drawn by script, SVG text and `em` sizes are exempt. Display sizes above 24 px are set per component.

## Page furniture

- **Skip link and `id="main"`** on the first header of every page (`tabindex="-1"` on reports). Keep the skip link first in `<body>`.
- **`theme-color` metas** for light and dark.
- **Theme toggle:** `assets/theme.js` and `assets/theme.css`, linked in the `<head>` of every page. Saves `bp-theme` (light or dark) in localStorage and sets `data-theme`; with no saved choice the system setting applies. The button is added to `nav.topnav` or `nav.ro-nav`.
- **`404.html`:** branded not-found page that lists the publications. It uses root-relative asset paths so it works at any depth.
- **JSON-LD:** each page has one `application/ld+json` block (home: `WebSite` and `Person`; reports: `Report`; Method: `Article`). Update `dateModified` with the sitemap `lastmod` when a page changes.
- **Headline finding:** `.gl-cap` under the at-a-glance infographic restates the report's own summary line. Do not write a new claim there.
- **Back link:** `.ro-crumb` ("← All publications") sits between the top bar and the header on every report and Method; it links to `/#publications`.
- **What changed (home):** `#updates` lists the three latest entries from `CHANGELOG.md` with dates. Update it when you add a changelog entry; keep it to four rows (add the new entry at the top, drop the oldest).
- **Text on trend colors (Mega Trends):** `--tc1`..`--tc7` set the text color on each trend fill per theme; do not hard-code white or black.
- **`<main>`** wraps the content between the contents bar and the "read next" block on every report.
- **Paper grain:** a faint SVG feTurbulence data-URI behind the light ground. Off in dark mode and print.
- **Page transitions:** CSS cross-document `@view-transition`, only under `prefers-reduced-motion: no-preference`.
- **Reading progress bar:** `.rp` element on the five reports, driven by `animation-timeline: scroll()`.
- **Journey figure (home):** draws once on scroll with IntersectionObserver. Static without script and with reduced motion.
- **Reduced motion:** every animation must be off or static under `prefers-reduced-motion: reduce`.

## Maps and figures

- Physical AI "Where the players are based": three panels (North America, Europe, East Asia) over an inline basemap from Natural Earth (public domain), about 60 KB, no external requests. Land and border paths are precomputed in the page's script and projected with the same equirectangular, cos-latitude function as the pins, so they line up. Land uses `--surface-2`, borders `--line-strong`. To change a panel's area, regenerate the paths with the same projection. Don't switch to tile maps or libraries without a reason.
- Figures use tokens and must read in both themes. Keep text out of AI-generated images; see the media style kit in the Site & Design project.

## Before you open a PR

Check every page (home, `method/`, and the five reports) at **1440, 768 and 390 px**, in light and dark:

1. No sideways scroll (`scrollWidth` ≤ viewport).
2. No console or script errors.
3. No unresolved `#` anchors.
4. A contrast scan of text nodes against their backgrounds.
5. For any change to a figure or map, look at the rendered result, including a zoomed crop of small details, not only the markup.
6. Add an entry at the top of `CHANGELOG.md`.

Local setup used so far: serve the repo with `python3 -m http.server`, drive it with Playwright and the preinstalled Chromium. Google Fonts is blocked in the sandbox, so install Newsreader, Saira, IBM Plex Mono (and IBM Plex Sans) from the `google/fonts` GitHub repository into `~/.fonts` before taking screenshots.

## Git and PRs

- Work on a branch, show the diff, and push or open a PR only when the owner says so.
- Commit as `blueplanet-ai <219496189+blueplanet-ai@users.noreply.github.com>`.
- Several open PRs all edit the top of `CHANGELOG.md` and conflict after one merges. Stack them in order, or open one at a time.

## Known follow-ups

- Static PNG infographics and social previews still show the old ground color. Regenerate with `python3 tools/export-infographics.py`.
- The media style kit still lists the old ground #F1F4F4. Update it before generating new media.
- Mobility Product Outlook body text still looks past 2031. Review at the October 2027 refresh.
