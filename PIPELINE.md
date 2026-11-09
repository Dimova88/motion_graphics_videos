# Pipeline — making 8–10 minute motion-graphics YouTube videos, free and unlimited

This is the standing workflow for long-form videos in this repo, built on the research in [YOUTUBE-HYPERFRAMES-PLAYBOOK.md](YOUTUBE-HYPERFRAMES-PLAYBOOK.md) and proven end-to-end in the 30s smoke test [`f1-brazil-2026-pipeline/`](f1-brazil-2026-pipeline/). Free and unlimited means: everything renders **locally** with the open-source HyperFrames CLI (Apache-2.0) and tools you already have — no HeyGen account, no credits, no metered services, as many renders as you like.

## Deliverable targets

| Property | Target |
| --- | --- |
| Length | 8–10 minutes (480–600 s). A length is a range, never padded to hit it |
| Canvas | 1920×1080 @ 30 fps |
| Loudness | −16 LUFS integrated (EBU R128), AAC |
| Container | H.264/AAC MP4 via `npx hyperframes render --quality delivery` |
| Structure | One clear idea; 6–9 acts of 45–75 s each; end card holds 2–3 s |
| Captions | Sidecar `.srt`/`.vtt` uploaded to YouTube (best for long form), or burned via caption blocks (Shorts) |
| Description | YouTube chapters (`0:00 Intro`, `1:05 Act I — …`) mirroring the acts |

## The dead-centre layout rule (1920×1080)

Every motion-graphic element is centred in **both column and row** — on the exact centre of the screen. No edge-anchored graphics, no left-aligned lower thirds, no bottom-right bugs. Concretely:

```css
#root {
  position: absolute; inset: 0; overflow: hidden;
  display: flex; align-items: center; justify-content: center;
  text-align: center;
}
.stack { display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 26px; }
```

- Backgrounds are full-bleed (`inset: 0` radial gradients / halo rings) — those centre themselves.
- Progress bars, checker strips, tickers: only full frame-width or a centred block (e.g. 640 px bar on the centre line); a ticker must span the full width and be vertically centred, or be dropped.
- Captions are centred too, not in a lower band.
- Decorative icons: inline SVG, `currentColor`/stroke — never icon fonts; no unicode arrows or glyphs that may render as tofu.
- Keep ids prefixed per scene (`#climb-*`), keep `pointer-events: none` on overlays, `overflow: hidden` on `#root`.

## Composition architecture (built for long form)

```
index.html                  # root: data-width/height/duration, fonts, mounts scenes
compositions/
  01-prologue.html          # each scene = one file in a <template>
  02-act-one.html
  ...
assets/{fonts,vendor,voice,sfx,images}/
```

Rules learned the hard way (see `skills/hyperframes/references/format.md`):

- Host div: `<div id="climb" data-composition-id="climb" data-composition-src="compositions/climb.html" data-start="16.5" data-duration="7.5" data-track-index="4" data-width="1920" data-height="1080">`. Scene root `<div id="root" data-composition-id="climb" data-width="1920" data-height="1080">`, timeline key `window.__timelines["climb"]`. Host, composition id and timeline key match.
- `data-start`/`data-duration` on media are **local to the composition** declaring them; in the file that media is composition-local. Lint `nested_media_start_basis_ambiguous` on nonzero local starts is informational — keep them local.
- `fromTo`, never `from`, inside scenes (the host re-seeks; `from` drifts on seek-back).
- **Every element in a scene must carry an entrance tween.** A scene's slot holds its final frame once the scene's timeline is done, and shows the frame before the host slot starts with anything un-timed (a static bottom row "pops"). Give even seemingly-static elements a `fromTo`.
- No CSS transitions/animations for visual state (`css_transition_used`); drive everything from the paused GSAP timeline so renders are seek-deterministic.
- `@font-face` needs to be declared in the file that uses the family — put it in every scene (and in `index.html`, which styles the assembled page). Vendored woff2, never Google Fonts links.
- Styles stay inline in the scene file (`<style>` inside `<template>`); style the scene root as `#root`, not by class; don't link a sheet that styles a scene's root by id.

## Free, unlimited workflow for one 8–10 min video

1. **Reduce the idea to one thing.** One sentence the viewer remembers; every claim traced to a source (numbers, names, times — real, from the article/PR/stats).
2. **Pre-production artefact** — `SPEC.md` before any building: the one thing, the hook (first 2 s), act beats with timestamps, quoted on-screen copy, look (ground, type, one material), sound (mood + level, e.g. "calm piano under it, −18 dB"). For story films the agent offers three storylines; pick one.
3. **Scaffold** — `npx hyperframes init <name> --skip-skills && cd <name> && npx skills add heygen-com/hyperframes` (Core Skills). Copy `assets/fonts` + `assets/vendor/gsap.min.js` from an existing project (this repo) — offline, deterministic.
4. **Write the script** as beats (hook ≤2 s → tension → reveal → proof per act → payoff ≥60 % in → claim → end card 2–3 s). Titles ≤ 6 words/line.
5. **Voice, free two ways** (write it fluent and direct: short declaratives, minimal comma-chains, one idea per breath — read it aloud before recording; ~1.15× rate keeps energy without rushing):
   - This machine/session: the assistant's built-in voice generation (voice-01 is the house narrator), clip per line, placed with `data-start` + `data-playback-rate="1.15"`. Free, no account.
   - Any normal workstation: **Kokoro-82M on-device** — `npx hyperframes tts "line" --voice am_adam -o assets/voice/01.wav` (needs `kokoro-onnx` + `soundfile` and, on first run, network access to GitHub release assets; point `HYPERFRAMES_PYTHON` at a venv that has the packages). Never HeyGen sign-in unless the user wants the Free plan's 3 min/month Voice Turbo.
6. **Assemble** — one composition per act; mount in `index.html`; dead-centre layout; prism/marker/count-up/progress techniques from the Playbook (registry-derived, vendored). For driver/team content prefer **team-colour driver chips** (F1 broadcast palette: McLaren #FF8000, Red Bull #3671C6, Mercedes #27F4D2, glossy radial-gradient discs with the 3-letter code — dim the chip at the story's start, brighten at the payoff, e.g. podium row on the end card) over text-only driver references.
7. **Gates** — `npx hyperframes lint` (0 errors; reassess warnings each video) → `npx hyperframes snapshot --at <act key moments>` → view the contact sheet → fix → re-snapshot.
8. **Render** — `npx hyperframes render -o renders/<name>.mp4 --quality delivery`. Expect roughly 1–2.5 min per 30 s of 1080p30 on one core — budget 25–50 min for a full video; iterate on `--quality draft` first.
9. **Verify** — ffprobe (codec/fps/resolution/duration), `ebur128` LUFS, frame extraction at every act cut (`-ss` before `-i`, compare md5s of successive seconds to catch boundary bugs), spot-listen with sound off/on/muted.
10. **Checkpoint** — entry in [CHECKPOINTS.md](CHECKPOINTS.md), commit + push, render committed (renders are deliberately tracked).
11. **Publish** — upload MP4; YouTube description with chapters mirroring acts; thumbnail = one bold centred frame (e.g. Act III); mention `Made with HyperFrames` only if you want to.

## Costs and how to stay at zero

| Item | Free route | Metered (avoid unless asked) |
| --- | --- | --- |
| HyperFrames CLI + local render | ✓ any resolution/count | `hyperframes cloud render` |
| Agent | OpenCode free models, Ollama local | Claude/Codex/Cursor plans |
| Voice | voice-01 assistant tool / local Kokoro | HeyGen voices, ElevenLabs |
| Music | own CC0/royalty-free files; local MusicGen | HeyGen 10k catalog |
| SFX | bundled pack + Openverse | — |
| Captions | `hyperframes transcribe` (Parakeet/Whisper local) | `--engine heygen` |
| Studio app | free account (but caps exports; sign-in routes media to HeyGen) | Pro $25/mo |

Caveat: model downloads (Kokoro, Parakeet, Whisper, MusicGen weights) come from GitHub releases / Hugging Face — blocked on allow-listed sandboxes like this one, where the assistant's voice tool is the working free path instead.

## Act structure template for 8–10 min

| # | ~Length | Beat | Job |
| --- | --- | --- | --- |
| 0 | 5–15 s | Hook | world + need, or result-first; ≤2 s to first motion |
| 1 | 45–75 s | Act I — setup | one real number/scene that poses the question |
| 2 | 45–75 s | Act II | development, claims traceable to sources |
| 3 | 60–90 s | Act III | payoff ≥ 60 % in; biggest visual moment |
| 4 | 45–75 s | Act IV | consequences, human stakes |
| 5 | 15–30 s | End card | mark + line + CTA, hold 2–3 s |

(For F1-style recaps: Prologue storm/grid → start → climb → flag → aftermath, as in `f1-brazil-2026-story/`.)

## Verification checklist before commit

- [ ] `lint` → 0 errors; warnings explicitly acknowledged
- [ ] contact sheet inspected (every act reads centred, type fits, no overlap/tofu)
- [ ] boundary frames at every cut show intentional content (no raw empty pop-ins)
- [ ] ffprobe: h264, 1920×1080, 30 fps, expected duration; ebur128: −16 ± 1 LUFS
- [ ] README + CHECKPOINTS updated; render committed
