<!-- GENERATED FILE — Do not edit by hand. Source: docs/design/surfaces.json and docs/product/catalog/features.json. Regenerate: python3 scripts/design/render_surfaces.py -->

# Brumel UI Surface Inventory

> **Status: Research.** No Brumel interface has been built yet. This inventory lists
> every screen and surface the browser needs, linked to the
> [feature catalog](../product/FEATURES.md), which stays the source of truth.

How to read it:

- **Phase** is the earliest catalog phase among the surface's features, so it is the
  phase in which the surface first has to exist. Later features extend it.
- **Status** counts the catalog status of the features on the surface. A surface is
  never further along than its features.
- **Tech** is how the surface is built in Chromium: native **Views** (C++), **WebUI**
  (HTML, CSS and TypeScript served from an internal origin), the installer, or assets.
- **Base** says whether Chromium already ships the surface (**Upstream**, so Brumel
  restyles or extends it with small patches) or Brumel adds it (**New**).
- Security surfaces (omnibox security indicator, permission prompts, download
  warnings, interstitials, credential bubbles) keep their upstream layout and wording.
  Brumel changes them only through the colour pipeline. See
  [DESIGN_SYSTEM.md § 9](DESIGN_SYSTEM.md#9-implementation-notes-chromium).

## Summary

| Phase | Surfaces |
|---|---|
| Technical Foundation | 10 |
| Internal Alpha | 43 |
| Public Alpha | 22 |
| Public Beta | 7 |
| **Total** | **82** |

## Main window (native Views)

| ID | Surface | Tech | Base | Phase | Features | Status | Notes |
|---|---|---|---|---|---|---|---|
| S-WIN-03 | Toolbar and omnibox | Views | Upstream | Technical Foundation | [CORE-020](../product/features/core.md#core-020), [CORE-047](../product/features/core.md#core-047), [SHD-007](../product/features/shield.md#shd-007), [UI-001](../product/features/interface.md#ui-001), [UI-012](../product/features/interface.md#ui-012), [CORE-004](../product/features/core.md#core-004) | In Development 1, Planned 5 | Security indicator stays upstream and is never themed by custom CSS. |
| S-WIN-06 | App menu | Views | Upstream | Technical Foundation | [CORE-004](../product/features/core.md#core-004), [CORE-027](../product/features/core.md#core-027), [CORE-028](../product/features/core.md#core-028), [CORE-038](../product/features/core.md#core-038), [CORE-043](../product/features/core.md#core-043), [ENG-020](../product/features/engine.md#eng-020), [ENG-018](../product/features/engine.md#eng-018) | In Development 1, Planned 6 | Remove Google entries, add Brumel entries behind progressive disclosure. |
| S-WIN-17 | Infobars and toasts (undo, restore, update, crash recovery) | Views | Upstream | Technical Foundation | [MEM-020](../product/features/memory.md#mem-020), [WRK-022](../product/features/workspace.md#wrk-022), [CORE-051](../product/features/core.md#core-051), [ENG-014](../product/features/engine.md#eng-014), [ENG-016](../product/features/engine.md#eng-016), [UI-019](../product/features/interface.md#ui-019) | Planned 6 | One quiet toast pattern; every destructive action offers undo. |
| S-WIN-01 | Horizontal tab strip | Views | Upstream | Internal Alpha | [WRK-001](../product/features/workspace.md#wrk-001), [CORE-032](../product/features/core.md#core-032), [CORE-033](../product/features/core.md#core-033), [ENG-019](../product/features/engine.md#eng-019), [WRK-013](../product/features/workspace.md#wrk-013), [WRK-022](../product/features/workspace.md#wrk-022), [UI-001](../product/features/interface.md#ui-001), [UI-018](../product/features/interface.md#ui-018), [UI-011](../product/features/interface.md#ui-011), [UI-017](../product/features/interface.md#ui-017) | Planned 10 | Default layout. Adds a visible suspended state and the Brumel colour mixer; no new layout code in Internal Alpha. |
| S-WIN-02 | Vertical tab sidebar | Views | Upstream | Internal Alpha | [WRK-001](../product/features/workspace.md#wrk-001), [WRK-002](../product/features/workspace.md#wrk-002), [WRK-003](../product/features/workspace.md#wrk-003), [WRK-008](../product/features/workspace.md#wrk-008), [WRK-021](../product/features/workspace.md#wrk-021), [UI-010](../product/features/interface.md#ui-010) | Planned 6 | Builds on upstream vertical tabs; trees, folders and archive come later. |
| S-WIN-07 | Clean Web button and per-site panel | Views | New | Internal Alpha | [SHD-001](../product/features/shield.md#shd-001), [SHD-002](../product/features/shield.md#shd-002), [SHD-003](../product/features/shield.md#shd-003), [SHD-005](../product/features/shield.md#shd-005), [SHD-007](../product/features/shield.md#shd-007), [SHD-004](../product/features/shield.md#shd-004), [SHD-010](../product/features/shield.md#shd-010), [SHD-014](../product/features/shield.md#shd-014) | Planned 6, Research 2 | Counts only what was really blocked on this page; per-site toggle. |
| S-WIN-08 | Page info and site permissions bubble | Views | Upstream | Internal Alpha | [CORE-045](../product/features/core.md#core-045), [SHD-011](../product/features/shield.md#shd-011), [SHD-012](../product/features/shield.md#shd-012), [TLS-021](../product/features/tools.md#tls-021), [ENG-042](../product/features/engine.md#eng-042) | Planned 5 | Security surface: restyle only through the colour mixer. |
| S-WIN-09 | Performance profile control | Views | New | Internal Alpha | [ENG-033](../product/features/engine.md#eng-033), [ENG-001](../product/features/engine.md#eng-001), [ENG-005](../product/features/engine.md#eng-005), [ENG-011](../product/features/engine.md#eng-011) | Planned 4 | Hidden by default; reachable from the menu and the palette. |
| S-WIN-10 | Downloads bubble | Views | Upstream | Internal Alpha | [CORE-031](../product/features/core.md#core-031), [CORE-050](../product/features/core.md#core-050), [TLS-004](../product/features/tools.md#tls-004), [SHD-038](../product/features/shield.md#shd-038) | Planned 3, Research 1 | Dangerous-file warnings keep upstream wording and layout. |
| S-WIN-11 | Extensions menu and site access | Views | Upstream | Internal Alpha | [CORE-022](../product/features/core.md#core-022), [ENG-044](../product/features/engine.md#eng-044), [ENG-013](../product/features/engine.md#eng-013), [SHD-013](../product/features/shield.md#shd-013) | Planned 4 |  |
| S-WIN-12 | Side panel host | Views + WebUI | Upstream | Internal Alpha | [UI-010](../product/features/interface.md#ui-010), [CORE-029](../product/features/core.md#core-029), [WRK-025](../product/features/workspace.md#wrk-025), [WRK-032](../product/features/workspace.md#wrk-032), [WRK-028](../product/features/workspace.md#wrk-028) | Planned 5 | Bookmarks, reading queue, web panels and highlights share one host. |
| S-WIN-13 | Split view | Views | Upstream | Internal Alpha | [WRK-006](../product/features/workspace.md#wrk-006), [ENG-023](../product/features/engine.md#eng-023) | Planned 2 | Extends upstream split view. |
| S-WIN-15 | Media and audio panel | Views | Upstream | Internal Alpha | [TLS-007](../product/features/tools.md#tls-007), [TLS-010](../product/features/tools.md#tls-010), [ENG-026](../product/features/engine.md#eng-026), [TLS-006](../product/features/tools.md#tls-006), [CORE-042](../product/features/core.md#core-042) | Planned 5 | Extends the upstream global media controls. |
| S-WIN-16 | Bookmarks bar | Views | Upstream | Internal Alpha | [CORE-029](../product/features/core.md#core-029) | Planned 1 | Hidden by default as upstream. |
| S-WIN-20 | Private, guest and temporary identity windows | Views | Upstream | Internal Alpha | [CORE-027](../product/features/core.md#core-027), [CORE-028](../product/features/core.md#core-028), [SHD-028](../product/features/shield.md#shd-028), [WRK-011](../product/features/workspace.md#wrk-011) | Planned 3, Research 1 | Must stay unmistakable from a normal window. |
| S-WIN-21 | Credential and autofill bubbles | Views | Upstream | Internal Alpha | [CORE-023](../product/features/core.md#core-023), [CORE-024](../product/features/core.md#core-024), [CORE-025](../product/features/core.md#core-025), [SHD-022](../product/features/shield.md#shd-022), [SHD-036](../product/features/shield.md#shd-036) | Planned 4, Research 1 | Security surface: restyle only through the colour mixer. |
| S-WIN-04 | Omnibox suggestions and Universal Search | Views | Upstream | Public Alpha | [WRK-017](../product/features/workspace.md#wrk-017), [MEM-026](../product/features/memory.md#mem-026) | Planned 1, Research 1 | Extra result groups (open tabs, archive, settings) on the existing popup. |
| S-WIN-05 | Command palette | Views + WebUI | New | Public Alpha | [WRK-018](../product/features/workspace.md#wrk-018) | Planned 1 | Open question: native popup or a WebUI bubble hosted in Views. |
| S-WIN-18 | Focus Mode | Views | New | Public Alpha | [WRK-026](../product/features/workspace.md#wrk-026), [ENG-037](../product/features/engine.md#eng-037) | Planned 2 |  |
| S-WIN-19 | Floating link preview and Link Inspector | Views | Upstream | Public Alpha | [WRK-007](../product/features/workspace.md#wrk-007), [SHD-016](../product/features/shield.md#shd-016) | Planned 2 |  |
| S-WIN-14 | Workspace and identity switcher | Views | New | Public Beta | [WRK-004](../product/features/workspace.md#wrk-004), [WRK-010](../product/features/workspace.md#wrk-010), [WRK-011](../product/features/workspace.md#wrk-011), [WRK-012](../product/features/workspace.md#wrk-012), [WRK-009](../product/features/workspace.md#wrk-009) | Planned 5 |  |

## Internal pages (WebUI)

| ID | Surface | Tech | Base | Phase | Features | Status | Notes |
|---|---|---|---|---|---|---|---|
| S-WEB-06 | Settings: Privacy and security | WebUI | Upstream | Technical Foundation | [CORE-046](../product/features/core.md#core-046), [CORE-047](../product/features/core.md#core-047), [CORE-050](../product/features/core.md#core-050), [CORE-012](../product/features/core.md#core-012), [SHD-015](../product/features/shield.md#shd-015), [SHD-020](../product/features/shield.md#shd-020), [SHD-027](../product/features/shield.md#shd-027), [SHD-019](../product/features/shield.md#shd-019) | Planned 7, Research 1 | Secure DNS default and HTTPS-Only live here from Technical Foundation. |
| S-WEB-17 | About Brumel and updates | WebUI | Upstream | Technical Foundation | [CORE-004](../product/features/core.md#core-004), [CORE-051](../product/features/core.md#core-051) | In Development 1, Planned 1 | Version, channel, update state, licences. |
| S-WEB-18 | Brumel module page (chrome://brumel) | WebUI | New | Technical Foundation | [CORE-005](../product/features/core.md#core-005) | Planned 1 | First Brumel WebUI page: lists registered modules and their state. |
| S-WEB-36 | Security interstitials | WebUI | Upstream | Technical Foundation | [CORE-047](../product/features/core.md#core-047), [CORE-050](../product/features/core.md#core-050), [SHD-008](../product/features/shield.md#shd-008) | Planned 3 | Security surface: upstream layout and wording; branding only. |
| S-WEB-01 | New Tab page | WebUI | New | Internal Alpha | [UI-022](../product/features/interface.md#ui-022) (related: [UI-018](../product/features/interface.md#ui-018), [MEM-019](../product/features/memory.md#mem-019), [WRK-035](../product/features/workspace.md#wrk-035)) | Planned 1 | Replaces the upstream page, which depends on Google services. |
| S-WEB-02 | Settings: shell, search and navigation | WebUI | Upstream | Internal Alpha | [UI-001](../product/features/interface.md#ui-001), [UI-019](../product/features/interface.md#ui-019), [CON-025](../product/features/connect.md#con-025) | Planned 3 | Chromium settings (Polymer/Lit) with Brumel sections added. |
| S-WEB-03 | Settings: Appearance | WebUI | Upstream | Internal Alpha | [UI-003](../product/features/interface.md#ui-003), [UI-014](../product/features/interface.md#ui-014), [UI-005](../product/features/interface.md#ui-005), [UI-011](../product/features/interface.md#ui-011), [UI-012](../product/features/interface.md#ui-012), [UI-013](../product/features/interface.md#ui-013), [UI-017](../product/features/interface.md#ui-017), [ENG-017](../product/features/engine.md#eng-017), [UI-002](../product/features/interface.md#ui-002), [UI-006](../product/features/interface.md#ui-006) | Planned 8, Research 2 |  |
| S-WEB-04 | Settings: Performance | WebUI | Upstream | Internal Alpha | [ENG-033](../product/features/engine.md#eng-033), [ENG-011](../product/features/engine.md#eng-011), [ENG-019](../product/features/engine.md#eng-019), [ENG-024](../product/features/engine.md#eng-024), [ENG-045](../product/features/engine.md#eng-045), [ENG-005](../product/features/engine.md#eng-005), [ENG-006](../product/features/engine.md#eng-006), [ENG-039](../product/features/engine.md#eng-039), [ENG-040](../product/features/engine.md#eng-040), [ENG-008](../product/features/engine.md#eng-008) | Planned 10 | Extends upstream Performance settings. |
| S-WEB-05 | Settings: Clean Web | WebUI | New | Internal Alpha | [SHD-001](../product/features/shield.md#shd-001), [SHD-002](../product/features/shield.md#shd-002), [SHD-003](../product/features/shield.md#shd-003), [SHD-005](../product/features/shield.md#shd-005), [SHD-007](../product/features/shield.md#shd-007), [SHD-004](../product/features/shield.md#shd-004), [SHD-006](../product/features/shield.md#shd-006), [SHD-031](../product/features/shield.md#shd-031) | Planned 6, Research 2 |  |
| S-WEB-07 | Settings: Site settings | WebUI | Upstream | Internal Alpha | [CORE-045](../product/features/core.md#core-045), [SHD-012](../product/features/shield.md#shd-012), [ENG-042](../product/features/engine.md#eng-042), [TLS-021](../product/features/tools.md#tls-021) | Planned 4 |  |
| S-WEB-08 | Settings: Profiles and local mode | WebUI | Upstream | Internal Alpha | [CORE-026](../product/features/core.md#core-026), [CON-025](../product/features/connect.md#con-025) | Planned 2 | Replaces the Google account card with a local profile card. |
| S-WEB-09 | Settings: Passwords and autofill | WebUI | Upstream | Internal Alpha | [CORE-023](../product/features/core.md#core-023), [CORE-024](../product/features/core.md#core-024), [CORE-025](../product/features/core.md#core-025), [SHD-022](../product/features/shield.md#shd-022) | Planned 4 | Upstream password manager page, branded. |
| S-WEB-10 | Settings: Languages and spellcheck | WebUI | Upstream | Internal Alpha | [CORE-039](../product/features/core.md#core-039), [CORE-014](../product/features/core.md#core-014), [CORE-034](../product/features/core.md#core-034) | Planned 3 |  |
| S-WEB-11 | Settings: Startup and sessions | WebUI | Upstream | Internal Alpha | [ENG-043](../product/features/engine.md#eng-043), [WRK-023](../product/features/workspace.md#wrk-023), [WRK-024](../product/features/workspace.md#wrk-024) | Planned 3 |  |
| S-WEB-13 | Settings: Accessibility Studio | WebUI | Upstream | Internal Alpha | [TLS-022](../product/features/tools.md#tls-022), [UI-014](../product/features/interface.md#ui-014) | Planned 2 |  |
| S-WEB-16 | Settings: Backups, settings history and reset | WebUI | New | Internal Alpha | [MEM-011](../product/features/memory.md#mem-011), [MEM-012](../product/features/memory.md#mem-012), [ENG-016](../product/features/engine.md#eng-016) | Planned 3 |  |
| S-WEB-19 | History | WebUI | Upstream | Internal Alpha | [CORE-030](../product/features/core.md#core-030), [MEM-018](../product/features/memory.md#mem-018), [MEM-026](../product/features/memory.md#mem-026) | Planned 2, Research 1 |  |
| S-WEB-20 | Downloads | WebUI | Upstream | Internal Alpha | [CORE-031](../product/features/core.md#core-031), [CORE-050](../product/features/core.md#core-050), [TLS-001](../product/features/tools.md#tls-001), [TLS-002](../product/features/tools.md#tls-002), [TLS-003](../product/features/tools.md#tls-003), [TLS-004](../product/features/tools.md#tls-004), [TLS-005](../product/features/tools.md#tls-005), [MEM-005](../product/features/memory.md#mem-005), [SHD-038](../product/features/shield.md#shd-038) | Planned 7, Research 2 |  |
| S-WEB-21 | Bookmarks manager | WebUI | Upstream | Internal Alpha | [CORE-029](../product/features/core.md#core-029), [WRK-016](../product/features/workspace.md#wrk-016) | Planned 2 |  |
| S-WEB-22 | Extensions | WebUI | Upstream | Internal Alpha | [CORE-022](../product/features/core.md#core-022), [ENG-013](../product/features/engine.md#eng-013), [ENG-044](../product/features/engine.md#eng-044), [SHD-013](../product/features/shield.md#shd-013), [SHD-035](../product/features/shield.md#shd-035) | Planned 5 |  |
| S-WEB-23 | Resource monitor | WebUI | Upstream | Internal Alpha | [ENG-031](../product/features/engine.md#eng-031), [ENG-020](../product/features/engine.md#eng-020) | Planned 2 | Upstream task manager is native Views; open question whether Brumel's monitor is a WebUI page. |
| S-WEB-24 | Browser Health (brumel://health) | WebUI | New | Internal Alpha | [ENG-015](../product/features/engine.md#eng-015), [ENG-012](../product/features/engine.md#eng-012), [ENG-014](../product/features/engine.md#eng-014), [ENG-046](../product/features/engine.md#eng-046), [ENG-018](../product/features/engine.md#eng-018) | Planned 5 |  |
| S-WEB-29 | Migration Assistant | WebUI | Upstream | Internal Alpha | [TLS-027](../product/features/tools.md#tls-027), [TLS-037](../product/features/tools.md#tls-037), [CORE-044](../product/features/core.md#core-044) | Planned 3 | Extends the upstream import dialog. |
| S-WEB-30 | Data export (Exit Freedom) | WebUI | New | Internal Alpha | [MEM-030](../product/features/memory.md#mem-030), [CORE-044](../product/features/core.md#core-044) | Planned 2 |  |
| S-WEB-32 | Web App Dock | WebUI | Upstream | Internal Alpha | [WRK-037](../product/features/workspace.md#wrk-037), [CORE-036](../product/features/core.md#core-036) | Planned 2 | Extends chrome://apps. |
| S-WEB-34 | PDF viewer | WebUI | Upstream | Internal Alpha | [CORE-037](../product/features/core.md#core-037), [TLS-017](../product/features/tools.md#tls-017) | Planned 1, Research 1 |  |
| S-WEB-35 | Private window New Tab page | WebUI | Upstream | Internal Alpha | [CORE-027](../product/features/core.md#core-027), [SHD-028](../product/features/shield.md#shd-028) | Planned 1, Research 1 | States plainly what private mode does and does not protect. |
| S-WEB-12 | Settings: Shortcuts and gestures | WebUI | New | Public Alpha | [UI-015](../product/features/interface.md#ui-015), [TLS-028](../product/features/tools.md#tls-028) | Planned 2 |  |
| S-WEB-25 | Glass Box (brumel://glass-box) | WebUI | New | Public Alpha | [SHD-034](../product/features/shield.md#shd-034), [SHD-027](../product/features/shield.md#shd-027) | Planned 2 | Every connection the browser itself makes, and the telemetry preview. |
| S-WEB-26 | Privacy Receipt and Permission Timeline | WebUI | New | Public Alpha | [SHD-014](../product/features/shield.md#shd-014), [SHD-011](../product/features/shield.md#shd-011) | Planned 2 |  |
| S-WEB-27 | Recovery center and Time Machine (brumel://memory) | WebUI | New | Public Alpha | [MEM-006](../product/features/memory.md#mem-006), [MEM-001](../product/features/memory.md#mem-001), [MEM-004](../product/features/memory.md#mem-004), [MEM-013](../product/features/memory.md#mem-013), [MEM-020](../product/features/memory.md#mem-020), [WRK-021](../product/features/workspace.md#wrk-021), [WRK-024](../product/features/workspace.md#wrk-024) | Planned 7 |  |
| S-WEB-28 | Library: archive, reading queue, highlights | WebUI | New | Public Alpha | [WRK-021](../product/features/workspace.md#wrk-021), [WRK-032](../product/features/workspace.md#wrk-032), [WRK-028](../product/features/workspace.md#wrk-028), [WRK-035](../product/features/workspace.md#wrk-035), [MEM-003](../product/features/memory.md#mem-003), [MEM-025](../product/features/memory.md#mem-025) | Planned 4, Research 2 |  |
| S-WEB-31 | Rules editor | WebUI | New | Public Alpha | [WRK-030](../product/features/workspace.md#wrk-030), [WRK-009](../product/features/workspace.md#wrk-009), [WRK-013](../product/features/workspace.md#wrk-013), [ENG-040](../product/features/engine.md#eng-040), [TLS-001](../product/features/tools.md#tls-001) | Planned 5 | One editor shared by every rule-based feature. |
| S-WEB-33 | Reader view | WebUI | Upstream | Public Alpha | [TLS-018](../product/features/tools.md#tls-018), [TLS-019](../product/features/tools.md#tls-019), [TLS-020](../product/features/tools.md#tls-020) | Planned 2, Research 1 | Upstream reading mode lives in the side panel. |
| S-WEB-37 | Built-in benchmark | WebUI | New | Public Alpha | [ENG-046](../product/features/engine.md#eng-046) | Planned 1 |  |
| S-WEB-14 | Settings: Brumel Nano | WebUI | New | Public Beta | [NANO-002](../product/features/nano.md#nano-002), [NANO-003](../product/features/nano.md#nano-003), [NANO-005](../product/features/nano.md#nano-005), [NANO-025](../product/features/nano.md#nano-025), [NANO-026](../product/features/nano.md#nano-026), [NANO-027](../product/features/nano.md#nano-027), [ENG-038](../product/features/engine.md#eng-038) | Research 7 | Off until enabled; shows models, size and where data goes. |
| S-WEB-15 | Settings: Connect and sync | WebUI | New | Public Beta | [CON-005](../product/features/connect.md#con-005), [CON-006](../product/features/connect.md#con-006), [CON-007](../product/features/connect.md#con-007), [CON-009](../product/features/connect.md#con-009), [CON-016](../product/features/connect.md#con-016), [CON-018](../product/features/connect.md#con-018), [CON-020](../product/features/connect.md#con-020) | Research 7 | Replaces Google sync settings. |
| S-WEB-38 | JSON viewer | WebUI | New | Public Beta | [DEV-003](../product/features/dev.md#dev-003) | Planned 1 |  |

## Dialogs, bubbles and panels

| ID | Surface | Tech | Base | Phase | Features | Status | Notes |
|---|---|---|---|---|---|---|---|
| S-DLG-01 | Profile picker | WebUI | Upstream | Internal Alpha | [CORE-026](../product/features/core.md#core-026), [CORE-028](../product/features/core.md#core-028) | Planned 2 | No Google sign-in card. |
| S-DLG-03 | Permission prompts | Views | Upstream | Internal Alpha | [CORE-045](../product/features/core.md#core-045), [SHD-012](../product/features/shield.md#shd-012), [SHD-005](../product/features/shield.md#shd-005) | Planned 3 | Security surface: upstream layout; adds 'this visit only'. |
| S-DLG-04 | Session restore and crash recovery | Views | Upstream | Internal Alpha | [WRK-023](../product/features/workspace.md#wrk-023), [ENG-014](../product/features/engine.md#eng-014), [MEM-006](../product/features/memory.md#mem-006) | Planned 3 |  |
| S-DLG-10 | Screenshot and full-page capture | Views | Upstream | Internal Alpha | [CORE-043](../product/features/core.md#core-043), [TLS-016](../product/features/tools.md#tls-016) | Planned 2 |  |
| S-DLG-11 | Print preview | WebUI | Upstream | Internal Alpha | [CORE-038](../product/features/core.md#core-038) | Planned 1 | Branding only. |
| S-DLG-02 | Clear data and Smart Cleanup | WebUI | Upstream | Public Alpha | [SHD-015](../product/features/shield.md#shd-015), [MEM-020](../product/features/memory.md#mem-020) | Planned 2 |  |
| S-DLG-05 | Smart Optimize review | Views | New | Public Alpha | [ENG-018](../product/features/engine.md#eng-018), [MEM-020](../product/features/memory.md#mem-020) | Planned 2 |  |
| S-DLG-06 | Extension Passport change review | Views | New | Public Alpha | [SHD-035](../product/features/shield.md#shd-035) | Planned 1 |  |
| S-DLG-07 | Self Repair | WebUI | New | Public Alpha | [SHD-010](../product/features/shield.md#shd-010) | Research 1 |  |
| S-DLG-08 | Clipboard Guard notice | Views | New | Public Alpha | [SHD-017](../product/features/shield.md#shd-017) | Planned 1 |  |
| S-DLG-09 | Smart Upload | Views | New | Public Alpha | [TLS-033](../product/features/tools.md#tls-033) | Planned 1 |  |
| S-DLG-14 | Tab Snooze picker | Views | New | Public Alpha | [WRK-031](../product/features/workspace.md#wrk-031) | Planned 1 |  |
| S-DLG-15 | Selection actions menu | Views | Upstream | Public Alpha | [TLS-031](../product/features/tools.md#tls-031), [MEM-021](../product/features/memory.md#mem-021), [TLS-030](../product/features/tools.md#tls-030), [TLS-038](../product/features/tools.md#tls-038) | Planned 3, Research 1 | Extends the context menu. |
| S-DLG-17 | Guaranteed Exit overlay | Views | New | Public Alpha | [SHD-032](../product/features/shield.md#shd-032) | Planned 1 | Drawn by the browser above web content; pages cannot style or cover it. |
| S-DLG-12 | Device pairing and send tab | WebUI | New | Public Beta | [CON-013](../product/features/connect.md#con-013), [CON-004](../product/features/connect.md#con-004), [CON-015](../product/features/connect.md#con-015) | Research 3 |  |
| S-DLG-13 | OS authentication lock | Views | New | Public Beta | [SHD-019](../product/features/shield.md#shd-019), [WRK-012](../product/features/workspace.md#wrk-012) | Planned 2 | Uses the OS prompt (Windows Hello, polkit); Brumel only frames it. |
| S-DLG-16 | Media overlays (cinema, captions, recording) | Views | Upstream | Public Beta | [TLS-011](../product/features/tools.md#tls-011), [TLS-013](../product/features/tools.md#tls-013), [TLS-015](../product/features/tools.md#tls-015) | Planned 1, Research 2 | Recording must always show a visible indicator. |

## Installer, first run and OS integration

| ID | Surface | Tech | Base | Phase | Features | Status | Notes |
|---|---|---|---|---|---|---|---|
| S-INS-01 | Windows installer | Installer | Upstream | Technical Foundation | [CORE-009](../product/features/core.md#core-009), [CORE-004](../product/features/core.md#core-004) | In Development 1, Planned 1 | Open question: Chromium's mini_installer shows almost no UI. Keep it silent and rely on first run, or add an installer window. |
| S-INS-02 | Windows uninstall dialog | Views | Upstream | Technical Foundation | [CORE-009](../product/features/core.md#core-009) | Planned 1 | Offers to keep or delete local data, with no retention prompts. |
| S-INS-03 | App icon, taskbar and desktop entries | Assets | Upstream | Technical Foundation | [CORE-004](../product/features/core.md#core-004), [CORE-010](../product/features/core.md#core-010) | In Development 1, Planned 1 | Blocked on the final logo; icon set is pending. |
| S-INS-04 | First-run welcome | WebUI | Upstream | Internal Alpha | [CON-025](../product/features/connect.md#con-025), [UI-018](../product/features/interface.md#ui-018), [UI-003](../product/features/interface.md#ui-003), [UI-019](../product/features/interface.md#ui-019), [ENG-004](../product/features/engine.md#eng-004), [SHD-034](../product/features/shield.md#shd-034) | Planned 6 | No account, no sign-in. Three steps at most: look, import, done. |
| S-INS-05 | First-run import step | WebUI | Upstream | Internal Alpha | [CORE-044](../product/features/core.md#core-044), [TLS-027](../product/features/tools.md#tls-027) | Planned 2 | Full Migration Assistant arrives in Public Alpha. |
| S-INS-06 | Default browser prompt | Views | Upstream | Public Alpha | [UI-019](../product/features/interface.md#ui-019) | Planned 1 | Upstream infobar. Asked once at first run, never repeated (UI-019 acceptance). |

## Catalog coverage

187 catalog features appear on at least one surface. Features without a
surface are build, engine or service work with no screen of their own (for example
the patch series, sandboxing or the sync relay); their effects show up on the
surfaces above, such as Glass Box or Browser Health.
