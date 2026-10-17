#!/usr/bin/env python3
"""Draw each report's cover motif as two static SVGs.

Usage:  python3 tools/make-covers.py
Outputs: <report>/cover.svg       (3:4 portrait, for cards and lists)
         <report>/cover-wide.svg  (16:9, for the lead story on the home page)

The motifs are drawn from each report's own structure, not decoration:
- Mega Trends Outlook 2040: seven arcs, one per force; arc length = the trend's
  total score out of 20 (the author's scores, from the report's T array).
- Mobility Product Outlook: twelve spokes, one per product-definition dimension.
- In-Car AI Assistant Benchmark: 21 dots in 7 columns (21 assistants, 7 dimensions).
- Agentic AI and the Consumer, Physical AI and the Rider's Cabin: abstract
  (a hand-off from one point to many; a cabin seen from above). No data.
Covers are always dark plates, so they read the same in light and dark themes.
They carry no text; titles are set in the page.
If a report's structure changes (a rescore, a new assistant), update the numbers
below and re-run.
"""
import math, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
INK, LINE, TEAL, ORANGE, PALE = "#0F1719", "#3C4B4E", "#2BB3C6", "#DB8A4F", "#E7EDEE"

# Mega Trends T1..T7 total scores (impact + certainty + speed + breadth, out of 20)
MEGA_TREND_SCORES = [18, 17, 17, 16, 16, 14, 14]
MOBILITY_DIMENSIONS = 12
BENCHMARK_ASSISTANTS, BENCHMARK_DIMENSIONS = 21, 7


def arc(cx, cy, r, frac):
    a = 2 * math.pi * frac * 0.75
    a0, a1 = -math.pi / 2, -math.pi / 2 + a
    p = lambda t: f"{cx + r * math.cos(t):.1f} {cy + r * math.sin(t):.1f}"
    return f"M{p(a0)} A{r} {r} 0 {1 if a > math.pi else 0} 1 {p(a1)}"


def mega(cx, cy, s):
    out = []
    for i, score in enumerate(MEGA_TREND_SCORES):
        r = (150 - i * 19) * s
        out.append(f'<path d="{arc(cx, cy, r, score / 20)}" fill="none" stroke="{ORANGE if i == 0 else TEAL}" stroke-width="{9 * s:.1f}" stroke-linecap="round"/>')
    return "".join(out)


def agentic(cx, cy, s):
    src = (cx - 130 * s, cy)
    targets = [(cx + 90 * s, cy - 120 * s), (cx + 130 * s, cy - 50 * s), (cx + 140 * s, cy + 30 * s), (cx + 110 * s, cy + 105 * s), (cx + 40 * s, cy + 140 * s)]
    out = [f'<path d="M{src[0]:.1f} {src[1]:.1f} C {cx - 20 * s:.1f} {src[1]:.1f} {cx - 10 * s:.1f} {y:.1f} {x:.1f} {y:.1f}" fill="none" stroke="{LINE}" stroke-width="{3 * s:.1f}"/>' for x, y in targets]
    out += [f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{12 * s:.1f}" fill="{TEAL}"/>' for x, y in targets]
    out.append(f'<circle cx="{src[0]:.1f}" cy="{src[1]:.1f}" r="{20 * s:.1f}" fill="{ORANGE}"/>')
    return "".join(out)


def mobility(cx, cy, s):
    out = []
    for i in range(MOBILITY_DIMENSIONS):
        a = 2 * math.pi * i / MOBILITY_DIMENSIONS - math.pi / 2
        r1, r2 = 38 * s, 150 * s
        out.append(f'<path d="M{cx + r1 * math.cos(a):.1f} {cy + r1 * math.sin(a):.1f} L{cx + r2 * math.cos(a):.1f} {cy + r2 * math.sin(a):.1f}" stroke="{ORANGE if i == 0 else TEAL}" stroke-width="{7 * s:.1f}" stroke-linecap="round"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{16 * s:.1f}" fill="{PALE}"/>')
    return "".join(out)


def cabin(cx, cy, s):
    w, h = 220 * s, 300 * s
    x0, y0 = cx - w / 2, cy - h / 2
    seat = lambda x, y, c: f'<rect x="{x:.1f}" y="{y:.1f}" width="{70 * s:.1f}" height="{90 * s:.1f}" rx="{6 * s:.1f}" fill="none" stroke="{c}" stroke-width="{6 * s:.1f}"/>'
    return (f'<rect x="{x0:.1f}" y="{y0:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{40 * s:.1f}" fill="none" stroke="{LINE}" stroke-width="{5 * s:.1f}"/>'
            + seat(x0 + 25 * s, y0 + 40 * s, TEAL) + seat(x0 + 125 * s, y0 + 40 * s, TEAL)
            + seat(x0 + 25 * s, y0 + 165 * s, ORANGE) + seat(x0 + 125 * s, y0 + 165 * s, TEAL)
            + f'<path d="M{x0 - 16 * s:.1f} {y0 + 70 * s:.1f} V{y0 + h - 70 * s:.1f}" stroke="{PALE}" stroke-width="{8 * s:.1f}" stroke-linecap="round"/>')


def benchmark(cx, cy, s):
    cols, rows = BENCHMARK_DIMENSIONS, math.ceil(BENCHMARK_ASSISTANTS / BENCHMARK_DIMENSIONS)
    gap = 42 * s
    x0, y0 = cx - gap * (cols - 1) / 2, cy - gap * (rows - 1) / 2
    return "".join(f'<circle cx="{x0 + (i % cols) * gap:.1f}" cy="{y0 + (i // cols) * gap:.1f}" r="{14 * s:.1f}" fill="{ORANGE if i % cols == 0 else TEAL}"/>' for i in range(BENCHMARK_ASSISTANTS))


REPORTS = {
    "mega-trends-2040": (mega, "Seven arcs, one per force in Mega Trends Outlook 2040; each arc's length is the trend's score out of 20."),
    "agentic-consumer-2027": (agentic, "Abstract cover: one point handing tasks to many."),
    "mobility-product-outlook": (mobility, "Twelve spokes, one per dimension of the product-definition framework."),
    "physical-ai-cabin": (cabin, "Abstract cover: a four-seat cabin seen from above, one rider marked."),
    "incar-ai-benchmark": (benchmark, "21 dots in 7 columns: 21 assistants scored on 7 capability dimensions."),
}


def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{title}">'
            f'<title>{title}</title><rect width="{w}" height="{h}" fill="{INK}"/>{body}</svg>\n')


for slug, (draw, title) in REPORTS.items():
    folder = ROOT / slug
    (folder / "cover.svg").write_text(svg(600, 800, draw(300, 400, 1.55), title), encoding="utf-8")
    (folder / "cover-wide.svg").write_text(svg(1600, 900, draw(800, 450, 2.1), title), encoding="utf-8")
    print("wrote", slug)
