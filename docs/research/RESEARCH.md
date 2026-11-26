# Research agenda

Brumel makes many assumptions about users, about Chromium and about small AI models. This
document keeps them **explicit and testable**. Each hypothesis has an ID (`H-xx`), an
evidence status and the next action. The [feature catalog](../product/FEATURES.md)
references these hypotheses in its *Evidence* field.

**Evidence statuses:**

| Status | Meaning |
|---|---|
| **Unverified** | Plausible but not yet tested. Treat it as an assumption. |
| **Partially supported** | Some evidence (for example competitor precedent or upstream documentation), but not tested for Brumel |
| **Supported** | Tested or measured, with data or sources linked |
| **Refuted** | Evidence contradicts it. The dependent features are re-evaluated. |

Competitor precedent proves that something is *feasible*. It does not prove that it is
*valued by users*. We keep those two questions separate.

## 1. Hypotheses

### Performance and efficiency

| ID | Hypothesis | Status | Evidence so far | Next action |
|---|---|---|---|---|
| H-01 | With many tabs open, adaptive tab suspension can cut browser memory well below an unmanaged session | Partially supported | Chromium/Chrome Memory Saver, Edge Sleeping Tabs and Vivaldi/Opera hibernation exist and are documented by their vendors | Measure Brumel against Chrome *with Memory Saver on*, which is the fair baseline |
| H-02 | Brumel can use **20–40% less RAM** than Chrome under equivalent conditions | Unverified | None. This is an initial target, not a result. | Benchmarks in Phase 2 ([BENCHMARKS.md](../benchmarks/BENCHMARKS.md)) |
| H-03 | Brumel can use **15–30% less energy** than Chrome under equivalent conditions | Unverified | None. This is an initial target, not a result. | Energy measurement method in Phase 2 |
| H-04 | Disabled optional modules can be made effectively zero-cost (no threads, no timers, no memory beyond the code itself) | Unverified | Architecture is designed for it ([ADR-0006](../architecture/adr/)) | Measure on, off and never-enabled states for each module |
| H-05 | Games can be detected reliably enough (full-screen exclusive or GPU-heavy foreground apps) without invasive process monitoring | Unverified | OSes expose game-mode / full-screen signals with platform differences | Prototype detection on Windows and Linux; measure false positives |
| H-06 | Throttling background tabs further than Chromium's defaults does not break common sites (chat, music, calls) | Unverified | Chromium already throttles timers and has intensive throttling policies; extra throttling risks breakage | Site compatibility test list plus an allow-list design |

### Maintenance and upstream

| ID | Hypothesis | Status | Evidence so far | Next action |
|---|---|---|---|---|
| H-07 | A small team can ship upstream Chromium security updates within days with a patch-based fork | Partially supported | ungoogled-chromium published 158.0.8127.36-1 (2026-11-19) and 158.0.8127.88-1 (2026-11-24) in quick succession; Helium ships near-daily | Measure our own time from upstream release to tag in Phase 1 |
| H-08 | Forks that rebase infrequently fall behind on security | Supported | Snapshot 2026-11: Thorium went from M156 (2026-11-09) to M158 (2026-11-20) while others had shipped M157 earlier ([CHROMIUM_BASES.md](CHROMIUM_BASES.md)) | Track lag continuously in CI |
| H-09 | Keeping Manifest V2 extensions working is sustainable for Brumel | Unverified (leaning negative) | Upstream Chromium is removing MV2 code paths ([Chrome MV2 deprecation timeline](https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline)). Restoring them grows the patch set significantly. | Rely on the native Clean Web blocker instead; revisit only with evidence |
| H-10 | A Widevine CDM licence is obtainable for a small open-source browser | Unverified | Commercial browsers (Brave, Vivaldi, Opera) ship Widevine; the terms for small projects are not public | Contact Widevine (Google) at Public Alpha; document the outcome in [COMPATIBILITY.md](../architecture/COMPATIBILITY.md) |

### Users and product

| ID | Hypothesis | Status | Evidence so far | Next action |
|---|---|---|---|---|
| H-11 | Losing tabs, sessions or form drafts is a frequent, painful problem | Unverified | Anecdotal; recovery features exist in several browsers | Survey plus analysis of public complaints (method below) |
| H-12 | Users with many tabs want vertical tabs and workspaces | Partially supported | Edge, Vivaldi, Brave, Arc and Zen ship vertical tabs or spaces (supply, not demand) | Survey; opt-in usage study during Internal Alpha |
| H-13 | Users want ad blocking built in, not as an extension | Partially supported | Brave's native blocker; the popularity of content blockers | Survey; measure breakage and complaints |
| H-14 | A transparent "every connection the browser makes" log (Glass Box) increases trust | Unverified | Some users already inspect traffic manually | User interviews at Public Alpha |
| H-15 | Progressive disclosure keeps the default UI familiar while advanced features stay discoverable | Unverified | A design principle, not tested | Usability testing with first-time users |
| H-16 | People want free, local, optional AI more than cloud AI in the browser | Unverified | Privacy concerns about cloud AI are widely discussed; demand is unmeasured | Survey; opt-in rates in beta |

### Local AI (Brumel Nano)

| ID | Hypothesis | Status | Evidence so far | Next action |
|---|---|---|---|---|
| H-17 | Embeddings plus deterministic clustering beat a small generative model for tab grouping | Unverified | EmbeddingGemma (308M params, under 200 MB RAM quantized per Google) makes embeddings cheap | Offline evaluation set of tab titles and URLs |
| H-18 | Models of 1B parameters or fewer (Gemma 3 270M, Qwen3 0.6B, Gemma 3 1B) are good enough for naming groups and classifying pages | Unverified | Model cards claim instruction following; quality for our tasks is untested | Task-specific evaluation; reject the model if quality is below threshold |
| H-19 | Deterministic parsers beat small models at extracting dates and amounts | Partially supported | Parsers and regular expressions are exact and cheap; small models hallucinate | Benchmark both on a labelled set |
| H-20 | Local generative summaries from small models are reliable enough to show | Unverified (high risk) | Known hallucination issues with small models | Ship extractive summaries first; generative only behind a quality gate |
| H-21 | Model memory can be fully released after idle without unacceptable reload latency | Unverified | llama.cpp and ONNX Runtime can load and unload; latency depends on disk and model size | Measure cold-load latency on reference and low-end hardware |

### Infrastructure and sync

| ID | Hypothesis | Status | Evidence so far | Next action |
|---|---|---|---|---|
| H-22 | A free-tier hosted backend (for example Supabase Free) can relay end-to-end encrypted sync for early testers | Unverified | Free-tier limits exist and may change; data is opaque to the server by design | Load model in [SYNC_ARCHITECTURE.md](../architecture/SYNC_ARCHITECTURE.md); fallback is self-hosting |
| H-23 | Direct device-to-device sync (WebRTC) works for a meaningful share of home networks | Unverified | NAT traversal fails in some networks, so a TURN or relay fallback is needed | Prototype in Phase 4 |

## 2. Open questions

1. Which upstream Chromium features depend on Google-only services, and what are the
   replacements? This covers Safe Browsing, translation, spellcheck dictionaries, push
   messaging, Cast and passkey sync. See [COMPATIBILITY.md](../architecture/COMPATIBILITY.md).
2. How much of ungoogled-chromium's patch set do we need, and what does importing selectively
   cost in maintenance?
3. Is adblock-rust (MPL-2.0) the right native blocking engine, and what is the cost of
   integrating it into the Chromium Rust toolchain?
4. What is the right update stack on Linux (distribution repositories, Flatpak,
   AppImage plus a self-updater)?
5. Which small models have licences compatible with redistribution as an optional
   download? Gemma models are under the [Gemma Terms of Use](https://ai.google.dev/gemma/terms)
   (not an OSI licence, with a prohibited-use policy); Qwen3 is Apache-2.0. See
   [LICENSING.md](../legal/LICENSING.md).
6. Can an NPU backend (via ONNX Runtime execution providers or WebNN) be supported without
   per-vendor maintenance burden?
7. What is the minimum hardware for a pleasant experience (4 GB RAM? 8 GB?), and what does
   Low-End Mode have to disable to reach it?
8. Which features are better delivered as a first-party extension than as a browser patch?
   This affects maintenance cost.

## 3. How we collect evidence about user problems

1. **Surveys.** Short, neutral questions with no leading wording ("How often do you lose an
   open tab or form you needed?" rather than "Wouldn't it be great if…"). Distributed through
   GitHub Discussions and community posts, with anonymous results published in aggregate.
2. **Public complaint mining, done with care.**
   - Sources: public Reddit threads, public forums, browser bug trackers (the Chromium issue
     tracker, where star counts are a useful signal), app-store reviews.
   - We record **aggregated themes and links**, never personal data. We do not scrape against
     a site's terms and we do not build profiles of individuals.
   - Quotes are only used when they are already public, and are attributed by link.
3. **Competitor analysis.** Vendor documentation, release notes and source code where
   available. We do not use leaked or confidential material.
4. **Opt-in usage studies.** Only from Internal Alpha onward, opt-in, with a published schema
   and no browsing content (see [PRIVACY.md](../privacy/PRIVACY.md)).
5. **Benchmarks.** Measured with the [benchmark methodology](../benchmarks/BENCHMARKS.md), never
   estimated.

## 4. How research feeds the catalog

- Every catalog entry has an **Evidence** field that links the hypotheses or sources it relies on.
- Status changes have gates:
  - `Research → Planned` needs feasibility evidence (upstream API, prototype or precedent) and
    an identified user need (at least *Partially supported*).
  - `Planned → In Development` needs an accepted design, a security and privacy review for
    medium or high risk items, and its dependencies done.
  - Any status can move to `Deferred` or `Rejected`, but **the entry is never deleted** and the
    reason is recorded.
- A **Refuted** hypothesis triggers a review of every dependent feature within the same
  milestone.

## 5. Sources

Primary sources consulted or planned. URLs are listed as they are linked, and are re-checked
when this document is updated.

**Chromium**

- Get the code and build instructions: https://www.chromium.org/developers/how-tos/get-the-code/
- Windows build instructions: https://chromium.googlesource.com/chromium/src/+/main/docs/windows_build_instructions.md
- Linux build instructions: https://chromium.googlesource.com/chromium/src/+/main/docs/linux/build_instructions.md
- Release schedule and versions (Chromium Dash): https://chromiumdash.appspot.com/releases
- Site isolation: https://www.chromium.org/Home/chromium-security/site-isolation/
- Sandbox design: https://chromium.googlesource.com/chromium/src/+/main/docs/design/sandbox.md
- The Rule of 2: https://chromium.googlesource.com/chromium/src/+/main/docs/security/rule-of-2.md
- Rust in Chromium: https://chromium.googlesource.com/chromium/src/+/main/docs/rust.md
- Limiting private API availability in Chromium (2021): https://blog.chromium.org/2021/01/limiting-private-api-availability-in.html
- Manifest V2 deprecation timeline: https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline

**Chromium-based projects**

- ungoogled-chromium (BSD-3-Clause): https://github.com/ungoogled-software/ungoogled-chromium
- Brave browser and brave-core (MPL-2.0): https://github.com/brave/brave-browser, https://github.com/brave/brave-core
- adblock-rust (MPL-2.0): https://github.com/brave/adblock-rust
- Helium (GPL-3.0): https://github.com/imputnet/helium
- Thorium (BSD-3-Clause): https://github.com/Alex313031/thorium

**Local AI**

- EmbeddingGemma announcement: https://developers.googleblog.com/en/introducing-embeddinggemma/
- Gemma models overview: https://ai.google.dev/gemma/docs
- Gemma Terms of Use: https://ai.google.dev/gemma/terms
- Qwen3: https://github.com/QwenLM/Qwen3
- llama.cpp (MIT): https://github.com/ggml-org/llama.cpp
- ONNX Runtime (MIT): https://github.com/microsoft/onnxruntime
- WebNN API (W3C): https://www.w3.org/TR/webnn/

**Accessibility and design**

- WCAG 2.2: https://www.w3.org/TR/WCAG22/

**Content blocking lists**

- EasyList (licensing information on the site): https://easylist.to/

**Community**

- Show HN guidelines: https://news.ycombinator.com/showhn.html
