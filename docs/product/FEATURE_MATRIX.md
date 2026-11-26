# Feature Matrix

> **Snapshot as of 2026-11. To be verified.** This matrix compares the **out-of-the-box desktop builds** of other
> browsers with Brumel's **targets**. Brumel is in pre-development: its column shows the *planned status* from the
> [feature catalog](FEATURES.md), never "Yes". Competitor cells come from vendor documentation, release notes and
> press coverage; cells we could not confirm are marked `?`. Corrections with sources are welcome through a
> *Documentation* issue.

## Why this matrix exists

Brumel's thesis is that people should not have to choose between Chrome's compatibility, Brave's privacy,
Vivaldi's power-user tools, Arc's and Zen's organization, Edge's efficiency features, Opera GX's resource controls,
Firefox's session isolation, Safari's simplicity and Helium's lightness. This page shows where each browser stands
today, so that Brumel's priorities target real gaps instead of features everyone already has.

It also keeps us honest in the other direction: many things Brumel wants are already in upstream Chromium
(native vertical tabs and Split View landed in Chrome in 2026, as reported below). For those, Brumel's job is to
inherit and refine, not to rebuild.

## Legend

| Symbol | Meaning |
| --- | --- |
| **Yes** | Built in and enabled or available in settings by default. |
| **Partial** | Built in but limited in scope, platform or default configuration (see notes). |
| **Ext** | Only through a first- or third-party extension. |
| **No** | Not available. |
| **?** | Unknown or not verified for this snapshot. |
| **N/A** | Not applicable. |

Brumel column values are catalog statuses: **Planned**, **Research**, **Deferred**, **Inherited** (Planned via upstream Chromium).

## Browsers compared

| Browser | Engine | Source model | Desktop platforms | Notes |
| --- | --- | --- | --- | --- |
| Chrome | Blink (Chromium) | Proprietary build of open-source Chromium | Windows, macOS, Linux | Reference for compatibility; Google services integrated. |
| Edge | Blink (Chromium) | Proprietary | Windows, macOS, Linux | Microsoft services; efficiency features (sleeping tabs). |
| Brave | Blink (Chromium) | Open source (MPL-2.0) | Windows, macOS, Linux | Native blocking (Shields), adblock-rust. |
| Vivaldi | Blink (Chromium) | Partly open (Chromium changes published; UI proprietary) | Windows, macOS, Linux | Power-user UI, built-in blocker. |
| Opera GX | Blink (Chromium) | Proprietary | Windows, macOS | Gaming-oriented resource limiters (GX Control). |
| Firefox | Gecko | Open source (MPL-2.0) | Windows, macOS, Linux | Containers, local translations. |
| Safari | WebKit | Proprietary app on open-source WebKit | macOS only (desktop) | Intelligent Tracking Prevention. |
| Zen | Gecko (Firefox-based) | Open source (MPL-2.0) | Windows, macOS, Linux | Arc-like layout on Firefox. |
| Arc | Blink (Chromium) | Proprietary | macOS, Windows | **Maintenance mode** — see note below. |
| Helium | Blink (Chromium, ungoogled-chromium based) | Open source (GPL-3.0) | Windows, macOS, Linux | Lightweight, privacy-oriented; very frequent releases. |
| Thorium | Blink (Chromium) | Open source (BSD-3-Clause) | Windows, macOS, Linux | Performance-tuned build flags; has lagged upstream majors (see [CHROMIUM_BASES](../research/CHROMIUM_BASES.md)). |
| **Brumel** | Blink (Chromium) | Open source (MPL-2.0 + BSD-3-Clause patches) | Windows, Linux (macOS Deferred) | Pre-development. |

**Arc status note.** The Browser Company announced in May 2025 that Arc would receive no new features while it focused
on Dia, and Atlassian completed its acquisition of The Browser Company in October 2025. Third-party reports from
October 2026 state that the company announced an Arc sunset for 2026-12-22; we have not verified this against
the company's own announcement. Arc remains in this matrix because its ideas (Spaces, sidebar, Peek, auto-archive)
shaped user expectations.

## Matrix

### Compatibility and platform

| Capability | Chrome | Edge | Brave | Vivaldi | Opera GX | Firefox | Safari | Zen | Arc | Helium | Thorium | **Brumel** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Chromium web compatibility | Yes | Yes | Yes | Yes | Yes | N/A | N/A | N/A | Yes | Yes | Yes | Inherited ([CORE-020](features/core.md#core-020)) |
| Chrome Web Store extensions | Yes | Yes | Yes | Yes | Yes | No | No | No | Yes | Yes (?) | Yes | Inherited ([CORE-022](features/core.md#core-022)) |
| Manifest V2 extensions | No | No | Partial | No | ? | Yes | N/A | Yes | No | ? | ? | Research ([CORE-022](features/core.md#core-022)) |
| Linux build | Yes | Yes | Yes | Yes | No | Yes | No | Yes | No | Yes | Yes | Planned ([CORE-010](features/core.md#core-010)) |
| Signed automatic updates | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | ? | Partial | Planned ([CORE-051](features/core.md#core-051)) |
| Widevine DRM | Yes | Yes | Yes (opt-in) | Yes | Yes | Yes | N/A (FairPlay) | Yes | Yes | ? | ? | Research ([CORE-053](features/core.md#core-053)) |
| Works without an account | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | Yes | Yes | Planned ([CON-025](features/connect.md#con-025)) |

### Efficiency

| Capability | Chrome | Edge | Brave | Vivaldi | Opera GX | Firefox | Safari | Zen | Arc | Helium | Thorium | **Brumel** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tab discarding / sleeping | Yes | Yes | Yes | Yes | Yes | Yes | Partial | Yes | Yes | Yes | Yes | Planned ([ENG-019](features/engine.md#eng-019)) |
| Energy saver mode | Yes | Yes | Yes | ? | Yes | ? | Partial (OS) | ? | ? | Yes (?) | Yes (?) | Planned ([ENG-033](features/engine.md#eng-033)) |
| User-set RAM / CPU / network limits | No | No | No | No | Yes | No | No | No | No | No | No | Planned ([ENG-005](features/engine.md#eng-005), [ENG-006](features/engine.md#eng-006)) |
| Per-site resource policies | No | Partial | No | No | No | No | No | No | No | No | No | Planned ([ENG-042](features/engine.md#eng-042)) |
| Per-extension impact attribution | Partial (task manager) | Partial | Partial | Partial | Partial | Partial (about:processes) | No | Partial | ? | Partial | Partial | Planned ([ENG-013](features/engine.md#eng-013)) |
| Extensions limited to chosen sites by default | Partial (site access) | Partial | Partial | Partial | Partial | Partial | Partial | Partial | ? | Partial | Partial | Planned ([ENG-044](features/engine.md#eng-044)) |
| Public reproducible benchmark suite | No | No | No | No | No | No | No | No | No | No | No | Planned ([ENG-046](features/engine.md#eng-046)) |

### Organization and productivity

| Capability | Chrome | Edge | Brave | Vivaldi | Opera GX | Firefox | Safari | Zen | Arc | Helium | Thorium | **Brumel** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Native vertical tabs | Yes (since 147, reported) | Yes | Yes | Yes | ? | Yes | No | Yes | Yes | ? | ? | Planned ([WRK-001](features/workspace.md#wrk-001)) |
| Tab trees / stacks | No | No | No | Yes (stacks) | No | Ext | No | Partial | Partial (folders) | No | No | Planned ([WRK-002](features/workspace.md#wrk-002)) |
| Split view | Yes (2 panes, since 145, reported) | Yes | ? | Yes (tiling) | ? | ? | No | Yes | Yes | ? | ? | Planned ([WRK-006](features/workspace.md#wrk-006)) |
| Workspaces / spaces | No | Yes | No | Yes | ? | No | Partial (profiles, tab groups) | Yes | Yes | No | No | Planned ([WRK-004](features/workspace.md#wrk-004)) |
| Container-style identities in one window | No | No | No | No | No | Ext (official) | No | Yes | No | No | No | Planned ([WRK-010](features/workspace.md#wrk-010)) |
| Command palette | Partial (tab search) | No | No | Yes | ? | Partial | No | Partial | Yes | No | No | Planned ([WRK-018](features/workspace.md#wrk-018)) |
| Web panels / sidebar apps | Partial (side panel) | Yes | Partial | Yes | Yes | Partial | No | Yes | No | No | No | Planned ([WRK-025](features/workspace.md#wrk-025)) |
| Mouse gestures | Ext | Partial | Ext | Yes | Yes | Ext | Partial (trackpad) | Ext | Ext | Ext | Ext | Planned ([TLS-028](features/tools.md#tls-028)) |

### Memory and recovery

| Capability | Chrome | Edge | Brave | Vivaldi | Opera GX | Firefox | Safari | Zen | Arc | Helium | Thorium | **Brumel** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Session restore after crash | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Inherited + hardened ([WRK-023](features/workspace.md#wrk-023)) |
| Named saved sessions | No | No | No | Yes | ? | Ext | No | Partial | No | No | No | Planned ([WRK-024](features/workspace.md#wrk-024)) |
| Session timeline (restore any past state) | No | No | No | No | No | No | No | No | No | No | No | Planned ([MEM-001](features/memory.md#mem-001)) |
| Auto-archive instead of closing | No | No | No | No | No | No | No | Partial | Yes | No | No | Planned ([WRK-021](features/workspace.md#wrk-021)) |
| Form draft recovery | No | No | No | No | No | Partial (session form data) | No | Partial | No | No | No | Planned ([MEM-004](features/memory.md#mem-004)) |
| Local semantic history search | No | ? | No | No | No | No | No | No | No | No | No | Research ([MEM-002](features/memory.md#mem-002)) |
| Full data export in open formats | Partial | Partial | Partial | Partial | Partial | Partial | Partial | Partial | Partial | Partial | Partial | Planned ([MEM-030](features/memory.md#mem-030)) |

### Clean Web and Trust

| Capability | Chrome | Edge | Brave | Vivaldi | Opera GX | Firefox | Safari | Zen | Arc | Helium | Thorium | **Brumel** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Native ad blocking | No | No | Yes | Yes | Yes | No | No | No | ? | Yes (bundled uBlock Origin, reported) | No | Planned ([SHD-001](features/shield.md#shd-001)) |
| Native tracker blocking | Partial | Yes | Yes | Yes | Yes | Yes | Yes | Yes | ? | Yes | No | Planned ([SHD-001](features/shield.md#shd-001)) |
| Fingerprinting protection | Partial | Partial | Yes | Partial | ? | Yes | Yes | Yes | ? | Partial | No | Research ([SHD-006](features/shield.md#shd-006)) |
| Automated cookie-banner rejection | No | No | Yes | ? | ? | Partial | No | Partial | ? | ? | No | Research ([SHD-004](features/shield.md#shd-004)) |
| Tracking-parameter stripping | No | No | Yes | ? | ? | Yes | Yes | Yes | ? | ? | No | Planned ([SHD-007](features/shield.md#shd-007)) |
| One-time permissions | Yes | Yes | Yes | Yes | ? | Yes | Yes | Yes | ? | Yes | Yes | Planned ([SHD-012](features/shield.md#shd-012)) |
| Extension permission-change review | Partial | Partial | Partial | Partial | Partial | Partial | Partial | Partial | ? | Partial | Partial | Planned ([SHD-035](features/shield.md#shd-035)) |
| User-facing log of browser-initiated connections | No | No | No | No | No | No | No | No | No | No | No | Planned ([SHD-034](features/shield.md#shd-034)) |
| Telemetry off by default | No | No | ? | Yes (claimed) | No | No | ? | ? | No | Yes (claimed) | ? | Planned ([SHD-027](features/shield.md#shd-027)) |
| Phishing / malware warnings | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | ? | ? | Research ([CORE-012](features/core.md#core-012)) |

### AI, sync and tools

| Capability | Chrome | Edge | Brave | Vivaldi | Opera GX | Firefox | Safari | Zen | Arc | Helium | Thorium | **Brumel** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Built-in AI assistant | Yes (cloud + on-device APIs) | Yes (cloud) | Yes (cloud; local via BYO model) | No (by policy) | Yes (cloud) | Partial (provider sidebar) | Partial (OS-level) | ? | Partial (cloud) | No | No | Research ([NANO-001](features/nano.md#nano-001)) |
| AI fully local and optional | Partial | No | Partial | N/A | No | Partial (translations) | Partial | ? | No | N/A | N/A | Research ([NANO-001](features/nano.md#nano-001)) |
| Local page translation | Partial | No | No | No | No | Yes | Partial | Yes (Firefox) | No | No | No | Research ([NANO-019](features/nano.md#nano-019)) |
| End-to-end encrypted sync | Partial (passphrase) | No | Yes | Yes | Partial | Yes | Partial | Yes (Firefox Sync) | ? | No | ? | Research ([CON-020](features/connect.md#con-020)) |
| Self-hostable sync server | No | No | No | No | No | Partial | No | Partial | No | No | No | Research ([CON-018](features/connect.md#con-018)) |
| Per-tab volume control | No | No | No | No | Yes | No | No | No | No | No | No | Planned ([TLS-007](features/tools.md#tls-007)) |
| Reader mode | Partial (side panel) | Yes | Yes | Yes | ? | Yes | Yes | Yes | ? | Partial | Partial | Planned ([TLS-018](features/tools.md#tls-018)) |
| PDF annotation | Partial (since 145, reported) | Yes | Partial | Partial | Partial | Yes | Partial | Yes | ? | Partial | Partial | Research ([TLS-017](features/tools.md#tls-017)) |
| Upload-time image compression / metadata strip | No | No | No | No | No | No | No | No | No | No | No | Planned ([TLS-033](features/tools.md#tls-033)) |

## Reading the matrix

- **Where Brumel inherits.** Compatibility, extensions, discarding, one-time permissions, vertical tabs and Split View
  already exist upstream. Brumel's work there is preserving them through patches and extending them carefully.
- **Where gaps look real.** No mainstream browser offers a user-facing log of its own connections, session timelines,
  form-draft recovery, upload-time file processing or a public benchmark suite. These map to Brumel's Trust,
  Memory and Everyday Tools pillars. "Nobody has it" can also mean "nobody wants it": each still needs user validation.
- **Where Brumel is not ahead.** Fingerprinting protection (Brave, Firefox, Safari), E2EE sync (Firefox, Brave) and
  local translation (Firefox) are mature elsewhere. Brumel's realistic goal is parity, preferably by reusing
  open-source components with compatible licenses.

## Methodology and limitations

1. **Scope.** Default desktop builds on Windows (macOS for Safari, Arc where relevant), without extensions, as of 2026-11.
2. **Sources.** Vendor help pages and release notes first, then reputable press. Items marked *reported* rely on press
   coverage. We did not run hands-on verification for every cell in this snapshot.
3. **Granularity.** "Partial" hides real differences; the catalog entries hold the details that matter for Brumel.
4. **Change rate.** Browsers ship monthly or faster. Re-verify before quoting any cell publicly, and update the
   snapshot date when you do.
5. **No marketing use.** This matrix is a planning tool. Brumel's public comparisons will use measured data from
   [BENCHMARKS.md](../benchmarks/BENCHMARKS.md), not this table.
