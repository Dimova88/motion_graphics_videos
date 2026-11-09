#!/usr/bin/env python3
"""Build EP01 v3 host index.html from measured voice-v2 clip durations.

Slots are contiguous: slot_i = clip_i + HOLD (0.45 s, last one 0.6 s). No dead air —
each section starts exactly when the previous ends. Rewrites each composition's
<audio ... data-duration> with the true measured duration and writes index.html.
"""
import json, re, subprocess, sys, pathlib

ROOT = pathlib.Path("/home/user/motion_graphics_videos/econ-channel/ep01")
FF = "/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v9.0.2"
HOLD = 0.45
HOLD_LAST = 0.60
VOICE = ROOT / "assets/voice-v2"
COMP = ROOT / "compositions-v2"

# filename of each composition per scene index 1..36
SCENES = {
    1: "01-hook1", 2: "02-pregunta", 3: "03-tresolas", 4: "04-cafe",
    5: "05-definicion", 6: "06-cesta", 7: "07-lineas", 8: "08-tres-olas",
    9: "09-ola1-title", 10: "10-cheques", 11: "11-atasco", 12: "12-misil",
    13: "13-picos", 14: "14-ola2-title", 15: "15-fed", 16: "16-bce",
    17: "17-enfriamiento", 18: "18-hipoteca", 19: "19-desinflacion",
    20: "20-nadie-devolvio", 21: "21-ola3-title", 22: "22-petroleo",
    23: "23-ormuz", 24: "24-precios-hoy", 25: "25-efecto-domino",
    26: "26-nl", 27: "27-prima", 28: "28-expectativas", 29: "29-escenarios",
    30: "30-serpiente", 31: "31-regla1", 32: "32-regla2", 33: "33-regla3",
    34: "34-tarea", 35: "35-repaso", 36: "36-outro",
}

def measure(path: pathlib.Path) -> float:
    out = subprocess.run([FF, "-i", str(path)], stderr=subprocess.PIPE).stderr.decode()
    m = re.search(r"Duration:\s*(\d+):(\d+):([\d.]+)", out)
    if not m:
        raise RuntimeError(f"no duration parsed for {path}")
    h, mnt, s = m.groups()
    return int(h) * 3600 + int(mnt) * 60 + float(s)

durs, missing = {}, []
for i in range(1, 37):
    p = VOICE / f"{i:02d}.mp3"
    if not p.exists():
        missing.append(i)
    else:
        durs[i] = measure(p)

if missing:
    print("MISSING CLIPS:", ", ".join(f"{m:02d}" for m in missing))
    sys.exit(1)

# Rewrite audio data-duration in each composition to the true clip length
for i, name in SCENES.items():
    comp = COMP / f"{name}.html"
    src = comp.read_text()
    new, n = re.subn(
        rf'(<audio id="s{i:02d}-vo"[^>]*?data-duration=")[0-9.]+(")',
        lambda m: m.group(1) + f"{durs[i]:.3f}" + m.group(2),
        src,
    )
    if n != 1:
        print(f"WARN: audio data-duration rewrite matched {n} times in {comp.name}")
    comp.write_text(new)

# Compute contiguous slots
starts, t = {}, 0.0
for i in range(1, 37):
    starts[i] = t
    hold = HOLD_LAST if i == 36 else HOLD
    t += durs[i] + hold
TOTAL = t

sections = []
for i in range(1, 37):
    comp_id = f"s{i:02d}"
    hold = HOLD_LAST if i == 36 else HOLD
    dur = durs[i] + hold
    sections.append(
        f'      <div id="{comp_id}" data-composition-id="{comp_id}" data-composition-src="compositions-v2/{SCENES[i]}.html"\n'
        f'           data-start="{starts[i]:.2f}" data-duration="{dur:.2f}" data-track-index="{i}" data-width="1920" data-height="1080"></div>'
    )
sections_html = "\n".join(sections)

index = f"""<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <title>El Precio de Todo — EP01 · ¿Por qué todo está más caro?</title>
    <script src="./assets/vendor/gsap.min.js"></script>
    <style>
      @font-face {{ font-family: "Anton"; src: url("./assets/fonts/anton-latin-400-normal.woff2") format("woff2"); font-weight: 400; font-style: normal; font-display: swap; }}
      @font-face {{ font-family: "Archivo Black"; src: url("./assets/fonts/archivo-black-latin-400-normal.woff2") format("woff2"); font-weight: 400; font-style: normal; font-display: swap; }}
      @font-face {{ font-family: "Archivo"; src: url("./assets/fonts/archivo-latin-400-normal.woff2") format("woff2"); font-weight: 400; font-style: normal; font-display: swap; }}
      @font-face {{ font-family: "Archivo"; src: url("./assets/fonts/archivo-latin-700-normal.woff2") format("woff2"); font-weight: 700; font-style: normal; font-display: swap; }}
      :root {{
        --board: #10312B;
        --board2: #0B241F;
        --chalk: #EDE6D3;
        --yellow: #FFD84D;
        --coral: #FF6B57;
        --mut: rgba(237,230,211,0.55);
        --mut2: rgba(237,230,211,0.32);
        --display: "Anton", "Archivo Black", sans-serif;
        --body: "Archivo", "Liberation Sans", sans-serif;
      }}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1920px; height: 1080px; overflow: hidden; background: var(--board2); }}
      #root {{ position: relative; width: 1920px; height: 1080px; overflow: hidden; background: var(--board2); font-family: var(--body); color: var(--chalk); }}
    </style>
  </head>
  <body>
    <div
      id="root"
      data-composition-id="main"
      data-start="0"
      data-duration="{TOTAL:.2f}"
      data-width="1920"
      data-height="1080"
    >
{sections_html}
    </div>
    <script>
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
"""

(ROOT / "index.html").write_text(index)
(ROOT / "durations.json").write_text(json.dumps({str(k): v for k, v in durs.items()}, indent=2))
print(f"TOTAL {TOTAL:.2f}s  ({TOTAL/60:.1f} min)  sections=36")
print("Wrote index.html + durations.json")
for i in range(1, 37):
    print(f"{i:02d} start={starts[i]:8.2f} dur={durs[i]:6.2f} slot={(HOLD_LAST if i==36 else HOLD)+durs[i]:6.2f}")
