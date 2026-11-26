# ADR-0011: Native content blocking based on adblock-rust

- Status: Proposed
- Date: 2026-11-26
- Deciders: @Elgeryy1
- Related: [Architecture](../ARCHITECTURE.md), [Compatibility §3](../COMPATIBILITY.md), [Threat Model §5.2](../../security/THREAT_MODEL.md)

## Context

Clean Web (native ad and tracker blocking) is a core pillar. Extension-based blockers are constrained by Manifest V3 limits and run in extension processes. Brave maintains **adblock-rust** (MPL-2.0), a Rust engine compatible with common filter-list syntaxes (EasyList/uBlock Origin-style network and cosmetic rules), integrated natively into a Chromium-based browser.

## Decision (proposed)

- Evaluate **adblock-rust** as Brumel's native blocking engine, integrated through Chromium's Rust support ([ADR-0010](0010-rust-for-new-components.md)) and hooked into network request handling in the browser/network layers with minimal patches.
- Filter lists are delivered as **signed components**; each list's license is tracked (filter lists use various licenses, e.g. GPL-3.0 or CC BY-SA for popular lists — to be verified per list) and lists are distributed as data with attribution.
- Cosmetic filtering and scriptlets use a vetted allow-list of scriptlets.
- Per-site toggles and Self Repair allow users to fix breakage.
- MV3 content-blocking extensions keep working alongside the native engine.

## Consequences

- Positive: proven engine; memory-safe; MPL-2.0 aligns with Brumel's license ([ADR-0004](0004-licensing.md)); not limited by MV3 rule caps.
- Negative: integration points in the network stack must be maintained across rebases; filter-list licensing needs care; scriptlet injection is a sensitive capability.
- Neutral: alternative engines can be benchmarked before final acceptance.

## Alternatives considered

- **Rely on extensions only**: MV3 constraints and extension overhead; not "native".
- **Chromium `subresource_filter` (used for ad-heavy sites)**: limited rule syntax and purpose.
- **Custom engine**: high cost, no benefit over a mature MPL-2.0 engine.

## Revisit when

Integration cost proves too high in the Phase 2 prototype, or upstream licensing/maintenance of adblock-rust changes.
