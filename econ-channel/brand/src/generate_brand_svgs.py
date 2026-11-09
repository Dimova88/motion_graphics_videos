#!/usr/bin/env python3
"""Genera los SVG maestros de la marca «El Precio de Todo» (Opción B).

Estilo: pizarra verde oscuro + tiza. Los circulos y garabatos usan jitter
muestral determinista (semilla fija) para simular trazo de mano.

Uso:  python3 generate_brand_svgs.py   (escribe los .svg en el directorio actual)
Render a PNG: ver BRAND-FINAL.md (cairosvg).
"""
import math, random, json

GREEN   = "#10312B"
GREEN2  = "#0B241F"
CREAM   = "#EDE6D3"
YELLOW  = "#FFD84D"
CORAL   = "#FF6B57"

def pts_circle(cx, cy, r, wobble, n=64, seed=1):
    rnd = random.Random(seed)
    pts = []
    for i in range(n):
        a = 2 * math.pi * i / n
        rr = r + rnd.uniform(-wobble, wobble)
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    d = "M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + " Z"
    return d

def polyline(points):
    return "M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in points)

def mark_group(cx, cy, scale, seed=7, euro=True):
    """Moneda de tiza con € partido por una grieta. Devuelve el <g> centrado en (cx,cy)."""
    s = scale
    o = []
    o.append(f'<g transform="translate({cx},{cy}) scale({s})">')
    # halo exterior impreciso (polvo de tiza)
    o.append(f'<path d="{pts_circle(0,0,300,26,72,seed)}" fill="none" stroke="{CREAM}" stroke-width="4" opacity="0.16"/>')
    # anillo exterior
    o.append(f'<path d="{pts_circle(0,0,284,11,72,seed+1)}" fill="{GREEN2}" fill-opacity="0" stroke="{CREAM}" stroke-width="24"/>')
    # anillo de puntos finos
    o.append(f'<circle cx="0" cy="0" r="244" fill="none" stroke="{CREAM}" stroke-width="7" stroke-dasharray="3 27" opacity="0.85"/>')
    # anillo interior
    o.append(f'<path d="{pts_circle(0,0,206,9,64,seed+2)}" fill="none" stroke="{CREAM}" stroke-width="10"/>')
    if euro:
        o.append(f'<text x="0" y="102" text-anchor="middle" font-family="Anton, \'Archivo Black\', sans-serif" '
                 f'font-size="284" fill="{YELLOW}" transform="rotate(-4)" letter-spacing="0">€</text>')
    # grieta: poligono jagged relleno con el color del tablero (recorta la moneda)
    crack = [(-52,-330),(18,-218),(-28,-128),(39,-18),(-8,84),(52,196),(8,332)]
    o.append(f'<path d="{polyline(crack)}" fill="none" stroke="{GREEN}" stroke-width="38" '
             f'stroke-linejoin="round" stroke-linecap="round" opacity="0.98"/>')
    o.append(f'<path d="{polyline(crack)}" fill="none" stroke="{CORAL}" stroke-width="6" '
             f'stroke-dasharray="18 14" stroke-linejoin="round" opacity="0.9"/>')
    # destellos de tiza en la grieta
    for (x1,y1,x2,y2) in [(-96,-96,-140,-132),(104,8,150,-6),(-92,152,-128,196)]:
        o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{CREAM}" stroke-width="7" '
                 f'stroke-linecap="round" opacity="0.8"/>')
    o.append('</g>')
    return "\n".join(o)

def svg(w, h, body, extra_defs=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs>
<radialGradient id="board" cx="50%" cy="42%" r="75%">
  <stop offset="0%" stop-color="{GREEN}"/>
  <stop offset="100%" stop-color="{GREEN2}"/>
</radialGradient>
{extra_defs}
</defs>
{body}
</svg>
'''

def ledger_lines(w, h, every=150, op=0.06):
    out = []
    y = every
    while y < h:
        out.append(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}" stroke="{CREAM}" stroke-width="2" opacity="{op}"/>')
        y += every
    return "\n".join(out)

# ---------- 1) LOGO MARK (avatar master) ----------
def logo_mark():
    body = f'''
<rect x="0" y="0" width="1024" height="1024" rx="212" fill="url(#board)"/>
<rect x="46" y="46" width="932" height="932" rx="172" fill="none" stroke="{CREAM}"
      stroke-width="4" stroke-dasharray="30 12 6 12" opacity="0.28"/>
{ledger_lines(1024, 1024, 170, 0.05)}
{mark_group(512, 500, 1.08, seed=7)}
'''
    return svg(1024, 1024, body)

# ---------- 2) LOCKUP HORIZONTAL ----------
def logo_lockup():
    body = f'''
<rect x="0" y="0" width="1680" height="560" rx="0" fill="url(#board)"/>
{ledger_lines(1680, 560, 112, 0.05)}
{mark_group(268, 268, 0.78, seed=11)}
<text x="520" y="238" font-family="Anton, 'Archivo Black', sans-serif" font-size="152"
      fill="{CREAM}" letter-spacing="2">EL PRECIO</text>
<g transform="rotate(-1.2 700 380)">
  <rect x="512" y="292" width="476" height="150" rx="8" fill="{YELLOW}"/>
  <text x="536" y="408" font-family="Anton, 'Archivo Black', sans-serif" font-size="128"
        fill="{GREEN}" letter-spacing="2">DE TODO</text>
</g>
<text x="520" y="516" font-family="Archivo, sans-serif" font-size="27.5" letter-spacing="6.5"
      fill="{CREAM}" opacity="0.78">TODO TIENE UN PRECIO — Y UNA HISTORIA.</text>
'''
    return svg(1680, 560, body)

# ---------- 3) BANNER PARA YOUTUBE (2560x1440, safe area central) ----------
def banner():
    # garabato de gráfico subiendo (a la derecha)
    rnd = random.Random(42)
    chart = [(1500 + i*72, 1080 - i*44 - rnd.uniform(0, 26)) for i in range(13)]
    arrow = f'<path d="{polyline(chart)}" fill="none" stroke="{CREAM}" stroke-width="12" opacity="0.9" stroke-linejoin="round"/>'
    ex, ey = chart[-1]
    arrow += f'''
<path d="{polyline([(ex-96, ey+40),(ex+8, ey-14)])}" fill="none" stroke="{CREAM}" stroke-width="12" stroke-linecap="round"/>
<path d="M{ex+8},{ey-14} L{ex-84},{ey-16} M{ex+8},{ey-14} L{ex-30},{ey+78}" stroke="{CREAM}" stroke-width="12" stroke-linecap="round" fill="none"/>
<path d="{pts_circle(ex+8, ey-14, 96, 12, 40, 5)}" fill="none" stroke="{YELLOW}" stroke-width="10"/>
'''
    body = f'''
<rect x="0" y="0" width="2560" height="1440" fill="url(#board)"/>
{ledger_lines(2560, 1440, 160, 0.05)}
{mark_group(430, 500, 0.92, seed=7)}
<text x="830" y="392" font-family="Anton, 'Archivo Black', sans-serif" font-size="188"
      fill="{CREAM}" letter-spacing="2">EL PRECIO</text>
<g transform="rotate(-1.1 1130 590)">
  <rect x="826" y="478" width="606" height="178" rx="8" fill="{YELLOW}"/>
  <text x="856" y="612" font-family="Anton, 'Archivo Black', sans-serif" font-size="152"
        fill="{GREEN}" letter-spacing="2">DE TODO</text>
</g>
<text x="830" y="760" font-family="Archivo, sans-serif" font-size="31" letter-spacing="7.5"
      fill="{CREAM}" opacity="0.8">TODO TIENE UN PRECIO — Y UNA HISTORIA.</text>
<text x="830" y="856" font-family="Archivo, sans-serif" font-size="22" letter-spacing="10"
      fill="{YELLOW}" opacity="0.9">ECONOMÍA · EJEMPLOS REALES · NÚMEROS DE HOY</text>
{arrow}
'''
    return svg(2560, 1440, body)

# ---------- 4) MINIATURA MOCK (formula B, candidato EP01-1) ----------
def thumb_mock():
    # garabato de subrayado coral bajo el número
    underline = polyline([(84 + i*24, 486 + random.Random(3).uniform(-5, 5)) for i in range(37)])
    body = f'''
<rect x="0" y="0" width="1280" height="720" fill="url(#board)"/>
{ledger_lines(1280, 720, 120, 0.06)}
<text x="72" y="104" font-family="Archivo, sans-serif" font-size="27" letter-spacing="11"
      fill="{CORAL}">FLASH · OCTUBRE 2026</text>
<g transform="rotate(-2 1105 96)">
  <rect x="902" y="40" width="330" height="116" rx="8" fill="{CREAM}"/>
  <text x="1067" y="122" text-anchor="middle" font-family="Anton, 'Archivo Black', sans-serif"
        font-size="84" fill="{GREEN}">OTRA VEZ</text>
</g>
<text x="64" y="452" font-family="Anton, 'Archivo Black', sans-serif" font-size="330"
      fill="{YELLOW}" letter-spacing="-4">+4,0%</text>
<path d="{underline}" fill="none" stroke="{CORAL}" stroke-width="14" stroke-linecap="round" opacity="0.95"/>
<line x1="72" y1="572" x2="1208" y2="572" stroke="{CREAM}" stroke-width="3" opacity="0.35"/>
<text x="72" y="640" font-family="Archivo, sans-serif" font-size="30" letter-spacing="4"
      fill="{CREAM}" opacity="0.9">ZONA EURO · IPC OCT-2026 · EUROSTAT</text>
'''
    return svg(1280, 720, body)

if __name__ == "__main__":
    for name, fn in [("logo-mark.svg", logo_mark), ("logo-lockup.svg", logo_lockup),
                     ("banner.svg", banner), ("thumbnail-mock.svg", thumb_mock)]:
        with open(name, "w") as fh:
            fh.write(fn())
        print("wrote", name)
