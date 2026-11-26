<!-- GENERATED FILE — Do not edit by hand. Source: docs/product/catalog/*.json. Regenerate: python scripts/catalog/render_features.py -->

# Brumel Engine — performance and efficiency

> **Project status: Pre-development.** Nothing listed here is available yet. Statuses, priorities and phases are proposals. See the [catalog index and legend](../FEATURES.md#legend).

46 entries. Epics in this module:

- **EP-ENG-01** Tab lifecycle and memory management — phase 2 (Internal Alpha), P0
- **EP-ENG-02** Adaptive engine, budgets and performance profiles — phase 2 (Internal Alpha), P1
- **EP-ENG-03** Fast startup and on-demand extensions — phase 2 (Internal Alpha), P1
- **EP-ENG-04** Diagnostics: resource monitor, Browser Health and benchmark — phase 2 (Internal Alpha), P1

| ID | Name | Tier | Status | Priority | Phase |
| --- | --- | --- | --- | --- | --- |
| [ENG-001](#eng-001) | Smart Performance | Flagship | Planned | P1 | 3 |
| [ENG-002](#eng-002) | Adaptive Engine *(→ ENG-001)* | Flagship | Planned | P1 | 3 |
| [ENG-003](#eng-003) | Smart Gaming Mode | Secondary | Research | P2 | 3 |
| [ENG-004](#eng-004) | Hardware Intelligence | Essential | Planned | P1 | 2 |
| [ENG-005](#eng-005) | RAM Budget | Flagship | Planned | P1 | 3 |
| [ENG-006](#eng-006) | CPU Budget | Secondary | Planned | P2 | 3 |
| [ENG-007](#eng-007) | Network Optimizer | Secondary | Research | P3 | 3 |
| [ENG-008](#eng-008) | Smart Preload | Secondary | Planned | P2 | 3 |
| [ENG-009](#eng-009) | Thermal Guard | Secondary | Research | P2 | 3 |
| [ENG-010](#eng-010) | Battery Forecast | Experimental | Research | P3 | 4 |
| [ENG-011](#eng-011) | Low-End Mode | Flagship | Planned | P1 | 2 |
| [ENG-012](#eng-012) | Performance History | Secondary | Planned | P2 | 3 |
| [ENG-013](#eng-013) | Extension Doctor | Flagship | Planned | P1 | 3 |
| [ENG-014](#eng-014) | Crash Shield | Secondary | Planned | P1 | 2 |
| [ENG-015](#eng-015) | Browser Health | Flagship | Planned | P1 | 3 |
| [ENG-016](#eng-016) | Update Guard | Essential | Planned | P1 | 2 |
| [ENG-017](#eng-017) | OLED Protection | Secondary | Planned | P3 | 4 |
| [ENG-018](#eng-018) | Smart Optimize | Flagship | Planned | P1 | 3 |
| [ENG-019](#eng-019) | Smart tab suspension | Essential | Planned | P0 | 2 |
| [ENG-020](#eng-020) | On-demand memory release | Secondary | Planned | P2 | 2 |
| [ENG-021](#eng-021) | Deferred startup loading *(→ ENG-043)* | Flagship | Planned | P1 | 2 |
| [ENG-022](#eng-022) | Active tab prioritization | Essential | Planned | P1 | 2 |
| [ENG-023](#eng-023) | Background tab frame-rate limit | Secondary | Planned | P2 | 2 |
| [ENG-024](#eng-024) | Background timer throttling | Essential | Planned | P1 | 2 |
| [ENG-025](#eng-025) | GPU preference | Secondary | Research | P2 | 3 |
| [ENG-026](#eng-026) | Media playback control | Secondary | Planned | P2 | 3 |
| [ENG-027](#eng-027) | Efficient hardware decoding *(→ ENG-041)* | Secondary | Research | P2 | 3 |
| [ENG-028](#eng-028) | Adaptive extension management *(→ ENG-044)* | Flagship | Planned | P1 | 3 |
| [ENG-029](#eng-029) | Process count reduction | Secondary | Research | P2 | 3 |
| [ENG-030](#eng-030) | Startup optimization *(→ ENG-043)* | Flagship | Planned | P1 | 2 |
| [ENG-031](#eng-031) | Advanced resource monitor | Essential | Planned | P1 | 2 |
| [ENG-032](#eng-032) | Energy saver mode *(→ ENG-033)* | Essential | Planned | P1 | 2 |
| [ENG-033](#eng-033) | Performance profiles (Performance, Balanced, Battery Saver) | Essential | Planned | P1 | 2 |
| [ENG-034](#eng-034) | Gaming profile *(→ ENG-003)* | Secondary | Research | P2 | 3 |
| [ENG-035](#eng-035) | Streaming profile | Secondary | Planned | P3 | 3 |
| [ENG-036](#eng-036) | Developer profile | Secondary | Planned | P3 | 3 |
| [ENG-037](#eng-037) | Focus profile | Secondary | Planned | P3 | 4 |
| [ENG-038](#eng-038) | AI profile | Experimental | Research | P3 | 4 |
| [ENG-039](#eng-039) | Custom profiles | Secondary | Planned | P2 | 3 |
| [ENG-040](#eng-040) | Automatic profiles and custom rules | Flagship | Planned | P2 | 3 |
| [ENG-041](#eng-041) | Efficient Video | Secondary | Research | P2 | 3 |
| [ENG-042](#eng-042) | Per-Site Resource Limits | Flagship | Planned | P2 | 3 |
| [ENG-043](#eng-043) | Instant Startup | Flagship | Planned | P1 | 2 |
| [ENG-044](#eng-044) | On-Demand Extensions | Flagship | Planned | P1 | 3 |
| [ENG-045](#eng-045) | Idle Scheduler | Essential | Planned | P0 | 2 |
| [ENG-046](#eng-046) | Built-in Benchmark | Flagship | Planned | P2 | 3 |

<a id="eng-001"></a>

## ENG-001 — Smart Performance

`Flagship` · `Planned` · **P1** · Impact High · Complexity L · Phase 3 (Public Alpha) · Pillar Efficiency · Epic EP-ENG-02 (Adaptive engine, budgets and performance profiles)

Central policy engine that adapts background activity, preloading and tab lifecycle to the machine's current state (load, battery, thermals, memory pressure).

- **Problem:** Browsers behave the same on a busy, hot, battery-powered laptop as on an idle desktop.
- **Use case:** While a user renders video on battery, Brumel automatically throttles background tabs and pauses preloading.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-004](#eng-004), [CORE-005](core.md#core-005)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Policy decisions are logged locally and explainable
  - Measured background CPU reduction vs Balanced baseline under load
  - Every automatic action is reversible
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Policies are heuristics; wrong guesses (throttling a tab the user cares about) erode trust, so every automatic action must be visible and reversible, which limits how aggressive it can be.

<a id="eng-002"></a>

## ENG-002 — Adaptive Engine

`Flagship` · `Planned` · **P1** · Impact High · Complexity L · Phase 3 (Public Alpha) · Pillar Efficiency · Epic EP-ENG-02 (Adaptive engine, budgets and performance profiles)

Tracked together with ENG-001 (Smart Performance).

- **Problem:** Browsers behave the same on a busy, hot, battery-powered laptop as on an idle desktop.
- **Use case:** Automatically tune CPU, memory and energy use without user configuration.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-001](#eng-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of ENG-001
  - Use case verified: Automatically tune CPU, memory and energy use without user configuration.
- **Origin:** A · **Duplicate of:** [ENG-001](#eng-001)
- **Limitations / notes:** Technical duplicate merged into ENG-001; kept as its own entry to preserve the use case and traceability.

<a id="eng-003"></a>

## ENG-003 — Smart Gaming Mode

`Secondary` · `Research` · **P2** · Impact Medium · Complexity M · Phase 3 (Public Alpha) · Pillar Efficiency · Epic EP-ENG-02 (Adaptive engine, budgets and performance profiles)

Detect fullscreen games (OS game mode signals, fullscreen exclusive apps) and reduce browser background activity.

- **Problem:** Background browser tabs steal CPU/GPU and cause stutter in games.
- **Use case:** A user starts a game; Brumel suspends background tabs and limits video tabs until the game exits.
- **Segments:** Gamers & streamers
- **Dependencies:** [ENG-001](#eng-001)
- **Platforms:** Windows Planned · Linux Research · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Medium — must not log which games are played.
- **Competitors / precedents:** Opera GX
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Detection works via documented OS signals only (no process scanning beyond what is necessary)
  - Measured frame-time impact in benchmark
  - User can exclude tabs (e.g. voice chat)
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Reliable game detection needs OS signals (fullscreen exclusive, Windows Game Mode) that are not exposed uniformly; it will not detect windowed or Linux games consistently.

<a id="eng-004"></a>

## ENG-004 — Hardware Intelligence

`Essential` · `Planned` · **P1** · Impact High · Complexity M · Phase 2 (Internal Alpha) · Pillar Efficiency · Epic EP-ENG-02 (Adaptive engine, budgets and performance profiles)

Local detection of CPU, GPU/iGPU, NPU, RAM, display and power capabilities to drive defaults and Nano backend selection.

- **Problem:** One-size-fits-all defaults are wrong for both 4 GB laptops and workstations.
- **Use case:** On first run, Brumel picks Low-End Mode defaults on a 4 GB machine.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [CORE-005](core.md#core-005)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Capability snapshot visible in an internal page
  - No hardware data leaves the device
  - Detection fails safely to conservative defaults
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** NPU and thermal capabilities are exposed differently by each vendor driver; detection will be incomplete on Linux and may report capabilities that drivers cannot actually use.

<a id="eng-005"></a>

## ENG-005 — RAM Budget

`Flagship` · `Planned` · **P1** · Impact High · Complexity L · Phase 3 (Public Alpha) · Pillar Efficiency · Epic EP-ENG-02 (Adaptive engine, budgets and performance profiles)

Global and per-workspace memory budgets enforced through tab discarding, freezing and cache trimming.

- **Problem:** Browsers grow until the OS starts swapping.
- **Use case:** A user sets a 4 GB budget; when exceeded, least-recently-used tabs are discarded first, never the active or audible ones.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-019](#eng-019), [ENG-004](#eng-004)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: 20–40% RAM reduction is a target to verify, not a result.
- **Acceptance criteria:**
  - Budget enforcement keeps measured browser memory near target in the 100-tab benchmark
  - Protected tabs are never discarded
  - User sees what was discarded and why
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** The browser cannot force renderers below their working set; a budget is enforced by discarding tabs, so very low budgets mean frequent reloads rather than magic savings.

<a id="eng-006"></a>

## ENG-006 — CPU Budget

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity M · Phase 3 (Public Alpha) · Pillar Efficiency · Epic EP-ENG-02 (Adaptive engine, budgets and performance profiles)

Limits for background tab and extension CPU usage with targets per profile.

- **Problem:** Background scripts and extensions waste CPU and battery.
- **Use case:** A user caps background activity; a runaway background tab gets frozen.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-024](#eng-024), [ENG-001](#eng-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Background CPU above threshold triggers throttle/freeze
  - Visible in resource monitor
  - Exceptions per site
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Throttling cannot limit work inside a foreground tab without breaking it; CPU budgets only apply to background tabs, extensions and Brumel's own tasks.

<a id="eng-007"></a>

## ENG-007 — Network Optimizer

`Secondary` · `Research` · **P3** · Impact Low · Complexity M · Phase 3 (Public Alpha) · Pillar Efficiency · Epic EP-ENG-02 (Adaptive engine, budgets and performance profiles)

Prioritize foreground navigation over background downloads, preloads and sync that the browser controls.

- **Problem:** Background traffic slows the page the user is waiting for.
- **Use case:** During a large download, the active page still loads quickly.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-001](#eng-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Only browser-controlled traffic is prioritized
  - Measured foreground load time under background download
  - No OS-level traffic shaping
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** The browser cannot shape other applications' traffic.

<a id="eng-008"></a>

## ENG-008 — Smart Preload

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity M · Phase 3 (Public Alpha) · Pillar Efficiency · Epic EP-ENG-01 (Tab lifecycle and memory management)

Speculative preloading (Speculation Rules, preconnect) only when resources, battery and network permit.

- **Problem:** Preloading speeds navigation but wastes data and battery when constrained.
- **Use case:** On AC power with spare memory, a likely next page is prerendered; on battery it is not.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-001](#eng-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Medium — prefetch must not leak to third parties beyond Chromium's protections.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Preload disabled under Battery Saver, metered networks and memory pressure
  - Measured navigation gains in benchmark
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Speculative loading leaks intent to destination sites and can be wasteful; benefits depend on prediction accuracy, which must be measured per scenario.

<a id="eng-009"></a>

## ENG-009 — Thermal Guard

`Secondary` · `Research` · **P2** · Impact Medium · Complexity M · Phase 3 (Public Alpha) · Pillar Efficiency · Epic EP-ENG-02 (Adaptive engine, budgets and performance profiles)

Reduce background activity when OS thermal-state signals report throttling.

- **Problem:** Hot laptops throttle and become noisy while the browser keeps working in the background.
- **Use case:** On a hot laptop, background video tabs are paused and preloading stops.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-004](#eng-004)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Uses OS thermal APIs where available
  - No-op where signals are absent
  - Documented per platform
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Thermal signal availability differs by OS and hardware; Linux support is Research.

<a id="eng-010"></a>

## ENG-010 — Battery Forecast

`Experimental` · `Research` · **P3** · Impact Low · Complexity M · Phase 4 (Public Beta) · Pillar Efficiency · Epic EP-ENG-02 (Adaptive engine, budgets and performance profiles)

Estimate the battery impact of open tabs and settings, only where measurements are reliable.

- **Problem:** Users cannot tell which tabs drain their battery.
- **Use case:** A user sees that a video-conference tab is the main battery consumer.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-012](#eng-012)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Research: per-tab energy attribution is imprecise; may be rejected if not reliable.
- **Acceptance criteria:**
  - Shown only when estimation error is validated within a published bound
  - Otherwise hidden
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Per-tab energy attribution relies on CPU time estimates and lacks accurate GPU/network energy data; if estimates cannot meet a published error bound the feature will be rejected.

<a id="eng-011"></a>

## ENG-011 — Low-End Mode

`Flagship` · `Planned` · **P1** · Impact High · Complexity M · Phase 2 (Internal Alpha) · Pillar Efficiency · Epic EP-ENG-01 (Tab lifecycle and memory management)

Defaults tuned for 4–8 GB machines: aggressive discarding, fewer animations, limited preloading, lighter UI.

- **Problem:** Modern browsers are painful on modest hardware still common in schools and homes.
- **Use case:** A student on a 4 GB laptop can keep 20 tabs without system swapping.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-004](#eng-004), [ENG-019](#eng-019)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Auto-suggested on detected low-memory hardware
  - Benchmarked on 4 GB and 8 GB tiers
  - Fully reversible
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Low-end defaults trade reload frequency and visual polish for memory; on 4 GB machines the OS itself consumes much of the RAM, so expectations must stay modest.

<a id="eng-012"></a>

## ENG-012 — Performance History

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity S · Phase 3 (Public Alpha) · Pillar Efficiency · Epic EP-ENG-04 (Diagnostics: resource monitor, Browser Health and benchmark)

Local timeline of browser CPU, memory and energy usage with top consumers.

- **Problem:** Users cannot see whether the browser got slower over time or why.
- **Use case:** A user sees memory usage spiked every afternoon when a dashboard tab is open.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-031](#eng-031), [MEM-014](memory.md#mem-014)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Data stored locally with retention limit
  - Clearable
  - Sampling overhead measured
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Continuous sampling has its own overhead and storage cost; history is coarse-grained by design and is not a profiler.

<a id="eng-013"></a>

## ENG-013 — Extension Doctor

`Flagship` · `Planned` · **P1** · Impact High · Complexity M · Phase 3 (Public Alpha) · Pillar Efficiency · Epic EP-ENG-03 (Fast startup and on-demand extensions)

Attribute CPU, memory, network and crash impact to individual extensions and suggest disabling or limiting them.

- **Problem:** Users blame the browser when an extension is the cause of slowness.
- **Use case:** A user learns one extension adds 300 ms to every page load and restricts it to specific sites.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-031](#eng-031)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Chrome (task manager), Edge
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Per-extension resource attribution shown
  - One-click disable / site restriction
  - Attribution method documented
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Chromium does not fully attribute work done by content scripts inside page renderers to extensions; attribution will be approximate for injected scripts.

<a id="eng-014"></a>

## ENG-014 — Crash Shield

`Secondary` · `Planned` · **P1** · Impact High · Complexity M · Phase 2 (Internal Alpha) · Pillar Efficiency · Epic EP-ENG-04 (Diagnostics: resource monitor, Browser Health and benchmark)

Detect crash loops (GPU process, extensions, renderer) and recover with safe defaults while preserving sessions.

- **Problem:** A crash loop after an update or bad extension can lock users out of their browser.
- **Use case:** After repeated GPU crashes, Brumel restarts with GPU acceleration disabled and explains why.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [WRK-023](workspace.md#wrk-023)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Crash loops detected and mitigated
  - Session preserved
  - User informed with a revert option
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Safe-mode fallbacks (disabling GPU acceleration, extensions) reduce functionality; detection cannot distinguish every crash cause and may need user confirmation.

<a id="eng-015"></a>

## ENG-015 — Browser Health

`Flagship` · `Planned` · **P1** · Impact High · Complexity M · Phase 3 (Public Alpha) · Pillar Efficiency · Epic EP-ENG-04 (Diagnostics: resource monitor, Browser Health and benchmark)

Diagnostic page combining resource use, extension impact, crash history, storage size and settings anomalies with suggested fixes.

- **Problem:** Users have no single place to understand why their browser misbehaves.
- **Use case:** A user opens Browser Health and sees that a huge cache and two extensions explain slow startup.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-013](#eng-013), [ENG-031](#eng-031), [ENG-014](#eng-014)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Each finding has an explanation and reversible fix
  - Works offline
  - No data leaves the device
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Diagnostics can explain common causes only; problems from OS drivers, antivirus injection or network issues will often be out of reach and must be reported as such.

<a id="eng-016"></a>

## ENG-016 — Update Guard

`Essential` · `Planned` · **P1** · Impact High · Complexity M · Phase 2 (Internal Alpha) · Pillar Trust · Epic EP-ENG-04 (Diagnostics: resource monitor, Browser Health and benchmark)

Protect user preferences, sessions and Brumel settings across updates; detect and roll back unexpected changes.

- **Problem:** Browser updates sometimes reset settings or re-enable features users turned off.
- **Use case:** After an update, a user's disabled features stay disabled and their session is intact.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [CORE-051](core.md#core-051)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Settings diff before/after update is recorded
  - Unexpected resets are reported
  - Upgrade tests cover preference persistence
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Some upstream changes intentionally reset or migrate preferences (security fixes, deprecated settings); Update Guard must respect those and can only report, not block, them.

<a id="eng-017"></a>

## ENG-017 — OLED Protection

`Secondary` · `Planned` · **P3** · Impact Low · Complexity S · Phase 4 (Public Beta) · Pillar Efficiency · Epic EP-ENG-02 (Adaptive engine, budgets and performance profiles)

Pure-black theme and optional dimming/shift of static UI elements to reduce OLED burn-in risk.

- **Problem:** Static UI on OLED displays can cause burn-in over time.
- **Use case:** An OLED laptop user enables pure black and auto-hiding toolbars.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [UI-003](interface.md#ui-003)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Opera GX, Vivaldi
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Pure black (#000) theme available
  - Static elements can auto-hide
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Pure-black UI does not protect web content itself, and pixel shifting is limited to browser chrome; real burn-in prevention depends on the OS and panel firmware.

<a id="eng-018"></a>

## ENG-018 — Smart Optimize

`Flagship` · `Planned` · **P1** · Impact High · Complexity M · Phase 3 (Public Alpha) · Pillar Efficiency · Epic EP-ENG-04 (Diagnostics: resource monitor, Browser Health and benchmark)

One-click analysis of open tabs and extensions that proposes optimizations (discard, archive, dedupe) and lets the user undo them.

- **Problem:** Users with many tabs do not know which ones cost resources.
- **Use case:** A user clicks Optimize, sees a preview of 40 tabs to archive and 3 duplicates, and applies it.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-019](#eng-019), [WRK-022](workspace.md#wrk-022), [MEM-020](memory.md#mem-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Preview before action
  - Single undo restores everything
  - Savings measured and shown honestly
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Savings shown are estimates until measured; aggressive suggestions risk discarding tabs with unsaved state, so protected-tab rules from ENG-019 are mandatory.

<a id="eng-019"></a>

## ENG-019 — Smart tab suspension

`Essential` · `Planned` · **P0** · Impact Critical · Complexity M · Phase 2 (Internal Alpha) · Pillar Efficiency · Epic EP-ENG-01 (Tab lifecycle and memory management)

Tab freezing and discarding policies with protections (audio, forms, pinned, WebRTC, user exceptions).

- **Problem:** Background tabs keep using memory and CPU.
- **Use case:** A user with 80 tabs has only recently used ones loaded; others restore on click with scroll position.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [CORE-005](core.md#core-005)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge (Sleeping tabs), Chrome (Memory Saver), Vivaldi, Opera GX
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Tabs with unsaved form input, audio or calls are protected
  - Discarded tabs restore state
  - Per-site exceptions
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Discarded tabs reload on activation and may lose ephemeral page state that sites do not persist; some web apps (chat, music) need exceptions to keep working.

<a id="eng-020"></a>

## ENG-020 — On-demand memory release

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity S · Phase 2 (Internal Alpha) · Pillar Efficiency · Epic EP-ENG-01 (Tab lifecycle and memory management)

Manual action to release memory: discard background tabs, trim caches, unload idle modules (e.g. Nano).

- **Problem:** Users need memory back immediately before launching a heavy app.
- **Use case:** Before starting a game, a user clicks Free memory and sees the released amount.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-019](#eng-019)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Released memory measured and displayed
  - Active and protected tabs untouched
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Freed memory may be quickly reclaimed by active tabs or the OS cache; the number shown is the browser's reduction, not guaranteed free system RAM.

<a id="eng-021"></a>

## ENG-021 — Deferred startup loading

`Flagship` · `Planned` · **P1** · Impact High · Complexity M · Phase 2 (Internal Alpha) · Pillar Efficiency · Epic EP-ENG-03 (Fast startup and on-demand extensions)

Tracked together with ENG-043 (Instant Startup).

- **Problem:** Restoring large sessions makes startup slow and spikes CPU.
- **Use case:** Load only the active tab at startup; restore others lazily.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-043](#eng-043)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of ENG-043
  - Use case verified: Load only the active tab at startup; restore others lazily.
- **Origin:** A · **Duplicate of:** [ENG-043](#eng-043)
- **Limitations / notes:** Technical duplicate merged into ENG-043; kept as its own entry to preserve the use case and traceability.

<a id="eng-022"></a>

## ENG-022 — Active tab prioritization

`Essential` · `Planned` · **P1** · Impact High · Complexity S · Phase 2 (Internal Alpha) · Pillar Efficiency · Epic EP-ENG-01 (Tab lifecycle and memory management)

Ensure foreground tab and UI get CPU/GPU/network priority over background work.

- **Problem:** Background activity makes the visible page feel slow.
- **Use case:** Typing in the active tab stays responsive while background tabs load.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-019](#eng-019)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Input latency in active tab measured under background load
  - No regression vs upstream
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Prioritization works within Chromium's scheduler; it cannot preempt OS-level contention from other applications.

<a id="eng-023"></a>

## ENG-023 — Background tab frame-rate limit

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity S · Phase 2 (Internal Alpha) · Pillar Efficiency · Epic EP-ENG-01 (Tab lifecycle and memory management)

Limit animation/rendering frame rate of visible-but-not-focused tabs and windows (e.g. split view, other monitors).

- **Problem:** Animations in secondary windows consume GPU and battery.
- **Use case:** A dashboard on a second monitor renders at a lower frame rate.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-022](#eng-022)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Configurable limit
  - Not applied to video playback or user-excluded sites
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Frame-rate limits can make legitimate dashboards or canvas apps look janky; must be off for video, games and user-excluded sites.

<a id="eng-024"></a>

## ENG-024 — Background timer throttling

`Essential` · `Planned` · **P1** · Impact High · Complexity S · Phase 2 (Internal Alpha) · Pillar Efficiency · Epic EP-ENG-01 (Tab lifecycle and memory management)

Stronger JavaScript timer throttling for background tabs beyond upstream defaults, with site exceptions.

- **Problem:** Background pages wake the CPU frequently, preventing idle power states.
- **Use case:** A user's 30 background tabs no longer wake the CPU every few milliseconds.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-019](#eng-019)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Idle wakeups measured in benchmark
  - Exceptions for calls, music, notifications
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Stronger throttling breaks sites relying on background timers (alarms, trading, monitoring); exceptions are required and upstream already throttles heavily, limiting extra gains.

<a id="eng-025"></a>

## ENG-025 — GPU preference

`Secondary` · `Research` · **P2** · Impact Medium · Complexity S · Phase 3 (Public Alpha) · Pillar Efficiency · Epic EP-ENG-02 (Adaptive engine, budgets and performance profiles)

Choose integrated or discrete GPU for the browser where the OS allows it.

- **Problem:** Using the discrete GPU for browsing drains laptop batteries.
- **Use case:** A laptop user sets the browser to prefer the integrated GPU on battery.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-004](#eng-004)
- **Platforms:** Windows Planned · Linux Research · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Uses OS GPU preference APIs
  - Documented per OS
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Mostly controlled by the OS; the browser can only request a preference.

<a id="eng-026"></a>

## ENG-026 — Media playback control

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity S · Phase 3 (Public Alpha) · Pillar Efficiency · Epic EP-ENG-01 (Tab lifecycle and memory management)

Policies for background media: pause hidden autoplaying video, limit background video decoding.

- **Problem:** Muted background videos keep decoding and draining battery.
- **Use case:** A hidden tab's muted video is paused until the tab is shown.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-019](#eng-019)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Hidden muted video pauses
  - Audio playback never interrupted without user policy
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Pausing hidden media can conflict with sites that expect continuous playback (live streams, background music videos); must never interrupt audible playback without policy.

<a id="eng-027"></a>

## ENG-027 — Efficient hardware decoding

`Secondary` · `Research` · **P2** · Impact Medium · Complexity M · Phase 3 (Public Alpha) · Pillar Efficiency · Epic EP-ENG-02 (Adaptive engine, budgets and performance profiles)

Tracked together with ENG-041 (Efficient Video). Inherited decoding is CORE-041.

- **Problem:** Software-decoded AV1/VP9 on unsupported hardware drains batteries quickly.
- **Use case:** Prefer hardware-decodable codecs and paths for lower power use.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-041](#eng-041)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of ENG-041
  - Use case verified: Prefer hardware-decodable codecs and paths for lower power use.
- **Origin:** A · **Duplicate of:** [ENG-041](#eng-041)
- **Limitations / notes:** Technical duplicate merged into ENG-041; kept as its own entry to preserve the use case and traceability.

<a id="eng-028"></a>

## ENG-028 — Adaptive extension management

`Flagship` · `Planned` · **P1** · Impact High · Complexity M · Phase 3 (Public Alpha) · Pillar Efficiency · Epic EP-ENG-03 (Fast startup and on-demand extensions)

Tracked together with ENG-044 (On-Demand Extensions).

- **Problem:** Extensions inject into every page, costing memory and leaking data.
- **Use case:** Automatically limit extensions to where they are needed.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-044](#eng-044)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — reduces extension exposure.
- **Privacy risk:** Low — reduces extension data access.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of ENG-044
  - Use case verified: Automatically limit extensions to where they are needed.
- **Origin:** A · **Duplicate of:** [ENG-044](#eng-044)
- **Limitations / notes:** Technical duplicate merged into ENG-044; kept as its own entry to preserve the use case and traceability.

<a id="eng-029"></a>

## ENG-029 — Process count reduction

`Secondary` · `Research` · **P2** · Impact Medium · Complexity L · Phase 3 (Public Alpha) · Pillar Efficiency · Epic EP-ENG-01 (Tab lifecycle and memory management)

Reduce unnecessary processes (unused utility services, spare renderers, disabled modules) without weakening site isolation.

- **Problem:** Process count is a visible complaint, but naive reduction weakens security.
- **Use case:** A user with Nano disabled sees no Nano process and no spare renderer on low-memory devices.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [CORE-005](core.md#core-005), [CORE-049](core.md#core-049)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** High — must never merge sites into shared processes.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Site isolation unchanged (CORE-049)
  - Measured process and memory delta
  - Each change documented
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Site isolation makes process count largely proportional to sites; achievable reductions are limited to spare and utility processes and may be small.

<a id="eng-030"></a>

## ENG-030 — Startup optimization

`Flagship` · `Planned` · **P1** · Impact High · Complexity M · Phase 2 (Internal Alpha) · Pillar Efficiency · Epic EP-ENG-03 (Fast startup and on-demand extensions)

Tracked together with ENG-043 (Instant Startup).

- **Problem:** Restoring large sessions makes startup slow and spikes CPU.
- **Use case:** Fast cold start through deferred work and lazy services.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-043](#eng-043)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of ENG-043
  - Use case verified: Fast cold start through deferred work and lazy services.
- **Origin:** A · **Duplicate of:** [ENG-043](#eng-043)
- **Limitations / notes:** Technical duplicate merged into ENG-043; kept as its own entry to preserve the use case and traceability.

<a id="eng-031"></a>

## ENG-031 — Advanced resource monitor

`Essential` · `Planned` · **P1** · Impact High · Complexity M · Phase 2 (Internal Alpha) · Pillar Efficiency · Epic EP-ENG-04 (Diagnostics: resource monitor, Browser Health and benchmark)

Task-manager-style monitor of CPU, RAM, GPU, VRAM and network per tab, extension, process and module.

- **Problem:** Chromium's task manager does not attribute everything users care about (modules, GPU, network).
- **Use case:** A user sorts by network usage and finds a tab uploading in the background.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [CORE-005](core.md#core-005)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Per-tab/extension/module attribution
  - Sampling overhead below a measured threshold
  - Exportable snapshot
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Per-process GPU and VRAM attribution varies by OS and driver; on Linux some GPU metrics will be unavailable.

<a id="eng-032"></a>

## ENG-032 — Energy saver mode

`Essential` · `Planned` · **P1** · Impact High · Complexity M · Phase 2 (Internal Alpha) · Pillar Efficiency · Epic EP-ENG-02 (Adaptive engine, budgets and performance profiles)

Tracked together with ENG-033 (Performance profiles (Performance, Balanced, Battery Saver)).

- **Problem:** Dozens of individual performance settings are unusable for most people.
- **Use case:** A dedicated mode to minimize energy use (covered by the Battery Saver profile).
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-033](#eng-033)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of ENG-033
  - Use case verified: A dedicated mode to minimize energy use (covered by the Battery Saver profile).
- **Origin:** A · **Duplicate of:** [ENG-033](#eng-033)
- **Limitations / notes:** Technical duplicate merged into ENG-033; kept as its own entry to preserve the use case and traceability.

<a id="eng-033"></a>

## ENG-033 — Performance profiles (Performance, Balanced, Battery Saver)

`Essential` · `Planned` · **P1** · Impact High · Complexity M · Phase 2 (Internal Alpha) · Pillar Efficiency · Epic EP-ENG-02 (Adaptive engine, budgets and performance profiles)

Three basic profiles that bundle tab lifecycle, throttling, preloading and visual effects settings.

- **Problem:** Dozens of individual performance settings are unusable for most people.
- **Use case:** A laptop user switches to Battery Saver before a flight.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-019](#eng-019), [ENG-024](#eng-024), [ENG-008](#eng-008)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Three profiles with documented settings
  - Measured differences in energy benchmark
  - Default is Balanced
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Profiles bundle settings and cannot guarantee specific savings; actual impact depends on the user's sites and must be presented as measured ranges, not promises.

<a id="eng-034"></a>

## ENG-034 — Gaming profile

`Secondary` · `Research` · **P2** · Impact Medium · Complexity M · Phase 3 (Public Alpha) · Pillar Efficiency · Epic EP-ENG-02 (Adaptive engine, budgets and performance profiles)

Tracked together with ENG-003 (Smart Gaming Mode).

- **Problem:** Background browser tabs steal CPU/GPU and cause stutter in games.
- **Use case:** Advanced profile tuned for playing games alongside the browser.
- **Segments:** Gamers & streamers
- **Dependencies:** [ENG-003](#eng-003)
- **Platforms:** Windows Planned · Linux Research · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Medium — must not log which games are played.
- **Competitors / precedents:** Opera GX
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of ENG-003
  - Use case verified: Advanced profile tuned for playing games alongside the browser.
- **Origin:** A · **Duplicate of:** [ENG-003](#eng-003)
- **Limitations / notes:** Technical duplicate merged into ENG-003; kept as its own entry to preserve the use case and traceability.

<a id="eng-035"></a>

## ENG-035 — Streaming profile

`Secondary` · `Planned` · **P3** · Impact Low · Complexity S · Phase 3 (Public Alpha) · Pillar Efficiency · Epic EP-ENG-02 (Adaptive engine, budgets and performance profiles)

Advanced profile that protects media and capture tabs while limiting everything else.

- **Problem:** Streamers need stable video/encoder performance while keeping chat tabs open.
- **Use case:** A streamer keeps chat and OBS browser sources responsive while other tabs are frozen.
- **Segments:** Gamers & streamers
- **Dependencies:** [ENG-033](#eng-033)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Media/capture tabs protected
  - Profile switch logged
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Brumel cannot reserve CPU for external encoders like OBS; the profile only reduces browser-side contention.

<a id="eng-036"></a>

## ENG-036 — Developer profile

`Secondary` · `Planned` · **P3** · Impact Low · Complexity S · Phase 3 (Public Alpha) · Pillar Efficiency · Epic EP-ENG-02 (Adaptive engine, budgets and performance profiles)

Advanced profile that disables discarding for localhost/dev hosts and keeps DevTools sessions alive.

- **Problem:** Aggressive discarding breaks local development workflows.
- **Use case:** A developer's localhost tabs are never discarded.
- **Segments:** Developers
- **Dependencies:** [ENG-033](#eng-033)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Configurable host patterns
  - No effect on other profiles
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Disabling discarding for dev hosts increases memory use; host patterns must be configured correctly or the profile does nothing useful.

<a id="eng-037"></a>

## ENG-037 — Focus profile

`Secondary` · `Planned` · **P3** · Impact Low · Complexity S · Phase 4 (Public Beta) · Pillar Efficiency · Epic EP-ENG-02 (Adaptive engine, budgets and performance profiles)

Advanced profile that pairs reduced notifications and distractions with lower background activity.

- **Problem:** Background tabs both distract and consume resources during deep work.
- **Use case:** A user starts Focus profile and only the current workspace stays active.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-033](#eng-033), [WRK-026](workspace.md#wrk-026)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Integrates with WRK-026 Focus Mode
  - Reversible
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Focus profile is a preset over existing features; it cannot block distractions outside the browser.

<a id="eng-038"></a>

## ENG-038 — AI profile

`Experimental` · `Research` · **P3** · Impact Low · Complexity S · Phase 4 (Public Beta) · Pillar Efficiency · Epic EP-ENG-02 (Adaptive engine, budgets and performance profiles)

Advanced profile that reserves memory/accelerators for Nano tasks or, conversely, disables Nano entirely.

- **Problem:** Local models compete with tabs for memory.
- **Use case:** A user running a long local indexing job lets Nano use the NPU while tabs are frozen.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-033](#eng-033), [NANO-001](nano.md#nano-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** Optional · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Explicit memory reservation and release
  - Disabled under Battery Saver
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Reserving memory for models competes directly with tabs; on 8 GB machines the AI profile may not be usable at all.

<a id="eng-039"></a>

## ENG-039 — Custom profiles

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity S · Phase 3 (Public Alpha) · Pillar Efficiency · Epic EP-ENG-02 (Adaptive engine, budgets and performance profiles)

User-defined profiles composed of the same settings as built-in profiles, exportable as recipes.

- **Problem:** Built-in profiles cannot fit every workflow.
- **Use case:** A user creates a 'Library' profile with no preloading and maximum discarding.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-033](#eng-033)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Create/edit/export/import profiles
  - Validation of conflicting settings
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Custom combinations can create contradictory or harmful settings; validation can only catch known conflicts.

<a id="eng-040"></a>

## ENG-040 — Automatic profiles and custom rules

`Flagship` · `Planned` · **P2** · Impact High · Complexity M · Phase 3 (Public Alpha) · Pillar Efficiency · Epic EP-ENG-02 (Adaptive engine, budgets and performance profiles)

Rules that switch profiles automatically on conditions (battery level, power source, fullscreen app, time, workspace).

- **Problem:** Users forget to switch modes, so manual profiles are rarely used.
- **Use case:** When the laptop unplugs below 40% battery, Brumel switches to Battery Saver automatically.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-033](#eng-033), [ENG-001](#eng-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Rules are explainable and logged
  - User can override instantly
  - Uses the visual rules engine (WRK-030) when available
- **Origin:** A · **Duplicate of:** —
- **Limitations / notes:** Automatic switching on power/battery events depends on OS notifications; rapid flapping must be damped, and complex rules become hard for users to predict.

<a id="eng-041"></a>

## ENG-041 — Efficient Video

`Secondary` · `Research` · **P2** · Impact Medium · Complexity M · Phase 3 (Public Alpha) · Pillar Efficiency · Epic EP-ENG-02 (Adaptive engine, budgets and performance profiles)

Adapt codec and resolution choices to hardware decode capabilities and power state (e.g. prefer hardware-decodable codecs, cap resolution on battery).

- **Problem:** Software-decoded AV1/VP9 on unsupported hardware drains batteries quickly.
- **Use case:** On battery, a user's video site gets a codec the GPU can decode in hardware.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [CORE-041](core.md#core-041), [ENG-004](#eng-004)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Uses Media Capabilities signals
  - Site-visible behavior stays standards-compliant
  - Measured power savings
- **Origin:** R52-48 · **Duplicate of:** —
- **Limitations / notes:** Sites choose codecs; the browser can influence only through capability reporting and must avoid breaking playback.

<a id="eng-042"></a>

## ENG-042 — Per-Site Resource Limits

`Flagship` · `Planned` · **P2** · Impact High · Complexity M · Phase 3 (Public Alpha) · Pillar Efficiency · Epic EP-ENG-02 (Adaptive engine, budgets and performance profiles)

Per-site policies for CPU, memory, background activity, autoplay and notifications.

- **Problem:** A few heavy sites dominate resource use, but users can only control them globally.
- **Use case:** A user limits a news site's background activity and blocks its autoplay permanently.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-006](#eng-006), [ENG-019](#eng-019)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Policies editable from the site info panel
  - Enforced via throttling/freezing, not by breaking isolation
  - Exportable
- **Origin:** R52-49 · **Duplicate of:** —
- **Limitations / notes:** Limits are enforced via throttling, freezing and permissions; Brumel cannot cap the memory of an active, visible site without breaking it.

<a id="eng-043"></a>

## ENG-043 — Instant Startup

`Flagship` · `Planned` · **P1** · Impact High · Complexity M · Phase 2 (Internal Alpha) · Pillar Efficiency · Epic EP-ENG-03 (Fast startup and on-demand extensions)

Fast startup by restoring the session UI immediately, loading only the active tab and deferring service initialization through the Idle Scheduler.

- **Problem:** Restoring large sessions makes startup slow and spikes CPU.
- **Use case:** A user with 200 tabs starts Brumel and can browse within seconds while other tabs stay unloaded.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-019](#eng-019), [ENG-045](#eng-045)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Cold and warm startup measured in benchmark vs upstream
  - Only active tab loads
  - Deferred services start without blocking UI
- **Origin:** R52-50 · **Duplicate of:** —
- **Limitations / notes:** Restoring the UI before tabs can surprise users when a background tab is needed immediately; sites that depend on being loaded at startup (e.g. notifications) need exceptions.

<a id="eng-044"></a>

## ENG-044 — On-Demand Extensions

`Flagship` · `Planned` · **P1** · Impact High · Complexity M · Phase 3 (Public Alpha) · Pillar Efficiency · Epic EP-ENG-03 (Fast startup and on-demand extensions)

Extensions run only on sites or contexts where the user wants them (site access rules + lazy activation), others stay idle.

- **Problem:** Extensions inject into every page, costing memory and leaking data.
- **Use case:** A user's coupon extension only runs on two shopping sites.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [CORE-022](core.md#core-022), [ENG-013](#eng-013)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — reduces extension exposure.
- **Privacy risk:** Low — reduces extension data access.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Site-access defaults configurable per extension
  - Measured memory/CPU saved
  - Clear UI for activation
- **Origin:** R52-51 · **Duplicate of:** —
- **Limitations / notes:** Extensions that need all-site access by design (password managers, accessibility tools) cannot be meaningfully limited; lazy activation may delay content scripts on first use.

<a id="eng-045"></a>

## ENG-045 — Idle Scheduler

`Essential` · `Planned` · **P0** · Impact High · Complexity M · Phase 2 (Internal Alpha) · Pillar Efficiency · Epic EP-ENG-02 (Adaptive engine, budgets and performance profiles)

Central scheduler for deferred and heavy work (indexing, OCR, embeddings, backups) that runs only when the device is idle and power allows.

- **Problem:** Independent background jobs from each feature collide and drain resources.
- **Use case:** Semantic indexing pauses while the user is gaming and resumes when the laptop is idle on AC power.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [CORE-005](core.md#core-005), [ENG-004](#eng-004)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - All Brumel background tasks register with the scheduler
  - Tasks respect profile and power state
  - Scheduler overhead measured
- **Origin:** R52-52 · **Duplicate of:** —
- **Limitations / notes:** Idle detection is imperfect (video playback, presentations); deferring tasks too long degrades features like search freshness.

<a id="eng-046"></a>

## ENG-046 — Built-in Benchmark

`Flagship` · `Planned` · **P2** · Impact High · Complexity M · Phase 3 (Public Alpha) · Pillar Trust · Epic EP-ENG-04 (Diagnostics: resource monitor, Browser Health and benchmark)

Public, reproducible benchmark suite runnable from the browser and CLI, comparing configurations and browsers under equal conditions.

- **Problem:** Browser performance claims are rarely reproducible.
- **Use case:** A reviewer runs the same suite on Brumel and Chrome and publishes the raw results.
- **Segments:** Reviewers, Power users, Contributors
- **Dependencies:** [ENG-031](#eng-031)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Edge, Opera GX, Chrome, Brave
- **Evidence:** Project principle; methodology in docs/benchmarks/BENCHMARKS.md.
- **Acceptance criteria:**
  - Suite and methodology are open
  - Raw data exportable
  - Results include hardware and configuration metadata
- **Origin:** R52-35 · **Duplicate of:** —
- **Limitations / notes:** Even with fixed methodology, results vary across hardware, OS versions and site changes; a browser-integrated benchmark must not be the only evidence, external harnesses are still needed.
