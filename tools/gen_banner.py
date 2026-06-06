#!/usr/bin/env python3
"""Banner = ASCII art figlet (fuente Doom) 'JAAvila' RASTERIZADO con una fuente
monoespaciada real (Consolas) + shimmer verde animado -> assets/banner.gif.
Rasterizar evita el problema de interlineado del <text> SVG (que varia por
fuente del visor y descoloca las filas). El GIF se ve identico en GitHub."""
import os, shutil, subprocess
from PIL import Image, ImageDraw, ImageFont

# figlet -f Doom "JAAvila"
ART = [
    r"   ___  ___    ___        _ _       ",
    r"  |_  |/ _ \  / _ \      (_) |      ",
    r"    | / /_\ \/ /_\ \_   ___| | __ _ ",
    r"    | |  _  ||  _  \ \ / / | |/ _` |",
    r"/\__/ / | | || | | |\ V /| | | (_| |",
    r"\____/\_| |_/\_| |_/ \_/ |_|_|\__,_|",
]
SUB = "language designer · Rust · .NET · BEAM"
BG = (13, 17, 23)
BASE = (57, 211, 83)      # #39d353 (siempre legible)
BRIGHT = (190, 255, 211)  # destello
DIM = (44, 122, 68)       # subtitulo
FRAMES, PAD = 40, 26

font = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 40)
sfont = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 16)
asc, desc = font.getmetrics(); LH = asc + desc
cw = font.getlength("M")
cols = max(len(l) for l in ART)
W = int(PAD * 2 + cols * cw)
H = int(PAD + len(ART) * LH + 38 + PAD)


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def frame(f):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    center = -0.25 * W + 1.5 * W * (f / (FRAMES - 1))
    band = 0.22 * W
    for r, line in enumerate(ART):
        y = PAD + r * LH
        for c, ch in enumerate(line):
            if ch == " ":
                continue
            x = PAD + c * cw
            t = max(0.0, 1 - abs(x - center) / band)
            d.text((x, y), ch, font=font, fill=lerp(BASE, BRIGHT, t))
    d.text((PAD + 4, PAD + len(ART) * LH + 8), SUB, font=sfont, fill=DIM)
    return img


tmp = "assets/_f_banner"
if os.path.isdir(tmp):
    shutil.rmtree(tmp)
os.makedirs(tmp)
for f in range(FRAMES):
    frame(f).save(f"{tmp}/f_{f+1:04d}.png")

subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", f"{tmp}/f_%04d.png",
                "-vf", "palettegen=max_colors=256:stats_mode=full", f"{tmp}/pal.png"], check=True)
subprocess.run(["ffmpeg", "-y", "-v", "error", "-framerate", "12",
                "-i", f"{tmp}/f_%04d.png", "-i", f"{tmp}/pal.png", "-filter_complex",
                "[0:v][1:v]paletteuse=dither=bayer:bayer_scale=3", "assets/banner.gif"], check=True)
shutil.rmtree(tmp)
print("assets/banner.gif generado:", W, "x", H, "-", FRAMES, "frames (Doom ASCII + shimmer)")
