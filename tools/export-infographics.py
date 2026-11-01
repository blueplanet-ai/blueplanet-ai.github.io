#!/usr/bin/env python3
"""Re-export each report's infographic PNG and 1200x630 social preview.

Usage:  python3 tools/export-infographics.py [report-folder ...]
Needs:  pip install playwright && playwright install chromium
Pages are served from a local web server (127.0.0.1, random port) so root paths
like /assets/... resolve. Fonts load from Google Fonts; if it can't be reached,
locally installed Newsreader, Saira and IBM Plex Mono are used instead (install
them from the google/fonts repository, e.g. into ~/.fonts). A warning is printed
for any family that is neither downloadable nor installed.
Outputs: <report>/<report>-at-a-glance.png  (from the #glanceBody block, light theme, 2x)
         <report>/og-image.png               (from tools/og-cards.json)
"""
import asyncio, contextlib, functools, html, http.server, json, pathlib, sys, threading, urllib.request
from playwright.async_api import async_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
CARDS = json.loads((ROOT / "tools/og-cards.json").read_text(encoding="utf-8"))
FONTS = "https://fonts.googleapis.com/css2?family=Saira:wght@400;500;600;700&family=Newsreader:wght@400;500&family=IBM+Plex+Mono:wght@400;500;600&display=swap"
FAMILIES = ("Newsreader", "Saira", "IBM Plex Mono")
HIDE = ".nav,.crumb,.idx,.rp{display:none!important}#glanceBody{width:1200px;margin:0}"

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass

@contextlib.contextmanager
def local_server():
    """Serve the repo root on 127.0.0.1 so root-absolute paths resolve as on the live site."""
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(QuietHandler, directory=str(ROOT)))
    t = threading.Thread(target=srv.serve_forever, daemon=True)
    t.start()
    try:
        yield f"http://127.0.0.1:{srv.server_address[1]}"
    finally:
        srv.shutdown(); srv.server_close()

def google_fonts_reachable(timeout=5):
    try:
        req = urllib.request.Request(FONTS, headers={"User-Agent": "Mozilla/5.0 Chrome/120"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status == 200
    except Exception:
        return False

async def use_local_fonts(ctx):
    """Answer Google Fonts requests with an empty stylesheet, so the pages fall back to the
    installed families by name instead of waiting on a blocked network request."""
    await ctx.route("https://fonts.googleapis.com/**", lambda r: r.fulfill(status=200, content_type="text/css", body=""))
    await ctx.route("https://fonts.gstatic.com/**", lambda r: r.abort())

MISSING_JS = """fams => fams.filter(f => {
  const c = document.createElement('canvas').getContext('2d'), s = 'Hamburgefonstiv 0123456789';
  return ['monospace', 'serif'].every(g => { c.font = `72px ${g}`; const w = c.measureText(s).width;
    c.font = `72px "${f}", ${g}`; return c.measureText(s).width === w; });
})"""

async def settle(pg):
    await pg.evaluate("document.fonts.ready.then(() => true)")
    return await pg.evaluate(MISSING_JS, list(FAMILIES))

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
    online = google_fonts_reachable()
    if not online:
        print("Google Fonts unreachable: using locally installed fonts")
    warned = set()

    async def new_ctx(b, **kw):
        ctx = await b.new_context(**kw)
        if not online:
            await use_local_fonts(ctx)
        return ctx

    def warn(missing):
        for f in missing:
            if f not in warned:
                warned.add(f)
                print(f"WARNING: font '{f}' is not available; output uses a fallback face", file=sys.stderr)

    tmp = ROOT / "tools" / "_og_tmp.html"
    with local_server() as base:
        async with async_playwright() as p:
            b = await p.chromium.launch()
            try:
                for slug in slugs:
                    ctx = await new_ctx(b, viewport={"width": 1240, "height": 900}, color_scheme="light", device_scale_factor=2)
                    pg = await ctx.new_page()
                    await pg.goto(f"{base}/{slug}/", wait_until="networkidle")
                    await pg.add_style_tag(content=HIDE)
                    warn(await settle(pg))
                    await pg.wait_for_timeout(500)
                    await (await pg.query_selector("#glanceBody")).screenshot(path=str(ROOT / slug / f"{slug}-at-a-glance.png"))
                    await ctx.close()
                    tmp.write_text(og_html(CARDS[slug], slug), encoding="utf-8")
                    try:
                        ctx = await new_ctx(b, viewport={"width": 1200, "height": 630})
                        pg = await ctx.new_page()
                        await pg.goto(f"{base}/tools/{tmp.name}", wait_until="networkidle")
                        warn(await settle(pg))
                        await pg.wait_for_timeout(400)
                        await pg.screenshot(path=str(ROOT / slug / "og-image.png"))
                        await ctx.close()
                    finally:
                        tmp.unlink(missing_ok=True)
                    print("exported", slug)
            finally:
                await b.close()

if __name__ == "__main__":
    asyncio.run(main(sys.argv[1:] or list(CARDS)))
