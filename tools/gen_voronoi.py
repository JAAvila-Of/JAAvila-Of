#!/usr/bin/env python3
"""Voronoi dinamico como SVG animado (assets/voronoi.svg).
Semillas que derivan en orbitas cerradas (loop perfecto). Cada celda se calcula
como interseccion de semiplanos (bisectrices) recortada al rectangulo via
Sutherland-Hodgman -> sin scipy. Frame-flip (steps) para mover las fronteras."""
import numpy as np

W, H, N, FRAMES, DUR = 760, 120, 18, 40, 3.0
PAL = ["#0e1f15", "#12281a", "#16331f", "#1c4a2b", "#235c34", "#2c7a44",
       "#15131f", "#221a33", "#2a2140", "#3b2d5e"]
ACCENT = {3: "#39d353", 11: "#bb9af7", 15: "#39d353"}

rng = np.random.default_rng(7)
base = rng.uniform([0, 0], [W, H], size=(N, 2))
amp = rng.uniform(10, 30, size=(N, 2))
pha = rng.uniform(0, 2 * np.pi, size=(N, 2))


def clip(poly, a, c):
    """Recorta poligono al semiplano a·x <= c (Sutherland-Hodgman)."""
    out = []
    n = len(poly)
    for k in range(n):
        S, E = poly[k], poly[(k + 1) % n]
        ds, de = a[0] * S[0] + a[1] * S[1] - c, a[0] * E[0] + a[1] * E[1] - c
        if ds <= 0:
            out.append(S)
        if (ds < 0) != (de < 0):
            t = ds / (ds - de)
            out.append((S[0] + t * (E[0] - S[0]), S[1] + t * (E[1] - S[1])))
    return out


def cell(pts, i):
    p = pts[i]
    poly = [(0.0, 0.0), (W, 0.0), (W, H), (0.0, H)]
    for j in range(len(pts)):
        if j == i:
            continue
        q = pts[j]
        a = (q[0] - p[0], q[1] - p[1])
        c = (q[0] ** 2 + q[1] ** 2 - p[0] ** 2 - p[1] ** 2) / 2.0
        poly = clip(poly, a, c)
        if len(poly) < 3:
            return None
    return poly


css = []
for i in range(FRAMES):
    a, b = i / FRAMES * 100, (i + 1) / FRAMES * 100
    css.append(f".v{i}{{opacity:0;animation:v{i} {DUR}s steps(1) infinite}}")
    css.append(f"@keyframes v{i}{{0%{{opacity:0}}{max(a-0.01,0):.3f}%{{opacity:0}}"
               f"{a:.3f}%{{opacity:1}}{b-0.01:.3f}%{{opacity:1}}{b:.3f}%{{opacity:0}}100%{{opacity:0}}}}")

parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
         f'role="img" aria-label="Dynamic Voronoi"><defs><style>{"".join(css)}</style></defs>',
         f'<rect width="{W}" height="{H}" fill="#0d1117"/>']
for f in range(FRAMES):
    t = f / FRAMES
    pts = base + amp * np.column_stack([np.cos(2 * np.pi * t + pha[:, 0]),
                                        np.sin(2 * np.pi * t + pha[:, 1])])
    pts = np.clip(pts, [2, 2], [W - 2, H - 2])
    parts.append(f'<g class="v{f}">')
    for i in range(N):
        poly = cell(pts, i)
        if poly is None:
            continue
        d = " ".join(f"{x:.1f},{y:.1f}" for x, y in poly)
        fill = ACCENT.get(i, PAL[i % len(PAL)])
        parts.append(f'<polygon points="{d}" fill="{fill}" stroke="#0d1117" stroke-width="1.4"/>')
    parts.append("</g>")
parts.append("</svg>")
open("assets/voronoi.svg", "w", encoding="utf-8").write("".join(parts))
print(f"assets/voronoi.svg generado: {W}x{H}, {FRAMES} frames, {N} celdas")
