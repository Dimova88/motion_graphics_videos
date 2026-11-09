# motion_graphics_videos

Motion-graphics videos for an **economics-education YouTube channel**, built with [HyperFrames](https://github.com/heygen-com/hyperframes) (HTML + CSS + GSAP compositions rendered headlessly to MP4). Every video pairs verified real-world data with the strict dead-centre layout and sub-composition architecture in [PIPELINE.md](PIPELINE.md).

## Status

Channel pivot (2026-11-09): the previous F1 content was removed at the channel owner's direction; the repo is being rebuilt around economics explainers with current, sourced examples. See [CHECKPOINTS.md](CHECKPOINTS.md).

- Brand options and niche analysis: [`econ-channel/BRAND.md`](econ-channel/BRAND.md)
- Episode 01 RENDERED: [`econ-channel/ep01/renders/el-precio-de-todo-ep01.mp4`](econ-channel/ep01/renders/el-precio-de-todo-ep01.mp4) (7:55, 1920×1080@30, H.264/AAC, −16.9 LUFS) + [`.srt`](econ-channel/ep01/renders/el-precio-de-todo-ep01.srt) — «¿Por qué todo está más caro?»

## Workflow

Each episode is a self-contained HyperFrames composition. You need Node.js 22+, FFmpeg on `PATH`, and a Chrome/Chromium executable (set `HYPERFRAMES_BROWSER_PATH` if Chrome is not auto-detected):

```bash
cd <episode>
npx hyperframes lint      # validate the composition
npx hyperframes render     # writes renders/<name>.mp4
```

Fonts and tooling are vendored locally, so builds are deterministic and offline. See [PIPELINE.md](PIPELINE.md) for the full workflow and [YOUTUBE-HYPERFRAMES-PLAYBOOK.md](YOUTUBE-HYPERFRAMES-PLAYBOOK.md) for the long-form/VO research.
