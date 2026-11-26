# Product Requirements

> **Status: Draft v0.1 — Pre-development (2026-11-26).** This document states what Brumel must do and how well it must
> do it. No requirement is implemented yet. Numeric targets are **hypotheses**. The public benchmark suite has to
> validate them before they can be called results.

| | |
| --- | --- |
| Owner | Gerard Alvear (@Elgeryy1) |
| Related | [Vision](VISION.md) · [Feature catalog](FEATURES.md) · [Feature matrix](FEATURE_MATRIX.md) · [Roadmap](../../ROADMAP.md) · [Architecture](../architecture/ARCHITECTURE.md) · [Threat model](../security/THREAT_MODEL.md) · [Privacy](../privacy/PRIVACY.md) · [Benchmarks](../benchmarks/BENCHMARKS.md) |
| Change process | Pull request that updates this file and, if needed, the catalog JSON. Requirement IDs are never reused. |

## 1. Purpose and scope

Brumel is an open-source, Chromium-based desktop browser that aims to be as compatible as Chrome while using
resources more carefully, protecting privacy by default, never losing user context, and solving everyday web
problems directly. The [Vision](VISION.md) explains why. This document covers the requirements for:

- the browser on **Windows 10/11 x64** and **Linux x64** (primary targets);
- the optional modules: Engine, Workspace, Memory, Shield, Nano, Connect, Tools, Interface and Dev;
- the project's build, update and distribution systems, where they affect users.

macOS is **Deferred** and Android belongs to the **Future** phase. iOS is out of scope for now. See [§8 Out of scope](#8-out-of-scope).

### Requirement keywords

**MUST**, **SHOULD** and **MAY** follow RFC 2119. Each functional requirement traces to catalog IDs, which hold the
detailed acceptance criteria. A requirement's phase is the phase in which it must first be met.

## 2. Product principles as constraints

Each principle below is binding. A design that breaks one needs an ADR that explains why.

| ID | Principle | Consequence |
| --- | --- | --- |
| PR-01 | Compatibility first | No patch may change web-visible behavior (Blink/V8) without an ADR and a compatibility test plan. |
| PR-02 | Security is not traded for benchmarks | Sandboxing, site isolation and exploit mitigations stay enabled ([CORE-055](features/core.md#core-055) is Rejected). |
| PR-03 | Optional means absent | A disabled module creates no services, timers, processes or network requests ([CORE-005](features/core.md#core-005)). |
| PR-04 | Local-first, no mandatory account | Every core feature works offline and without an account ([CON-025](features/connect.md#con-025)). |
| PR-05 | No mandatory telemetry, no own ads | Telemetry is opt-in and auditable ([SHD-027](features/shield.md#shd-027)). Brumel shows no advertising of its own. |
| PR-06 | Verifiable transparency | Every connection the browser initiates is logged with a purpose ([SHD-034](features/shield.md#shd-034)). |
| PR-07 | Familiar by default, powerful on demand | Defaults resemble mainstream browsers. Advanced features appear progressively ([UI-018](features/interface.md#ui-018), [UI-019](features/interface.md#ui-019)). |
| PR-08 | Deterministic before AI | Use deterministic algorithms whenever they are reliable enough. AI never makes security decisions ([NANO-028](features/nano.md#nano-028)). |
| PR-09 | Data portability | Users can export all their data in open formats ([MEM-030](features/memory.md#mem-030)). |
| PR-10 | No Electron | The browser chrome is native Chromium (Views + WebUI), per ADR-0005 ([CORE-056](features/core.md#core-056) is Rejected). |

## 3. Users and segments

Brumel serves several overlapping groups. The catalog's `segments` field uses the same names.

| Persona | Segment | Main needs | Representative features |
| --- | --- | --- | --- |
| **Lucía**, student, 8 GB laptop | Everyday users, Low-end hardware users, Students & researchers | Many tabs without slowdown, battery life, no lost work | [ENG-011](features/engine.md#eng-011), [WRK-008](features/workspace.md#wrk-008), [MEM-004](features/memory.md#mem-004), [WRK-032](features/workspace.md#wrk-032) |
| **Marc**, freelance developer | Developers, Power users | Separate client identities, stable dev tabs, keyboard-driven work | [WRK-010](features/workspace.md#wrk-010), [ENG-036](features/engine.md#eng-036), [WRK-018](features/workspace.md#wrk-018), [CORE-035](features/core.md#core-035) |
| **Ana**, privacy-conscious professional | Privacy-conscious users | Blocking, no phoning home, local-only data | [SHD-001](features/shield.md#shd-001), [SHD-034](features/shield.md#shd-034), [SHD-027](features/shield.md#shd-027), [MEM-018](features/memory.md#mem-018) |
| **Jordi**, gamer and streamer | Gamers & streamers | Browser that stays out of the way during games and streams | [ENG-003](features/engine.md#eng-003), [ENG-035](features/engine.md#eng-035), [TLS-007](features/tools.md#tls-007) |
| **Carmen**, retired, shared family PC | Everyday users, Accessibility users | Readability, scam protection, simple UI | [TLS-022](features/tools.md#tls-022), [SHD-032](features/shield.md#shd-032), [SHD-017](features/shield.md#shd-017), [CON-028](features/connect.md#con-028) |
| **Sam**, self-hoster | Self-hosters | Own sync server, local AI endpoints | [CON-018](features/connect.md#con-018), [NANO-026](features/nano.md#nano-026) |
| **Contributors and maintainers** | Maintainers, Contributors | Reproducible builds, fast upstream rebases | [CORE-001](features/core.md#core-001)–[CORE-008](features/core.md#core-008) |

The personas are illustrative and do not come from user research yet. Validating them through interviews and
Discussions is a Phase 0–2 activity (see [RESEARCH.md](../research/RESEARCH.md)).

## 4. Functional requirements

Requirements are grouped by module. "Phase" is the first phase in which the requirement **MUST** hold.

### 4.1 Core: platform, parity and distribution

| ID | Requirement | Phase | Catalog |
| --- | --- | --- | --- |
| FR-001 | The build system MUST fetch the pinned Chromium revision reproducibly and apply the Brumel patch series without manual steps. | 1 | CORE-001, CORE-002 |
| FR-002 | The project MUST detect new upstream stable and security releases automatically. | 1 | CORE-003 |
| FR-003 | Builds MUST be branded Brumel and MUST NOT show Google or Chrome trademarks in the UI. | 1 | CORE-004 |
| FR-004 | Every optional module MUST be registered in the module registry and be fully disableable through settings and enterprise policy. | 1 | CORE-005 |
| FR-005 | Browser-initiated requests to Google services MUST be removed, replaced or individually justified. | 1 | CORE-006, CORE-012, CORE-013, CORE-014 |
| FR-006 | The browser MUST provide the Chromium essentials: navigation, extensions, password manager, passkeys, autofill, profiles, incognito, guest, bookmarks, history, downloads, tab groups, pinned tabs, DevTools, PWAs, PDF, printing, spellcheck, GPU acceleration, hardware decoding, PiP, screenshots, import/export and permissions. | 2 | CORE-020 – CORE-045 |
| FR-007 | Releases MUST be signed and delivered through automatic, verifiable updates on Windows and Linux. | 1 (internal), 3 (public) | CORE-009, CORE-010, CORE-051 |
| FR-008 | Phishing and malware protection MUST exist before the first public build, without sending full URLs to third parties by default. | 3 | CORE-012, CORE-050 |
| FR-009 | Widevine, proprietary codecs and Cast SHOULD ship only once licensing is resolved. Until then their limitations MUST be stated clearly to users. | 3 | CORE-052, CORE-053, CORE-054 |

### 4.2 Engine: efficiency

| ID | Requirement | Phase | Catalog |
| --- | --- | --- | --- |
| FR-010 | Background tabs MUST be frozen or discarded according to policy. Tabs with audio, active calls, unsaved form input or user exceptions MUST be protected. | 2 | ENG-019, ENG-024, ENG-022 |
| FR-011 | The browser MUST offer Performance, Balanced and Battery Saver profiles, with Balanced as the default. | 2 | ENG-033 |
| FR-012 | Startup MUST load only the active tab and defer non-critical services. | 2 | ENG-043, ENG-045 |
| FR-013 | A resource monitor MUST attribute CPU, memory, GPU and network use to tabs, extensions and Brumel modules. | 2 | ENG-031 |
| FR-014 | Heavy background work (indexing, OCR, embeddings, backups) MUST run through the Idle Scheduler. | 2 | ENG-045 |
| FR-015 | Users SHOULD be able to set RAM and CPU budgets, per-site resource limits and automatic profile rules. | 3 | ENG-005, ENG-006, ENG-040, ENG-042 |
| FR-016 | Extension Doctor and Browser Health SHOULD explain slowness and propose reversible fixes. | 3 | ENG-013, ENG-015, ENG-018 |

### 4.3 Workspace: organization

| ID | Requirement | Phase | Catalog |
| --- | --- | --- | --- |
| FR-020 | Users MUST be able to switch between horizontal and vertical tabs without restarting. | 2 | WRK-001 |
| FR-021 | Session state (windows, groups, pinned tabs) MUST survive crashes, updates and forced shutdowns. | 2 | WRK-023 |
| FR-022 | Users SHOULD be able to archive tabs, keep hundreds of unloaded tabs and search across open and archived tabs. | 3 | WRK-008, WRK-017, WRK-021 |
| FR-023 | Workspaces, Multi Identity and Smart Router SHOULD let users separate contexts without separate windows or profiles. | 4 | WRK-004, WRK-009, WRK-010 |
| FR-024 | A shared, visual rules engine SHOULD back every rule-based feature (routing, profiles, downloads, temporary tabs). | 4 | WRK-030 |

### 4.4 Memory: never lose context

| ID | Requirement | Phase | Catalog |
| --- | --- | --- | --- |
| FR-030 | Brumel modules MUST store data in the shared Brumel Store, with quotas and schema migrations. | 2 | MEM-014 |
| FR-031 | Incognito, guest, locked spaces and excluded sites MUST never be recorded by any Memory feature. | 2 | MEM-018 |
| FR-032 | Users SHOULD be able to restore earlier session states, undo destructive actions and recover drafts. | 3 | MEM-001, MEM-004, MEM-006, MEM-020 |
| FR-033 | Users MUST be able to export all their data in documented open formats. | 3 | MEM-030 |
| FR-034 | Semantic recall MAY be offered once local models meet quality thresholds. | 4 | MEM-002 |

### 4.5 Shield: privacy and security

| ID | Requirement | Phase | Catalog |
| --- | --- | --- | --- |
| FR-040 | Native ad and tracker blocking MUST be on by default, with a per-site toggle. | 2 | SHD-001 |
| FR-041 | Pop-ups, audible autoplay and notification prompts MUST be blocked or quieted by default. | 2 | SHD-002, SHD-003, SHD-005 |
| FR-042 | Known tracking parameters MUST be removed from navigations and copied links. | 2 | SHD-007 |
| FR-043 | Glass Box MUST list every browser-initiated connection with its purpose before the first public build. | 3 | SHD-034 |
| FR-044 | Telemetry MUST be off by default. If a user enables it, the user MUST be able to view each payload before it is sent. | 3 | SHD-027 |
| FR-045 | Users SHOULD be able to grant one-time permissions, review a permission timeline and restrict extensions by site and destination. | 3 | SHD-011, SHD-012, SHD-013, SHD-035 |
| FR-046 | Sensitive Brumel data MUST be encrypted at rest with OS-protected keys. | 2 | SHD-020 |

### 4.6 Nano: local AI

| ID | Requirement | Phase | Catalog |
| --- | --- | --- | --- |
| FR-050 | Nano MUST be optional, downloaded separately, and completely removable. | 4 | NANO-002 |
| FR-051 | Inference MUST run in a sandboxed utility process with no network access, load on demand and unload after idle. | 4 | NANO-001, NANO-003 |
| FR-052 | Web content MUST be treated as untrusted model input. Model output MUST NOT trigger privileged actions without deterministic validation and user confirmation. | 4 | NANO-007 |
| FR-053 | Nano MUST pause automatically under Battery Saver, gaming, thermal throttling and memory pressure. | 4 | NANO-005 |
| FR-054 | Each AI feature MUST have a non-AI fallback or MUST be clearly labeled optional. | 4 | NANO-009 – NANO-024 |
| FR-055 | External providers (BYOK, Ollama, OpenAI-compatible) MAY be offered as opt-in, showing exactly what will be sent before each request. | 4 | NANO-025, NANO-026, NANO-027 |

### 4.7 Connect: continuity

| ID | Requirement | Phase | Catalog |
| --- | --- | --- | --- |
| FR-060 | Sync MUST be end-to-end encrypted in the client. Servers MUST only store ciphertext and minimal metadata. | 4 | CON-020, CON-023 |
| FR-061 | Sync MUST work offline-first, incrementally, and with deterministic conflict handling. | 4 | CON-014, CON-015, CON-016 |
| FR-062 | Users MUST be able to pair devices without an account (QR) and to self-host the sync server. | 4 | CON-013, CON-018 |
| FR-063 | Password sync MUST NOT ship before a dedicated security review. | 5 | CON-019 |

### 4.8 Tools and interface

| ID | Requirement | Phase | Catalog |
| --- | --- | --- | --- |
| FR-070 | The Migration Assistant MUST import data from Chrome, Edge, Brave and Firefox without modifying the source browser. | 3 | TLS-027, CORE-044 |
| FR-071 | Smart Upload SHOULD let users compress, convert and strip metadata from files locally before upload. | 3 | TLS-033 |
| FR-072 | Accessibility Studio SHOULD provide reading, contrast and reduced-stimuli presets. | 4 | TLS-022 |
| FR-073 | Default UI MUST resemble mainstream browsers. Every Brumel toolbar element MUST be hideable. | 2 | UI-018, UI-012 |
| FR-074 | The UI MUST honor OS dark/light and reduced-motion settings. | 2 | UI-003, UI-014 |

### 4.9 Developers and automation

| ID | Requirement | Phase | Catalog |
| --- | --- | --- | --- |
| FR-080 | Automation, userscripts, MCP, terminals and agents MUST NOT be enabled until the Agent Clean Room capability model has been designed and reviewed. | 6 | SHD-037, DEV-010, DEV-012, DEV-013, DEV-017 |

## 5. Non-functional requirements

### 5.1 Security

| ID | Requirement |
| --- | --- |
| NFR-SEC-01 | Sandboxing and full site isolation MUST stay enabled on every supported platform, and CI MUST check this on every release build. |
| NFR-SEC-02 | **Update latency goal:** ship upstream Chromium security fixes to the stable channel within **7 days** of the upstream stable release, and within **72 hours** for fixes to vulnerabilities exploited in the wild. These are goals; the actual latency of every release is published. |
| NFR-SEC-03 | Release artifacts and update metadata MUST be signed. Signing keys MUST NOT be reachable from jobs that run untrusted pull request code. |
| NFR-SEC-04 | Each release MUST publish an SBOM and checksums. |
| NFR-SEC-05 | New parsers of untrusted input (files, filters, model inputs) MUST run sandboxed or be written in a memory-safe language, and SHOULD be fuzzed. |
| NFR-SEC-06 | Vulnerabilities MUST be reportable privately (see [SECURITY.md](../../SECURITY.md)). Acknowledgement goal: 72 hours. |
| NFR-SEC-07 | No AI component MAY make security decisions or hold privileged capabilities. |

### 5.2 Privacy

| ID | Requirement |
| --- | --- |
| NFR-PRI-01 | A fresh profile MUST make no request that is undocumented in Glass Box. An undocumented request is a release-blocking bug. |
| NFR-PRI-02 | No unique, long-lived identifiers MAY be sent by default. |
| NFR-PRI-03 | All Memory and Nano data MUST be local by default, deletable per item and in bulk, and excluded from incognito. |
| NFR-PRI-04 | Every data flow to the network MUST be described in [PRIVACY.md](../privacy/PRIVACY.md) before it ships. |

### 5.3 Performance (hypotheses until measured)

All targets compare Brumel to the **same Chromium version** and to Chrome, on identical hardware, pages and
configuration, using [BENCHMARKS.md](../benchmarks/BENCHMARKS.md). None of these figures has been demonstrated.

| ID | Target (hypothesis) |
| --- | --- |
| NFR-PERF-01 | With Balanced defaults, browser memory with 50–200 open tabs (most of them in the background) is **20–40% lower** than Chrome. |
| NFR-PERF-02 | Energy use in the idle and background-tab scenarios is **15–30% lower** than Chrome. |
| NFR-PERF-03 | Cold startup with a 200-tab session is no slower than the same Chromium version with a 1-tab session plus a small fixed overhead (to be defined after Phase 1 measurements). |
| NFR-PERF-04 | Disabled modules add **no measurable** memory, CPU wakeups or processes compared with a build without those modules (within measurement noise). |
| NFR-PERF-05 | Brumel UI interactions (tab switch, palette open) show no regression against the same Chromium version on the reference hardware. |
| NFR-PERF-06 | Nano uses zero resident memory when idle. Loaded models stay within a published per-model budget. |
| NFR-PERF-07 | Web performance (Speedometer, JetStream, MotionMark) does not regress compared with the same Chromium version, beyond measurement noise. |

If a measured result misses a hypothesis, the documentation is corrected. The benchmark is never tuned to hit the target.

### 5.4 Reliability

| ID | Requirement |
| --- | --- |
| NFR-REL-01 | Session data writes MUST be atomic and versioned. A crash at any point MUST NOT lose more than the last few seconds of tab changes. |
| NFR-REL-02 | Updates MUST preserve settings, sessions and module state. Upgrade tests run before every release. |
| NFR-REL-03 | Crash loops MUST be detected and mitigated with safe-mode recovery ([ENG-014](features/engine.md#eng-014)). |
| NFR-REL-04 | Brumel Store migrations MUST be tested forward and must be recoverable from corruption. |

### 5.5 Accessibility

| ID | Requirement |
| --- | --- |
| NFR-A11Y-01 | Brumel-specific UI MUST meet **WCAG 2.2 AA** for contrast, focus visibility, keyboard operability and target size. |
| NFR-A11Y-02 | All Brumel UI MUST work with the screen readers supported by Chromium on each platform (Narrator/NVDA/JAWS on Windows, Orca on Linux). |
| NFR-A11Y-03 | Reduced motion and high-contrast OS settings MUST be honored. |

### 5.6 Compatibility

| ID | Requirement |
| --- | --- |
| NFR-COMP-01 | Web Platform Tests pass rate MUST stay within an agreed tolerance of the same Chromium version. |
| NFR-COMP-02 | A top-sites smoke suite and a top-extensions suite MUST pass before each release. See [COMPATIBILITY.md](../architecture/COMPATIBILITY.md). |
| NFR-COMP-03 | Content-blocking breakage MUST be fixable by users with a per-site toggle, and reportable. |

### 5.7 Maintainability

| ID | Requirement |
| --- | --- |
| NFR-MAINT-01 | Brumel changes to Chromium files MUST be small patches with a header (purpose, owner, upstream status). New code SHOULD live in Brumel-owned directories. |
| NFR-MAINT-02 | The patch series MUST be rebasable onto a new Chromium major within one release cycle. Patches that keep failing to rebase are reconsidered. |
| NFR-MAINT-03 | Every module has an owner and tests, and can be disabled in builds. |
| NFR-MAINT-04 | Architectural decisions are recorded as ADRs in [docs/architecture/adr/](../architecture/adr/). |

### 5.8 Transparency and governance

| ID | Requirement |
| --- | --- |
| NFR-GOV-01 | Benchmarks, metric dictionaries, build scripts and server code (sync relay, update manifests) MUST be open source. |
| NFR-GOV-02 | Every claim in public communication MUST be backed by a published measurement or explicitly labeled as a goal. |

## 6. Constraints

- **Small team.** At the start this is a personal project with one maintainer. Scope and dates follow real capacity, and the roadmap uses no fixed dates.
- **Chromium build cost.** Full builds need large machines, about 100 GB or more of disk, and hours of compute. CI capacity limits iteration speed (see [INFRASTRUCTURE.md](../development/INFRASTRUCTURE.md)).
- **Licensing.** Brumel-original files use MPL-2.0. Patches to Chromium files use BSD-3-Clause. Third-party licenses are preserved. Model licenses (for example the Gemma Terms of Use) and filter-list licenses require review (see [LICENSING.md](../legal/LICENSING.md)).
- **Google services.** Brumel cannot rely on private Google APIs (Sync, Translate and similar) or redistribute Google-proprietary components without an agreement (Widevine).
- **Budget.** Free tiers and self-hosting come first. Paid services require the owner's approval.

## 7. Release criteria per phase

| Phase | Exit criteria |
| --- | --- |
| **0 Pre-development** | Vision, catalog, architecture, ADRs, threat model, licensing decision, roadmap and repository infrastructure are published. Build strategy is documented. |
| **1 Technical Foundation** | Reproducible fetch and patch application. A branded build runs on Windows and Linux. Module registry exists. Signed internal update channel works. CI enforces sandbox and site isolation. Upstream tracking is automated. |
| **2 Internal Alpha** | FR-006, FR-010–FR-014, FR-020, FR-021, FR-030, FR-031, FR-040–FR-042, FR-046, FR-073, FR-074 met. First benchmark runs are published, whatever the result. Used daily by the maintainer. |
| **3 Public Alpha** | Signed public builds with verifiable installers. Glass Box, phishing protection and opt-in telemetry policy in place (FR-008, FR-043, FR-044). Migration Assistant and data export work. Feedback channels are open. Known limitations (DRM, codecs, sync) are published. |
| **4 Public Beta** | Nano and Connect pass security review and benchmarks. Accessibility audit of Brumel UI against WCAG 2.2 AA. External security review of the sync cryptography. Public benchmark comparisons are published. |
| **5 Version 1.0** | Update latency goals met consistently for several consecutive upstream majors. Stability metrics (crash rate from opt-in reports) are acceptable. Documentation is complete. Vulnerability process tested. Infrastructure costs are sustainable. |
| **6 Future** | Opened per feature, each one with its own requirements. |

## 8. Out of scope

- A new rendering or JavaScript engine. Brumel uses Blink and V8.
- Electron or any non-Chromium shell for the browser (PR-10).
- iOS, for now: outside the EU, browsers on iOS must use WebKit.
- Brumel-owned advertising, sponsored tiles, affiliate injection or selling user data.
- Mandatory accounts, subscriptions for essential features, or paid AI as a requirement.
- Autonomous AI agents, command execution or MCP before the capability model exists ([SHD-037](features/shield.md#shd-037)).
- Claims of anonymity equivalent to Tor Browser.

## 9. Traceability

- **Catalog → requirements:** each FR lists catalog IDs. The detailed, testable acceptance criteria live in the catalog cards.
- **Catalog → issues:** epics (`EP-*`) are mirrored as GitHub issues, and issues reference feature IDs in their titles or bodies.
- **Requirements → tests:** from Phase 1 on, tests reference FR/NFR IDs in their names or docstrings where practical.

## 10. Open questions

1. What is the Safe Browsing strategy: proxy, alternative lists or licensed access ([CORE-012](features/core.md#core-012))?
2. Is there a path to Widevine licensing for a small open-source project ([CORE-053](features/core.md#core-053))?
3. Which local models meet quality thresholds for EN/ES tasks, and under which licenses ([NANO-006](features/nano.md#nano-006))?
4. Does Brumel keep any Manifest V2 support, given the cost ([CORE-022](features/core.md#core-022))?
5. Which sync merge model (CRDT or operation log) fits each data type ([CON-015](features/connect.md#con-015))?
6. Are the update latency goals in NFR-SEC-02 sustainable with the available CI capacity?
