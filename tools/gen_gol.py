#!/usr/bin/env python3
"""Genera un Game of Life ASCII animado como SVG (assets/gol.svg).
Patron: Gosper glider gun (dispara planeadores en bucle).
Tecnica: cada generacion es un <g> de tspans; se muestran por turnos via
keyframes CSS (todas con la misma duracion para loop limpio en GitHub)."""
import numpy as np

COLS, ROWS, FRAMES = 54, 22, 62
ALIVE, FG, DIM, BG = "39d353", "e6edf3", "8b949e", "0d1117"
CHW, CHH, PAD, TOP = 9.0, 16.0, 16, 40
W = int(PAD * 2 + COLS * CHW)
H = int(TOP + PAD + ROWS * CHH)
DUR = 9.2  # segundos por ciclo completo

# Gosper glider gun (col,row), desplazado 1,1
GUN = [(0,4),(0,5),(1,4),(1,5),(10,4),(10,5),(10,6),(11,3),(11,7),(12,2),
       (12,8),(13,2),(13,8),(14,5),(15,3),(15,7),(16,4),(16,5),(16,6),(17,5),
       (20,2),(20,3),(20,4),(21,2),(21,3),(21,4),(22,1),(22,5),(24,0),(24,1),
       (24,5),(24,6),(34,2),(34,3),(35,2),(35,3)]

def step(g):
    n = sum(np.roll(np.roll(g, i, 0), j, 1)
            for i in (-1,0,1) for j in (-1,0,1) if (i,j) != (0,0))
    return (n == 3) | (g & (n == 2))

# simular (sin wrap: limpiamos bordes en cada paso)
grid = np.zeros((ROWS, COLS), bool)
for x, y in GUN:
    grid[y + 1, x + 1] = True
frames = []
for _ in range(FRAMES):
    frames.append(grid.copy())
    grid = step(grid)
    grid[0,:] = grid[-1,:] = grid[:,0] = grid[:,-1] = False

# construir SVG
css = [
    f".cap{{font:600 13px 'JetBrains Mono',monospace;fill:#{DIM}}}",
    f".gen{{font:700 13px 'JetBrains Mono',monospace;fill:#{ALIVE}}}",
    f".cell{{font:15px 'JetBrains Mono',monospace;fill:#{ALIVE}}}",
    f".scr{{animation:scr {DUR}s linear infinite}}",
    "@keyframes scr{0%{opacity:0}2%{opacity:1}97%{opacity:1}100%{opacity:0}}",
]
for i in range(FRAMES):
    a, b = i / FRAMES * 100, (i + 1) / FRAMES * 100
    css.append(f".f{i}{{opacity:0;animation:f{i} {DUR}s steps(1) infinite}}")
    css.append(
        f"@keyframes f{i}{{0%{{opacity:0}}{max(a-0.01,0):.3f}%{{opacity:0}}"
        f"{a:.3f}%{{opacity:1}}{b-0.01:.3f}%{{opacity:1}}{b:.3f}%{{opacity:0}}"
        f"100%{{opacity:0}}}}")

parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
    f'width="{W}" height="{H}" role="img" aria-label="Conway Game of Life in ASCII">',
    f"<defs><style>{''.join(css)}</style></defs>",
    f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="10" fill="#{BG}" '
    f'stroke="#30363d" stroke-width="1.5"/>',
    f'<text x="{PAD}" y="26" class="cap">$ ridge run examples/game_of_life.ridge</text>',
    f'<g class="scr">',
]
for i, fr in enumerate(frames):
    parts.append(f'<g class="f{i}">')
    parts.append(f'<text x="{W-PAD}" y="26" text-anchor="end" class="gen">gen {i:02d}</text>')
    parts.append(f'<text xml:space="preserve" class="cell">')
    for r in range(ROWS):
        if not fr[r].any():
            continue
        row = "".join("█" if fr[r, c] else " " for c in range(COLS)).rstrip()
        y = TOP + PAD + r * CHH
        row = row.replace("&", "&amp;").replace("<", "&lt;")
        parts.append(f'<tspan x="{PAD}" y="{y:.0f}">{row}</tspan>')
    parts.append("</text></g>")
parts.append("</g></svg>")

open("assets/gol.svg", "w", encoding="utf-8").write("".join(parts))
print(f"assets/gol.svg generado: {W}x{H}, {FRAMES} frames")
