# ADR-0002: Chromium upstream as base, with selected ungoogled-chromium patches

- Status: Accepted (provisional)
- Date: 2026-11-26
- Deciders: @Elgeryy1
- Related: [Chromium Bases](../../research/CHROMIUM_BASES.md), [Upstream Strategy](../UPSTREAM_STRATEGY.md), [ADR-0003](0003-patch-based-repository.md), [ADR-0004](0004-licensing.md)

## Context

Brumel needs a Chromium base that maximizes compatibility, keeps security updates fast, removes dependence on Google services and leaves room for Brumel's own features. Candidate bases (detailed comparison in [Chromium Bases](../../research/CHROMIUM_BASES.md)):

- Chromium upstream (BSD-3-Clause).
- ungoogled-chromium (BSD-3-Clause): a patch set and tooling for removing Google integration, tracking Chromium stable closely (e.g. tags `158.0.8127.88-1` on 2026-11-24 and `158.0.8127.36-1` on 2026-11-19).
- Brave (`brave-core`, MPL-2.0): a large, product-specific layer with its own services and build system.
- Helium (GPL-3.0): a newer browser built on ungoogled-chromium with frequent releases.
- Thorium (BSD-3-Clause): performance-focused builds; public release data shows it lagged a full major version behind other forks in late 2026 (M156 → M158 while others shipped M157).

## Decision

Brumel builds **Chromium upstream stable tags** and applies:

1. A **selected subset of ungoogled-chromium patches** for de-Googling, imported from the tag that matches the pinned Chromium version.
2. Brumel's own **patch series** and added files ([ADR-0003](0003-patch-based-repository.md)).

Brumel does **not** fork Brave, Helium or Thorium. Their designs may be studied and, where licenses allow and it is worth it, individual components reused with attribution (e.g. adblock-rust, [ADR-0011](0011-native-content-blocking.md)).

## Consequences

- Positive: closest possible tracking of upstream security releases; BSD-3-Clause base keeps licensing simple; no dependency on another product's roadmap; ungoogled-chromium's community-maintained privacy work is reused instead of duplicated.
- Negative: Brumel must build its own replacements for features Brave/Helium already have (blocking integration, UI); Brumel depends partly on ungoogled-chromium's cadence for de-Googling patches.
- Neutral: some ungoogled patches remove things Brumel wants (e.g. smoother Chrome Web Store integration); Brumel imports selectively and documents which patches are skipped.

## Alternatives considered

- **Fork Brave**: strongest privacy features, but brave-core is large and tightly coupled to Brave's services, branding and build system; rebasing Brave's layer is harder than rebasing Chromium. Rejected.
- **Fork Helium**: attractive and active, but GPL-3.0 would impose strong copyleft on Brumel derivatives, and following a young project adds a second upstream. Rejected as base; studied as reference.
- **Fork Thorium**: performance patches are interesting, but update lag is a security risk. Rejected.
- **Pure Chromium without ungoogled patches**: would require re-implementing well-maintained de-Googling work. Rejected.

## Revisit when

- The first build spike (Phase 1) shows the ungoogled patch subset is too costly to maintain.
- ungoogled-chromium stops tracking stable closely.
- A base with substantially better security-update latency or tooling appears.
