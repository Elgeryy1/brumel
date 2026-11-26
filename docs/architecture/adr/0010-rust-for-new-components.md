# ADR-0010: Rust for new memory-safety-sensitive components

- Status: Proposed
- Date: 2026-11-26
- Deciders: @Elgeryy1
- Related: [Architecture](../ARCHITECTURE.md), [Threat Model](../../security/THREAT_MODEL.md)

## Context

Memory-safety bugs are a large share of serious browser vulnerabilities. Chromium supports Rust in-tree (toolchain, GN integration, a curated set of third-party crates, C++ interop through tools such as CXX) and upstream already uses Rust for some parsers. Brumel will add new code that parses untrusted inputs: filter lists, sync payloads, page-change diffs, file conversions for Smart Upload, model metadata.

## Decision (proposed)

- New Brumel components that **parse or transform untrusted data** should be written in **Rust** when practical, using Chromium's in-tree Rust toolchain and crate policies.
- C++ remains the language for integration with browser code (services, UI, Mojo hosts).
- Rust components expose narrow interfaces to C++; unsafe code requires justification and review.
- Third-party crates are vendored through Chromium's mechanism, reviewed, and listed in third-party notices.
- Rust code is fuzzed like C++ parsers.

## Consequences

- Positive: eliminates classes of memory bugs in the riskiest new code; good performance.
- Negative: contributors need Rust and C++ interop knowledge; crate vetting adds work; build complexity.
- Neutral: language choice is per component, not a rewrite of upstream code.

## Alternatives considered

- **C++ only, with sandboxing and fuzzing**: viable for low-risk code; sandboxing remains required regardless.
- **Other memory-safe languages**: not supported in the Chromium build.

## Revisit when

Chromium's Rust policy changes materially, or interop costs outweigh benefits for a component.
