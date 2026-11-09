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
