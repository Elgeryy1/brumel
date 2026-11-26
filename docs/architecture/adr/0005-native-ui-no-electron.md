# ADR-0005: Native UI with Chromium Views and WebUI; no Electron

- Status: Accepted
- Date: 2026-11-26
- Deciders: @Elgeryy1
- Related: [Architecture](../ARCHITECTURE.md), [Design System](../../design/DESIGN_SYSTEM.md)

## Context

Brumel needs custom UI (vertical tabs, spaces, command palette, side panels, health and memory pages). Options range from extending Chromium's native UI to wrapping Chromium in another shell. Electron-based browsers ship a second copy of Chromium's runtime for the shell, lag behind Chromium security releases, and cannot reuse Chromium's browser features (extensions, profiles, password manager, sync hooks) without re-implementing them.

## Decision

- Browser chrome (tab strip, toolbar, side panels, split view) is built with **Chromium Views** in C++.
- Internal pages and complex settings are built as **WebUI** with **TypeScript and Lit**, the stack Chromium itself uses for its WebUI.
- WebUI pages are served from `brumel://` (or `chrome://`) origins with strict CSP and Trusted Types, and receive Mojo interfaces bound only to their own origin.
- **Electron and any second embedded browser runtime are not used** for the browser.

## Consequences

- Positive: one engine, one security update stream; full access to Chromium features; best performance.
- Negative: Views development has a learning curve and patches to upstream UI code must be kept small.
- Neutral: some features may be prototyped as extensions or WebUI first and moved to Views when stable.

## Alternatives considered

- **Electron shell**: rejected (duplicated runtime, security lag, loss of Chromium features).
- **Full WebUI browser chrome** (UI entirely in HTML): attractive for theming, but increases attack surface and latency for core UI; studied for specific surfaces only.
- **Other toolkits (Qt, GTK)**: platform-specific, poor integration. Rejected.

## Revisit when

Upstream Chromium changes its UI technology direction.
