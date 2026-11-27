# Architecture Decision Records

Brumel records significant technical decisions as Architecture Decision Records (ADRs), following a lightweight [MADR](https://adr.github.io/madr/)-style format ([ADR-0001](0001-record-architecture-decisions.md)).

## Status values

| Status | Meaning |
| --- | --- |
| Proposed | Under discussion; not yet binding |
| Accepted | Binding until superseded |
| Accepted (provisional) | Binding for now, with an explicit revisit trigger |
| Superseded | Replaced by a later ADR (linked) |
| Rejected | Considered and declined; kept for history |

## Index

| ADR | Title | Status |
| --- | --- | --- |
| [0001](0001-record-architecture-decisions.md) | Record architecture decisions | Accepted |
| [0002](0002-chromium-base-selection.md) | Chromium upstream as base, with selected ungoogled-chromium patches | Accepted (provisional) |
| [0003](0003-patch-based-repository.md) | Patch-based repository; Chromium source never committed | Accepted |
| [0004](0004-licensing.md) | MPL-2.0 for Brumel files, BSD-3-Clause for Chromium patches | Accepted |
| [0005](0005-native-ui-no-electron.md) | Native UI with Chromium Views and WebUI; no Electron | Accepted |
| [0006](0006-in-process-modules.md) | Modules as lazily created in-process components | Accepted |
| [0007](0007-brumel-store-sqlite.md) | Shared encrypted SQLite "Brumel Store" per profile | Proposed |
| [0008](0008-local-ai-runtime.md) | Local AI runtime: llama.cpp and ONNX Runtime in a sandboxed process | Proposed |
| [0009](0009-local-first-e2ee-sync.md) | Local-first, end-to-end encrypted sync | Proposed |
| [0010](0010-rust-for-new-components.md) | Rust for new memory-safety-sensitive components | Proposed |
| [0011](0011-native-content-blocking.md) | Native content blocking based on adblock-rust | Proposed |
| [0012](0012-update-system.md) | Update system: Chromium updater on Windows, signed repositories on Linux | Proposed |
| [0013](0013-git-backed-patch-tooling.md) | Git-backed patch series tooling | Accepted (provisional) |
| [0014](0014-upstream-pin-policy.md) | Upstream pin policy | Accepted (provisional) |

## Template

Copy this into `NNNN-short-title.md` with the next free number. Numbers are never reused.

```markdown
# ADR-NNNN: Title

- Status: Proposed
- Date: YYYY-MM-DD
- Deciders: @Elgeryy1
- Related: links to issues, docs, other ADRs

## Context

What problem or force requires a decision? What constraints apply?

## Decision

What we decided, stated precisely.

## Consequences

Positive, negative and neutral effects. What becomes easier or harder.

## Alternatives considered

Each option with the reason it was not chosen.

## Revisit when

Concrete triggers that should reopen this decision.
```
