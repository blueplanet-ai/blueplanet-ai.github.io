#!/usr/bin/env python3
"""Re-export each report's infographic PNG and 1200x630 social preview.

Usage:  python3 tools/export-infographics.py [report-folder ...]
Needs:  pip install playwright && playwright install chromium
Fonts load from Google Fonts (network needed); if offline, system fallbacks are used.
Outputs: <report>/<report>-at-a-glance.png  (from the #glanceBody block, light theme, 2x)
         <report>/og-image.png               (from tools/og-cards.json)
"""
import asyncio, html, json, pathlib, sys
from playwright.async_api import async_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
CARDS = json.loads((ROOT / "tools/og-cards.json").read_text(encoding="utf-8"))
FONTS = "https://fonts.googleapis.com/css2?family=Saira:wght@400;500;600;700&family=Newsreader:wght@400;500&family=IBM+Plex+Mono:wght@400;500;600&display=swap"

def og_html(c, slug):
    st = "".join(f'<div class="st"><b>{html.escape(n)}</b><span>{html.escape(l)}</span></div>' for n, l in c["stats"])
    return f"""<!doctype html><meta charset=utf-8><link rel=stylesheet href="{FONTS}"><style>
*{{box-sizing:border-box;margin:0}}body{{width:1200px;height:630px;background:#0D1213;font-family:Saira,sans-serif;color:#E7EDEE;position:relative;overflow:hidden}}
.bar{{position:absolute;left:0;top:0;bottom:0;width:14px;background:#2BB3C6}}
.eb{{position:absolute;left:84px;top:66px;font:400 22px 'IBM Plex Mono',monospace;letter-spacing:.08em;color:#7F8D90;display:flex;align-items:center;gap:14px}}
.eb i{{width:14px;height:14px;border-radius:50%;background:#C2622D;display:block}}
h1{{position:absolute;left:80px;top:128px;font-weight:600;font-size:96px;line-height:1.08;letter-spacing:-.015em}}
h1 span{{color:#2BB3C6;display:block}}
.sts{{position:absolute;left:84px;right:84px;top:372px;display:flex}}
.st{{flex:1;padding:4px 28px;border-left:2px solid #283436}}.st:first-child{{padding-left:0;border-left:0}}
.st b{{display:block;font-weight:600;font-size:54px;letter-spacing:-.01em;line-height:1.1}}
.st span{{display:block;margin-top:6px;font:400 20px/1.3 'IBM Plex Mono',monospace;color:#AFBDBF}}
.by{{position:absolute;left:84px;bottom:46px;font-size:30px;color:#AFBDBF}}.by b{{color:#E7EDEE;font-weight:600}}
.url{{position:absolute;right:84px;bottom:50px;font:400 24px 'IBM Plex Mono',monospace;color:#7F8D90}}
</style><div class=bar></div><div class=eb><i></i>{html.escape(c['eyebrow'])}</div><h1>{html.escape(c['line1'])}<span>{html.escape(c['line2'])}</span></h1><div class=sts>{st}</div><div class=by>By <b>Chuhee Lee</b></div><div class=url>blueplanet-ai.github.io/{slug}</div>"""

async def main(slugs):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for slug in slugs:
            ctx = await b.new_context(viewport={"width": 1240, "height": 900}, color_scheme="light", device_scale_factor=2)
            pg = await ctx.new_page()
            await pg.goto((ROOT / slug / "index.html").as_uri(), wait_until="networkidle")
            await pg.add_style_tag(content=".nav,.crumb,.idx{display:none!important}#glanceBody{width:1200px;margin:0}")
            await pg.wait_for_timeout(500)
            await (await pg.query_selector("#glanceBody")).screenshot(path=str(ROOT / slug / f"{slug}-at-a-glance.png"))
            await ctx.close()
            tmp = ROOT / "tools" / "_og_tmp.html"
            tmp.write_text(og_html(CARDS[slug], slug), encoding="utf-8")
            ctx = await b.new_context(viewport={"width": 1200, "height": 630})
            pg = await ctx.new_page()
            await pg.goto(tmp.as_uri(), wait_until="networkidle")
            await pg.wait_for_timeout(400)
            await pg.screenshot(path=str(ROOT / slug / "og-image.png"))
            await ctx.close(); tmp.unlink()
            print("exported", slug)
        await b.close()

if __name__ == "__main__":
    asyncio.run(main(sys.argv[1:] or list(CARDS)))
