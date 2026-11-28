# Brumel documentation

Brumel is in **pre-development**: these documents describe intent, decisions and research, not
shipped behavior. Each document states the status of what it describes using the project
vocabulary: **Available, In Development, Planned, Research, Experimental, Deferred, Rejected**.

Public documentation is written in English. Corrections are welcome through pull requests or
[Discussions](https://github.com/Elgeryy1/brumel/discussions).

## Start here

1. [Vision](product/VISION.md) — why Brumel exists and what it will not do.
2. [Roadmap](../ROADMAP.md) — phases, dependencies and exit criteria.
3. [Feature catalog](product/FEATURES.md) — every proposal with a stable ID.
4. [Architecture](architecture/ARCHITECTURE.md) — how the pieces fit on top of Chromium.

## Product

| Document | Purpose |
|---|---|
| [VISION.md](product/VISION.md) | Philosophy, principles, five pillars, positioning, non-goals |
| [FEATURES.md](product/FEATURES.md) | Generated catalog index, legend, counts, epics, the 52 research proposals |
| [features/](product/features/core.md) | Full feature cards per module (generated) |
| [catalog/features.json](product/catalog/features.json) | Source of truth for the catalog |
| [catalog/epics.json](product/catalog/epics.json) | Epics, their features and dependencies |
| [FEATURE_MATRIX.md](product/FEATURE_MATRIX.md) | Conservative comparison with other browsers |
| [PRODUCT_REQUIREMENTS.md](product/PRODUCT_REQUIREMENTS.md) | Functional and non-functional requirements, release criteria |

## Architecture

| Document | Purpose |
|---|---|
| [ARCHITECTURE.md](architecture/ARCHITECTURE.md) | System overview, modules, process model, shared store, scheduler |
| [AI_ARCHITECTURE.md](architecture/AI_ARCHITECTURE.md) | Brumel Nano: local AI runtime, models, safety boundaries |
| [SYNC_ARCHITECTURE.md](architecture/SYNC_ARCHITECTURE.md) | Brumel Connect: local-first, end-to-end encrypted sync |
| [UPSTREAM_STRATEGY.md](architecture/UPSTREAM_STRATEGY.md) | Pinned upstream, patch series, rebases, security updates |
| [COMPATIBILITY.md](architecture/COMPATIBILITY.md) | Web standards, extensions, DRM, codecs, Cast, passkeys |
| [MODULE_SYSTEM.md](architecture/MODULE_SYSTEM.md) | Module registry, gates, lifecycle and the "off means zero" tests (design) |
| [adr/](architecture/adr/README.md) | Architecture Decision Records |

## Security and privacy

| Document | Purpose |
|---|---|
| [SECURITY.md](../SECURITY.md) | Security model summary and private vulnerability reporting |
| [THREAT_MODEL.md](security/THREAT_MODEL.md) | Assets, adversaries, trust boundaries, mitigations |
| [PRIVACY.md](privacy/PRIVACY.md) | Principles, data inventory, network connections, portability |

## Development

| Document | Purpose |
|---|---|
| [PHASE1_PLAN.md](development/PHASE1_PLAN.md) | Step-by-step plan for Phase 1 — Technical Foundation |
| [BUILDING.md](development/BUILDING.md) | Build strategy, tooling and requirements to validate |
| [INFRASTRUCTURE.md](development/INFRASTRUCTURE.md) | Services, runners, signing, costs and alternatives |
| [BENCHMARKS.md](benchmarks/BENCHMARKS.md) | Reproducible performance methodology |
| [GOOD_FIRST_ISSUES.md](development/GOOD_FIRST_ISSUES.md) | Starter contributions |
| [patches/README.md](../patches/README.md) | Patch series conventions |
| [scripts/README.md](../scripts/README.md) | Repository scripts |

## Research, design, community and legal

| Document | Purpose |
|---|---|
| [RESEARCH.md](research/RESEARCH.md) | Hypotheses, evidence status, open questions, sources |
| [CHROMIUM_BASES.md](research/CHROMIUM_BASES.md) | Chromium vs ungoogled-chromium vs Brave vs Helium vs Thorium |
| [NAME_CHECK.md](research/NAME_CHECK.md) | Preliminary name check and its limits |
| [DESIGN_SYSTEM.md](design/DESIGN_SYSTEM.md) | Identity, tokens, typography, UI principles |
| [INTERFACE.md](design/INTERFACE.md) | Interface design: shell, pages, Chromium patch plan |
| [UI_INVENTORY.md](design/UI_INVENTORY.md) | Every screen and surface, linked to the feature catalog (generated) |
| [Mockups](design/mockups/README.md) | HTML mockups of the first screens |
| [COMMUNITY.md](community/COMMUNITY.md) | Build-in-public approach and channels |
| [LAUNCH_PLAN.md](community/LAUNCH_PLAN.md) | Launch strategy and demo ideas |
| [Devlog](community/devlog/0001-pre-development.md) | Development log |
| [WEBSITE.md](website/WEBSITE.md) | GitHub Pages site strategy |
| [LICENSING.md](legal/LICENSING.md) | License evaluation, decision, trademark draft |

Root documents: [README](../README.md) · [ROADMAP](../ROADMAP.md) ·
[CONTRIBUTING](../CONTRIBUTING.md) · [GOVERNANCE](../GOVERNANCE.md) ·
[CODE_OF_CONDUCT](../CODE_OF_CONDUCT.md) · [CHANGELOG](../CHANGELOG.md) ·
[THIRD_PARTY_NOTICES](../THIRD_PARTY_NOTICES.md)
