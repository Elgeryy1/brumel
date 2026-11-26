# ADR-0001: Record architecture decisions

- Status: Accepted
- Date: 2026-11-26
- Deciders: @Elgeryy1

## Context

Brumel is a long-lived project built on a very large upstream codebase. Decisions about the base, licensing, process model and data handling have consequences for years and will be questioned by new contributors. Without a record, the reasoning behind them is lost and decisions get re-litigated or silently reversed.

## Decision

Significant technical decisions are recorded as Architecture Decision Records in `docs/architecture/adr/`, one Markdown file per decision, numbered sequentially, using the template in the [ADR index](README.md).

A decision is "significant" when it affects security, privacy, licensing, the process model, data formats, public interfaces, the build/release pipeline, or is expensive to reverse.

ADRs are immutable once Accepted except for status updates and links; changing a decision means writing a new ADR that supersedes the old one.

## Consequences

- Contributors can understand why things are the way they are.
- Pull requests that contradict an Accepted ADR must either follow it or propose a superseding ADR.
- Small overhead per decision.

## Alternatives considered

- **Wiki pages**: not versioned with the code, easy to edit silently.
- **Decisions only in issues/discussions**: hard to find later; mixed with noise.

## Revisit when

The number of ADRs makes the index hard to navigate, or a different tool becomes standard in the project.
