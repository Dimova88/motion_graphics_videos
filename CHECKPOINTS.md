# Checkpoints

## v1 — f1-brazil-2026 (2026-11-09)

State of the first rendered video, saved before the story-driven rework.

- Tag: `f1-brazil-2026/v1` (points at branch commit containing the video)
- Project: `f1-brazil-2026/`
- Render: `f1-brazil-2026/renders/f1-brazil-2026-race-recap.mp4` (30s, 1920x1080, H.264/AAC)
- Voice: `voice-00` (male, en)
- Fact-check: Norris 1:35:23.504, Verstappen +14.602, Hadjar +24.485, Antonelli P5 (PEN), Russell P4, Piastri P6, Hamilton P9

Restore: `git checkout f1-brazil-2026/v1`

## v2 — f1-brazil-2026-story (2026-11-09)

Story-driven rework of the São Paulo GP recap, built on the v1 configuration.

- Project: `f1-brazil-2026-story/`
- Render: `f1-brazil-2026-story/renders/f1-brazil-2026-race-recap-story.mp4` (30s, 1920x1080, H.264/AAC, -16.7 LUFS)
- Voice: `voice-01` (more engaging, storyteller delivery), narration written as a five-act arc: Prologue (the storm) → Act I (the trap/grid penalties) → Act II (the start) → Act III (the climb, P21→P2) → Act IV (the flag) → Epilogue (pole to victory)
- Visual techniques adapted from the HyperFrames registry (github.com/heygen-com/hyperframes): `yt-prism-title` (chromatic red/blue offset title with focus-in blur), `hw-title` (marker underline draw-on), `news-ticker` (seamless two-copy marquee)
- Film grain (seed-stable feTurbulence SVG) + stronger vignette; facts unchanged from v1

v1 remains intact at tag `f1-brazil-2026/v1`.

## v3 — f1-brazil-2026-pipeline (2026-11-09)

Test of the new free/unlimited YouTube pipeline (see `PIPELINE.md`) on a 30s brief, ahead of 8–10 minute videos.

- Project: `f1-brazil-2026-pipeline/`
- Render: `f1-brazil-2026-pipeline/renders/f1-brazil-2026-pipeline-test.mp4` (30s, 1920x1080@30, H.264/AAC, -16.6 LUFS)
- Voice: `voice-01` rate 1.15 (assistant voice tool; Kokoro `hyperframes tts` is the local free path on machines that can reach model hosts — see `YOUTUBE-HYPERFRAMES-PLAYBOOK.md`)
- New vs v2: **sub-composition architecture** — `index.html` mounts one `compositions/<act>.html` per scene (`data-composition-src`, composition-local timing, `#root` inset:0 flex stage) instead of one monolithic file; **strict dead-centre layout** — every motion-graphic element column+row centred in the 1920×1080 frame (no edge-anchored graphics); halo ring + radial-gradient backdrops
- Techniques reused/adapted from the registry: `yt-prism-title`, `hw-title` (marker underline draw-on on "P21" and "pole."); climb scene adds an animated P21→P2 arrow + fill bar + `+19` counter; lights scene counts 0→71 laps with five sequential start lights
- Visual language: **team-colour driver chips** — glossy circles in the F1 broadcast palette (McLaren #FF8000, Red Bull #3671C6, Mercedes #27F4D2) carrying the 3-letter code (NOR/VER/HAD), dimmed chip at the start and bright chip at the payoff; podium row (P2 VER · P1 NOR elevated · P3 HAD) on the end card
- Verification: `lint` 0 errors (5 warnings `nested_media_start_basis_ambiguous` — intentional, timing is composition-local); frames extracted at act boundaries; EBU R128 integrated -16.4 LUFS
- Note: all act elements must carry an entrance tween — a scene's slot holds its final frame and would otherwise pop in static elements raw
- v4 revision (same day): VO rewritten fluent/direct (no comma-heavy phrasing, e.g. "Interlagos, under a dark sky. Norris has pole."); team chips added to Act I (duel row), Act III (dim→bright flanking P21→P2), Act IV (podium row); TRAP type scaled up
- v5 revision (same day): driver chips restyled **racing-tire style** — rubber body with tread blocks, team-colour sidewall stripe, glossy team-colour rim (McLaren #FF8000 / Red Bull #3671C6) with inner barrel ring, centre specular, 3-letter code in Anton italic; P1 tire carries yellow drop-shadow (winner halo)

v2 remains intact at commit `711564d`.

## v6 — f1-brazil-2026-2min (2026-11-09)

~2-minute extension of the São Paulo 2026 recap through the same pipeline (sub-compositions, strict dead-centre, racing-tire chips, voice-01 @1.15).

- Project: `f1-brazil-2026-2min/`
- Render: `f1-brazil-2026-2min/renders/f1-brazil-2026-2min.mp4` (2:00.0, 1920x1080@30, H.264/AAC, -16.8 LUFS, -1.0 dBFS true peak)
- Captions: `f1-brazil-2026-2min/renders/f1-brazil-2026-2min.srt` — YouTube sidecar (no burned-in captions; dead-centre rule untouched); cue starts = host act start + local voice start, duration = raw/1.15
- Structure: eight acts, sum 120.0s — 01 storm 0–10.5 · 02 grid 10.5–28.0 · 03 start 28.0–43.0 · 04 climb 43.0–69.0 · 05 flag 69.0–84.0 · 06 result 84.0–99.0 · 07 title 99.0–113.0 · 08 end 113.0–120.0
- Photos reused from v2 (interlagos-rain.jpg hero, interlagos-podium.jpg); no new stock assets
- New vs v5: act-count for full-length arc, `06 result` full-classification cascade (six rows, tire chips generated programmatically), `07 title` crowned-champion card (ANT chip, confetti-podium photo), **synthesized SFX** via numpy (`thunder.wav`, `lights.wav` = 5 blips + release boom, `crowd.wav` 12s swell, `boom.wav`) — no licensed samples; VO-synced act staging (grid cells land with the spoken names)
- Verification: `lint` 0 errors (12 warnings — composition-local media starts, accepted); frames extracted per act (storm/grid/start/climb×2/flag/result/title/end); EBU R128 -16.8 LUFS; grid staging timings corrected to track the narration before final render
