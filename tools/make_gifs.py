#!/usr/bin/env python3
"""GIFs de alta calidad de cada asset animado, via ffmpeg (palette global ->
sin parpadeo ni bandas). cairosvg renderiza cada frame a PNG; ffmpeg ensambla.
Salida en assets/_preview/."""
import cairosvg, os, re, shutil, subprocess

OUT = "assets/_preview"
os.makedirs(OUT, exist_ok=True)
BG = "#0d1117"


def render_png(svg, w, path):
    cairosvg.svg2png(bytestring=svg.encode("utf-8"), output_width=w,
                     write_to=path, background_color=BG)


def gif(name, fps):
    d = f"{OUT}/_f_{name}"
    pal = f"{d}/pal.png"
    out = f"{OUT}/{name}.gif"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", f"{d}/f_%04d.png",
                    "-vf", "palettegen=max_colors=256:stats_mode=full", pal], check=True)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-framerate", str(fps),
                    "-i", f"{d}/f_%04d.png", "-i", pal, "-filter_complex",
                    "[0:v][1:v]paletteuse=dither=bayer:bayer_scale=3", out], check=True)
    shutil.rmtree(d)
    print(f"  {out}  ({os.path.getsize(out)//1024} KB)")


def frames_dir(name):
    d = f"{OUT}/_f_{name}"
    if os.path.isdir(d):
        shutil.rmtree(d)
    os.makedirs(d)
    return d


# ── 1) Game of Life ────────────────────────────────────────────────
print("game of life…")
gol = open("assets/gol.svg", encoding="utf-8").read()
d = frames_dir("gol")
for i in range(62):
    s = gol.replace(f'<g class="f{i}">', f'<g class="f{i}" style="opacity:1">')
    render_png(s, 560, f"{d}/f_{i+1:04d}.png")
gif("gol", 8)

# ── 2) Voronoi ─────────────────────────────────────────────────────
print("voronoi…")
vor = open("assets/voronoi.svg", encoding="utf-8").read()
d = frames_dir("voronoi")
for i in range(40):
    s = vor.replace(f'<g class="v{i}">', f'<g class="v{i}" style="opacity:1">')
    render_png(s, 760, f"{d}/f_{i+1:04d}.png")
gif("voronoi", 14)

# ── 3) Banner (shimmer) ────────────────────────────────────────────
print("banner…")
banner = re.sub(r"<animateTransform[^>]*/>", "",
                open("assets/banner.svg", encoding="utf-8").read())
d = frames_dir("banner")
for k in range(36):
    x = -1 + 2 * k / 35
    s = banner.replace('<linearGradient id="shine" x1="0" y1="0" x2="1" y2="0">',
                       f'<linearGradient id="shine" x1="0" y1="0" x2="1" y2="0" '
                       f'gradientTransform="translate({x:.3f} 0)">')
    render_png(s, 760, f"{d}/f_{k+1:04d}.png")
gif("banner", 12)

# ── 4) Terminal (reconstruida por frame) ───────────────────────────
print("terminal…")
G, CMD, DIM, DK, PUR = "#39d353", "#e6edf3", "#8b949e", "#30363d", "#bb9af7"


def reveal(t, p, s, e):
    if p <= s: return 0
    if p >= e: return len(t)
    return int(len(t) * (p - s) / (e - s))


def term(p, idx):
    c1 = "whoami"[:reveal("whoami", p, .05, .14)]
    c2v = "ridge run hello.ridge"
    c2 = c2v[:reveal(c2v, p, .24, .40)]
    out1, out2 = p >= .17, p >= .44
    nb = int(round(10 * max(0.0, min(1.0, (p - .46) / .10))))
    okv, out3, pr = p >= .60, p >= .68, p >= .76
    cur = pr and (idx // 3) % 2 == 0
    e = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 290" '
         'font-family="\'JetBrains Mono\',\'Consolas\',monospace" font-size="16">',
         '<rect x="6" y="6" width="708" height="278" rx="12" fill="#0d1117" stroke="#30363d" stroke-width="1.5"/>',
         '<rect x="6" y="6" width="708" height="34" fill="#161b22"/>']
    for cx, col in ((26, "#ff5f56"), (48, "#ffbd2e"), (70, "#27c93f")):
        e.append(f'<circle cx="{cx}" cy="23" r="6" fill="{col}"/>')
    e.append('<text x="360" y="28" text-anchor="middle" fill="#8b949e" font-size="13">jose@ridge: ~/profile</text>')
    e.append(f'<text x="22" y="82" fill="{G}">$</text><text x="40" y="82" fill="{CMD}">{c1}</text>')
    if out1:
        e.append(f'<text x="22" y="110" xml:space="preserve"><tspan fill="{CMD}">Jose Angel Avila</tspan>'
                 f'<tspan fill="{DIM}">  ·  language designer</tspan></text>')
    e.append(f'<text x="22" y="142" fill="{G}">$</text>'
             f'<text x="40" y="142" fill="{CMD}" xml:space="preserve">{c2}</text>')
    if out2:
        e.append(f'<text x="22" y="170" fill="{DIM}">compiling</text>'
                 f'<text x="118" y="170" fill="{DK}">[</text>')
        if nb:
            e.append(f'<text x="128" y="170" fill="{G}" letter-spacing="1">{"█"*nb}</text>')
        e.append(f'<text x="248" y="170" fill="{DK}">]</text>')
    if okv:
        e.append(f'<text x="266" y="170" xml:space="preserve"><tspan fill="{G}">ok</tspan>'
                 f'<tspan fill="{DIM}">  ·  target </tspan><tspan fill="{PUR}">BEAM</tspan></text>')
    if out3:
        e.append(f'<text x="22" y="198" fill="{G}">Hello from the BEAM!</text>')
    if pr:
        e.append(f'<text x="22" y="232" fill="{G}">$</text>')
    if cur:
        e.append(f'<rect x="40" y="218" width="11" height="19" fill="{G}"/>')
    e.append("</svg>")
    return "".join(e)


N = 60
d = frames_dir("terminal")
for k in range(N):
    render_png(term(k / N, k), 720, f"{d}/f_{k+1:04d}.png")
gif("terminal", 7)

print("LISTO")
