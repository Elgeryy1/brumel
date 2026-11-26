# ADR-0006: Modules as lazily created in-process components

- Status: Accepted
- Date: 2026-11-26
- Deciders: @Elgeryy1
- Related: [Architecture §5](../ARCHITECTURE.md), [Benchmarks](../../benchmarks/BENCHMARKS.md)

## Context

Brumel's catalog contains hundreds of feature proposals grouped into modules (Engine, Workspace, Memory, Shield, Nano, Connect, Tools, Dev). The product promise is that available features do not cost resources unless used. Creating a process per module would multiply memory overhead (each Chromium process carries a fixed cost) and IPC complexity without a security benefit for code that needs browser-process privileges anyway.

## Decision

- Modules are **logical groupings** of code, implemented as profile-keyed services (`KeyedService`) and UI controllers **inside existing Chromium processes**.
- Each module and optional feature is gated by: a build flag (can be compiled out), a `base::Feature` (runtime availability) and a user preference (on/off).
- Services are **created lazily** on first use and **not** with the profile.
- **Disabled means zero**: no service instance, no observers, no timers, no network, no open databases. This is enforced by browser tests.
- **Dormant services** release caches and close database handles after inactivity.
- **Separate processes are used only when justified**: parsing or processing untrusted data (indexing, OCR, ASR, filter-list parsing if not in Rust) and Nano inference run in **sandboxed utility processes** that start on demand and exit when idle.

## Consequences

- Positive: minimal idle cost; simple IPC; consistent lifecycle; testable "off means off".
- Negative: discipline required — any feature that registers global observers at startup violates the model; code review must check it.
- Neutral: modules share the Brumel Store and Idle Scheduler ([ADR-0007](0007-brumel-store-sqlite.md)).

## Alternatives considered

- **Process per module**: rejected (overhead, no security gain for privileged orchestration code).
- **Everything as built-in extensions**: limited APIs, extension process overhead, weaker integration. Considered only for prototypes.

## Revisit when

A module requires isolation for security or stability reasons not covered by utility processes.
