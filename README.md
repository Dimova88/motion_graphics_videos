# motion_graphics_videos

Motion-graphics videos built with [HyperFrames](https://github.com/heygen-com/hyperframes) (HTML + CSS + GSAP compositions rendered headlessly to MP4).

## Videos

| Project | Length | Description |
| --- | --- | --- |
| [`f1-brazil-2026/`](f1-brazil-2026/) | 30s | Race recap of the **2026 Formula 1 São Paulo Grand Prix** (Interlagos, 08.11.2026): Norris converts pole to victory, Verstappen charges from P21 to P2, Hadjar secures a Red Bull double podium. Narrated motion-graphics recap. |

### Rebuilding a video

Each project folder is a self-contained HyperFrames composition. You need Node.js 22+, FFmpeg on `PATH`, and a Chrome/Chromium executable (set `HYPERFRAMES_BROWSER_PATH` if Chrome is not auto-detected):

```bash
cd f1-brazil-2026
npx hyperframes lint      # validate the composition
npx hyperframes render     # writes renders/<name>.mp4
```

Fonts (Anton, Archivo, Archivo Black) and SFX-free voiceover clips are vendored under `assets/`, so builds are deterministic and offline.
