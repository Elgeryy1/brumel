# Chromium Base Comparison

Status: **Research** — snapshot taken on 2026-11-26. License and release data were collected from the GitHub API on that date. Other statements reflect public project documentation and general knowledge and are marked *to be verified* where they need confirmation before being relied upon.

Decision: [ADR-0002](../architecture/adr/0002-chromium-base-selection.md). Process: [Upstream Strategy](../architecture/UPSTREAM_STRATEGY.md).

## 1. Candidates

| Base | What it is | License (GitHub API) |
| --- | --- | --- |
| **Chromium upstream** | The open-source project behind Chrome, Edge, Brave, Opera, Vivaldi and others | BSD-3-Clause (plus many third-party licenses) |
| **ungoogled-chromium** | Patch set + build tooling that removes Google web-service dependencies, tracking Chromium stable | BSD-3-Clause |
| **Brave** (`brave-core`, `brave-browser`) | A full product layer on Chromium with native ad blocking (adblock-rust), Shields, Rewards, Wallet, VPN, Leo AI, own sync | MPL-2.0 |
| **Helium** (`helium`, `helium-chromium`) | A privacy-focused browser built on ungoogled-chromium with a minimal UI and bundled blocking | GPL-3.0 |
| **Thorium** | Performance-oriented Chromium builds (compiler flags, CPU-specific builds, some feature patches) | BSD-3-Clause |

Non-forkable references (closed or largely closed UI layers, studied for product ideas only): **Microsoft Edge**, **Opera / Opera GX**, **Vivaldi** (Chromium modifications published, UI proprietary), **Arc** and its successor efforts. Mobile-focused forks **Bromite** (discontinued) and **Cromite** (its continuation, Android/Windows) are relevant for anti-fingerprinting patches but not as a desktop base.

## 2. Release cadence snapshot (2026-11-26)

| Project | Recent releases (tag — date) | Observation |
| --- | --- | --- |
| ungoogled-chromium | `158.0.8127.88-1` — 2026-11-24; `158.0.8127.36-1` — 2026-11-19; `157.0.8103.78-1` — 2026-11-13 | Tags track Chromium stable versions closely |
| ungoogled-chromium-windows | `158.0.8127.36-1.1` — 2026-11-22; `157.0.8103.78-1.1` — 2026-11-15 | Platform packaging follows a few days later |
| Helium (Windows/Linux) | `0.22.5.1` — 2026-11-25; `0.22.4.1` — 2026-11-24; `0.22.3.1` — 2026-11-23 | Near-daily releases |
| Brave | `v1.102.44` — 2026-11-26; `v1.102.43`, `v1.102.42` — 2026-11-26 | Multiple builds per day across channels |
| Thorium | `M158.0.8127.41` — 2026-11-20; previous `M156.0.8078.80` — 2026-11-09 | **Skipped/lagged major 157** while ungoogled-chromium shipped 157 and 158 |

Interpretation: projects with a small patch surface and strong automation (ungoogled-chromium) or large teams (Brave) track stable closely. A single-maintainer, patch-heavy project (Thorium) shows major-version lag, which means delayed security fixes. This is the central risk Brumel must avoid.

## 3. Comparison

| Criterion | Chromium upstream | ungoogled-chromium | Brave | Helium | Thorium |
| --- | --- | --- | --- | --- | --- |
| Maintenance | Google + large community | Community, active | Company (Brave Software), large team | Small team, very active | Essentially single maintainer |
| License | BSD-3-Clause | BSD-3-Clause | MPL-2.0 | GPL-3.0 | BSD-3-Clause |
| Security update latency | Reference | Close to upstream (days) | Close to upstream | Close to upstream (frequent releases) | Can lag a major version (see §2) |
| Web compatibility | Reference | Very high; some breakage from removed services | Very high | Very high | High |
| Google dependencies | Many (Safe Browsing, sync, translate, component updates, etc.) | Removed by design | Mostly removed or proxied through Brave services | Removed (inherits ungoogled) plus own services where needed (to be verified) | Mostly upstream defaults (to be verified) |
| Widevine | Integration hooks; licensing via Google | Not shipped; user can add with limitations (to be verified) | Licensed, opt-in | To be verified | Bundled/enabled in some builds (to be verified) |
| Proprietary codecs | Build flag | Builds commonly enable them (to be verified per platform) | Enabled | To be verified | Enabled (marketing point) |
| Build system | depot_tools, GN, Ninja | Upstream toolchain + Python patch/pruning utilities | Upstream toolchain + npm-driven wrapper scripts | Built on ungoogled tooling | Upstream toolchain + custom args |
| Native blocking | No (only `subresource_filter`) | No (extensions) | Yes — adblock-rust (MPL-2.0) | Yes — bundled blocker (implementation to be verified) | No |
| Customization room | Full | Full | Constrained by Brave's product layer | Constrained by Helium's product direction | Full |
| Platforms | All | Windows, Linux, macOS (community packaging) | Windows, macOS, Linux, Android, iOS | Windows, Linux, macOS (to be verified) | Windows, Linux, macOS, others |
| Cost to adopt | Highest initial work | Low — reuse patch set | High — large layer to carry | Medium — follow a second upstream | Low initially, high security risk |
| Rebase complexity for Brumel | Own patches only | Own patches + selected ungoogled patches | Very high | High (two upstreams) | Medium-high |

## 4. Licensing implications

- **BSD-3-Clause bases** (Chromium, ungoogled-chromium, Thorium) impose only attribution; Brumel can use MPL-2.0 for its own files ([ADR-0004](../architecture/adr/0004-licensing.md)).
- **MPL-2.0 (Brave)**: individual Brave components (e.g. adblock-rust) can be reused file-by-file under MPL-2.0, compatible with Brumel's license.
- **GPL-3.0 (Helium)**: reusing Helium code would require distributing the combined work under GPL-3.0-compatible terms. Brumel may study Helium's approach but should not copy its code without a deliberate licensing decision.

## 5. Recommendation

**Chromium upstream stable tags + selected ungoogled-chromium patches + Brumel patch series** ([ADR-0002](../architecture/adr/0002-chromium-base-selection.md)).

Reasons:

1. Shortest path from upstream security fix to Brumel release.
2. Permissive, simple licensing.
3. Reuses well-maintained, community de-Googling work instead of duplicating it.
4. No dependency on another product's roadmap or services.
5. Selective reuse of MPL-2.0 components such as adblock-rust remains possible.

What Brumel takes from others as **ideas** (not code unless license-compatible and deliberate): Brave's native blocking integration model and Safe Browsing proxy approach; Helium's minimalism and release automation; Vivaldi's and Arc's workspace UX; Thorium's lesson that performance patches are not worth security lag.

## 6. Validation plan (Phase 1)

- Build the pinned Chromium tag with a minimal ungoogled subset on the reference hardware and measure disk, RAM, build time and rebase effort.
- Inventory which ungoogled patches Brumel takes, skips or modifies, with reasons.
- Confirm Chrome Web Store installation and update flows with the chosen subset.
- Re-evaluate this comparison with fresh release data.
