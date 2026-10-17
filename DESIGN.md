# Design system: blueplanet-ai.github.io

How the site looks and how to change it safely. Read this and `CHANGELOG.md` before touching styles. Report content and research findings are out of scope here; this file covers look, feel and code only.

Last updated 17 October 2026, after the Sage paper tone (PR #15).

## Direction

Editorial and calm, not corporate. Type does most of the work. Colour is restrained: ink on paper, with teal for the main subject and one burnt-orange accent per view.

- **Newsreader** (serif): titles, body, quotes.
- **Saira** (sans): labels, navigation, UI.
- **IBM Plex Mono**: data, numbers, small captions. (Mega Trends also uses IBM Plex Sans.)
- Dark mode is a first-class theme. Don't change it unless asked.

## Colour tokens

Each page carries an inline `<style>` token block: bare `:root` for light, then dark twice, once in `@media (prefers-color-scheme: dark)` guarded by `:root:not([data-theme="light"])` and once in `:root[data-theme="dark"]`. The shared `assets/report-opener.css` uses the same values with a `--ro-` prefix. Mega Trends names a few tokens differently (`--bg`, `--muted`, `--rule`). If you change a token, change it on all seven pages and in the opener CSS.

| Token | Light (Sage paper) | Dark | Use |
|---|---|---|---|
| ground | #EBF0E6 | #0D1213 | Page background |
| surface | #F4F7F0 | #151D1F | Cards, bars |
| surface-2 | #E0E7DA | #1D2729 | Second surface, wells |
| line | #CDD6C6 | #283436 | Hairlines |
| line-strong | #B3BFAB | #3C4B4E | Stronger rules |
| ink | #0F1719 | #E7EDEE | Main text |
| ink-2 | #3F4C50 | #AFBDBF | Secondary text |
| ink-3 | #5A676B | see note | Small grey text, captions |
| signal | #0892A5 | #2BB3C6 | Main subject, links, data |
| signal-deep | #066A79 | #5FCCDB | Text on light, emphasis |
| opp | #C2622D | #DB8A4F | The single accent |
| opp-ink | #9A4A1F | #DB8A4F | Accent as text on light |

Note: dark `ink-3` is #7F8D90 on the home page and #8C9A9D in `report-opener.css`. Keep each as it is unless you are fixing a contrast problem.

The print stylesheet forces a white ground with `!important`. That is intentional.

### Rules

- Light-mode ground is never white. If it looks white, check the surfaces too: ground and cards need a visible tint difference.
- Normal text must reach WCAG 2.2 AA, 4.5:1, on the surface it sits on. `ink-3` #5A676B gives 5.06:1 on ground and 4.63:1 on surface-2.
- Known gap: some small teal and orange accent labels and numerals are below 4.5:1. They are left as designed. Don't add more; fix them if you touch them.
- Use tokens, never raw hex, in page CSS and SVG (`var(--ink)`, `fill:var(--surface-2)`), so dark mode follows.

## Type scale

Sizes in page CSS snap to 12, 13, 14, 15, 16, 18, 20, 22 and 24 px. Nothing in page text or labels goes below 12 px. Chart labels drawn by script, SVG text and `em` sizes are exempt. Display sizes above 24 px are set per component.

## Page furniture

- **Skip link and `id="main"`** on the first header of every page (`tabindex="-1"` on reports). Keep the skip link first in `<body>`.
- **`theme-color` metas** for light and dark.
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

- Static PNG infographics and social previews still show the old ground colour. Regenerate with `python3 tools/export-infographics.py`.
- The media style kit still lists the old ground #F1F4F4. Update it before generating new media.
- Mobility Product Outlook body text still looks past 2031. Review at the October 2027 refresh.
