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

## v7 — f1-brazil-2026-2min rebuild (2026-11-09)

User feedback addressed: (a) not enough slides / too much dead air, (b) VO volume inconsistent, (c) factual error — Antonelli was crowned World Champion at the Mexico City GP (Nov 1), not Interlagos, (d) weird synthesized "crowd"/"boom" noises from 1:09 to the end, (e) VO should be fluent, constant, easy to follow; slides as support; overall more dynamic.

- Facts re-verified (web, Nov 2026 sources): Antonelli crowned 2026 drivers' champion at Mexico City (P3, youngest ever — 20y, first Italian since Ascari 1953, 380 pts, +119; round 19 of 23). Brazil (round 20, Nov 6–8, MSC Cruises Grande Prêmio, Autódromo José Carlos Pace, 71 laps / 305.879 km): Norris pole→win 1:35:23.504 (+14.602), Verstappen P21 (cumulative 30-place power-unit penalty)→P2 (driver of the day), Hadjar P3 (RB double podium, +24.485), Russell P4 (+33.991, team-order swap in the wet), Antonelli P5 (+41.017, +5s unsafe release re: Colapinto; fastest lap 1:12.689 L55), Piastri P6 (+56.475). Antonelli led into Turn 1, spun at the Senna S on lap 20, Norris took the lead and never relinquished it. Mercedes sealed the 2026 constructors' championship at Interlagos (RUS 12 + ANT 10 = 22 pts, three rounds remaining).
- Structure: ten acts, sum 120.0s — 01 storm 0–9.5 · 02 crown 9.5–21.0 (NEW — the Mexico City backstory / constructors' stakes) · 03 grid 21.0–33.5 · 04 start 33.5–44.0 · 05 senna 44.0–54.5 (NEW — lap 20, the spin, Norris through) · 06 climb 54.5–75.0 · 07 flag 75.0–86.0 · 08 result 86.0–99.5 (now narrated; fastest-lap footnote; MERCEDES constructors' banner) · 09 double 99.5–113.0 ("DOUBLE CHAMPIONS" — drivers' + constructors' cards) · 10 end 113.0–120.0 ("Round 20 of 23 — three races to go").
- VO: rewritten fluent, story-led, ~200 spoken words across 10 takes covering ~95% of the runtime; ALL takes loudness-normalised (two-pass linear loudnorm, I=-19.5 LUFS / TP=-1.5) measured spread ≤0.8 LUFS — previously ±1+ LUFS; rate 1.15 voice-01.
- Audio hygiene: crowd.wav and boom.wav DELETED — the 1:09→end "weird noises" are gone; remaining SFX: thunder.wav (storm) + lights.wav (start), both pre-1:09 and unproblematic.
- Dynamism: every act now carries continuous motion (Ken Burns photos, spinning glow ring, S-curve SVG with traveling ANT/NOR dots + spark burst at the spin, sliding VO-synced act beats, kicker shimmer, constructors' banner pop, crowned double-champions card); no act is a static hold. Act count 8 → 10; grid/senna/result beats re-timed to land on the spoken words.
- SRT sidecar regenerated to the new script/timeline (cue = host slot + local start; duration = raw/1.15).
- Verification: lint 0 errors; frames extracted per act; EBU R128 −16.8 LUFS; −1.0 dBFS true peak; 120.000s.

## v8 — Channel pivot: F1 removed; economics-education rebrand (2026-11-09)

All F1 projects (`f1-brazil-2026`, `f1-brazil-2026-story`, `f1-brazil-2026-pipeline`, `f1-brazil-2026-2min`, including renders and sources) were deleted from the working tree at the channel owner's direction; restore only via git history (tags gone, commits remain). PIPELINE.md and YOUTUBE-HYPERFRAMES-PLAYBOOK.md were scrubbed of F1-specific references; the generic 8–10 min HyperFrames workflow stands. README rebuilt around the economics-education channel.
New deliverables: `econ-channel/BRAND.md` (niche analysis + 3 brand options) and `econ-channel/EP01-STORYBOARD.md` (8:00 episode storyboard, no motion graphics yet — pending owner review).

### v8 update — decisions locked (2026-11-09)
Channel owner decisions: **Español-first · Opción B “El Precio de Todo” (deep green/cream/chalk yellow; chalkboard ledger look) · faceless (VO + motion graphics) · EP01 «¿Por qué todo está más caro?» aprobado como piloto.** BRAND.md and EP01-STORYBOARD.md rewritten to v2 (Spanish, Option B palette, Spanish VO sample lines). No motion graphics produced yet — pending design adjustments from owner review of EP01-STORYBOARD.md. Open items with owner: handle availability, final tagline, ES voice audition choice.

### v8 update 2 — brand v1 built (2026-11-09)
Handle probe (YouTube, fetch tool): `@elpreciodetodo` TAKEN (pre-existing tiny channel, 6 subs, joined Oct-2025); `@elprecio.detodo`, `@elprecio_detodo`, `@elpreciodetodo_ec` all 404 (available at check time; IG/TikTok/X not verifiable from sandbox). Brand assets generated vector-first: `econ-channel/brand/` (logo-mark/lockup SVG masters + resvg PNG renders: avatar-800, banner-2560x1440, thumbnail-mock, Anton/Archivo TTFs recovered from git history and renamed to clean family names, SIL OFL). Spec + sign-off checklist: `econ-channel/BRAND-FINAL.md`. Pending owner: handle pick, tagline confirm, brand sign-off, then EP01 build.

### v8 update 3 — marca cerrada + build EP01 autorizado (2026-11-09)
Owner sign-off: **handle `@elprecio_detodo`** (disponible verificado en YouTube 2026-11-09) · **tagline «Todo tiene un precio — y una historia.»** · OK para construir **EP01**. Flujo: audition voz ES (2 candidatas, owner elige) → script VO ES → composiciones HyperFrames → render + SRT.

## v9 — EP01 «¿Por qué todo está más caro?» RENDER (2026-11-09)

Full production of the pilot episode for **El Precio de Todo / @elprecio_detodo** (ES · Opción B chalkboard ledger · faceless, VO voice-02 educativa).

- Project: `econ-channel/ep01/` — 10 sub-compositions (`compositions/01-frio` … `10-outro`), dead-centre stage, Option B palette (#10312B pizarra, #EDE6D3 tiza, #FFD84D números, #FF6B57 alertas), Anton/Archivo vendored woff2, gsap from v7 vendor pack, synth SFX (stamp/tap/flip via numpy)
- VO: 10 tomas ES voice-02 (natural rate 1.0), two-pass loudnorm to −19.5 LUFS (spread ≤0.4 LU); frases cortas, guion en `VO-SCRIPT.md`
- Facts verified and baked in (chip on every number): **EA 4,0% flash oct-2026** (Eurostat, 4-nov) · **US 3,7% sep-2026 / core 2,6%** (BLS, 14-oct, gasolina +34,2%) · **NL 3,7% oct-2026** snelle raming (CBS, 4-nov; gas +52,5%, HICP 3,3%) · **renta real hogares EA +0,1% t/t 2T-2026** · **Fed +3,75–4,00% primera subida desde 2023 (sep-2026)** · **Hormuz: guerra desde el 28-feb-2026, tráfico 20→2,7M b/d, $78→$131 en 8 días, ~20% LNG** (EIA/IEA) · expectativas EE. UU. 3,6→3,9% (sep-2026). Series: CPIAUCSL vía FRED (gráfico 2016–2026 calculado), Eurostat prc_hicp_minr EA21 (consulta API verificada, sep → dic-2025 = 2,0%)
- Render: `renders/el-precio-de-todo-ep01.mp4` — **7:55.4, 14261 frames, −16.9 LUFS, −1.0 dBFS TP, H.264/AAC 1920×1080@30, 30.8 MB** (hyperframes 0.9.26 delivery; NVIDIA-free SwiftShader; ffmpeg at /tmp/ff + chmod'ed /usr/local/bin/ffmpeg/ffprobe)
- SRT sidecar: `renders/el-precio-de-todo-ep01.srt` (110 cues, distribución proporcional por caracteres dentro de cada toma) · Descripción+capítulos: `EP01-DESCRIPCION.md`
- Gates: lint 0 errors (25 warnings, todos `nested_media_start_basis_ambiguous` intencionales composition-local); 12 frames + 9 boundary frames verificados; sin pop-ins crudos (corte en negro ≤0.3 s por acto, estilo hard-cut con VO continuo — valorar crossfades si el owner lo prefiere)
- Known cosmetic trade-offs: stamp del acto 1 cubre parcialmente el ticket (intencional); callouts de pico en el gráfico reposicionados; `#ou-cta` segundo fromTo con immediateRender:false
- Restored from git history (v7 assets, no F1 content): gsap.min.js; Anton/Archivo TTFs for the brand sheet (SIL OFL)
- Next: owner review of the MP4 (diseño/ritmo/VO) → ajustes → upload + descripción. Voice-02 stays the house narrator unless replaced.
