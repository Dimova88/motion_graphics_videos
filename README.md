# motion_graphics_videos

Motion-graphics videos built with [HyperFrames](https://github.com/heygen-com/hyperframes) (HTML + CSS + GSAP compositions rendered headlessly to MP4).

## Videos

| Project | Length | Description |
| --- | --- | --- |
| [`f1-brazil-2026/`](f1-brazil-2026/) | 30s | **v1 — narrated recap** of the **2026 Formula 1 São Paulo Grand Prix** (Interlagos, 08.11.2026): Norris converts pole to victory, Verstappen charges from P21 to P2, Hadjar secures a Red Bull double podium. |
| [`f1-brazil-2026-story/`](f1-brazil-2026-story/) | 30s | **v2 — story-driven recap** of the same race: five-act narrative arc (Prologue → Epilogue), storyteller voiceover (voice-01), prism title treatment, marker-underline emphasis, seamless scrolling wire ticker, film grain + cinematic grade. |
| [`f1-brazil-2026-pipeline/`](f1-brazil-2026-pipeline/) | 30s | **v3 — pipeline test** for the new 8–10 min YouTube workflow: sub-composition architecture (`compositions/`, one file per act), **strictly dead-centre layout** (every motion-graphic element column+row centred in 1920×1080), local narration + registry-derived prism/marker techniques. See [PIPELINE.md](PIPELINE.md). |
| [`f1-brazil-2026-2min/`](f1-brazil-2026-2min/) | 2min | **v6 — long-form cut** of the same race through the [pipeline](PIPELINE.md): eight dead-centred acts (storm → grid → lights out → the charge → the flag → final classification → champion title card), storyteller VO (voice-01 @1.15), racing-tire driver chips, synthesized thunder/lights/crowd SFX (numpy, no licensed samples), YouTube `.srt` sidecar. |

Rendered videos are committed: [`f1-brazil-2026/renders/f1-brazil-2026-race-recap.mp4`](f1-brazil-2026/renders/f1-brazil-2026-race-recap.mp4) (12 MB), [`f1-brazil-2026-story/renders/f1-brazil-2026-race-recap-story.mp4`](f1-brazil-2026-story/renders/f1-brazil-2026-race-recap-story.mp4) (13 MB) and [`f1-brazil-2026-pipeline/renders/f1-brazil-2026-pipeline-test.mp4`](f1-brazil-2026-pipeline/renders/f1-brazil-2026-pipeline-test.mp4) (3.2 MB), [`f1-brazil-2026-2min/renders/f1-brazil-2026-2min.mp4`](f1-brazil-2026-2min/renders/f1-brazil-2026-2min.mp4) (14 MB, captions: [`f1-brazil-2026-2min.srt`](f1-brazil-2026-2min/renders/f1-brazil-2026-2min.srt)). All 1920×1080@30 H.264/AAC. See [CHECKPOINTS.md](CHECKPOINTS.md) for restore points.

### Rebuilding a video

Each project folder is a self-contained HyperFrames composition. You need Node.js 22+, FFmpeg on `PATH`, and a Chrome/Chromium executable (set `HYPERFRAMES_BROWSER_PATH` if Chrome is not auto-detected):

```bash
cd f1-brazil-2026
npx hyperframes lint      # validate the composition
npx hyperframes render     # writes renders/<name>.mp4
```

Fonts (Anton, Archivo, Archivo Black) and SFX-free voiceover clips are vendored under `assets/`, so builds are deterministic and offline.

## Long-form workflow

For 8–10 minute motion-graphics videos (dead-centre 1920×1080 layout, sub-composition architecture, free/unlimited local stack), see [PIPELINE.md](PIPELINE.md) — researched and verified end-to-end in [`f1-brazil-2026-pipeline/`](f1-brazil-2026-pipeline/) (v3, 30s). The free/unlimited tooling research behind it lives in [YOUTUBE-HYPERFRAMES-PLAYBOOK.md](YOUTUBE-HYPERFRAMES-PLAYBOOK.md).
