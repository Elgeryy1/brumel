<!-- GENERATED FILE — Do not edit by hand. Source: docs/product/catalog/*.json. Regenerate: python scripts/catalog/render_features.py -->

# Brumel Tools — media and everyday utilities

> **Project status: Pre-development.** Nothing listed here is available yet. Statuses, priorities and phases are proposals. See the [catalog index and legend](../FEATURES.md#legend).

39 entries. Epics in this module:

- **EP-TLS-01** Downloads — phase 3 (Public Alpha), P1
- **EP-TLS-02** Media controls and Meeting Mode — phase 4 (Public Beta), P2
- **EP-TLS-03** Capture, reading and accessibility — phase 3 (Public Alpha), P2
- **EP-TLS-04** Everyday web and file utilities — phase 3 (Public Alpha), P1
- **EP-TLS-05** Migration and coexistence — phase 3 (Public Alpha), P1

| ID | Name | Tier | Status | Priority | Phase |
| --- | --- | --- | --- | --- | --- |
| [TLS-001](#tls-001) | Smart Downloads | Secondary | Planned | P2 | 3 |
| [TLS-002](#tls-002) | Advanced download manager | Secondary | Planned | P2 | 3 |
| [TLS-003](#tls-003) | Parallel downloads | Experimental | Research | P3 | 3 |
| [TLS-004](#tls-004) | Resumable downloads | Essential | Planned | P1 | 3 |
| [TLS-005](#tls-005) | Download speed limiter | Secondary | Planned | P3 | 3 |
| [TLS-006](#tls-006) | Universal PiP | Secondary | Planned | P2 | 4 |
| [TLS-007](#tls-007) | Audio Mixer | Flagship | Planned | P2 | 4 |
| [TLS-008](#tls-008) | Equalizer | Secondary | Research | P3 | 4 |
| [TLS-009](#tls-009) | Volume boost | Secondary | Research | P3 | 4 |
| [TLS-010](#tls-010) | Media speed control | Secondary | Planned | P2 | 4 |
| [TLS-011](#tls-011) | Cinema mode | Secondary | Planned | P3 | 4 |
| [TLS-012](#tls-012) | GPU video enhancement | Experimental | Research | P3 | 4 |
| [TLS-013](#tls-013) | Live Captions | Secondary | Research | P2 | 4 |
| [TLS-014](#tls-014) | Subtitle translation | Experimental | Research | P3 | 4 |
| [TLS-015](#tls-015) | Tab recording | Secondary | Research | P2 | 4 |
| [TLS-016](#tls-016) | Full-page screenshots | Secondary | Planned | P2 | 3 |
| [TLS-017](#tls-017) | Basic PDF editor | Secondary | Research | P3 | 4 |
| [TLS-018](#tls-018) | Smart Reader | Secondary | Planned | P2 | 3 |
| [TLS-019](#tls-019) | Text-to-speech reading | Secondary | Research | P2 | 4 |
| [TLS-020](#tls-020) | Distraction Cleaner | Secondary | Planned | P2 | 3 |
| [TLS-021](#tls-021) | Website Profiles | Secondary | Planned | P2 | 3 |
| [TLS-022](#tls-022) | Accessibility Studio | Flagship | Planned | P1 | 4 |
| [TLS-023](#tls-023) | Fonts and contrast options *(→ TLS-022)* | Flagship | Planned | P1 | 4 |
| [TLS-024](#tls-024) | Reduced visual stimuli *(→ TLS-022)* | Flagship | Planned | P1 | 4 |
| [TLS-025](#tls-025) | Adapted reading options *(→ TLS-022)* | Flagship | Planned | P1 | 4 |
| [TLS-026](#tls-026) | Meeting Mode | Secondary | Planned | P2 | 4 |
| [TLS-027](#tls-027) | Migration Assistant | Flagship | Planned | P0 | 3 |
| [TLS-028](#tls-028) | Mouse and trackpad gestures | Secondary | Planned | P3 | 4 |
| [TLS-029](#tls-029) | Subscription Radar | Secondary | Research | P2 | 4 |
| [TLS-030](#tls-030) | Tables to Data | Secondary | Planned | P2 | 3 |
| [TLS-031](#tls-031) | Selection Actions | Secondary | Planned | P2 | 3 |
| [TLS-032](#tls-032) | My Search Results | Secondary | Research | P2 | 4 |
| [TLS-033](#tls-033) | Smart Upload | Flagship | Planned | P1 | 3 |
| [TLS-034](#tls-034) | Local File Workshop | Secondary | Research | P2 | 4 |
| [TLS-035](#tls-035) | Live Text | Secondary | Research | P2 | 4 |
| [TLS-036](#tls-036) | Universal Local Dictation | Secondary | Research | P2 | 4 |
| [TLS-037](#tls-037) | Chrome Coexistence | Secondary | Planned | P2 | 3 |
| [TLS-038](#tls-038) | Destinations | Experimental | Research | P3 | 4 |
| [TLS-039](#tls-039) | Quick Tab Recording *(→ TLS-015)* | Secondary | Research | P2 | 4 |

<a id="tls-001"></a>

## TLS-001 — Smart Downloads

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity M · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-TLS-01 (Downloads)

Rule-based organization of downloads into folders by type, source or name.

- **Problem:** Downloads folders become a mess.
- **Use case:** Bank statements automatically go to Documents/Finance.
- **Segments:** Everyday users, Power users
- **Dependencies:** [CORE-031](core.md#core-031), [WRK-030](workspace.md#wrk-030)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** Deterministic-first · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Vivaldi, Opera, Edge, Safari
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Uses rules engine
  - Deterministic by default
  - Undo moves
- **Origin:** G · **Duplicate of:** —
- **Limitations / notes:** Moving files after download can confuse users and other apps; rules are applied only to new downloads and never touch existing folders.

<a id="tls-002"></a>

## TLS-002 — Advanced download manager

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity M · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-TLS-01 (Downloads)

Download manager with queue, pause/resume, scheduling and source info.

- **Problem:** Chromium's download page is minimal.
- **Use case:** A user queues large downloads to run overnight.
- **Segments:** Everyday users, Power users
- **Dependencies:** [CORE-031](core.md#core-031)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Vivaldi, Opera, Download manager extensions
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Queue and schedule
  - Per-download details
- **Origin:** G · **Duplicate of:** —
- **Limitations / notes:** Scheduling requires the browser to be running; resuming after server-side expiry of download URLs is impossible.

<a id="tls-003"></a>

## TLS-003 — Parallel downloads

`Experimental` · `Research` · **P3** · Impact Low · Complexity M · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-TLS-01 (Downloads)

Multi-connection downloads for servers that support range requests.

- **Problem:** Single-connection downloads can be slow on some servers.
- **Use case:** A large ISO downloads faster using several ranges.
- **Segments:** Everyday users, Power users
- **Dependencies:** [TLS-002](#tls-002)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Vivaldi, Opera, Edge, Safari
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Only when server supports ranges
  - Respect rate limits
  - Measured benefit
- **Origin:** G · **Duplicate of:** —
- **Limitations / notes:** Chromium has an experimental parallel download flag; benefit varies and can annoy servers.

<a id="tls-004"></a>

## TLS-004 — Resumable downloads

`Essential` · `Planned` · **P1** · Impact Medium · Complexity S · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-TLS-01 (Downloads)

Reliable resume after network loss or restart where servers allow.

- **Problem:** Large downloads fail and restart from zero.
- **Use case:** A 4 GB download resumes after a laptop sleep.
- **Segments:** Everyday users, Power users
- **Dependencies:** [CORE-031](core.md#core-031)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Vivaldi, Opera, Edge, Safari
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Resume across restarts tested
- **Origin:** G · **Duplicate of:** —
- **Limitations / notes:** Resumption depends on servers supporting range requests and stable URLs; signed, expiring URLs cannot be resumed.

<a id="tls-005"></a>

## TLS-005 — Download speed limiter

`Secondary` · `Planned` · **P3** · Impact Low · Complexity S · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-TLS-01 (Downloads)

Limit browser download bandwidth.

- **Problem:** Downloads saturate shared connections.
- **Use case:** A user caps downloads during a video call.
- **Segments:** Everyday users, Power users
- **Dependencies:** [TLS-002](#tls-002)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Vivaldi, Opera, Edge, Safari
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Global and per-download limits
- **Origin:** G · **Duplicate of:** —
- **Limitations / notes:** Limits apply only to downloads Brumel controls, not to page traffic or other applications.

<a id="tls-006"></a>

## TLS-006 — Universal PiP

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-TLS-02 (Media controls and Meeting Mode)

Enhanced Picture-in-Picture for any video, with controls and multiple windows.

- **Problem:** Many sites disable PiP.
- **Use case:** A user floats a video from a site that hides the PiP button.
- **Segments:** Everyday users, Power users
- **Dependencies:** [CORE-042](core.md#core-042)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Opera (video pop-out), Vivaldi
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Works on most HTML5 video
  - Respects DRM restrictions
- **Origin:** G · **Duplicate of:** —
- **Limitations / notes:** DRM-protected video and some custom players block or break PiP; multiple PiP windows increase decoding load.

<a id="tls-007"></a>

## TLS-007 — Audio Mixer

`Flagship` · `Planned` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-TLS-02 (Media controls and Meeting Mode)

Per-tab volume control and mute in one panel.

- **Problem:** Only whole-tab mute exists.
- **Use case:** A user lowers a music tab while on a call.
- **Segments:** Everyday users, Power users
- **Dependencies:** [CORE-020](core.md#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Opera GX, Extensions
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Per-tab volume
  - Persist per site optional
- **Origin:** G · **Duplicate of:** —
- **Limitations / notes:** Per-tab volume requires routing tab audio through Brumel's audio pipeline, which may add latency or conflict with WebRTC echo cancellation.

<a id="tls-008"></a>

## TLS-008 — Equalizer

`Secondary` · `Research` · **P3** · Impact Low · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-TLS-02 (Media controls and Meeting Mode)

Per-tab or global audio equalizer.

- **Problem:** Laptop speakers and headphones need tuning.
- **Use case:** A user boosts bass on a music tab.
- **Segments:** Everyday users, Power users
- **Dependencies:** [TLS-007](#tls-007)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Vivaldi, Opera, Edge, Safari
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Presets
  - Low overhead measured
- **Origin:** G · **Duplicate of:** —
- **Limitations / notes:** Equalization adds audio processing on every sample; it is unsuitable for latency-sensitive calls and is mostly a niche feature.

<a id="tls-009"></a>

## TLS-009 — Volume boost

`Secondary` · `Research` · **P3** · Impact Low · Complexity S · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-TLS-02 (Media controls and Meeting Mode)

Amplify quiet tabs above 100% with limiter to avoid clipping.

- **Problem:** Some videos are too quiet.
- **Use case:** A user boosts a quiet lecture to 150%.
- **Segments:** Everyday users, Power users
- **Dependencies:** [TLS-007](#tls-007)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Vivaldi, Opera, Edge, Safari
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Limiter prevents clipping
  - Per-tab
- **Origin:** G · **Duplicate of:** —
- **Limitations / notes:** Amplification can damage hearing or speakers if abused and increases distortion; must be capped and clearly indicated.

<a id="tls-010"></a>

## TLS-010 — Media speed control

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity S · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-TLS-02 (Media controls and Meeting Mode)

Playback speed control for any HTML5 media, beyond site limits.

- **Problem:** Sites limit speed choices.
- **Use case:** A user watches a lecture at 1.75x.
- **Segments:** Everyday users, Power users
- **Dependencies:** [CORE-020](core.md#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Vivaldi, Opera, Edge, Safari
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Keyboard shortcuts
  - Per-site default
- **Origin:** G · **Duplicate of:** —
- **Limitations / notes:** Sites that implement their own players may override or reset playback speed; live streams cannot be sped up.

<a id="tls-011"></a>

## TLS-011 — Cinema mode

`Secondary` · `Planned` · **P3** · Impact Low · Complexity S · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-TLS-02 (Media controls and Meeting Mode)

Dim everything except the video.

- **Problem:** Page clutter distracts from video.
- **Use case:** A user dims a page while watching a film.
- **Segments:** Everyday users, Power users
- **Dependencies:** [CORE-020](core.md#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Vivaldi, Opera, Edge, Safari
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Works on common players
- **Origin:** G · **Duplicate of:** —
- **Limitations / notes:** Detecting the main video element is heuristic; unusual layouts may dim the wrong elements.

<a id="tls-012"></a>

## TLS-012 — GPU video enhancement

`Experimental` · `Research` · **P3** · Impact Low · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-TLS-02 (Media controls and Meeting Mode)

Use GPU vendor video enhancement/upscaling where supported.

- **Problem:** Low-resolution video looks poor on large displays.
- **Use case:** A user enables upscaling for a 720p video.
- **Segments:** Everyday users, Power users
- **Dependencies:** [CORE-041](core.md#core-041)
- **Platforms:** Windows Planned · Linux Research · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Chrome/Edge (vendor super resolution, verify)
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Uses OS/driver features
  - Off on battery
- **Origin:** G · **Duplicate of:** —
- **Limitations / notes:** Depends on GPU vendor drivers exposing video super-resolution to Chromium (mainly Windows with recent NVIDIA/Intel drivers); costs significant GPU power and has no effect on most Linux setups.

<a id="tls-013"></a>

## TLS-013 — Live Captions

`Secondary` · `Research` · **P2** · Impact High · Complexity L · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-TLS-03 (Capture, reading and accessibility)

Real-time local captions for any audio playing in a tab.

- **Problem:** Deaf and hard-of-hearing users need captions everywhere.
- **Use case:** A user gets captions for a podcast with no transcript.
- **Segments:** Accessibility users, Everyday users
- **Dependencies:** [NANO-021](nano.md#nano-021)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** Required · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Chrome (Live Caption, uses Google component), Edge
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Local ASR only
  - Latency measured
  - Languages documented
- **Origin:** G · **Duplicate of:** —
- **Limitations / notes:** Chrome's Live Caption depends on a Google component; Brumel needs its own model.

<a id="tls-014"></a>

## TLS-014 — Subtitle translation

`Experimental` · `Research` · **P3** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-TLS-03 (Capture, reading and accessibility)

Translate captions/subtitles locally.

- **Problem:** Foreign-language video is inaccessible.
- **Use case:** A user watches a Japanese video with Spanish subtitles.
- **Segments:** Everyday users, Power users
- **Dependencies:** [TLS-013](#tls-013), [NANO-019](nano.md#nano-019)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** Required · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Vivaldi, Opera, Edge, Safari
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Local models only by default
- **Origin:** G · **Duplicate of:** —
- **Limitations / notes:** Chains two error-prone systems (ASR and translation), compounding mistakes; real-time performance on modest hardware is unlikely.

<a id="tls-015"></a>

## TLS-015 — Tab recording

`Secondary` · `Research` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-TLS-03 (Capture, reading and accessibility)

Record a tab's video and audio to a local file.

- **Problem:** Recording requires separate software.
- **Use case:** A user records a short demo of a web app.
- **Segments:** Everyday users, Power users
- **Dependencies:** [CORE-020](core.md#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Vivaldi, Opera, Edge, Safari
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Local file output
  - Clear recording indicator
  - Respects DRM
- **Origin:** G · **Duplicate of:** —
- **Limitations / notes:** DRM content cannot be recorded; long recordings produce large files and encoding uses CPU/GPU.

<a id="tls-016"></a>

## TLS-016 — Full-page screenshots

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity S · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-TLS-03 (Capture, reading and accessibility)

Capture the entire scrolling page to image or PDF.

- **Problem:** Scrolling captures need extensions.
- **Use case:** A user saves a full receipt page as an image.
- **Segments:** Everyday users, Power users
- **Dependencies:** [CORE-043](core.md#core-043)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Vivaldi, Opera, Edge, Safari
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Handles long pages
  - Annotate optional
- **Origin:** G · **Duplicate of:** —
- **Limitations / notes:** Pages with lazy loading, sticky elements or infinite scroll produce imperfect full-page captures.

<a id="tls-017"></a>

## TLS-017 — Basic PDF editor

`Secondary` · `Research` · **P3** · Impact Medium · Complexity L · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-TLS-04 (Everyday web and file utilities)

Annotate, fill, sign, reorder and delete pages in PDFs locally.

- **Problem:** Simple PDF edits require paid software or uploading to websites.
- **Use case:** A user fills and signs a form PDF.
- **Segments:** Everyday users, Power users
- **Dependencies:** [CORE-037](core.md#core-037)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Edge, Firefox (PDF.js editing)
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Edits stay local
  - Output valid PDF
  - PDFium limits documented
- **Origin:** G · **Duplicate of:** —
- **Limitations / notes:** PDFium's editing capabilities are limited compared with dedicated editors; signatures are visual, not cryptographic, unless a separate signing workflow is designed.

<a id="tls-018"></a>

## TLS-018 — Smart Reader

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity M · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-TLS-03 (Capture, reading and accessibility)

Reader mode with typography, themes and focus options.

- **Problem:** Cluttered pages are hard to read.
- **Use case:** A user reads a long article in a clean view.
- **Segments:** Everyday users, Power users
- **Dependencies:** [CORE-020](core.md#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Safari, Firefox, Edge, Chrome (reading mode)
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Readability extraction quality measured
  - Keeps images and links
- **Origin:** G · **Duplicate of:** —
- **Limitations / notes:** Content extraction fails on some layouts (forums, web apps, paywalls); reader mode upstream exists and Brumel should extend it rather than replace it.

<a id="tls-019"></a>

## TLS-019 — Text-to-speech reading

`Secondary` · `Research` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-TLS-03 (Capture, reading and accessibility)

Read pages aloud using OS voices or local TTS models.

- **Problem:** Listening helps accessibility and multitasking.
- **Use case:** A user listens to an article while cooking.
- **Segments:** Accessibility users, Everyday users
- **Dependencies:** [TLS-018](#tls-018)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** Optional · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Vivaldi, Opera, Edge, Safari
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - OS voices first
  - Local models optional
  - Highlight current sentence
- **Origin:** G · **Duplicate of:** —
- **Limitations / notes:** OS voices differ by platform and language; local neural TTS models are large and their licenses vary.

<a id="tls-020"></a>

## TLS-020 — Distraction Cleaner

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity M · Phase 3 (Public Alpha) · Pillar Clean Web · Epic EP-TLS-03 (Capture, reading and accessibility)

Hide page elements (sticky banners, sidebars, popups) persistently per site.

- **Problem:** Pages are full of distracting elements beyond ads.
- **Use case:** A user hides a site's sticky newsletter bar forever.
- **Segments:** Everyday users, Power users
- **Dependencies:** [SHD-001](shield.md#shd-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Vivaldi, Opera, Edge, Safari
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Element picker
  - Per-site rules
  - Undo
- **Origin:** G · **Duplicate of:** —
- **Limitations / notes:** Element-hiding rules break when sites change markup; hiding the wrong element can hide important information (cookie choices, warnings).

<a id="tls-021"></a>

## TLS-021 — Website Profiles

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity M · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-TLS-03 (Capture, reading and accessibility)

Per-site bundle of settings (zoom, font, theme, permissions, blocking, resource limits).

- **Problem:** Per-site preferences are scattered.
- **Use case:** A user sets a large font and dark theme only for one forum.
- **Segments:** Everyday users, Power users
- **Dependencies:** [ENG-042](engine.md#eng-042), [CORE-045](core.md#core-045)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Vivaldi, Opera, Edge, Safari
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Single per-site panel
  - Exportable
- **Origin:** G · **Duplicate of:** —
- **Limitations / notes:** Many settings already exist per site in Chromium; the panel aggregates them but each underlying setting keeps its own limits.

<a id="tls-022"></a>

## TLS-022 — Accessibility Studio

`Flagship` · `Planned` · **P1** · Impact High · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-TLS-03 (Capture, reading and accessibility)

Central place for accessibility adaptations: fonts (incl. dyslexia-friendly), contrast, spacing, reduced stimuli, reading aids.

- **Problem:** Accessibility options are spread across OS, browser and extensions.
- **Use case:** A user with low vision sets high contrast, larger spacing and a readable font for all sites.
- **Segments:** Accessibility users
- **Dependencies:** [UI-001](interface.md#ui-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Vivaldi, Opera, Edge, Safari
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - WCAG-informed presets
  - Per-site overrides
  - Tested with users of assistive tech
- **Origin:** G · **Duplicate of:** —
- **Limitations / notes:** Browser adaptations cannot fix inaccessible sites (missing labels, images of text); presets need validation with people who use assistive technology.

<a id="tls-023"></a>

## TLS-023 — Fonts and contrast options

`Flagship` · `Planned` · **P1** · Impact High · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-TLS-03 (Capture, reading and accessibility)

Tracked together with TLS-022 (Accessibility Studio).

- **Problem:** Accessibility options are spread across OS, browser and extensions.
- **Use case:** Change fonts and contrast for readability.
- **Segments:** Accessibility users
- **Dependencies:** [TLS-022](#tls-022)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Vivaldi, Opera, Edge, Safari
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of TLS-022
  - Use case verified: Change fonts and contrast for readability.
- **Origin:** G · **Duplicate of:** [TLS-022](#tls-022)
- **Limitations / notes:** Technical duplicate merged into TLS-022; kept as its own entry to preserve the use case and traceability.

<a id="tls-024"></a>

## TLS-024 — Reduced visual stimuli

`Flagship` · `Planned` · **P1** · Impact High · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-TLS-03 (Capture, reading and accessibility)

Tracked together with TLS-022 (Accessibility Studio).

- **Problem:** Accessibility options are spread across OS, browser and extensions.
- **Use case:** Reduce animations, flashing and visual noise on pages.
- **Segments:** Accessibility users
- **Dependencies:** [TLS-022](#tls-022)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Vivaldi, Opera, Edge, Safari
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of TLS-022
  - Use case verified: Reduce animations, flashing and visual noise on pages.
- **Origin:** G · **Duplicate of:** [TLS-022](#tls-022)
- **Limitations / notes:** Technical duplicate merged into TLS-022; kept as its own entry to preserve the use case and traceability.

<a id="tls-025"></a>

## TLS-025 — Adapted reading options

`Flagship` · `Planned` · **P1** · Impact High · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-TLS-03 (Capture, reading and accessibility)

Tracked together with TLS-022 (Accessibility Studio).

- **Problem:** Accessibility options are spread across OS, browser and extensions.
- **Use case:** Reading aids such as line focus and spacing.
- **Segments:** Accessibility users
- **Dependencies:** [TLS-022](#tls-022)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Vivaldi, Opera, Edge, Safari
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of TLS-022
  - Use case verified: Reading aids such as line focus and spacing.
- **Origin:** G · **Duplicate of:** [TLS-022](#tls-022)
- **Limitations / notes:** Technical duplicate merged into TLS-022; kept as its own entry to preserve the use case and traceability.

<a id="tls-026"></a>

## TLS-026 — Meeting Mode

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity S · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-TLS-02 (Media controls and Meeting Mode)

During calls: protect the call tab from throttling, silence other tabs and notifications, optionally enable Screen Share Shield.

- **Problem:** Calls stutter and notifications pop up during meetings.
- **Use case:** Joining a video call automatically mutes other tabs and pauses background work.
- **Segments:** Everyday users, Power users
- **Dependencies:** [ENG-019](engine.md#eng-019), [SHD-033](shield.md#shd-033)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Vivaldi, Opera, Edge, Safari
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Auto-detect active WebRTC call
  - Restore state after call
- **Origin:** G · **Duplicate of:** —
- **Limitations / notes:** Call detection relies on active WebRTC/media capture; calls in desktop apps outside Brumel are not detected.

<a id="tls-027"></a>

## TLS-027 — Migration Assistant

`Flagship` · `Planned` · **P0** · Impact High · Complexity M · Phase 3 (Public Alpha) · Pillar Trust · Epic EP-TLS-05 (Migration and coexistence)

Guided import from Chrome, Edge, Brave, Firefox, Vivaldi, Opera, Arc (where possible): data, open tabs, extensions list and equivalent settings.

- **Problem:** Switching cost is the biggest barrier to trying a new browser.
- **Use case:** A Chrome user imports passwords, bookmarks, open tabs and a list of extensions to reinstall.
- **Segments:** Everyday users, Power users
- **Dependencies:** [CORE-044](core.md#core-044)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Vivaldi, Opera, Edge, Safari
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Import preview with counts
  - Extensions listed with install links
  - Nothing deleted from source browser
- **Origin:** G · **Duplicate of:** —
- **Limitations / notes:** Other browsers encrypt data with OS-bound keys and change formats; some data (Arc spaces, Safari data on Windows, extension data) cannot be imported.

<a id="tls-028"></a>

## TLS-028 — Mouse and trackpad gestures

`Secondary` · `Planned` · **P3** · Impact Low · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-TLS-05 (Migration and coexistence)

Configurable mouse gestures and trackpad swipe actions.

- **Problem:** Power users rely on gestures for speed.
- **Use case:** A user draws a gesture to close a tab.
- **Segments:** Everyday users, Power users
- **Dependencies:** [UI-001](interface.md#ui-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Vivaldi, Opera
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Configurable
  - Off by default for mouse gestures
- **Origin:** G · **Duplicate of:** —
- **Limitations / notes:** Mouse gestures conflict with right-click-drag in some web apps; trackpad gesture support differs between Windows precision touchpads and Linux input stacks.

<a id="tls-029"></a>

## TLS-029 — Subscription Radar

`Secondary` · `Research` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-TLS-04 (Everyday web and file utilities)

Help users remember renewal dates and free-trial endings from pages they explicitly save (sign-up confirmations).

- **Problem:** Forgotten free trials turn into unwanted charges.
- **Use case:** Saving a trial confirmation creates a reminder two days before it ends.
- **Segments:** Everyday users, Power users
- **Dependencies:** [NANO-015](nano.md#nano-015), [MEM-025](memory.md#mem-025)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** Deterministic-first · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Vivaldi, Opera, Edge, Safari
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - User-confirmed entries only
  - Local reminders
  - No payment data stored
- **Origin:** R52-17 · **Duplicate of:** —
- **Limitations / notes:** Renewal terms are expressed inconsistently; extracted dates can be wrong, so reminders require user confirmation and are not financial advice.

<a id="tls-030"></a>

## TLS-030 — Tables to Data

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity S · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-TLS-04 (Everyday web and file utilities)

Export HTML tables to CSV, Markdown or clipboard.

- **Problem:** Copying tables from pages breaks formatting.
- **Use case:** A user exports a statistics table to CSV.
- **Segments:** Everyday users, Power users
- **Dependencies:** [CORE-020](core.md#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Vivaldi, Opera, Edge, Safari
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Handles colspan/rowspan reasonably
  - Preview before export
- **Origin:** R52-21 · **Duplicate of:** —
- **Limitations / notes:** Tables built with divs or rendered in canvas are not detected; complex merged cells may not round-trip perfectly.

<a id="tls-031"></a>

## TLS-031 — Selection Actions

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity M · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-TLS-04 (Everyday web and file utilities)

Context actions for selected dates, addresses, amounts and units (add to calendar, open map, convert currency/units).

- **Problem:** Users copy-paste details into other apps manually.
- **Use case:** Selecting '3 pm EST' offers conversion to local time.
- **Segments:** Everyday users, Power users
- **Dependencies:** [CORE-020](core.md#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** Deterministic-first · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Vivaldi, Opera, Edge, Safari
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Deterministic parsers
  - No network unless action requires it (e.g. maps)
- **Origin:** R52-22 · **Duplicate of:** —
- **Limitations / notes:** Natural-language dates, addresses and units are locale-dependent and ambiguous; conversions using live exchange rates need a network source.

<a id="tls-032"></a>

## TLS-032 — My Search Results

`Secondary` · `Research` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Clean Web · Epic EP-TLS-04 (Everyday web and file utilities)

Prioritize, hide or highlight domains in supported search engines' result pages.

- **Problem:** Search results are filled with low-quality or unwanted domains.
- **Use case:** A user hides content-farm domains from search results permanently.
- **Segments:** Everyday users, Power users
- **Dependencies:** [SHD-001](shield.md#shd-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Kagi (search-side), uBlacklist extension
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Works on documented search engines
  - Rules local
  - Breakage-tolerant
- **Origin:** R52-23 · **Duplicate of:** —
- **Limitations / notes:** Depends on search engine page structure; may break.

<a id="tls-033"></a>

## TLS-033 — Smart Upload

`Flagship` · `Planned` · **P1** · Impact High · Complexity M · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-TLS-04 (Everyday web and file utilities)

When uploading, offer to compress, convert, crop or strip metadata (EXIF/GPS) locally before the file is sent.

- **Problem:** Users upload huge photos with location metadata or get rejected by size limits.
- **Use case:** A user uploads a 12 MB photo to a form with a 2 MB limit; Brumel offers to compress and strip GPS.
- **Segments:** Everyday users, Power users
- **Dependencies:** [CORE-020](core.md#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — image/PDF parsing in sandboxed utility process.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Vivaldi, Opera, Edge, Safari
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Processing local and sandboxed
  - Original file untouched
  - Metadata stripping verified
- **Origin:** R52-25 · **Duplicate of:** —
- **Limitations / notes:** Processing large videos locally is slow; recompression reduces quality, and sites may reject converted formats or require original files for verification.

<a id="tls-034"></a>

## TLS-034 — Local File Workshop

`Secondary` · `Research` · **P2** · Impact Medium · Complexity L · Phase 4 (Public Beta) · Pillar Trust · Epic EP-TLS-04 (Everyday web and file utilities)

Local tools to merge, split, convert and compress PDFs and images without uploading them to websites.

- **Problem:** Users upload private documents to random online converters.
- **Use case:** A user merges three PDFs locally.
- **Segments:** Everyday users, Power users
- **Dependencies:** [TLS-033](#tls-033)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Vivaldi, Opera, Edge, Safari
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - No network
  - Sandboxed processing
  - Common formats documented
- **Origin:** R52-26 · **Duplicate of:** —
- **Limitations / notes:** Format support depends on bundled libraries and their licenses (codecs, PDF tools); complex conversions (DOCX to PDF) are out of scope.

<a id="tls-035"></a>

## TLS-035 — Live Text

`Secondary` · `Research` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-TLS-03 (Capture, reading and accessibility)

Select and copy text in images and paused video frames via local OCR.

- **Problem:** Text in images is not selectable.
- **Use case:** A user copies a phone number from an image.
- **Segments:** Everyday users, Power users
- **Dependencies:** [NANO-020](nano.md#nano-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** Required · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Safari (Live Text), Edge
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Uses NANO-020
  - Only on user action
- **Origin:** R52-27 · **Duplicate of:** —
- **Limitations / notes:** OCR on images requires access to decoded pixels; cross-origin or DRM-protected content may not be accessible.

<a id="tls-036"></a>

## TLS-036 — Universal Local Dictation

`Secondary` · `Research` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-TLS-03 (Capture, reading and accessibility)

Dictate into any text field using local speech recognition.

- **Problem:** Dictation is often cloud-based or unavailable.
- **Use case:** A user dictates a long message in a web form.
- **Segments:** Accessibility users, Everyday users
- **Dependencies:** [NANO-021](nano.md#nano-021)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** Required · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Vivaldi, Opera, Edge, Safari
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Local ASR
  - Microphone indicator
  - Language selection
- **Origin:** R52-28 · **Duplicate of:** —
- **Limitations / notes:** Real-time dictation needs a capable CPU/GPU; injecting text into custom editors may not work everywhere.

<a id="tls-037"></a>

## TLS-037 — Chrome Coexistence

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity M · Phase 3 (Public Alpha) · Pillar Trust · Epic EP-TLS-05 (Migration and coexistence)

Progressive, consent-based import from Chrome while users still use both (re-import new bookmarks/passwords).

- **Problem:** Users test a new browser gradually rather than switching at once.
- **Use case:** Each week, a user imports new Chrome bookmarks with one click.
- **Segments:** Everyday users, Power users
- **Dependencies:** [TLS-027](#tls-027)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Medium — reads other browser's data only on explicit action.
- **Competitors / precedents:** Vivaldi, Opera, Edge, Safari
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Each import requires consent
  - Diff preview
  - No background reading of Chrome data
- **Origin:** R52-29 · **Duplicate of:** —
- **Limitations / notes:** Chrome must be closed or its files readable for import; repeated imports risk duplicates if diffing is imperfect.

<a id="tls-038"></a>

## TLS-038 — Destinations

`Experimental` · `Research` · **P3** · Impact Low · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-TLS-04 (Everyday web and file utilities)

Send page, selection or file to authorized external tools (notes apps, task managers, local folders) via standard mechanisms.

- **Problem:** Saving content to other tools requires many extensions.
- **Use case:** A user sends a selection to their notes app's inbox.
- **Segments:** Everyday users, Power users
- **Dependencies:** [UI-001](interface.md#ui-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Medium — data leaves Brumel by user action.
- **Competitors / precedents:** Vivaldi, Opera, Edge, Safari
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Each destination explicitly authorized
  - Shows what is sent
- **Origin:** R52-39 · **Duplicate of:** —
- **Limitations / notes:** Integration depends on each external tool's API or URL scheme; maintaining many destinations is a long tail of breakage.

<a id="tls-039"></a>

## TLS-039 — Quick Tab Recording

`Secondary` · `Research` · **P2** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-TLS-03 (Capture, reading and accessibility)

Tracked together with TLS-015 (Tab recording).

- **Problem:** Recording requires separate software.
- **Use case:** Record and trim a short clip of a tab quickly.
- **Segments:** Everyday users, Power users
- **Dependencies:** [TLS-015](#tls-015)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low when idle — loaded on demand only. · **Infrastructure cost:** None
- **Security risk:** Medium — processes untrusted files/media; parsing must be sandboxed.
- **Privacy risk:** Low — processing stays local.
- **Competitors / precedents:** Vivaldi, Opera, Edge, Safari
- **Evidence:** Competitor precedent or common extension category; demand to be validated.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of TLS-015
  - Use case verified: Record and trim a short clip of a tab quickly.
- **Origin:** R52-41 · **Duplicate of:** [TLS-015](#tls-015)
- **Limitations / notes:** Technical duplicate merged into TLS-015; kept as its own entry to preserve the use case and traceability.
