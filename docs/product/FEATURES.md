<!-- GENERATED FILE — Do not edit by hand. Source: docs/product/catalog/*.json. Regenerate: python scripts/catalog/render_features.py -->

# Brumel Feature Catalog

> **Project status: Pre-development.** Nothing in this catalog is available yet. Every entry is a proposal with a status, a priority and acceptance criteria. Performance and resource targets are hypotheses until the public benchmark suite measures them.

This catalog is the single source of truth for what Brumel might become. It keeps every idea that has been proposed — including deferred and rejected ones — under a stable ID, so that issues, pull requests, ADRs and roadmap items can reference it. Technical duplicates keep their own ID and point to the entry that implements them (*Duplicate of*), so no use case is silently dropped.

- Canonical data: [`catalog/features.json`](catalog/features.json) and [`catalog/epics.json`](catalog/epics.json)
- Related: [Vision](VISION.md) · [Product requirements](PRODUCT_REQUIREMENTS.md) · [Feature matrix](FEATURE_MATRIX.md) · [Roadmap](../../ROADMAP.md) · [Architecture](../architecture/ARCHITECTURE.md)
- To propose a change, open a *Feature request* issue or edit the JSON and run the renderer (see [CONTRIBUTING](../../CONTRIBUTING.md)).

## Contents

- [Legend](#legend)
- [Summary](#summary)
- [Epics](#epics)
- [Feature cards by module](#feature-cards-by-module)
- [The 52 research proposals](#the-52-research-proposals)
- [Feature index](#feature-index)

## Legend

**Status** — where the work stands:

| Status | Meaning |
| --- | --- |
| Available | Shipped in a public build. *(None yet.)* |
| In Development | Actively being implemented. *(None yet.)* |
| Planned | Accepted for a phase; understood well enough to build. Chromium-inherited items are Planned until the first build proves them. |
| Research | Needs investigation (feasibility, licensing, quality, security) before committing. |
| Experimental | Built behind a flag for evaluation; may be removed. *(None yet.)* |
| Deferred | Valid idea postponed because of risk, cost or dependencies; revisited later. |
| Rejected | Not pursued as stated, for technical or security reasons. The entry records why and names the safer alternative. |

**Tier** — role in the product: **Essential** (required for a credible daily browser), **Flagship** (differentiating; communicates the pillars), **Secondary** (useful, lower priority), **Experimental** (uncertain value or feasibility), **Community** (best driven by contributors), **Deferred**, **Rejected**.

**Priority** — P0 blocking for its phase · P1 high · P2 normal · P3 low/opportunistic. **Impact** — Low, Medium, High, Critical. **Complexity** — XS, S, M, L, XL (relative effort, not time).

**Phases** — 0 Pre-development · 1 Technical Foundation · 2 Internal Alpha · 3 Public Alpha · 4 Public Beta · 5 Version 1.0 · 6 Future. See [ROADMAP.md](../../ROADMAP.md).

**Pillars** — Efficiency · Memory · Clean Web · Trust · Everyday Tools. *Foundation* marks platform work. Brumel Nano is a cross-cutting technology, not a pillar.

**Origin** — `S8` Chromium-inherited essentials · `A`–`I` module backlogs (A Engine, B Workspace, C Memory, D Shield, E Nano, F Connect, G Tools, H Interface, I Dev) · `R52-nn` the 52 product-research proposals · `FOUND` foundation work required by the plan · `S3`/`S16` project principles (rejected patterns).

**Platforms** — Windows and Linux x64 are the primary targets; macOS is Deferred; Android belongs to the Future phase. `N/A` means the feature does not apply to that platform.

## Summary

The catalog holds **339 entries** grouped in **40 epics**. **33** of them are technical duplicates tracked under a primary entry, so the number of distinct implementation items is **306**.

### By module

| Module | Entries |
| --- | ---: |
| [CORE](features/core.md) — Brumel Core | 51 |
| [ENG](features/engine.md) — Brumel Engine | 46 |
| [WRK](features/workspace.md) — Brumel Workspace | 38 |
| [MEM](features/memory.md) — Brumel Memory | 30 |
| [SHD](features/shield.md) — Brumel Shield | 39 |
| [NANO](features/nano.md) — Brumel Nano | 30 |
| [CON](features/connect.md) — Brumel Connect | 28 |
| [TLS](features/tools.md) — Brumel Tools | 39 |
| [UI](features/interface.md) — Personalization and interface | 21 |
| [DEV](features/dev.md) — Brumel Dev | 17 |
| **Total** | **339** |

### By tier

| Tier | Entries |
| --- | ---: |
| Essential | 104 |
| Flagship | 57 |
| Secondary | 130 |
| Experimental | 34 |
| Community | 2 |
| Deferred | 7 |
| Rejected | 5 |
| **Total** | **339** |

### By status

| Status | Entries |
| --- | ---: |
| Planned | 195 |
| Research | 125 |
| Deferred | 14 |
| Rejected | 5 |
| **Total** | **339** |

### By proposed phase

| Phase | Entries |
| --- | ---: |
| 0 — Pre-development | 6 |
| 1 — Technical Foundation | 17 |
| 2 — Internal Alpha | 65 |
| 3 — Public Alpha | 101 |
| 4 — Public Beta | 130 |
| 5 — Version 1.0 | 1 |
| 6 — Future | 19 |
| **Total** | **339** |

### By priority

| Priority | Entries |
| --- | ---: |
| P0 | 53 |
| P1 | 90 |
| P2 | 118 |
| P3 | 78 |
| **Total** | **339** |

## Epics

Epics group features for planning and are mirrored as GitHub issues. The epic phase is the earliest phase in which the epic is expected to deliver something.

| Epic | Title | Phase | Priority | Entries | Depends on |
| --- | --- | --- | --- | ---: | --- |
| EP-CORE-01 | Reproducible build, upstream tracking and supply chain | 1 — Technical Foundation | P0 | 6 | — |
| EP-CORE-02 | Branding, packaging and signed updates | 1 — Technical Foundation | P0 | 4 | EP-CORE-01 |
| EP-CORE-03 | Module system and feature registry | 1 — Technical Foundation | P0 | 3 | EP-CORE-01 |
| EP-CORE-04 | Chromium feature parity | 2 — Internal Alpha | P0 | 26 | EP-CORE-01, EP-CORE-02 |
| EP-CORE-05 | Google-service replacements, DRM, codecs and Cast | 2 — Internal Alpha | P1 | 11 | EP-CORE-04 |
| EP-CORE-06 | Security baseline: sandbox, site isolation, HTTPS and DNS | 1 — Technical Foundation | P0 | 7 | EP-CORE-01 |
| EP-ENG-01 | Tab lifecycle and memory management | 2 — Internal Alpha | P0 | 9 | EP-CORE-03, EP-CORE-04 |
| EP-ENG-02 | Adaptive engine, budgets and performance profiles | 2 — Internal Alpha | P1 | 25 | EP-ENG-01, EP-ENG-04 |
| EP-ENG-03 | Fast startup and on-demand extensions | 2 — Internal Alpha | P1 | 6 | EP-ENG-01 |
| EP-ENG-04 | Diagnostics: resource monitor, Browser Health and benchmark | 2 — Internal Alpha | P1 | 8 | EP-CORE-03 |
| EP-WRK-01 | Tab strip: vertical tabs, trees and folders | 2 — Internal Alpha | P0 | 6 | EP-UI-01 |
| EP-WRK-02 | Workspaces, identities and routing | 4 — Public Beta | P1 | 6 | EP-WRK-01, EP-MEM-01 |
| EP-WRK-03 | Infinite Tabs, archiving and session recovery | 2 — Internal Alpha | P0 | 6 | EP-ENG-01, EP-MEM-01 |
| EP-WRK-04 | Universal search, quick actions, split view and panels | 3 — Public Alpha | P1 | 9 | EP-MEM-01, EP-UI-01 |
| EP-WRK-05 | Attention tools, collections and rules engine | 3 — Public Alpha | P2 | 14 | EP-WRK-02 |
| EP-MEM-01 | Brumel Store and local index | 2 — Internal Alpha | P0 | 2 | EP-CORE-03 |
| EP-MEM-02 | Browser Time Machine, Zero Loss and data portability | 3 — Public Alpha | P1 | 12 | EP-MEM-01, EP-WRK-03 |
| EP-MEM-03 | Draft, form and login protection | 3 — Public Alpha | P1 | 3 | EP-MEM-01 |
| EP-MEM-04 | Recall, vaults and page history | 3 — Public Alpha | P2 | 15 | EP-MEM-01, EP-NANO-01 |
| EP-SHD-01 | Native content blocking (Clean Web) | 2 — Internal Alpha | P0 | 9 | EP-CORE-03 |
| EP-SHD-02 | Permissions and extension control | 3 — Public Alpha | P1 | 4 | EP-CORE-04 |
| EP-SHD-03 | Transparency: Glass Box, Privacy Receipt and telemetry | 3 — Public Alpha | P1 | 3 | EP-CORE-03 |
| EP-SHD-04 | Local data, credential and session protection | 2 — Internal Alpha | P1 | 7 | EP-MEM-01 |
| EP-SHD-05 | Web safety tools and advanced privacy | 3 — Public Alpha | P2 | 10 | EP-SHD-01 |
| EP-NANO-01 | Nano runtime, model management and safety boundaries | 4 — Public Beta | P1 | 10 | EP-CORE-03, EP-ENG-02 |
| EP-NANO-02 | Nano organization and classification | 4 — Public Beta | P2 | 7 | EP-NANO-01 |
| EP-NANO-03 | Nano language, speech and vision | 4 — Public Beta | P2 | 6 | EP-NANO-01 |
| EP-NANO-04 | Optional cloud and BYOK providers | 4 — Public Beta | P3 | 3 | EP-NANO-01 |
| EP-CON-01 | E2EE sync core and infrastructure | 4 — Public Beta | P1 | 12 | EP-MEM-01, EP-SHD-04 |
| EP-CON-02 | Synced data types | 4 — Public Beta | P1 | 8 | EP-CON-01 |
| EP-CON-03 | Device mesh, sharing and pairing | 4 — Public Beta | P2 | 8 | EP-CON-01 |
| EP-TLS-01 | Downloads | 3 — Public Alpha | P1 | 5 | EP-CORE-04 |
| EP-TLS-02 | Media controls and Meeting Mode | 4 — Public Beta | P2 | 8 | EP-CORE-04 |
| EP-TLS-03 | Capture, reading and accessibility | 3 — Public Alpha | P2 | 16 | EP-CORE-04 |
| EP-TLS-04 | Everyday web and file utilities | 3 — Public Alpha | P1 | 8 | EP-CORE-04 |
| EP-TLS-05 | Migration and coexistence | 3 — Public Alpha | P1 | 3 | EP-CORE-04 |
| EP-UI-01 | UI shell, design system and progressive discovery | 2 — Internal Alpha | P0 | 10 | EP-CORE-02 |
| EP-UI-02 | Themes and customization | 3 — Public Alpha | P2 | 9 | EP-UI-01 |
| EP-DEV-01 | Developer tools | 4 — Public Beta | P3 | 9 | EP-CORE-04 |
| EP-DEV-02 | Automation and privileged integrations (deferred) | 6 — Future | P3 | 6 | EP-SHD-05 |

## Feature cards by module

Full cards — problem, use case, segments, dependencies, platforms, AI need, resource and infrastructure cost, security and privacy risks, competitors, evidence, acceptance criteria, origin and limitations — are on one page per module:

| Module | Entries |
| --- | ---: |
| [Brumel Core — Chromium parity, build, update and distribution](features/core.md) | 51 |
| [Brumel Engine — performance and efficiency](features/engine.md) | 46 |
| [Brumel Workspace — tabs and productivity](features/workspace.md) | 38 |
| [Brumel Memory — memory and recovery](features/memory.md) | 30 |
| [Brumel Shield — privacy and security](features/shield.md) | 39 |
| [Brumel Nano — local AI](features/nano.md) | 30 |
| [Brumel Connect — continuity between devices](features/connect.md) | 28 |
| [Brumel Tools — media and everyday utilities](features/tools.md) | 39 |
| [Personalization and interface](features/interface.md) | 21 |
| [Brumel Dev — developers](features/dev.md) | 17 |

## The 52 research proposals

Each of the 52 proposals from the product research appears exactly once in the catalog. They are proposals to evaluate, not commitments: many are Research or Experimental, and none is assumed to be unique to Brumel.

| Proposal | ID | Name | Module | Tier | Status | Phase |
| --- | --- | --- | --- | --- | --- | --- |
| R52-01 | [MEM-019](features/memory.md#mem-019) | Resume Cards | MEM | Flagship | Research | 4 |
| R52-02 | [MEM-020](features/memory.md#mem-020) | Universal Undo | MEM | Flagship | Planned | 3 |
| R52-03 | [MEM-021](features/memory.md#mem-021) | Copy with Source | MEM | Secondary | Planned | 3 |
| R52-04 | [MEM-022](features/memory.md#mem-022) | Page Change History | MEM | Secondary | Research | 4 |
| R52-05 | [MEM-023](features/memory.md#mem-023) | Page Watchers | MEM | Flagship | Research | 4 |
| R52-06 | [MEM-024](features/memory.md#mem-024) | Dead Link Recovery | MEM | Secondary | Research | 4 |
| R52-07 | [MEM-025](features/memory.md#mem-025) | Receipt Vault | MEM | Secondary | Research | 4 |
| R52-08 | [MEM-026](features/memory.md#mem-026) | Already Searched | MEM | Secondary | Research | 4 |
| R52-09 | [MEM-027](features/memory.md#mem-027) | Video Search | MEM | Experimental | Research | 4 |
| R52-10 | [WRK-031](features/workspace.md#wrk-031) | Tab Snooze | WRK | Secondary | Planned | 3 |
| R52-11 | [WRK-032](features/workspace.md#wrk-032) | Reading Queue | WRK | Secondary | Planned | 3 |
| R52-12 | [WRK-033](features/workspace.md#wrk-033) | Intent Anchor | WRK | Experimental | Research | 4 |
| R52-13 | [WRK-034](features/workspace.md#wrk-034) | Infinite Scroll Brake | WRK | Experimental | Research | 4 |
| R52-14 | [WRK-035](features/workspace.md#wrk-035) | Spaced Highlights | WRK | Experimental | Research | 4 |
| R52-15 | [WRK-036](features/workspace.md#wrk-036) | Quiet Inbox | WRK | Secondary | Research | 4 |
| R52-16 | [SHD-030](features/shield.md#shd-030) | Dark Pattern Radar | SHD | Experimental | Research | 4 |
| R52-17 | [TLS-029](features/tools.md#tls-029) | Subscription Radar | TLS | Secondary | Research | 4 |
| R52-18 | [MEM-028](features/memory.md#mem-028) | Session Guardian | MEM | Secondary | Research | 3 |
| R52-19 | [MEM-029](features/memory.md#mem-029) | Login Memory | MEM | Flagship | Planned | 3 |
| R52-20 | [SHD-031](features/shield.md#shd-031) | User Rights | SHD | Secondary | Planned | 3 |
| R52-21 | [TLS-030](features/tools.md#tls-030) | Tables to Data | TLS | Secondary | Planned | 3 |
| R52-22 | [TLS-031](features/tools.md#tls-031) | Selection Actions | TLS | Secondary | Planned | 3 |
| R52-23 | [TLS-032](features/tools.md#tls-032) | My Search Results | TLS | Secondary | Research | 4 |
| R52-24 | [SHD-032](features/shield.md#shd-032) | Guaranteed Exit | SHD | Secondary | Planned | 3 |
| R52-25 | [TLS-033](features/tools.md#tls-033) | Smart Upload | TLS | Flagship | Planned | 3 |
| R52-26 | [TLS-034](features/tools.md#tls-034) | Local File Workshop | TLS | Secondary | Research | 4 |
| R52-27 | [TLS-035](features/tools.md#tls-035) | Live Text | TLS | Secondary | Research | 4 |
| R52-28 | [TLS-036](features/tools.md#tls-036) | Universal Local Dictation | TLS | Secondary | Research | 4 |
| R52-29 | [TLS-037](features/tools.md#tls-037) | Chrome Coexistence | TLS | Secondary | Planned | 3 |
| R52-30 | [UI-020](features/interface.md#ui-020) | Progressive Discovery | UI | Essential | Planned | 3 |
| R52-31 | [MEM-030](features/memory.md#mem-030) | Exit Freedom | MEM | Essential | Planned | 3 |
| R52-32 | [CON-027](features/connect.md#con-027) | Pocket Profile | CON | Experimental | Research | 6 |
| R52-33 | [UI-021](features/interface.md#ui-021) | Configuration Recipes | UI | Community | Research | 4 |
| R52-34 | [SHD-034](features/shield.md#shd-034) | Glass Box | SHD | Flagship | Planned | 3 |
| R52-35 | [ENG-046](features/engine.md#eng-046) | Built-in Benchmark | ENG | Flagship | Planned | 3 |
| R52-36 | [WRK-037](features/workspace.md#wrk-037) | Web App Dock | WRK | Secondary | Planned | 4 |
| R52-37 | [SHD-033](features/shield.md#shd-033) | Screen Share Shield | SHD | Secondary | Research | 4 |
| R52-38 | [WRK-038](features/workspace.md#wrk-038) | System Search Integration | WRK | Experimental | Research | 4 |
| R52-39 | [TLS-038](features/tools.md#tls-038) | Destinations | TLS | Experimental | Research | 4 |
| R52-40 | [CON-026](features/connect.md#con-026) | Mobile Upload | CON | Secondary | Research | 4 |
| R52-41 | [TLS-039](features/tools.md#tls-039) | Quick Tab Recording | TLS | Secondary | Research | 4 |
| R52-42 | [SHD-035](features/shield.md#shd-035) | Extension Passport | SHD | Flagship | Planned | 3 |
| R52-43 | [SHD-036](features/shield.md#shd-036) | Credential Sentinel | SHD | Experimental | Research | 4 |
| R52-44 | [SHD-037](features/shield.md#shd-037) | Agent Clean Room | SHD | Deferred | Research | 6 |
| R52-45 | [SHD-038](features/shield.md#shd-038) | Verified Downloads | SHD | Secondary | Research | 4 |
| R52-46 | [CON-028](features/connect.md#con-028) | Trusted Remote Help | CON | Experimental | Research | 6 |
| R52-47 | [SHD-039](features/shield.md#shd-039) | Hardened Sessions | SHD | Experimental | Research | 4 |
| R52-48 | [ENG-041](features/engine.md#eng-041) | Efficient Video | ENG | Secondary | Research | 3 |
| R52-49 | [ENG-042](features/engine.md#eng-042) | Per-Site Resource Limits | ENG | Flagship | Planned | 3 |
| R52-50 | [ENG-043](features/engine.md#eng-043) | Instant Startup | ENG | Flagship | Planned | 2 |
| R52-51 | [ENG-044](features/engine.md#eng-044) | On-Demand Extensions | ENG | Flagship | Planned | 3 |
| R52-52 | [ENG-045](features/engine.md#eng-045) | Idle Scheduler | ENG | Essential | Planned | 2 |

## Feature index

| ID | Name | Module | Tier | Status | Priority | Phase |
| --- | --- | --- | --- | --- | --- | --- |
| [CORE-001](features/core.md#core-001) | Reproducible upstream fetch | CORE | Essential | Planned | P0 | 1 |
| [CORE-002](features/core.md#core-002) | Patch series system | CORE | Essential | Planned | P0 | 1 |
| [CORE-003](features/core.md#core-003) | Upstream release tracking automation | CORE | Essential | Planned | P0 | 1 |
| [CORE-004](features/core.md#core-004) | Brumel branding | CORE | Essential | Planned | P0 | 1 |
| [CORE-005](features/core.md#core-005) | Module system and feature registry | CORE | Essential | Planned | P0 | 1 |
| [CORE-006](features/core.md#core-006) | De-Googling and Google API audit | CORE | Essential | Planned | P0 | 1 |
| [CORE-007](features/core.md#core-007) | CI build and release signing pipeline | CORE | Essential | Planned | P0 | 1 |
| [CORE-008](features/core.md#core-008) | SBOM and dependency governance | CORE | Essential | Planned | P1 | 1 |
| [CORE-009](features/core.md#core-009) | Windows installer packaging | CORE | Essential | Planned | P0 | 1 |
| [CORE-010](features/core.md#core-010) | Linux packaging | CORE | Essential | Planned | P1 | 1 |
| [CORE-011](features/core.md#core-011) | Crash reporting without Google | CORE | Secondary | Research | P1 | 2 |
| [CORE-012](features/core.md#core-012) | Safe Browsing service strategy | CORE | Essential | Research | P0 | 2 |
| [CORE-013](features/core.md#core-013) | Translation backend replacement | CORE | Secondary | Research | P2 | 4 |
| [CORE-014](features/core.md#core-014) | Spellcheck dictionary hosting | CORE | Essential | Planned | P1 | 2 |
| [CORE-020](features/core.md#core-020) | Modern web navigation | CORE | Essential | Planned | P0 | 2 |
| [CORE-021](features/core.md#core-021) | Web standards compatibility | CORE | Essential | Planned | P0 | 2 |
| [CORE-022](features/core.md#core-022) | Chrome Web Store and extensions | CORE | Essential | Planned | P0 | 2 |
| [CORE-023](features/core.md#core-023) | Password manager | CORE | Essential | Planned | P0 | 2 |
| [CORE-024](features/core.md#core-024) | Passkeys | CORE | Essential | Planned | P1 | 2 |
| [CORE-025](features/core.md#core-025) | Autofill | CORE | Essential | Planned | P1 | 2 |
| [CORE-026](features/core.md#core-026) | User profiles | CORE | Essential | Planned | P0 | 2 |
| [CORE-027](features/core.md#core-027) | Incognito mode | CORE | Essential | Planned | P0 | 2 |
| [CORE-028](features/core.md#core-028) | Guest mode | CORE | Essential | Planned | P2 | 2 |
| [CORE-029](features/core.md#core-029) | Bookmarks | CORE | Essential | Planned | P0 | 2 |
| [CORE-030](features/core.md#core-030) | History | CORE | Essential | Planned | P0 | 2 |
| [CORE-031](features/core.md#core-031) | Downloads | CORE | Essential | Planned | P0 | 2 |
| [CORE-032](features/core.md#core-032) | Tab groups | CORE | Essential | Planned | P1 | 2 |
| [CORE-033](features/core.md#core-033) | Pinned tabs | CORE | Essential | Planned | P1 | 2 |
| [CORE-034](features/core.md#core-034) | Page translation | CORE | Essential | Planned | P2 | 4 |
| [CORE-035](features/core.md#core-035) | DevTools | CORE | Essential | Planned | P0 | 2 |
| [CORE-036](features/core.md#core-036) | Progressive Web Apps | CORE | Essential | Planned | P1 | 2 |
| [CORE-037](features/core.md#core-037) | PDF viewer | CORE | Essential | Planned | P0 | 2 |
| [CORE-038](features/core.md#core-038) | Printing | CORE | Essential | Planned | P0 | 2 |
| [CORE-039](features/core.md#core-039) | Spellcheck | CORE | Essential | Planned | P1 | 2 |
| [CORE-040](features/core.md#core-040) | Graphics acceleration | CORE | Essential | Planned | P0 | 2 |
| [CORE-041](features/core.md#core-041) | Hardware media decoding | CORE | Essential | Planned | P0 | 2 |
| [CORE-042](features/core.md#core-042) | Picture-in-Picture | CORE | Essential | Planned | P1 | 2 |
| [CORE-043](features/core.md#core-043) | Screenshots | CORE | Essential | Planned | P2 | 2 |
| [CORE-044](features/core.md#core-044) | Data import and export | CORE | Essential | Planned | P0 | 2 |
| [CORE-045](features/core.md#core-045) | Permission management | CORE | Essential | Planned | P0 | 2 |
| [CORE-046](features/core.md#core-046) | Secure DNS (DNS over HTTPS) | CORE | Essential | Planned | P0 | 1 |
| [CORE-047](features/core.md#core-047) | HTTPS-First / HTTPS-Only | CORE | Essential | Planned | P0 | 1 |
| [CORE-048](features/core.md#core-048) | Sandboxing | CORE | Essential | Planned | P0 | 1 |
| [CORE-049](features/core.md#core-049) | Site isolation | CORE | Essential | Planned | P0 | 1 |
| [CORE-050](features/core.md#core-050) | Phishing and malware protection | CORE | Essential | Planned | P0 | 2 |
| [CORE-051](features/core.md#core-051) | Signed automatic updates | CORE | Essential | Planned | P0 | 1 |
| [CORE-052](features/core.md#core-052) | Chromecast / Cast | CORE | Essential | Planned | P3 | 4 |
| [CORE-053](features/core.md#core-053) | DRM (Widevine) | CORE | Essential | Research | P1 | 3 |
| [CORE-054](features/core.md#core-054) | Proprietary codecs | CORE | Essential | Research | P1 | 2 |
| [CORE-055](features/core.md#core-055) | Disable sandbox or site isolation to reduce memory | CORE | Rejected | Rejected | P3 | 0 |
| [CORE-056](features/core.md#core-056) | Electron-based browser shell | CORE | Rejected | Rejected | P3 | 0 |
| [ENG-001](features/engine.md#eng-001) | Smart Performance | ENG | Flagship | Planned | P1 | 3 |
| [ENG-002](features/engine.md#eng-002) | Adaptive Engine *(→ ENG-001)* | ENG | Flagship | Planned | P1 | 3 |
| [ENG-003](features/engine.md#eng-003) | Smart Gaming Mode | ENG | Secondary | Research | P2 | 3 |
| [ENG-004](features/engine.md#eng-004) | Hardware Intelligence | ENG | Essential | Planned | P1 | 2 |
| [ENG-005](features/engine.md#eng-005) | RAM Budget | ENG | Flagship | Planned | P1 | 3 |
| [ENG-006](features/engine.md#eng-006) | CPU Budget | ENG | Secondary | Planned | P2 | 3 |
| [ENG-007](features/engine.md#eng-007) | Network Optimizer | ENG | Secondary | Research | P3 | 3 |
| [ENG-008](features/engine.md#eng-008) | Smart Preload | ENG | Secondary | Planned | P2 | 3 |
| [ENG-009](features/engine.md#eng-009) | Thermal Guard | ENG | Secondary | Research | P2 | 3 |
| [ENG-010](features/engine.md#eng-010) | Battery Forecast | ENG | Experimental | Research | P3 | 4 |
| [ENG-011](features/engine.md#eng-011) | Low-End Mode | ENG | Flagship | Planned | P1 | 2 |
| [ENG-012](features/engine.md#eng-012) | Performance History | ENG | Secondary | Planned | P2 | 3 |
| [ENG-013](features/engine.md#eng-013) | Extension Doctor | ENG | Flagship | Planned | P1 | 3 |
| [ENG-014](features/engine.md#eng-014) | Crash Shield | ENG | Secondary | Planned | P1 | 2 |
| [ENG-015](features/engine.md#eng-015) | Browser Health | ENG | Flagship | Planned | P1 | 3 |
| [ENG-016](features/engine.md#eng-016) | Update Guard | ENG | Essential | Planned | P1 | 2 |
| [ENG-017](features/engine.md#eng-017) | OLED Protection | ENG | Secondary | Planned | P3 | 4 |
| [ENG-018](features/engine.md#eng-018) | Smart Optimize | ENG | Flagship | Planned | P1 | 3 |
| [ENG-019](features/engine.md#eng-019) | Smart tab suspension | ENG | Essential | Planned | P0 | 2 |
| [ENG-020](features/engine.md#eng-020) | On-demand memory release | ENG | Secondary | Planned | P2 | 2 |
| [ENG-021](features/engine.md#eng-021) | Deferred startup loading *(→ ENG-043)* | ENG | Flagship | Planned | P1 | 2 |
| [ENG-022](features/engine.md#eng-022) | Active tab prioritization | ENG | Essential | Planned | P1 | 2 |
| [ENG-023](features/engine.md#eng-023) | Background tab frame-rate limit | ENG | Secondary | Planned | P2 | 2 |
| [ENG-024](features/engine.md#eng-024) | Background timer throttling | ENG | Essential | Planned | P1 | 2 |
| [ENG-025](features/engine.md#eng-025) | GPU preference | ENG | Secondary | Research | P2 | 3 |
| [ENG-026](features/engine.md#eng-026) | Media playback control | ENG | Secondary | Planned | P2 | 3 |
| [ENG-027](features/engine.md#eng-027) | Efficient hardware decoding *(→ ENG-041)* | ENG | Secondary | Research | P2 | 3 |
| [ENG-028](features/engine.md#eng-028) | Adaptive extension management *(→ ENG-044)* | ENG | Flagship | Planned | P1 | 3 |
| [ENG-029](features/engine.md#eng-029) | Process count reduction | ENG | Secondary | Research | P2 | 3 |
| [ENG-030](features/engine.md#eng-030) | Startup optimization *(→ ENG-043)* | ENG | Flagship | Planned | P1 | 2 |
| [ENG-031](features/engine.md#eng-031) | Advanced resource monitor | ENG | Essential | Planned | P1 | 2 |
| [ENG-032](features/engine.md#eng-032) | Energy saver mode *(→ ENG-033)* | ENG | Essential | Planned | P1 | 2 |
| [ENG-033](features/engine.md#eng-033) | Performance profiles (Performance, Balanced, Battery Saver) | ENG | Essential | Planned | P1 | 2 |
| [ENG-034](features/engine.md#eng-034) | Gaming profile *(→ ENG-003)* | ENG | Secondary | Research | P2 | 3 |
| [ENG-035](features/engine.md#eng-035) | Streaming profile | ENG | Secondary | Planned | P3 | 3 |
| [ENG-036](features/engine.md#eng-036) | Developer profile | ENG | Secondary | Planned | P3 | 3 |
| [ENG-037](features/engine.md#eng-037) | Focus profile | ENG | Secondary | Planned | P3 | 4 |
| [ENG-038](features/engine.md#eng-038) | AI profile | ENG | Experimental | Research | P3 | 4 |
| [ENG-039](features/engine.md#eng-039) | Custom profiles | ENG | Secondary | Planned | P2 | 3 |
| [ENG-040](features/engine.md#eng-040) | Automatic profiles and custom rules | ENG | Flagship | Planned | P2 | 3 |
| [ENG-041](features/engine.md#eng-041) | Efficient Video | ENG | Secondary | Research | P2 | 3 |
| [ENG-042](features/engine.md#eng-042) | Per-Site Resource Limits | ENG | Flagship | Planned | P2 | 3 |
| [ENG-043](features/engine.md#eng-043) | Instant Startup | ENG | Flagship | Planned | P1 | 2 |
| [ENG-044](features/engine.md#eng-044) | On-Demand Extensions | ENG | Flagship | Planned | P1 | 3 |
| [ENG-045](features/engine.md#eng-045) | Idle Scheduler | ENG | Essential | Planned | P0 | 2 |
| [ENG-046](features/engine.md#eng-046) | Built-in Benchmark | ENG | Flagship | Planned | P2 | 3 |
| [WRK-001](features/workspace.md#wrk-001) | Horizontal and vertical tabs | WRK | Essential | Planned | P0 | 2 |
| [WRK-002](features/workspace.md#wrk-002) | Tab trees | WRK | Secondary | Planned | P2 | 3 |
| [WRK-003](features/workspace.md#wrk-003) | Folders and subfolders | WRK | Secondary | Planned | P2 | 3 |
| [WRK-004](features/workspace.md#wrk-004) | Workspaces | WRK | Flagship | Planned | P1 | 4 |
| [WRK-005](features/workspace.md#wrk-005) | Pinned and temporary tabs *(→ WRK-013)* | WRK | Secondary | Planned | P2 | 3 |
| [WRK-006](features/workspace.md#wrk-006) | Split view | WRK | Flagship | Planned | P1 | 3 |
| [WRK-007](features/workspace.md#wrk-007) | Floating link preview | WRK | Secondary | Planned | P2 | 3 |
| [WRK-008](features/workspace.md#wrk-008) | Infinite Tabs | WRK | Flagship | Planned | P1 | 3 |
| [WRK-009](features/workspace.md#wrk-009) | Smart Router | WRK | Flagship | Planned | P2 | 4 |
| [WRK-010](features/workspace.md#wrk-010) | Multi Identity | WRK | Flagship | Planned | P1 | 4 |
| [WRK-011](features/workspace.md#wrk-011) | Temporary Identity | WRK | Secondary | Planned | P2 | 4 |
| [WRK-012](features/workspace.md#wrk-012) | Private Spaces | WRK | Secondary | Planned | P2 | 4 |
| [WRK-013](features/workspace.md#wrk-013) | Temporary Tabs | WRK | Secondary | Planned | P2 | 3 |
| [WRK-014](features/workspace.md#wrk-014) | Tab DNA | WRK | Experimental | Research | P3 | 4 |
| [WRK-015](features/workspace.md#wrk-015) | Live Collections | WRK | Experimental | Research | P3 | 4 |
| [WRK-016](features/workspace.md#wrk-016) | Smart Bookmarks | WRK | Secondary | Planned | P2 | 4 |
| [WRK-017](features/workspace.md#wrk-017) | Universal Search | WRK | Flagship | Planned | P1 | 3 |
| [WRK-018](features/workspace.md#wrk-018) | Quick Actions | WRK | Flagship | Planned | P1 | 3 |
| [WRK-019](features/workspace.md#wrk-019) | Search across all tabs *(→ WRK-017)* | WRK | Flagship | Planned | P1 | 3 |
| [WRK-020](features/workspace.md#wrk-020) | Local-AI automatic tab grouping | WRK | Secondary | Research | P2 | 4 |
| [WRK-021](features/workspace.md#wrk-021) | Smart archiving | WRK | Essential | Planned | P1 | 3 |
| [WRK-022](features/workspace.md#wrk-022) | Duplicate tab detection | WRK | Secondary | Planned | P2 | 3 |
| [WRK-023](features/workspace.md#wrk-023) | Session recovery | WRK | Essential | Planned | P0 | 2 |
| [WRK-024](features/workspace.md#wrk-024) | Named saved sessions | WRK | Secondary | Planned | P2 | 3 |
| [WRK-025](features/workspace.md#wrk-025) | Web side panels | WRK | Secondary | Planned | P2 | 3 |
| [WRK-026](features/workspace.md#wrk-026) | Focus Mode | WRK | Secondary | Planned | P2 | 3 |
| [WRK-027](features/workspace.md#wrk-027) | Research Mode | WRK | Experimental | Research | P3 | 4 |
| [WRK-028](features/workspace.md#wrk-028) | Web Highlights | WRK | Secondary | Planned | P2 | 4 |
| [WRK-029](features/workspace.md#wrk-029) | Smart Compare | WRK | Experimental | Research | P3 | 4 |
| [WRK-030](features/workspace.md#wrk-030) | Visual no-code rules engine | WRK | Flagship | Planned | P2 | 4 |
| [WRK-031](features/workspace.md#wrk-031) | Tab Snooze | WRK | Secondary | Planned | P2 | 3 |
| [WRK-032](features/workspace.md#wrk-032) | Reading Queue | WRK | Secondary | Planned | P2 | 3 |
| [WRK-033](features/workspace.md#wrk-033) | Intent Anchor | WRK | Experimental | Research | P3 | 4 |
| [WRK-034](features/workspace.md#wrk-034) | Infinite Scroll Brake | WRK | Experimental | Research | P3 | 4 |
| [WRK-035](features/workspace.md#wrk-035) | Spaced Highlights | WRK | Experimental | Research | P3 | 4 |
| [WRK-036](features/workspace.md#wrk-036) | Quiet Inbox | WRK | Secondary | Research | P2 | 4 |
| [WRK-037](features/workspace.md#wrk-037) | Web App Dock | WRK | Secondary | Planned | P2 | 4 |
| [WRK-038](features/workspace.md#wrk-038) | System Search Integration | WRK | Experimental | Research | P3 | 4 |
| [MEM-001](features/memory.md#mem-001) | Browser Time Machine | MEM | Flagship | Planned | P1 | 3 |
| [MEM-002](features/memory.md#mem-002) | Smart Memory | MEM | Flagship | Research | P2 | 4 |
| [MEM-003](features/memory.md#mem-003) | Offline Vault | MEM | Secondary | Planned | P2 | 4 |
| [MEM-004](features/memory.md#mem-004) | Draft Protection | MEM | Flagship | Planned | P1 | 3 |
| [MEM-005](features/memory.md#mem-005) | Download Vault | MEM | Secondary | Planned | P2 | 3 |
| [MEM-006](features/memory.md#mem-006) | Zero Loss | MEM | Flagship | Planned | P1 | 3 |
| [MEM-007](features/memory.md#mem-007) | Session and workspace history *(→ MEM-001)* | MEM | Flagship | Planned | P1 | 3 |
| [MEM-008](features/memory.md#mem-008) | Restore closed windows *(→ MEM-006)* | MEM | Flagship | Planned | P1 | 3 |
| [MEM-009](features/memory.md#mem-009) | Reading position recovery | MEM | Secondary | Planned | P2 | 3 |
| [MEM-010](features/memory.md#mem-010) | Media playback position recovery | MEM | Secondary | Research | P3 | 4 |
| [MEM-011](features/memory.md#mem-011) | Local backups | MEM | Essential | Planned | P1 | 3 |
| [MEM-012](features/memory.md#mem-012) | Settings history | MEM | Secondary | Planned | P2 | 3 |
| [MEM-013](features/memory.md#mem-013) | Non-destructive restore | MEM | Essential | Planned | P1 | 3 |
| [MEM-014](features/memory.md#mem-014) | Brumel Store and local index | MEM | Essential | Planned | P0 | 2 |
| [MEM-015](features/memory.md#mem-015) | Semantic and text search *(→ MEM-002)* | MEM | Flagship | Research | P2 | 4 |
| [MEM-016](features/memory.md#mem-016) | Memory export and import *(→ MEM-030)* | MEM | Essential | Planned | P1 | 3 |
| [MEM-017](features/memory.md#mem-017) | Configurable local activity journal | MEM | Experimental | Research | P3 | 4 |
| [MEM-018](features/memory.md#mem-018) | Incognito and sensitive-site exclusion | MEM | Essential | Planned | P0 | 2 |
| [MEM-019](features/memory.md#mem-019) | Resume Cards | MEM | Flagship | Research | P2 | 4 |
| [MEM-020](features/memory.md#mem-020) | Universal Undo | MEM | Flagship | Planned | P1 | 3 |
| [MEM-021](features/memory.md#mem-021) | Copy with Source | MEM | Secondary | Planned | P2 | 3 |
| [MEM-022](features/memory.md#mem-022) | Page Change History | MEM | Secondary | Research | P3 | 4 |
| [MEM-023](features/memory.md#mem-023) | Page Watchers | MEM | Flagship | Research | P2 | 4 |
| [MEM-024](features/memory.md#mem-024) | Dead Link Recovery | MEM | Secondary | Research | P3 | 4 |
| [MEM-025](features/memory.md#mem-025) | Receipt Vault | MEM | Secondary | Research | P2 | 4 |
| [MEM-026](features/memory.md#mem-026) | Already Searched | MEM | Secondary | Research | P3 | 4 |
| [MEM-027](features/memory.md#mem-027) | Video Search | MEM | Experimental | Research | P3 | 4 |
| [MEM-028](features/memory.md#mem-028) | Session Guardian | MEM | Secondary | Research | P2 | 3 |
| [MEM-029](features/memory.md#mem-029) | Login Memory | MEM | Flagship | Planned | P2 | 3 |
| [MEM-030](features/memory.md#mem-030) | Exit Freedom | MEM | Essential | Planned | P1 | 3 |
| [SHD-001](features/shield.md#shd-001) | Clean Web native content blocking | SHD | Flagship | Planned | P0 | 2 |
| [SHD-002](features/shield.md#shd-002) | Pop-up blocking | SHD | Essential | Planned | P0 | 2 |
| [SHD-003](features/shield.md#shd-003) | Autoplay blocking | SHD | Essential | Planned | P1 | 2 |
| [SHD-004](features/shield.md#shd-004) | Automated optional-cookie rejection | SHD | Flagship | Research | P1 | 3 |
| [SHD-005](features/shield.md#shd-005) | Notification prompt blocking | SHD | Essential | Planned | P1 | 2 |
| [SHD-006](features/shield.md#shd-006) | Fingerprinting protection | SHD | Flagship | Research | P1 | 3 |
| [SHD-007](features/shield.md#shd-007) | Tracking parameter stripping | SHD | Essential | Planned | P1 | 2 |
| [SHD-008](features/shield.md#shd-008) | Malicious redirect protection | SHD | Secondary | Planned | P2 | 3 |
| [SHD-009](features/shield.md#shd-009) | Smart Back | SHD | Secondary | Planned | P2 | 3 |
| [SHD-010](features/shield.md#shd-010) | Self Repair | SHD | Secondary | Research | P2 | 3 |
| [SHD-011](features/shield.md#shd-011) | Permission Timeline | SHD | Secondary | Planned | P2 | 3 |
| [SHD-012](features/shield.md#shd-012) | One-Time Permissions | SHD | Essential | Planned | P1 | 3 |
| [SHD-013](features/shield.md#shd-013) | Extension Firewall | SHD | Flagship | Planned | P1 | 3 |
| [SHD-014](features/shield.md#shd-014) | Privacy Receipt | SHD | Secondary | Planned | P2 | 3 |
| [SHD-015](features/shield.md#shd-015) | Smart Cleanup | SHD | Secondary | Planned | P2 | 3 |
| [SHD-016](features/shield.md#shd-016) | Link Inspector | SHD | Secondary | Planned | P2 | 3 |
| [SHD-017](features/shield.md#shd-017) | Clipboard Guard | SHD | Secondary | Planned | P2 | 3 |
| [SHD-018](features/shield.md#shd-018) | Settings Lock *(→ ENG-016)* | SHD | Essential | Planned | P1 | 2 |
| [SHD-019](features/shield.md#shd-019) | Biometric lock | SHD | Secondary | Planned | P2 | 4 |
| [SHD-020](features/shield.md#shd-020) | Local data encryption | SHD | Essential | Planned | P1 | 2 |
| [SHD-021](features/shield.md#shd-021) | End-to-end encrypted sync *(→ CON-020)* | SHD | Essential | Research | P0 | 4 |
| [SHD-022](features/shield.md#shd-022) | Credential protection | SHD | Essential | Planned | P1 | 3 |
| [SHD-023](features/shield.md#shd-023) | DNS over HTTPS (Shield) *(→ CORE-046)* | SHD | Essential | Planned | P0 | 1 |
| [SHD-024](features/shield.md#shd-024) | HTTPS-only mode (Shield) *(→ CORE-047)* | SHD | Essential | Planned | P0 | 1 |
| [SHD-025](features/shield.md#shd-025) | Session isolation *(→ WRK-010)* | SHD | Flagship | Planned | P1 | 4 |
| [SHD-026](features/shield.md#shd-026) | Phishing protection (Shield) *(→ CORE-050)* | SHD | Essential | Planned | P0 | 2 |
| [SHD-027](features/shield.md#shd-027) | Optional, auditable telemetry | SHD | Essential | Planned | P1 | 3 |
| [SHD-028](features/shield.md#shd-028) | Advanced private mode | SHD | Secondary | Research | P2 | 4 |
| [SHD-029](features/shield.md#shd-029) | Tor integration | SHD | Deferred | Deferred | P3 | 6 |
| [SHD-030](features/shield.md#shd-030) | Dark Pattern Radar | SHD | Experimental | Research | P3 | 4 |
| [SHD-031](features/shield.md#shd-031) | User Rights | SHD | Secondary | Planned | P2 | 3 |
| [SHD-032](features/shield.md#shd-032) | Guaranteed Exit | SHD | Secondary | Planned | P2 | 3 |
| [SHD-033](features/shield.md#shd-033) | Screen Share Shield | SHD | Secondary | Research | P2 | 4 |
| [SHD-034](features/shield.md#shd-034) | Glass Box | SHD | Flagship | Planned | P1 | 3 |
| [SHD-035](features/shield.md#shd-035) | Extension Passport | SHD | Flagship | Planned | P1 | 3 |
| [SHD-036](features/shield.md#shd-036) | Credential Sentinel | SHD | Experimental | Research | P2 | 4 |
| [SHD-037](features/shield.md#shd-037) | Agent Clean Room | SHD | Deferred | Research | P3 | 6 |
| [SHD-038](features/shield.md#shd-038) | Verified Downloads | SHD | Secondary | Research | P2 | 4 |
| [SHD-039](features/shield.md#shd-039) | Hardened Sessions | SHD | Experimental | Research | P2 | 4 |
| [NANO-001](features/nano.md#nano-001) | Nano runtime (sandboxed local inference) | NANO | Flagship | Research | P1 | 4 |
| [NANO-002](features/nano.md#nano-002) | Model component manager | NANO | Essential | Research | P1 | 4 |
| [NANO-003](features/nano.md#nano-003) | On-demand load and idle unload | NANO | Essential | Research | P1 | 4 |
| [NANO-004](features/nano.md#nano-004) | Hardware-adaptive backends | NANO | Essential | Research | P2 | 4 |
| [NANO-005](features/nano.md#nano-005) | Power-aware auto-disable | NANO | Essential | Research | P1 | 4 |
| [NANO-006](features/nano.md#nano-006) | Model evaluation program | NANO | Essential | Research | P1 | 0 |
| [NANO-007](features/nano.md#nano-007) | Untrusted-content boundary | NANO | Essential | Research | P0 | 4 |
| [NANO-008](features/nano.md#nano-008) | AI tab grouping *(→ WRK-020)* | NANO | Secondary | Research | P2 | 4 |
| [NANO-009](features/nano.md#nano-009) | Page classification | NANO | Secondary | Research | P2 | 4 |
| [NANO-010](features/nano.md#nano-010) | Group naming | NANO | Secondary | Research | P3 | 4 |
| [NANO-011](features/nano.md#nano-011) | Workspace organization suggestions | NANO | Experimental | Research | P3 | 4 |
| [NANO-012](features/nano.md#nano-012) | Semantic search (Nano) *(→ MEM-002)* | NANO | Flagship | Research | P2 | 4 |
| [NANO-013](features/nano.md#nano-013) | Information retrieval *(→ MEM-002)* | NANO | Flagship | Research | P2 | 4 |
| [NANO-014](features/nano.md#nano-014) | Tagging | NANO | Secondary | Research | P3 | 4 |
| [NANO-015](features/nano.md#nano-015) | Structured extraction (dates, amounts) | NANO | Secondary | Research | P2 | 4 |
| [NANO-016](features/nano.md#nano-016) | Download classification | NANO | Secondary | Research | P3 | 4 |
| [NANO-017](features/nano.md#nano-017) | Command routing | NANO | Experimental | Research | P3 | 4 |
| [NANO-018](features/nano.md#nano-018) | Spelling and grammar correction | NANO | Experimental | Research | P3 | 4 |
| [NANO-019](features/nano.md#nano-019) | Local translation models | NANO | Secondary | Research | P2 | 4 |
| [NANO-020](features/nano.md#nano-020) | Local OCR | NANO | Secondary | Research | P2 | 4 |
| [NANO-021](features/nano.md#nano-021) | Local speech recognition | NANO | Secondary | Research | P2 | 4 |
| [NANO-022](features/nano.md#nano-022) | Captions (Nano) *(→ TLS-013)* | NANO | Secondary | Research | P2 | 4 |
| [NANO-023](features/nano.md#nano-023) | Extractive summaries | NANO | Secondary | Research | P2 | 4 |
| [NANO-024](features/nano.md#nano-024) | Generative summaries | NANO | Experimental | Research | P3 | 4 |
| [NANO-025](features/nano.md#nano-025) | Optional cloud AI providers (BYOK) | NANO | Secondary | Research | P3 | 4 |
| [NANO-026](features/nano.md#nano-026) | Ollama and OpenAI-compatible endpoints | NANO | Secondary | Research | P3 | 4 |
| [NANO-027](features/nano.md#nano-027) | API key storage | NANO | Essential | Research | P3 | 4 |
| [NANO-028](features/nano.md#nano-028) | Small-model security decisions | NANO | Rejected | Rejected | P3 | 0 |
| [NANO-029](features/nano.md#nano-029) | Autonomous agents on small models | NANO | Rejected | Rejected | P3 | 0 |
| [NANO-030](features/nano.md#nano-030) | Unverified AI factual comparisons | NANO | Rejected | Rejected | P3 | 0 |
| [CON-001](features/connect.md#con-001) | Smart Continuity | CON | Flagship | Research | P1 | 4 |
| [CON-002](features/connect.md#con-002) | Device Mesh | CON | Experimental | Research | P2 | 4 |
| [CON-003](features/connect.md#con-003) | Quick Share | CON | Secondary | Research | P2 | 4 |
| [CON-004](features/connect.md#con-004) | Send tab to device | CON | Essential | Research | P1 | 4 |
| [CON-005](features/connect.md#con-005) | Bookmark sync | CON | Essential | Research | P1 | 4 |
| [CON-006](features/connect.md#con-006) | Workspace sync | CON | Flagship | Research | P1 | 4 |
| [CON-007](features/connect.md#con-007) | Preferences sync | CON | Essential | Research | P2 | 4 |
| [CON-008](features/connect.md#con-008) | Rules sync | CON | Secondary | Research | P2 | 4 |
| [CON-009](features/connect.md#con-009) | Optional history sync | CON | Secondary | Research | P2 | 4 |
| [CON-010](features/connect.md#con-010) | Optional extension sync | CON | Secondary | Research | P3 | 4 |
| [CON-011](features/connect.md#con-011) | Clipboard sync | CON | Experimental | Research | P3 | 4 |
| [CON-012](features/connect.md#con-012) | Reading continuity | CON | Secondary | Research | P3 | 4 |
| [CON-013](features/connect.md#con-013) | QR pairing | CON | Essential | Research | P1 | 4 |
| [CON-014](features/connect.md#con-014) | Incremental sync | CON | Essential | Research | P1 | 4 |
| [CON-015](features/connect.md#con-015) | Conflict management | CON | Essential | Research | P1 | 4 |
| [CON-016](features/connect.md#con-016) | Offline operation | CON | Essential | Research | P0 | 4 |
| [CON-017](features/connect.md#con-017) | Encrypted backups (remote) | CON | Secondary | Research | P2 | 4 |
| [CON-018](features/connect.md#con-018) | Self-hosting | CON | Flagship | Research | P1 | 4 |
| [CON-019](features/connect.md#con-019) | Password sync | CON | Deferred | Deferred | P2 | 5 |
| [CON-020](features/connect.md#con-020) | Client-side E2EE layer | CON | Essential | Research | P0 | 4 |
| [CON-021](features/connect.md#con-021) | Hosted relay candidate (Supabase Free / PostgreSQL) | CON | Experimental | Research | P2 | 4 |
| [CON-022](features/connect.md#con-022) | WebRTC transport | CON | Experimental | Research | P2 | 4 |
| [CON-023](features/connect.md#con-023) | Encrypted blob relay | CON | Essential | Research | P1 | 4 |
| [CON-024](features/connect.md#con-024) | Docker self-hosted server *(→ CON-018)* | CON | Flagship | Research | P1 | 4 |
| [CON-025](features/connect.md#con-025) | No-account local mode guarantee | CON | Essential | Planned | P0 | 2 |
| [CON-026](features/connect.md#con-026) | Mobile Upload | CON | Secondary | Research | P2 | 4 |
| [CON-027](features/connect.md#con-027) | Pocket Profile | CON | Experimental | Research | P3 | 6 |
| [CON-028](features/connect.md#con-028) | Trusted Remote Help | CON | Experimental | Research | P3 | 6 |
| [TLS-001](features/tools.md#tls-001) | Smart Downloads | TLS | Secondary | Planned | P2 | 3 |
| [TLS-002](features/tools.md#tls-002) | Advanced download manager | TLS | Secondary | Planned | P2 | 3 |
| [TLS-003](features/tools.md#tls-003) | Parallel downloads | TLS | Experimental | Research | P3 | 3 |
| [TLS-004](features/tools.md#tls-004) | Resumable downloads | TLS | Essential | Planned | P1 | 3 |
| [TLS-005](features/tools.md#tls-005) | Download speed limiter | TLS | Secondary | Planned | P3 | 3 |
| [TLS-006](features/tools.md#tls-006) | Universal PiP | TLS | Secondary | Planned | P2 | 4 |
| [TLS-007](features/tools.md#tls-007) | Audio Mixer | TLS | Flagship | Planned | P2 | 4 |
| [TLS-008](features/tools.md#tls-008) | Equalizer | TLS | Secondary | Research | P3 | 4 |
| [TLS-009](features/tools.md#tls-009) | Volume boost | TLS | Secondary | Research | P3 | 4 |
| [TLS-010](features/tools.md#tls-010) | Media speed control | TLS | Secondary | Planned | P2 | 4 |
| [TLS-011](features/tools.md#tls-011) | Cinema mode | TLS | Secondary | Planned | P3 | 4 |
| [TLS-012](features/tools.md#tls-012) | GPU video enhancement | TLS | Experimental | Research | P3 | 4 |
| [TLS-013](features/tools.md#tls-013) | Live Captions | TLS | Secondary | Research | P2 | 4 |
| [TLS-014](features/tools.md#tls-014) | Subtitle translation | TLS | Experimental | Research | P3 | 4 |
| [TLS-015](features/tools.md#tls-015) | Tab recording | TLS | Secondary | Research | P2 | 4 |
| [TLS-016](features/tools.md#tls-016) | Full-page screenshots | TLS | Secondary | Planned | P2 | 3 |
| [TLS-017](features/tools.md#tls-017) | Basic PDF editor | TLS | Secondary | Research | P3 | 4 |
| [TLS-018](features/tools.md#tls-018) | Smart Reader | TLS | Secondary | Planned | P2 | 3 |
| [TLS-019](features/tools.md#tls-019) | Text-to-speech reading | TLS | Secondary | Research | P2 | 4 |
| [TLS-020](features/tools.md#tls-020) | Distraction Cleaner | TLS | Secondary | Planned | P2 | 3 |
| [TLS-021](features/tools.md#tls-021) | Website Profiles | TLS | Secondary | Planned | P2 | 3 |
| [TLS-022](features/tools.md#tls-022) | Accessibility Studio | TLS | Flagship | Planned | P1 | 4 |
| [TLS-023](features/tools.md#tls-023) | Fonts and contrast options *(→ TLS-022)* | TLS | Flagship | Planned | P1 | 4 |
| [TLS-024](features/tools.md#tls-024) | Reduced visual stimuli *(→ TLS-022)* | TLS | Flagship | Planned | P1 | 4 |
| [TLS-025](features/tools.md#tls-025) | Adapted reading options *(→ TLS-022)* | TLS | Flagship | Planned | P1 | 4 |
| [TLS-026](features/tools.md#tls-026) | Meeting Mode | TLS | Secondary | Planned | P2 | 4 |
| [TLS-027](features/tools.md#tls-027) | Migration Assistant | TLS | Flagship | Planned | P0 | 3 |
| [TLS-028](features/tools.md#tls-028) | Mouse and trackpad gestures | TLS | Secondary | Planned | P3 | 4 |
| [TLS-029](features/tools.md#tls-029) | Subscription Radar | TLS | Secondary | Research | P2 | 4 |
| [TLS-030](features/tools.md#tls-030) | Tables to Data | TLS | Secondary | Planned | P2 | 3 |
| [TLS-031](features/tools.md#tls-031) | Selection Actions | TLS | Secondary | Planned | P2 | 3 |
| [TLS-032](features/tools.md#tls-032) | My Search Results | TLS | Secondary | Research | P2 | 4 |
| [TLS-033](features/tools.md#tls-033) | Smart Upload | TLS | Flagship | Planned | P1 | 3 |
| [TLS-034](features/tools.md#tls-034) | Local File Workshop | TLS | Secondary | Research | P2 | 4 |
| [TLS-035](features/tools.md#tls-035) | Live Text | TLS | Secondary | Research | P2 | 4 |
| [TLS-036](features/tools.md#tls-036) | Universal Local Dictation | TLS | Secondary | Research | P2 | 4 |
| [TLS-037](features/tools.md#tls-037) | Chrome Coexistence | TLS | Secondary | Planned | P2 | 3 |
| [TLS-038](features/tools.md#tls-038) | Destinations | TLS | Experimental | Research | P3 | 4 |
| [TLS-039](features/tools.md#tls-039) | Quick Tab Recording *(→ TLS-015)* | TLS | Secondary | Research | P2 | 4 |
| [UI-001](features/interface.md#ui-001) | Modern minimalist design | UI | Essential | Planned | P0 | 2 |
| [UI-002](features/interface.md#ui-002) | Mica and transparency | UI | Secondary | Research | P3 | 4 |
| [UI-003](features/interface.md#ui-003) | Dark and light mode | UI | Essential | Planned | P0 | 2 |
| [UI-004](features/interface.md#ui-004) | OLED black theme *(→ ENG-017)* | UI | Secondary | Planned | P3 | 4 |
| [UI-005](features/interface.md#ui-005) | Accent colors | UI | Secondary | Planned | P3 | 4 |
| [UI-006](features/interface.md#ui-006) | Dynamic themes | UI | Experimental | Research | P3 | 4 |
| [UI-007](features/interface.md#ui-007) | Advanced theme editor | UI | Secondary | Research | P3 | 4 |
| [UI-008](features/interface.md#ui-008) | Controlled CSS customization | UI | Experimental | Research | P3 | 6 |
| [UI-009](features/interface.md#ui-009) | Community theme store | UI | Community | Deferred | P3 | 6 |
| [UI-010](features/interface.md#ui-010) | Customizable sidebar | UI | Secondary | Planned | P2 | 3 |
| [UI-011](features/interface.md#ui-011) | Compact mode | UI | Secondary | Planned | P2 | 3 |
| [UI-012](features/interface.md#ui-012) | Hide UI elements | UI | Secondary | Planned | P2 | 3 |
| [UI-013](features/interface.md#ui-013) | Configurable animations | UI | Secondary | Planned | P3 | 3 |
| [UI-014](features/interface.md#ui-014) | Reduced motion | UI | Essential | Planned | P1 | 2 |
| [UI-015](features/interface.md#ui-015) | Custom shortcuts | UI | Secondary | Planned | P2 | 3 |
| [UI-016](features/interface.md#ui-016) | Command palette *(→ WRK-018)* | UI | Flagship | Planned | P1 | 3 |
| [UI-017](features/interface.md#ui-017) | Touch support | UI | Secondary | Planned | P2 | 3 |
| [UI-018](features/interface.md#ui-018) | Familiar default layout | UI | Essential | Planned | P0 | 2 |
| [UI-019](features/interface.md#ui-019) | Progressive disclosure | UI | Essential | Planned | P1 | 3 |
| [UI-020](features/interface.md#ui-020) | Progressive Discovery *(→ UI-019)* | UI | Essential | Planned | P1 | 3 |
| [UI-021](features/interface.md#ui-021) | Configuration Recipes | UI | Community | Research | P3 | 4 |
| [DEV-001](features/dev.md#dev-001) | REST API client | DEV | Secondary | Deferred | P3 | 6 |
| [DEV-002](features/dev.md#dev-002) | WebSocket client | DEV | Secondary | Deferred | P3 | 6 |
| [DEV-003](features/dev.md#dev-003) | JSON viewer and editor | DEV | Secondary | Planned | P3 | 4 |
| [DEV-004](features/dev.md#dev-004) | Storage viewer | DEV | Secondary | Deferred | P3 | 6 |
| [DEV-005](features/dev.md#dev-005) | Network diagnostics | DEV | Secondary | Deferred | P3 | 6 |
| [DEV-006](features/dev.md#dev-006) | Per-workspace proxies | DEV | Secondary | Research | P2 | 4 |
| [DEV-007](features/dev.md#dev-007) | Mobile emulation *(→ CORE-035)* | DEV | Essential | Planned | P0 | 2 |
| [DEV-008](features/dev.md#dev-008) | Development auto-reload | DEV | Secondary | Deferred | P3 | 6 |
| [DEV-009](features/dev.md#dev-009) | Performance audit *(→ CORE-035)* | DEV | Essential | Planned | P0 | 2 |
| [DEV-010](features/dev.md#dev-010) | Custom scripts (userscripts) | DEV | Deferred | Deferred | P3 | 6 |
| [DEV-011](features/dev.md#dev-011) | GitHub integration | DEV | Experimental | Research | P3 | 6 |
| [DEV-012](features/dev.md#dev-012) | Playwright automation | DEV | Deferred | Deferred | P3 | 6 |
| [DEV-013](features/dev.md#dev-013) | MCP integration | DEV | Deferred | Deferred | P3 | 6 |
| [DEV-014](features/dev.md#dev-014) | Homelab Mode | DEV | Experimental | Deferred | P3 | 6 |
| [DEV-015](features/dev.md#dev-015) | Self-hosted service management | DEV | Experimental | Deferred | P3 | 6 |
| [DEV-016](features/dev.md#dev-016) | Local certificates | DEV | Secondary | Research | P3 | 6 |
| [DEV-017](features/dev.md#dev-017) | Local terminal | DEV | Deferred | Deferred | P3 | 6 |
