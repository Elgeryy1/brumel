# ADR-0012: Update system — Chromium updater on Windows, signed repositories on Linux

- Status: Proposed
- Date: 2026-11-26
- Deciders: @Elgeryy1
- Related: [Upstream Strategy](../UPSTREAM_STRATEGY.md), [Infrastructure](../../development/INFRASTRUCTURE.md), [Threat Model §5.7](../../security/THREAT_MODEL.md)

## Context

Fast, reliable, secure updates are essential for a Chromium-based browser. Chromium includes an open-source updater (`//chrome/updater`) that speaks the Omaha 4 protocol and supports signed request/response handling; Google Chrome uses Google's update servers. On Linux, users expect updates through package managers.

## Decision (proposed)

- **Windows**: use Chromium's open-source updater, branded for Brumel, against a Brumel-operated update service that serves **signed manifests**. Binaries are Authenticode-signed. The client verifies signatures and enforces monotonic versions (no rollback to vulnerable versions).
- **Linux**: signed **apt and rpm repositories**; **Flatpak** as a candidate channel; AppImage only if it can be kept updated securely (Research).
- **Update Guard**: preference migrations are tested and user settings are preserved across updates.
- **Delta updates**: Research (Chromium updater supports differential updates; server-side cost to evaluate).
- Update metadata requests carry only version, platform, architecture and channel.

## Consequences

- Positive: reuses maintained upstream code; strong integrity guarantees; familiar Linux distribution.
- Negative: operating an update service and code signing has costs ([Infrastructure](../../development/INFRASTRUCTURE.md)); key management becomes critical.
- Neutral: macOS updates are Deferred with the macOS platform.

## Alternatives considered

- **Third-party updaters (e.g. WinSparkle)**: smaller, but less integrated with Chromium (background updates, component updates).
- **Manual downloads only**: unacceptable for security.
- **Microsoft Store / winget only**: useful as additional channels, not as the sole update mechanism.

## Revisit when

Operating costs or signing requirements change, or upstream updater design changes.
