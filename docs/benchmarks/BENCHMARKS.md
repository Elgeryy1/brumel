# Benchmark Methodology

Status: **Planned** — no Brumel build exists, so **no Brumel measurements exist**. This document defines how measurements will be made so that results, when they exist, are reproducible and fair. Any number published by the project must come from this methodology, with raw data.

Related: [Architecture](../architecture/ARCHITECTURE.md) · [AI Architecture](../architecture/AI_ARCHITECTURE.md) · Built-in Benchmark feature in [FEATURES.md](../product/FEATURES.md)

## 1. Hypotheses (unproven)

The project's initial performance goals are **hypotheses**, not results:

| Hypothesis | Compared with | Conditions |
| --- | --- | --- |
| H1: 20–40 % lower RAM with many tabs | Chrome stable of the same Chromium version | Same pages, same extensions, Balanced profile, after tabs settle |
| H2: 15–30 % lower energy use during typical browsing | Chrome stable of the same Chromium version | Same workload, same power plan |
| H3: Disabled modules have no measurable idle cost | Brumel with module compiled out | Idle CPU, wake-ups, RAM |

They will be reported as confirmed, partially confirmed or rejected. A rejected hypothesis will be published as such.

## 2. Browsers compared

- **Brumel** (each profile: Performance, Balanced, Battery Saver, and relevant advanced profiles).
- **Google Chrome** stable — the primary baseline, ideally on the same Chromium major.
- **Brave**, **Microsoft Edge**, **Zen Browser** (Firefox-based), **Helium**, and others as relevant (Vivaldi, Opera, Firefox).

Each browser is tested with **default settings** and, separately, with **equivalent settings** (e.g. Chrome's Memory Saver and Energy Saver enabled, Edge's sleeping tabs enabled, equivalent ad blocking) so that comparisons do not confuse defaults with capability.

## 3. Metrics

| Area | Metric | Method |
| --- | --- | --- |
| Memory | Total private memory / proportional set size with **1, 10, 25, 50, 100, 200** tabs | Fixed page corpus; measure after a settle period; OS counters (Windows: Private Working Set / commit via ETW or PDH; Linux: PSS via `smaps_rollup`) summed over all browser processes |
| CPU | Idle CPU % and wake-ups per second with N background tabs | ETW (Windows), `perf`/`powertop`/`/proc` (Linux) over fixed windows |
| GPU | GPU utilization and dedicated/shared VRAM | ETW GPU events / vendor tools (Windows), `nvidia-smi`, `radeontop`, `intel_gpu_top` (Linux) |
| Startup | Cold and warm startup to first paint of the start page and to interactive UI | Scripted launches, Chromium trace events |
| Restore | Time and memory to restore a 50/200-tab session (with lazy restore) | Session fixture, traces |
| Energy | Package/system energy during scripted workloads | Windows: Energy Estimation Engine / `powercfg /srumutil`, WPR power profiles; Linux: RAPL counters (`turbostat`, `perf stat -e power/energy-pkg/`); AMD uProf and Intel PCM as cross-checks; battery drain tests for end-to-end validation |
| Page load | Navigation timing, LCP, CLS, INP-style interaction latency | Replayed corpus, Chromium tracing, crossbench |
| Responsiveness | Speedometer 3, JetStream 2, MotionMark; UI frame times (tab switching, scrolling, opening panels) | Standard suites + UI traces |
| Media | Dropped frames, CPU/GPU and energy during 1080p/4K playback, hardware decode usage | Local media files and replayed pages |
| Extensions | Delta of all metrics with a fixed extension set (e.g. a password manager, a content blocker, a grammar tool) | Same corpus with and without |
| Local AI | Latency, peak RAM/VRAM, energy per Nano task; idle cost when Nano is installed but not used | Nano benchmark harness ([AI Architecture §8](../architecture/AI_ARCHITECTURE.md)) |
| Stability | Crashes, hangs, renderer OOM kills per hour under stress | Long-running soak tests |
| Gaming impact | Game FPS (average, 1 % lows) and frame-time variance with the browser in the background (video playing, N tabs) vs browser closed | Fixed built-in game benchmarks, PresentMon/MangoHud |
| Memory tiers | Behavior on **4, 8, 16, 32 GB** RAM | VMs with fixed memory and/or OS boot-time memory limits on the reference machines; community hardware |
| Module idle cost | RAM/CPU/wake-ups with each module off, dormant, active | Brumel-specific harness (validates [ADR-0006](../architecture/adr/0006-in-process-modules.md)) |

## 4. Controlled conditions

Every run records and controls:

- Same hardware, firmware/BIOS version, OS build, drivers, power plan, display resolution and refresh rate.
- Same browser versions (recorded exactly), clean profiles, same extensions and settings.
- Network: page corpus served locally via **Web Page Replay (WPR)** archives so that ads, A/B tests and server latency do not vary between runs; live-site tests are reported separately.
- Background activity minimized: OS updates paused, indexing and antivirus scheduled off during runs (documented), no other user applications.
- Thermal state: cool-down between runs; ambient temperature noted; laptops on AC unless measuring battery.
- Order randomized across browsers to avoid systematic bias.

## 5. Page corpus

- A versioned set of pages representative of real use: news, social feeds, video, web mail, documents, maps, shopping, developer documentation, web apps.
- Recorded with WPR; archives stored as release artifacts (subject to content licensing; pages with restrictive terms are replaced by synthetic equivalents).
- Corpus changes produce a new corpus version; results are only compared within the same version.

## 6. Tools

| Tool | Use |
| --- | --- |
| crossbench (Chromium) and Telemetry-style scripts | Cross-browser scripted stories |
| Speedometer 3, JetStream 2, MotionMark | Standard responsiveness/graphics suites |
| Web Page Replay | Deterministic network replay |
| Windows Performance Recorder / Analyzer (ETW) | CPU, memory, GPU, power on Windows |
| `powercfg`, Energy Estimation Engine | Energy estimates on Windows |
| RAPL via `turbostat` / `perf` | Energy on Linux |
| AMD uProf, Intel PCM | Vendor energy and counter cross-checks |
| `perf`, `smaps_rollup`, `powertop` | CPU, memory, wake-ups on Linux |
| PresentMon, MangoHud | Game frame timing |

## 7. Reference hardware

Described generically (exact models are recorded in each raw-data bundle when results are published):

- **Ref-A**: current-generation 12-core mobile x86 APU with integrated NPU, 8 GB discrete laptop GPU, 32 GB RAM — Windows and Linux.
- **Ref-B**: 8-core desktop x86 CPU, 8 GB 2018-era discrete GPU, 32 GB RAM — Linux.
- **Low-memory tiers**: 4/8/16 GB emulated with VMs or memory limits on the machines above, complemented by community-contributed runs on real low-end hardware.

Results from one machine are never generalized to all hardware.

## 8. Statistics

- Minimum **10 runs** per configuration for timing metrics, **5** for long memory/energy runs (raised if variance is high).
- Report **median**, interquartile range and **95 % confidence intervals** (bootstrap); report the number of runs and discarded outliers with the rule used.
- Differences are called significant only when confidence intervals do not overlap or a suitable test (e.g. Mann–Whitney U) supports it.
- No cherry-picking: every configured run is published, including failed runs.

## 9. Reporting format

Each published result includes:

1. Hardware/OS/driver manifest.
2. Exact browser versions and settings (exported).
3. Corpus version and workload script commit.
4. Raw data (CSV/JSON) and traces where size allows.
5. Summary table with medians and confidence intervals.
6. Known limitations.

Results live under `docs/benchmarks/results/<date>-<corpus>-<machine>/` once they exist, and the Built-in Benchmark feature will let users run the same suite locally.

## 10. Rules

- Never disable sandboxing, Site Isolation or other security mitigations to improve numbers.
- Never compare a tuned Brumel against an untuned competitor without also showing the equivalent-settings comparison.
- Never publish marketing claims that are not backed by a published result from this methodology.
