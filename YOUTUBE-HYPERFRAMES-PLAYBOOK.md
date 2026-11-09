# Making YouTube videos with HyperFrames — the real-world process

Researched November 2026 from the official docs, the `heygen-com/hyperframes` repo (skills, registry), and real community repos (`coleam00/hyperframes-ai-video-generation`, ~158★; `sanky369/yt-hyperframes-agent`). Goal: a pipeline that is **completely free and unlimited** — no HeyGen account, no credits, no metered services.

## TL;DR

HyperFrames itself is Apache-2.0 and everything *official* runs free and unmetered **on your own machine**: the CLI, browser preview, `lint`/`check`/`doctor`, **unlimited local renders**, the agent skills, **Kokoro** local text-to-speech, **local** Whisper/Parakeet transcription, the bundled sound-effect set, **Openverse** assets, and whatever media/fonts you add yourself. You only spend (or hit limits) when you opt into HeyGen's hosted services or a paid agent — both are avoidable.

| Bucket | What you get free & unlimited | What is metered / paid (avoid) |
| --- | --- | --- |
| Framework & CLI | Everything (Apache 2.0) | — |
| Rendering | Local, any resolution/fps/quality, as many times as you like | `hyperframes cloud render` (HeyGen credits), Studio app cloud exports beyond the Free plan's 5/month |
| Studio app (desktop) | Free HeyGen account: AI voiceovers, captions, music, SFX, 3 AI clips + 5 cloud exports/mo | Studio Pro **$25/mo** (unlimited cloud exports, top models) |
| Agent | OpenCode free models (built into Studio, no sign-in), local models via Ollama, or free tiers of hosted models — open-weight models scored within ~50 Elo of top in HeyGen's Code2Video benchmark | Claude/Codex/Cursor plans (that's the agent's billing, not HyperFrames') |
| Voice | **Kokoro-82M on-device** via `npx hyperframes tts` (12 voices, 9 languages) — no API key | HeyGen Voice Turbo/voices/cloning (free allowance: 3 min/month Voice Turbo on the Free plan when signed in), ElevenLabs |
| Music | Your own tracks, **MusicGen** local generation (`pip install transformers torch soundfile numpy`), or any CC0/royalty-free track you supply (loop it with `<audio loop>`) | HeyGen 10,000-track catalog (credits); Studio catalog beyond the free allowance |
| Sound effects | Bundled SFX pack + Openverse search | — |
| Transcription/captions | `npx hyperframes transcribe` — auto engine: **Parakeet** (`npx hyperframes models install parakeet`, ~600 MB model) if installed, else local **Whisper** (`small.en` default, `--model tiny.en…large-v3`); `.srt`/`.vtt` import | HeyGen speech model (`--engine heygen`, bills credits); Studio app transcription |
| Avatars / AI video clips | — (avoid if you need unlimited) | HeyGen avatars, AI clips (credits) |

## What people actually do — step by step

1. **Start from the idea, and reduce it to one thing.** “One video, one idea, one viewer doing one real task.” People with a source (a URL, PDF, CSV, transcript, PR) hand *that* to the agent — it yields richer videos than invented copy.
2. **One-time setup.** Node 22+, FFmpeg, a Chrome/Chromium. Then either the desktop Studio app (freest path to start), or any coding agent + `npx skills add heygen-com/hyperframes` (pick **Core Skills**; Claude Code users: `claude plugin marketplace add heygen-com/hyperframes && claude plugin install hyperframes@hyperframes`). Verify with `npx hyperframes doctor`.
3. **Prompt with the skill.** `/hyperframes, make a 45-second 1920×1080 video about …` For a story-driven film (>15 s) the agent first offers **three storylines** (different worlds/devices/forms); you pick one. It then writes `SPEC.md` — the idea, the beats with timings, the exact quoted copy, and the look/sound taken from the subject.
4. **Agent scaffolds the project** — `index.html` (root composition), `compositions/` per scene, `assets/`. Everything visible is HTML/CSS with a paused, seekable GSAP timeline; audio and images are timed with `data-start`/`data-duration`.
5. **Audio in.** Free path: write/quote the script → **Kokoro TTS** (or your own mic) → place clips per scene with `data-start`, mixed under the music; voiceover dips the bed via a voiceover-carve; transcribe locally for captions; add bundled or Openverse SFX. Voice engine order in the media pipeline: **HeyGen Starfish (if signed in) → ElevenLabs (if a key is set) → local Kokoro (no key needed)**. Because the skill otherwise asks for a free HeyGen sign-in, say explicitly *"no HeyGen, local tools only"* to guarantee the fully-free path.
6. **(Optional) storyboard first.** The agent poses each shot as stills, you approve frames as a board (`boards/storyboard.html`), then it animates the approved stills. For fast turns, people approve the preview instead.
7. **Iterate on the live preview** (`npx hyperframes preview`) — change copy, timing, layout in chat or by pointing at elements in the browser editor.
8. **Gate before render:** `npx hyperframes doctor`, `npx hyperframes lint` (fix every error, weigh warnings), `npx hyperframes check --json`, and `npx hyperframes snapshot --review` for a frame-level review; community setups tell the agent to fix lint until clean.
9. **Render locally** — `npx hyperframes render` (or `--quality draft` for quick reviews). Deterministic, free, unlimited. Community kits usually make this an explicit manual step so you control when renders happen.
10. **Publish** — upload the MP4 to YouTube; Studio/editor stats/thumbnails are outside HyperFrames.

## The story discipline people follow (from the skills, and why most AI videos look generated)

- **One thing** the viewer must remember; every claim on screen traces to the source; real numbers only.
- **Three storylines → SPEC.md**: hook (~8%) → tension (~12%) → reveal (~8%) → proof (~40%) → payoff (~20%, the biggest visual moment) → claim (~8%) → end card (~8%, hold 2–3 s).
- **Show, don't list** — no bullet slides; giant type/moments over cards; keep one world, one carrier, a constant palette.
- **Kills the “generated film” look**: the first 2 seconds carry the hook; no "Introducing…" opener; no three-cards-in-a-row, no dark void with small things floating, no everything-fades-in; titles don't keep moving after they land; the mark lands once, on the end card.
- **Titles ≤ 6 words/line**, ~0.3 s per word + 0.5 s, last line held ≥ 2 s; say exactly what you *don't* want ("no narration", "no audio", "no image files").

See `skills/hyperframes/references/story.md` in the repo for the full method.

## What the community repos do (and you can copy)

- **`coleam00/hyperframes-ai-video-generation`** — "topic prompt → polished vertical YouTube Short": researches the topic, drafts narration, **Kokoro (free) or ElevenLabs** TTS, edits `index.html`, runs `lint` + `inspect`, opens a preview; render is a manual step. Brands are cloned and re-skinned templates; one command per brand (`archon workflow run create-classic-short`).
- **`sanky369/yt-hyperframes-agent`** — turns a long recording into a tight YouTube edit: probe duration → detect silences → transcribe (Whisper) → AI (or offline `--ai none --transcribe none`) builds an edit decision list → prune keep-segments → chapter cards + captions → render. People review the plan, then render `--quality high`.
- **Registry blocks** people remix instead of designing from scratch: `yt-logo-intro`, `yt-lower-third`, `yt-prism-title` (chromatic offset titles), `news-ticker` (scrolling wire), `mk-progress-stat`, `hw-title` (marker underline), `logo-outro`. `npx hyperframes add <slug>` — free, Apache-2.0; if the CDN hosts are blocked, fetch the block HTML via `api.github.com` (as we did for the three used in `f1-brazil-2026-story/`).

## The minimal free & unlimited recipe

```bash
# 1) prereqs: node 22+, ffmpeg on PATH, Chrome/Chromium
npx hyperframes init my-video --skip-skills
cd my-video
npx skills add heygen-com/hyperframes        # choose Core Skills (free)
# 2) agent prompt (example)
/hyperframes make a 60-second 1920x1080 explainer about <topic, with source/URL>;
story-driven, quoted copy, Kokoro voiceover, no HeyGen services.
# 3) iterate, then ship — as many renders as you like, locally
npx hyperframes preview            # review + hand edits
npx hyperframes doctor && npx hyperframes lint
npx hyperframes render -o final.mp4
```

Voice without HeyGen: `npx hyperframes tts "line" --voice am_adam -o voice.wav` — Kokoro-82M on device, 12 voices, 9 languages. First run auto-downloads the model (kokoro-v1.0.onnx, ~310 MB) and voices file from GitHub releases; it needs the `kokoro-onnx` and `soundfile` pip packages visible to the Python it finds, or `HYPERFRAMES_PYTHON=/path/to/venv/bin/python` pointing at a venv that has them. Music without HeyGen: your own files, or local MusicGen (weights download from Hugging Face on first run); or loop one short track with the native `loop` attribute on `<audio>` (see the voice-and-audio guide). Captions: `npx hyperframes transcribe video.mp4` (auto: Parakeet if installed — `npx hyperframes models install parakeet` — else local Whisper) or import `.srt`/`.vtt`.

## Honest limits and traps

- "Free and unlimited" applies to **this toolchain on your compute**. The Studio app's Free plan caps cloud exports (5/month) and AI clips (3); unlimited cloud exports are the $25/mo Pro plan. Don't rely on them if unlimited matters.
- **A paid agent is the invisible cost** — Claude/Codex/Cursor subscriptions bill your usage. OpenCode's free models (or local Ollama models) are the fully-free route, at the price of speed/quality on hard compositions.
- **Watch out for invented APIs.** One popular blog describes `api.hyperframes.ai` and `HYPERFRAMES_API_KEY` — there is no such REST service in the official docs; HyperFrames is a local/open-source renderer. Don't build a pipeline on it. The real integration points are the CLI, the skills, and the Studio app.
- **Model downloads need network access to their hosts.** Kokoro's files come from GitHub release assets; Parakeet (~600 MB), Whisper weights and MusicGen weights come from Hugging Face. On a machine that can't reach those (locked-down CI, sandboxes with an allowlist), the free path breaks at first use even though everything else works — prefetch the files or use a different mirror, or bring your own audio (our repo narration was generated with the assistant's voice tool and placed as plain `<audio>` elements — free too). Your HeyGen-free setup means local renders; don't let `cloud render` back in by default.
- **The Studio app defaults toward HeyGen.** Signed-in, it routes media (voice/music/clips) to HeyGen and bills credits; without a HeyGen API key it uses local Kokoro voices. With your own agent, the media skill asks you to sign in first — answer *"no sign-in, local tools only"* or explicitly request local everywhere to stay at zero cost.
- Network-dependent extras (Google Fonts links, CDN GSAP) are avoided by vendoring fonts/GSAP into `assets/` — keeps renders deterministic and offline (as done in this repo).
- Lint can't judge taste. Run `snapshot --review`, watch with sound off and on, and check title/caption safe areas before uploading; captions get a human pass for names and numbers.

## Applied in this repo

- `f1-brazil-2026/` — v1 fact-based recap (voice-00).
- `f1-brazil-2026-story/` — v2 story-driven recap (voice-01): the three-storyline method, five-act structure, registry-derived techniques (prism titles, marker underline, scrolling ticker), narration generated locally (assistant voice tool) and placed as `<audio>` — not a HeyGen service. Restore points in [CHECKPOINTS.md](CHECKPOINTS.md).
