<!-- GENERATED FILE — Do not edit by hand. Source: docs/product/catalog/*.json. Regenerate: python scripts/catalog/render_features.py -->

# Brumel Dev — developers

> **Project status: Pre-development.** Nothing listed here is available yet. Statuses, priorities and phases are proposals. See the [catalog index and legend](../FEATURES.md#legend).

17 entries. Epics in this module:

- **EP-DEV-01** Developer tools — phase 4 (Public Beta), P3
- **EP-DEV-02** Automation and privileged integrations (deferred) — phase 6 (Future), P3

| ID | Name | Tier | Status | Priority | Phase |
| --- | --- | --- | --- | --- | --- |
| [DEV-001](#dev-001) | REST API client | Secondary | Deferred | P3 | 6 |
| [DEV-002](#dev-002) | WebSocket client | Secondary | Deferred | P3 | 6 |
| [DEV-003](#dev-003) | JSON viewer and editor | Secondary | Planned | P3 | 4 |
| [DEV-004](#dev-004) | Storage viewer | Secondary | Deferred | P3 | 6 |
| [DEV-005](#dev-005) | Network diagnostics | Secondary | Deferred | P3 | 6 |
| [DEV-006](#dev-006) | Per-workspace proxies | Secondary | Research | P2 | 4 |
| [DEV-007](#dev-007) | Mobile emulation *(→ CORE-035)* | Essential | Planned | P0 | 2 |
| [DEV-008](#dev-008) | Development auto-reload | Secondary | Deferred | P3 | 6 |
| [DEV-009](#dev-009) | Performance audit *(→ CORE-035)* | Essential | Planned | P0 | 2 |
| [DEV-010](#dev-010) | Custom scripts (userscripts) | Deferred | Deferred | P3 | 6 |
| [DEV-011](#dev-011) | GitHub integration | Experimental | Research | P3 | 6 |
| [DEV-012](#dev-012) | Playwright automation | Deferred | Deferred | P3 | 6 |
| [DEV-013](#dev-013) | MCP integration | Deferred | Deferred | P3 | 6 |
| [DEV-014](#dev-014) | Homelab Mode | Experimental | Deferred | P3 | 6 |
| [DEV-015](#dev-015) | Self-hosted service management | Experimental | Deferred | P3 | 6 |
| [DEV-016](#dev-016) | Local certificates | Secondary | Research | P3 | 6 |
| [DEV-017](#dev-017) | Local terminal | Deferred | Deferred | P3 | 6 |

<a id="dev-001"></a>

## DEV-001 — REST API client

`Secondary` · `Deferred` · **P3** · Impact Low · Complexity M · Phase 6 (Future) · Pillar Everyday Tools · Epic EP-DEV-01 (Developer tools)

Built-in HTTP request builder.

- **Problem:** Developers switch to separate tools for quick API calls.
- **Use case:** A developer tests an endpoint with auth headers.
- **Segments:** Developers, Self-hosters
- **Dependencies:** [CORE-035](core.md#core-035)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — loaded only when enabled. · **Infrastructure cost:** None
- **Security risk:** High — developer and automation features expand the privileged surface.
- **Privacy risk:** Low
- **Competitors / precedents:** Chrome DevTools, Edge, Firefox Developer Edition, Polypane
- **Evidence:** Research: demand from developers to be validated; many needs are already met by DevTools.
- **Acceptance criteria:**
  - Requests use browser network stack
  - History local
- **Origin:** I · **Duplicate of:** —
- **Limitations / notes:** Overlaps with mature tools (DevTools, curl, dedicated clients); maintaining parity with their features is not a goal.

<a id="dev-002"></a>

## DEV-002 — WebSocket client

`Secondary` · `Deferred` · **P3** · Impact Low · Complexity S · Phase 6 (Future) · Pillar Everyday Tools · Epic EP-DEV-01 (Developer tools)

Connect, send and inspect WebSocket messages.

- **Problem:** Debugging sockets needs external tools.
- **Use case:** A developer sends test frames.
- **Segments:** Developers, Self-hosters
- **Dependencies:** [DEV-001](#dev-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — loaded only when enabled. · **Infrastructure cost:** None
- **Security risk:** High — developer and automation features expand the privileged surface.
- **Privacy risk:** Low
- **Competitors / precedents:** Chrome DevTools, Edge, Firefox Developer Edition, Polypane
- **Evidence:** Research: demand from developers to be validated; many needs are already met by DevTools.
- **Acceptance criteria:**
  - Message log
  - Export
- **Origin:** I · **Duplicate of:** —
- **Limitations / notes:** Limited to WebSocket; other protocols (gRPC, MQTT) are out of scope.

<a id="dev-003"></a>

## DEV-003 — JSON viewer and editor

`Secondary` · `Planned` · **P3** · Impact Medium · Complexity S · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-DEV-01 (Developer tools)

Pretty JSON viewing with folding, search and editing.

- **Problem:** Raw JSON is unreadable.
- **Use case:** A developer browses a large API response.
- **Segments:** Developers, Self-hosters
- **Dependencies:** [CORE-020](core.md#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — loaded only when enabled. · **Infrastructure cost:** None
- **Security risk:** High — developer and automation features expand the privileged surface.
- **Privacy risk:** Low
- **Competitors / precedents:** Firefox, Edge (JSON viewer)
- **Evidence:** Research: demand from developers to be validated; many needs are already met by DevTools.
- **Acceptance criteria:**
  - Handles large files
  - No network
- **Origin:** I · **Duplicate of:** —
- **Limitations / notes:** Very large JSON (hundreds of MB) may exceed renderer memory; Chromium's built-in JSON viewer was removed/limited upstream, so this is Brumel-owned code to maintain.

<a id="dev-004"></a>

## DEV-004 — Storage viewer

`Secondary` · `Deferred` · **P3** · Impact Low · Complexity S · Phase 6 (Future) · Pillar Everyday Tools · Epic EP-DEV-01 (Developer tools)

User-friendly view of site storage beyond DevTools.

- **Problem:** DevTools storage panels are scattered.
- **Use case:** A developer inspects IndexedDB of a PWA.
- **Segments:** Developers, Self-hosters
- **Dependencies:** [CORE-035](core.md#core-035)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — loaded only when enabled. · **Infrastructure cost:** None
- **Security risk:** High — developer and automation features expand the privileged surface.
- **Privacy risk:** Low
- **Competitors / precedents:** Chrome DevTools, Edge, Firefox Developer Edition, Polypane
- **Evidence:** Research: demand from developers to be validated; many needs are already met by DevTools.
- **Acceptance criteria:**
  - Read-only by default
- **Origin:** I · **Duplicate of:** —
- **Limitations / notes:** DevTools already exposes storage; a separate viewer duplicates functionality and must keep up with storage API changes.

<a id="dev-005"></a>

## DEV-005 — Network diagnostics

`Secondary` · `Deferred` · **P3** · Impact Low · Complexity M · Phase 6 (Future) · Pillar Everyday Tools · Epic EP-DEV-01 (Developer tools)

DNS, TLS and connectivity diagnostics page.

- **Problem:** Diagnosing connection issues requires several tools.
- **Use case:** A user checks why a site fails TLS.
- **Segments:** Developers, Self-hosters
- **Dependencies:** [CORE-020](core.md#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — loaded only when enabled. · **Infrastructure cost:** None
- **Security risk:** High — developer and automation features expand the privileged surface.
- **Privacy risk:** Low
- **Competitors / precedents:** Chrome DevTools, Edge, Firefox Developer Edition, Polypane
- **Evidence:** Research: demand from developers to be validated; many needs are already met by DevTools.
- **Acceptance criteria:**
  - No privileged commands
- **Origin:** I · **Duplicate of:** —
- **Limitations / notes:** Diagnostics run inside the browser's network stack and cannot replace OS tools (traceroute, packet capture) without privileged access, which is out of scope.

<a id="dev-006"></a>

## DEV-006 — Per-workspace proxies

`Secondary` · `Research` · **P2** · Impact Medium · Complexity L · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-DEV-01 (Developer tools)

Assign a proxy configuration per workspace or identity.

- **Problem:** Chromium proxy settings are global.
- **Use case:** A developer routes the 'Staging' workspace through a proxy.
- **Segments:** Developers, Self-hosters
- **Dependencies:** [WRK-010](workspace.md#wrk-010)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — loaded only when enabled. · **Infrastructure cost:** None
- **Security risk:** Medium — misrouting risks leaks.
- **Privacy risk:** Low
- **Competitors / precedents:** Chrome DevTools, Edge, Firefox Developer Edition, Polypane
- **Evidence:** Research: demand from developers to be validated; many needs are already met by DevTools.
- **Acceptance criteria:**
  - Proxy per StoragePartition
  - Leak tests
- **Origin:** I · **Duplicate of:** —
- **Limitations / notes:** Requires network-context changes; complexity high.

<a id="dev-007"></a>

## DEV-007 — Mobile emulation

`Essential` · `Planned` · **P0** · Impact High · Complexity XS · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-04 (Chromium feature parity)

Tracked together with CORE-035 (DevTools).

- **Problem:** Developers need standard tooling.
- **Use case:** Emulate mobile devices (DevTools device mode).
- **Segments:** Developers
- **Dependencies:** [CORE-035](core.md#core-035)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of CORE-035
  - Use case verified: Emulate mobile devices (DevTools device mode).
- **Origin:** I · **Duplicate of:** [CORE-035](core.md#core-035)
- **Limitations / notes:** Technical duplicate merged into CORE-035; kept as its own entry to preserve the use case and traceability.

<a id="dev-008"></a>

## DEV-008 — Development auto-reload

`Secondary` · `Deferred` · **P3** · Impact Low · Complexity S · Phase 6 (Future) · Pillar Everyday Tools · Epic EP-DEV-01 (Developer tools)

Auto-reload local pages on file change.

- **Problem:** Manual reloads slow iteration.
- **Use case:** A developer's localhost page reloads on save.
- **Segments:** Developers, Self-hosters
- **Dependencies:** [CORE-020](core.md#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — loaded only when enabled. · **Infrastructure cost:** None
- **Security risk:** High — developer and automation features expand the privileged surface.
- **Privacy risk:** Low
- **Competitors / precedents:** Chrome DevTools, Edge, Firefox Developer Edition, Polypane
- **Evidence:** Research: demand from developers to be validated; many needs are already met by DevTools.
- **Acceptance criteria:**
  - Localhost only
- **Origin:** I · **Duplicate of:** —
- **Limitations / notes:** Watching local files requires file system access outside the sandbox; scope is limited to localhost-served pages reloading on server signals.

<a id="dev-009"></a>

## DEV-009 — Performance audit

`Essential` · `Planned` · **P0** · Impact High · Complexity XS · Phase 2 (Internal Alpha) · Pillar Foundation · Epic EP-CORE-04 (Chromium feature parity)

Tracked together with CORE-035 (DevTools).

- **Problem:** Developers need standard tooling.
- **Use case:** Lighthouse-style audits (available in DevTools).
- **Segments:** Developers
- **Dependencies:** [CORE-035](core.md#core-035)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Inherited from Chromium; no Brumel-specific overhead expected. · **Infrastructure cost:** None
- **Security risk:** Medium — must track upstream security fixes without regressions.
- **Privacy risk:** Low — Google service endpoints must be removed or replaced.
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Helium
- **Evidence:** Competitor precedent: standard in Chromium-based browsers.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of CORE-035
  - Use case verified: Lighthouse-style audits (available in DevTools).
- **Origin:** I · **Duplicate of:** [CORE-035](core.md#core-035)
- **Limitations / notes:** Technical duplicate merged into CORE-035; kept as its own entry to preserve the use case and traceability.

<a id="dev-010"></a>

## DEV-010 — Custom scripts (userscripts)

`Deferred` · `Deferred` · **P3** · Impact Medium · Complexity L · Phase 6 (Future) · Pillar Everyday Tools · Epic EP-DEV-02 (Automation and privileged integrations (deferred))

Run user-provided scripts on pages.

- **Problem:** Power users rely on userscript managers.
- **Use case:** A user runs a script that adds a button to a site.
- **Segments:** Developers, Self-hosters
- **Dependencies:** [SHD-037](shield.md#shd-037)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — loaded only when enabled. · **Infrastructure cost:** None
- **Security risk:** High — script injection risk.
- **Privacy risk:** Low
- **Competitors / precedents:** Chrome DevTools, Edge, Firefox Developer Edition, Polypane
- **Evidence:** Research: demand from developers to be validated; many needs are already met by DevTools.
- **Acceptance criteria:**
  - Requires capability model (SHD-037)
  - Clear warnings
- **Origin:** I · **Duplicate of:** —
- **Limitations / notes:** Extensions already cover this; Deferred.

<a id="dev-011"></a>

## DEV-011 — GitHub integration

`Experimental` · `Research` · **P3** · Impact Low · Complexity M · Phase 6 (Future) · Pillar Everyday Tools · Epic EP-DEV-01 (Developer tools)

Notifications/PR views for GitHub as an optional module.

- **Problem:** Developers live in GitHub tabs.
- **Use case:** A developer sees PR review requests in a panel.
- **Segments:** Developers, Self-hosters
- **Dependencies:** [WRK-025](workspace.md#wrk-025)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — loaded only when enabled. · **Infrastructure cost:** None
- **Security risk:** High — developer and automation features expand the privileged surface.
- **Privacy risk:** Low
- **Competitors / precedents:** Chrome DevTools, Edge, Firefox Developer Edition, Polypane
- **Evidence:** Research: demand from developers to be validated; many needs are already met by DevTools.
- **Acceptance criteria:**
  - Uses official APIs
  - Token in OS storage
- **Origin:** I · **Duplicate of:** —
- **Limitations / notes:** GitHub APIs and rate limits change; a niche integration may not justify maintenance compared with the web UI.

<a id="dev-012"></a>

## DEV-012 — Playwright automation

`Deferred` · `Deferred` · **P3** · Impact Medium · Complexity M · Phase 6 (Future) · Pillar Everyday Tools · Epic EP-DEV-02 (Automation and privileged integrations (deferred))

First-class automation hooks for Playwright/CDP.

- **Problem:** Testing tools need a controllable browser.
- **Use case:** A developer runs tests against Brumel.
- **Segments:** Developers, Self-hosters
- **Dependencies:** [SHD-037](shield.md#shd-037)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — loaded only when enabled. · **Infrastructure cost:** None
- **Security risk:** High — CDP grants full control.
- **Privacy risk:** Low
- **Competitors / precedents:** Chrome DevTools, Edge, Firefox Developer Edition, Polypane
- **Evidence:** Research: demand from developers to be validated; many needs are already met by DevTools.
- **Acceptance criteria:**
  - Disabled by default
  - Explicit, visible automation indicator
- **Origin:** I · **Duplicate of:** —
- **Limitations / notes:** Chromium's remote debugging already allows this; deeper integration Deferred until capability model.

<a id="dev-013"></a>

## DEV-013 — MCP integration

`Deferred` · `Deferred` · **P3** · Impact Medium · Complexity L · Phase 6 (Future) · Pillar Everyday Tools · Epic EP-DEV-02 (Automation and privileged integrations (deferred))

Model Context Protocol server/client capabilities for the browser.

- **Problem:** AI tools want structured browser access.
- **Use case:** A local AI tool reads the open tab list with permission.
- **Segments:** Developers, Self-hosters
- **Dependencies:** [SHD-037](shield.md#shd-037)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — loaded only when enabled. · **Infrastructure cost:** None
- **Security risk:** High — exposes browser data to external agents.
- **Privacy risk:** Low
- **Competitors / precedents:** Chrome DevTools, Edge, Firefox Developer Edition, Polypane
- **Evidence:** Research: demand from developers to be validated; many needs are already met by DevTools.
- **Acceptance criteria:**
  - Only after SHD-037
  - Per-capability grants
- **Origin:** I · **Duplicate of:** —
- **Limitations / notes:** MCP is an evolving protocol; any integration exposes browser data to external agents and is blocked until SHD-037 exists.

<a id="dev-014"></a>

## DEV-014 — Homelab Mode

`Experimental` · `Deferred` · **P3** · Impact Low · Complexity M · Phase 6 (Future) · Pillar Everyday Tools · Epic EP-DEV-02 (Automation and privileged integrations (deferred))

Workspace preset for self-hosted dashboards with local certificates and LAN-friendly settings.

- **Problem:** Self-hosters fight certificate and LAN warnings.
- **Use case:** A self-hoster opens internal dashboards without repeated warnings.
- **Segments:** Self-hosters
- **Dependencies:** [DEV-016](#dev-016)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — loaded only when enabled. · **Infrastructure cost:** None
- **Security risk:** High — developer and automation features expand the privileged surface.
- **Privacy risk:** Low
- **Competitors / precedents:** Chrome DevTools, Edge, Firefox Developer Edition, Polypane
- **Evidence:** Research: demand from developers to be validated; many needs are already met by DevTools.
- **Acceptance criteria:**
  - Never weakens TLS for public sites
  - Scoped to LAN hosts
- **Origin:** I · **Duplicate of:** —
- **Limitations / notes:** Relaxing warnings for LAN hosts must never weaken TLS validation for public sites; misconfigured scopes could enable interception.

<a id="dev-015"></a>

## DEV-015 — Self-hosted service management

`Experimental` · `Deferred` · **P3** · Impact Low · Complexity L · Phase 6 (Future) · Pillar Everyday Tools · Epic EP-DEV-02 (Automation and privileged integrations (deferred))

Overview of self-hosted services (status, links).

- **Problem:** Self-hosters juggle many dashboards.
- **Use case:** A user sees which home services are down.
- **Segments:** Self-hosters
- **Dependencies:** [DEV-014](#dev-014)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — loaded only when enabled. · **Infrastructure cost:** None
- **Security risk:** High — developer and automation features expand the privileged surface.
- **Privacy risk:** Low
- **Competitors / precedents:** Chrome DevTools, Edge, Firefox Developer Edition, Polypane
- **Evidence:** Research: demand from developers to be validated; many needs are already met by DevTools.
- **Acceptance criteria:**
  - Read-only status checks
  - No command execution
- **Origin:** I · **Duplicate of:** —
- **Limitations / notes:** Status checks to LAN services reveal network topology and could be abused by web pages if exposed; read-only and browser-UI-only by design.

<a id="dev-016"></a>

## DEV-016 — Local certificates

`Secondary` · `Research` · **P3** · Impact Low · Complexity M · Phase 6 (Future) · Pillar Everyday Tools · Epic EP-DEV-01 (Developer tools)

Manage trust of local development CAs per profile.

- **Problem:** Local HTTPS setups are painful.
- **Use case:** A developer trusts a local CA only in the Dev workspace.
- **Segments:** Developers, Self-hosters
- **Dependencies:** [CORE-020](core.md#core-020)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — loaded only when enabled. · **Infrastructure cost:** None
- **Security risk:** High — custom CAs enable interception.
- **Privacy risk:** Low
- **Competitors / precedents:** Chrome DevTools, Edge, Firefox Developer Edition, Polypane
- **Evidence:** Research: demand from developers to be validated; many needs are already met by DevTools.
- **Acceptance criteria:**
  - Scoped trust
  - Clear warnings
- **Origin:** I · **Duplicate of:** —
- **Limitations / notes:** Custom CAs enable traffic interception if misused or stolen; scoping trust per profile requires changes to certificate verification code.

<a id="dev-017"></a>

## DEV-017 — Local terminal

`Deferred` · `Deferred` · **P3** · Impact Low · Complexity L · Phase 6 (Future) · Pillar Everyday Tools · Epic EP-DEV-02 (Automation and privileged integrations (deferred))

Embedded terminal.

- **Problem:** Developers switch windows to a terminal.
- **Use case:** A developer runs a command next to their tab.
- **Segments:** Developers, Self-hosters
- **Dependencies:** [SHD-037](shield.md#shd-037)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — loaded only when enabled. · **Infrastructure cost:** None
- **Security risk:** Critical — command execution from the browser.
- **Privacy risk:** Low
- **Competitors / precedents:** Chrome DevTools, Edge, Firefox Developer Edition, Polypane
- **Evidence:** Research: demand from developers to be validated; many needs are already met by DevTools.
- **Acceptance criteria:**
  - Only after SHD-037 and a dedicated threat model
  - Never reachable from web content
- **Origin:** I · **Duplicate of:** —
- **Limitations / notes:** Deferred; OS terminals already exist.
