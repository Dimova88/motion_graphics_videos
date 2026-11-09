# motion_graphics_videos

Motion-graphics videos built with [HyperFrames](https://github.com/heygen-com/hyperframes) (HTML + CSS + GSAP compositions rendered headlessly to MP4).

## Videos

| Project | Length | Description |
| --- | --- | --- |
| [`f1-brazil-2026/`](f1-brazil-2026/) | 30s | **v1 — narrated recap** of the **2026 Formula 1 São Paulo Grand Prix** (Interlagos, 08.11.2026): Norris converts pole to victory, Verstappen charges from P21 to P2, Hadjar secures a Red Bull double podium. |
| [`f1-brazil-2026-story/`](f1-brazil-2026-story/) | 30s | **v2 — story-driven recap** of the same race: five-act narrative arc (Prologue → Epilogue), storyteller voiceover (voice-01), prism title treatment, marker-underline emphasis, seamless scrolling wire ticker, film grain + cinematic grade. |

Rendered videos are committed: [`f1-brazil-2026/renders/f1-brazil-2026-race-recap.mp4`](f1-brazil-2026/renders/f1-brazil-2026-race-recap.mp4) (12 MB) and [`f1-brazil-2026-story/renders/f1-brazil-2026-race-recap-story.mp4`](f1-brazil-2026-story/renders/f1-brazil-2026-race-recap-story.mp4) (13 MB). Both 1920×1080@30 H.264/AAC. See [CHECKPOINTS.md](CHECKPOINTS.md) for restore points.

### Rebuilding a video

Each project folder is a self-contained HyperFrames composition. You need Node.js 22+, FFmpeg on `PATH`, and a Chrome/Chromium executable (set `HYPERFRAMES_BROWSER_PATH` if Chrome is not auto-detected):

```bash
cd f1-brazil-2026
npx hyperframes lint      # validate the composition
npx hyperframes render     # writes renders/<name>.mp4
```

Fonts (Anton, Archivo, Archivo Black) and SFX-free voiceover clips are vendored under `assets/`, so builds are deterministic and offline.
