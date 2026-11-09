#!/usr/bin/env python3
"""Build EP01 v3 subtitle files (.srt + .ass) from VO-SCRIPT-v2.md + durations.json.

Cues are sentence-sized, time-proportional to character count, and share the exact
slot timeline of build_index.py (clip starts at slot_start + 0.15 s). The .ass file is
burned into the video with ffmpeg's subtitles filter (libass, Archivo font).
"""
import json, pathlib, re, sys

ROOT = pathlib.Path("/home/user/motion_graphics_videos/econ-channel/ep01")
SCRIPT = ROOT / "VO-SCRIPT-v2.md"
HOLD = 0.45
HOLD_LAST = 0.60
PAD_START = 0.15
MAX_CUE = 72          # chars per cue
CUE_MIN = 0.9         # s, minimum cue length
LINE_WRAP = 40        # chars per line when wrapping

text = SCRIPT.read_text()

# Parse scenes: "## 01\ntext..." until next "##" or EOF
scenes = {}
for m in re.finditer(r"^##\s+(\d+)\s*$\n(.*?)(?=^##\s+\d+\s*$|\Z)", text, re.M | re.S):
    n = int(m.group(1))
    body = " ".join(m.group(2).split()).strip()
    scenes[n] = body

missing_scenes = [i for i in range(1, 37) if i not in scenes]
if missing_scenes:
    print("MISSING SCENES IN SCRIPT:", missing_scenes)
    sys.exit(1)

durs = {int(k): v for k, v in json.loads((ROOT / "durations.json").read_text()).items()}
starts = {}
t = 0.0
for i in range(1, 37):
    starts[i] = t
    t += durs[i] + (HOLD_LAST if i == 36 else HOLD)

def split_units(s: str):
    units = re.split(r"(?<=[.!?…])\s+", s)
    out = []
    for u in units:
        u = u.strip()
        if not u:
            continue
        # hard-split very long units at commas
        while len(u) > MAX_CUE:
            cut = u.rfind(", ", 0, MAX_CUE)
            if cut <= 10:
                cut = u.rfind(" ", 0, MAX_CUE)
            if cut <= 10:
                cut = MAX_CUE
            out.append(u[:cut + 1].strip())
            u = u[cut + 1:].strip()
        out.append(u)
    return out

def wrap_two(s: str):
    if len(s) <= LINE_WRAP:
        return s
    cut = s.rfind(" ", 0, LINE_WRAP + 1)
    if cut == -1:
        cut = LINE_WRAP
    return s[:cut] + "\n" + s[cut + 1:]

cues = []  # (start, end, text)
for i in range(1, 37):
    body = scenes[i]
    clip = durs[i]
    units = split_units(body)
    total = sum(len(u) for u in units)
    clip_units = [max(CUE_MIN, (len(u) / total) * clip) for u in units]
    scale = clip / sum(clip_units)
    clip_units = [d * scale for d in clip_units]
    t_scene = starts[i] + PAD_START
    acc = 0.0
    for u, dur in zip(units, clip_units):
        cues.append([t_scene + acc, t_scene + acc + dur, u])
        acc += dur

def fmt_srt(t):
    h = int(t // 3600); m = int((t % 3600) // 60); s = int(t % 60); ms = int(round((t - int(t)) * 1000))
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def fmt_ass(t):
    h = int(t // 3600); m = int((t % 3600) // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"

srt_lines = []
for idx, (a, b, txt) in enumerate(cues, 1):
    srt_lines.append(str(idx))
    srt_lines.append(f"{fmt_srt(a)} --> {fmt_srt(b)}")
    srt_lines.append(wrap_two(txt))
    srt_lines.append("")
(ROOT / "renders" / "el-precio-de-todo-ep01.srt").write_text("\n".join(srt_lines))

header = """[Script Info]
Title: El Precio de Todo — EP01
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Archivo,46,&H00D3E6ED,&H00D3E6ED,&H00000000,&H80000000,-1,0,0,0,100,100,0.5,0,1,3.2,0,2,80,80,64,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
events = []
for a, b, txt in cues:
    t = wrap_two(txt).replace("\n", "\\N")
    events.append(f"Dialogue: 0,{fmt_ass(a)},{fmt_ass(b)},Default,,0,0,0,,{t}")
(ROOT / "renders" / "el-precio-de-todo-ep01.ass").write_text(header + "\n".join(events) + "\n")
print(f"Cues: {len(cues)}  -> renders/el-precio-de-todo-ep01.srt + .ass")
