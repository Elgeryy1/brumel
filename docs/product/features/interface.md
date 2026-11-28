<!-- GENERATED FILE — Do not edit by hand. Source: docs/product/catalog/*.json. Regenerate: python scripts/catalog/render_features.py -->

# Personalization and interface

> **Project status: Pre-development.** Nothing listed here is available yet. Statuses, priorities and phases are proposals. See the [catalog index and legend](../FEATURES.md#legend).

22 entries. Epics in this module:

- **EP-UI-01** UI shell, design system and progressive discovery — phase 2 (Internal Alpha), P0
- **EP-UI-02** Themes and customization — phase 3 (Public Alpha), P2

| ID | Name | Tier | Status | Priority | Phase |
| --- | --- | --- | --- | --- | --- |
| [UI-001](#ui-001) | Modern minimalist design | Essential | Planned | P0 | 2 |
| [UI-002](#ui-002) | Mica and transparency | Secondary | Research | P3 | 4 |
| [UI-003](#ui-003) | Dark and light mode | Essential | Planned | P0 | 2 |
| [UI-004](#ui-004) | OLED black theme *(→ ENG-017)* | Secondary | Planned | P3 | 4 |
| [UI-005](#ui-005) | Accent colors | Secondary | Planned | P3 | 4 |
| [UI-006](#ui-006) | Dynamic themes | Experimental | Research | P3 | 4 |
| [UI-007](#ui-007) | Advanced theme editor | Secondary | Research | P3 | 4 |
| [UI-008](#ui-008) | Controlled CSS customization | Experimental | Research | P3 | 6 |
| [UI-009](#ui-009) | Community theme store | Community | Deferred | P3 | 6 |
| [UI-010](#ui-010) | Customizable sidebar | Secondary | Planned | P2 | 3 |
| [UI-011](#ui-011) | Compact mode | Secondary | Planned | P2 | 3 |
| [UI-012](#ui-012) | Hide UI elements | Secondary | Planned | P2 | 3 |
| [UI-013](#ui-013) | Configurable animations | Secondary | Planned | P3 | 3 |
| [UI-014](#ui-014) | Reduced motion | Essential | Planned | P1 | 2 |
| [UI-015](#ui-015) | Custom shortcuts | Secondary | Planned | P2 | 3 |
| [UI-016](#ui-016) | Command palette *(→ WRK-018)* | Flagship | Planned | P1 | 3 |
| [UI-017](#ui-017) | Touch support | Secondary | Planned | P2 | 3 |
| [UI-018](#ui-018) | Familiar default layout | Essential | Planned | P0 | 2 |
| [UI-019](#ui-019) | Progressive disclosure | Essential | Planned | P1 | 3 |
| [UI-020](#ui-020) | Progressive Discovery *(→ UI-019)* | Essential | Planned | P1 | 3 |
| [UI-021](#ui-021) | Configuration Recipes | Community | Research | P3 | 4 |
| [UI-022](#ui-022) | Quiet New Tab page | Essential | Planned | P1 | 2 |

<a id="ui-001"></a>

## UI-001 — Modern minimalist design

`Essential` · `Planned` · **P0** · Impact High · Complexity L · Phase 2 (Internal Alpha) · Pillar Everyday Tools · Epic EP-UI-01 (UI shell, design system and progressive discovery)

Brumel's native Views UI design: calm, minimal chrome following the design system.

- **Problem:** Feature-rich browsers often look cluttered.
- **Use case:** A new user sees a familiar, uncluttered window with no promotional UI.
- **Segments:** Everyday users, Power users
- **Dependencies:** [CORE-004](core.md#core-004)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — must respect GPU/battery budgets (animations, transparency). · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low
- **Competitors / precedents:** Zen, Arc, Vivaldi, Opera GX, Edge
- **Evidence:** Competitor precedent; visual preferences validated through community feedback.
- **Acceptance criteria:**
  - Matches design system tokens
  - Keyboard and screen reader accessible
  - No ads or promotional surfaces
- **Origin:** H · **Duplicate of:** —
- **Limitations / notes:** Native Views UI changes are patches to upstream UI code; a heavily redesigned chrome multiplies rebase conflicts, so redesign must be incremental.

<a id="ui-002"></a>

## UI-002 — Mica and transparency

`Secondary` · `Research` · **P3** · Impact Low · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-UI-02 (Themes and customization)

Windows 11 Mica/Acrylic backdrop and Linux compositor transparency where supported.

- **Problem:** Users want the browser to feel native to the OS.
- **Use case:** On Windows 11, the toolbar uses Mica.
- **Segments:** Everyday users, Power users
- **Dependencies:** [UI-001](#ui-001)
- **Platforms:** Windows Planned · Linux Research · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — must respect GPU/battery budgets (animations, transparency). · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low
- **Competitors / precedents:** Zen, Arc, Vivaldi, Opera GX, Edge
- **Evidence:** Competitor precedent; visual preferences validated through community feedback.
- **Acceptance criteria:**
  - Off under Battery Saver
  - Fallback on unsupported systems
- **Origin:** H · **Duplicate of:** —
- **Limitations / notes:** Mica/Acrylic only exist on Windows 11 and cost GPU power; Linux transparency depends on the compositor and may look inconsistent.

<a id="ui-003"></a>

## UI-003 — Dark and light mode

`Essential` · `Planned` · **P0** · Impact High · Complexity S · Phase 2 (Internal Alpha) · Pillar Everyday Tools · Epic EP-UI-01 (UI shell, design system and progressive discovery)

Follow OS theme or set dark/light manually.

- **Problem:** Users need comfortable themes.
- **Use case:** UI follows the OS dark mode.
- **Segments:** Everyday users, Power users
- **Dependencies:** [UI-001](#ui-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — must respect GPU/battery budgets (animations, transparency). · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low
- **Competitors / precedents:** Zen, Arc, Vivaldi, Opera GX, Edge
- **Evidence:** Competitor precedent; visual preferences validated through community feedback.
- **Acceptance criteria:**
  - System, light, dark options
- **Origin:** H · **Duplicate of:** —
- **Limitations / notes:** Web content theming depends on sites supporting prefers-color-scheme; forced dark mode for web content is a separate, imperfect upstream feature.

<a id="ui-004"></a>

## UI-004 — OLED black theme

`Secondary` · `Planned` · **P3** · Impact Low · Complexity S · Phase 4 (Public Beta) · Pillar Efficiency · Epic EP-ENG-02 (Adaptive engine, budgets and performance profiles)

Tracked together with ENG-017 (OLED Protection).

- **Problem:** Static UI on OLED displays can cause burn-in over time.
- **Use case:** Pure black UI theme.
- **Segments:** Everyday users, Laptop users, Low-end hardware users
- **Dependencies:** [ENG-017](engine.md#eng-017)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android N/A
- **AI:** None · **Resource cost:** Low — sampling and policy evaluation in the browser process; must be measured. · **Infrastructure cost:** None
- **Security risk:** Low — must not weaken process isolation.
- **Privacy risk:** Low — resource data stays local.
- **Competitors / precedents:** Opera GX, Vivaldi
- **Evidence:** Hypothesis: resource savings must be proven with the public benchmark suite.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of ENG-017
  - Use case verified: Pure black UI theme.
- **Origin:** H · **Duplicate of:** [ENG-017](engine.md#eng-017)
- **Limitations / notes:** Technical duplicate merged into ENG-017; kept as its own entry to preserve the use case and traceability.

<a id="ui-005"></a>

## UI-005 — Accent colors

`Secondary` · `Planned` · **P3** · Impact Low · Complexity S · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-UI-02 (Themes and customization)

Choose accent colors, optionally from OS.

- **Problem:** Personalization is part of comfort.
- **Use case:** A user picks a blue accent.
- **Segments:** Everyday users, Power users
- **Dependencies:** [UI-001](#ui-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — must respect GPU/battery budgets (animations, transparency). · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low
- **Competitors / precedents:** Zen, Arc, Vivaldi, Opera GX, Edge
- **Evidence:** Competitor precedent; visual preferences validated through community feedback.
- **Acceptance criteria:**
  - Contrast checked automatically
- **Origin:** H · **Duplicate of:** —
- **Limitations / notes:** Accent colors must be constrained to keep WCAG contrast; some combinations will be refused or adjusted automatically.

<a id="ui-006"></a>

## UI-006 — Dynamic themes

`Experimental` · `Research` · **P3** · Impact Low · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-UI-02 (Themes and customization)

Theme tint from site colors or wallpaper, per workspace.

- **Problem:** Workspaces are hard to distinguish.
- **Use case:** Work workspace is tinted blue, Personal green.
- **Segments:** Everyday users, Power users
- **Dependencies:** [UI-005](#ui-005), [WRK-004](workspace.md#wrk-004)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — must respect GPU/battery budgets (animations, transparency). · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low
- **Competitors / precedents:** Vivaldi, Arc, Zen
- **Evidence:** Competitor precedent; visual preferences validated through community feedback.
- **Acceptance criteria:**
  - Contrast always meets WCAG AA
- **Origin:** H · **Duplicate of:** —
- **Limitations / notes:** Site-derived colors can produce low-contrast or garish UI; dynamic theming adds repaint work.

<a id="ui-007"></a>

## UI-007 — Advanced theme editor

`Secondary` · `Research` · **P3** · Impact Low · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-UI-02 (Themes and customization)

Visual editor for theme tokens (colors, radius, density).

- **Problem:** Theme customization requires code.
- **Use case:** A user creates and exports a theme.
- **Segments:** Everyday users, Power users
- **Dependencies:** [UI-005](#ui-005)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — must respect GPU/battery budgets (animations, transparency). · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low
- **Competitors / precedents:** Zen, Arc, Vivaldi, Opera GX, Edge
- **Evidence:** Competitor precedent; visual preferences validated through community feedback.
- **Acceptance criteria:**
  - Token-based
  - Export/import
- **Origin:** H · **Duplicate of:** —
- **Limitations / notes:** Exposing too many tokens makes themes fragile across Brumel updates; theme compatibility must be versioned.

<a id="ui-008"></a>

## UI-008 — Controlled CSS customization

`Experimental` · `Research` · **P3** · Impact Low · Complexity L · Phase 6 (Future) · Pillar Everyday Tools · Epic EP-UI-02 (Themes and customization)

Limited, sandboxed styling hooks for the browser UI (not arbitrary code).

- **Problem:** Power users want deep customization (like Zen/Firefox userChrome).
- **Use case:** A user hides a toolbar element via a supported style hook.
- **Segments:** Everyday users, Power users
- **Dependencies:** [UI-007](#ui-007)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — must respect GPU/battery budgets (animations, transparency). · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low
- **Competitors / precedents:** Zen, Arc, Vivaldi, Opera GX, Edge
- **Evidence:** Competitor precedent; visual preferences validated through community feedback.
- **Acceptance criteria:**
  - No script execution
  - Breakage isolated
  - Reset button
- **Origin:** H · **Duplicate of:** —
- **Limitations / notes:** Native Views UI is not CSS-based; only WebUI surfaces can support CSS hooks. Moved to Future.

<a id="ui-009"></a>

## UI-009 — Community theme store

`Community` · `Deferred` · **P3** · Impact Low · Complexity L · Phase 6 (Future) · Pillar Everyday Tools · Epic EP-UI-02 (Themes and customization)

Community-submitted themes with review.

- **Problem:** Users want to share themes.
- **Use case:** A user installs a community theme.
- **Segments:** Everyday users, Power users
- **Dependencies:** [UI-007](#ui-007)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — must respect GPU/battery budgets (animations, transparency). · **Infrastructure cost:** Low/Medium — hosting and moderation.
- **Security risk:** Low
- **Privacy risk:** Low
- **Competitors / precedents:** Zen, Arc, Vivaldi, Opera GX, Edge
- **Evidence:** Competitor precedent; visual preferences validated through community feedback.
- **Acceptance criteria:**
  - Themes are data-only
  - Review process defined
- **Origin:** H · **Duplicate of:** —
- **Limitations / notes:** A store requires moderation, hosting and a takedown process; data-only themes limit what creators can do.

<a id="ui-010"></a>

## UI-010 — Customizable sidebar

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity M · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-UI-02 (Themes and customization)

Choose sidebar contents (tabs, panels, bookmarks, tools) and position.

- **Problem:** One layout does not fit all.
- **Use case:** A user moves the sidebar to the right and adds Reading Queue.
- **Segments:** Everyday users, Power users
- **Dependencies:** [WRK-001](workspace.md#wrk-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — must respect GPU/battery budgets (animations, transparency). · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low
- **Competitors / precedents:** Zen, Arc, Vivaldi, Opera GX, Edge
- **Evidence:** Competitor precedent; visual preferences validated through community feedback.
- **Acceptance criteria:**
  - Persisted per workspace optional
- **Origin:** H · **Duplicate of:** —
- **Limitations / notes:** More layout options multiply UI test combinations and accessibility checks.

<a id="ui-011"></a>

## UI-011 — Compact mode

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity S · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-UI-01 (UI shell, design system and progressive discovery)

Reduce toolbar heights and paddings.

- **Problem:** Small screens waste vertical space.
- **Use case:** A user on a 13-inch laptop gains vertical space.
- **Segments:** Everyday users, Power users
- **Dependencies:** [UI-001](#ui-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — must respect GPU/battery budgets (animations, transparency). · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low
- **Competitors / precedents:** Zen, Arc, Vivaldi, Opera GX, Edge
- **Evidence:** Competitor precedent; visual preferences validated through community feedback.
- **Acceptance criteria:**
  - Density setting
- **Origin:** H · **Duplicate of:** —
- **Limitations / notes:** Smaller targets reduce touch and accessibility usability; compact mode must stay above minimum target sizes.

<a id="ui-012"></a>

## UI-012 — Hide UI elements

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity S · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-UI-01 (UI shell, design system and progressive discovery)

Hide toolbar buttons and UI elements users do not need, including Brumel features.

- **Problem:** Unused buttons are noise.
- **Use case:** A user hides the Nano button permanently.
- **Segments:** Everyday users, Power users
- **Dependencies:** [UI-001](#ui-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — must respect GPU/battery budgets (animations, transparency). · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low
- **Competitors / precedents:** Zen, Arc, Vivaldi, Opera GX, Edge
- **Evidence:** Competitor precedent; visual preferences validated through community feedback.
- **Acceptance criteria:**
  - Every Brumel button hideable
  - Hidden ≠ disabled clarified
- **Origin:** H · **Duplicate of:** —
- **Limitations / notes:** Hidden features are harder to discover and support; hiding does not disable a module (that is CORE-005).

<a id="ui-013"></a>

## UI-013 — Configurable animations

`Secondary` · `Planned` · **P3** · Impact Low · Complexity S · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-UI-01 (UI shell, design system and progressive discovery)

Control animation speed and type.

- **Problem:** Animations can feel slow or cost battery.
- **Use case:** A user sets fast animations.
- **Segments:** Everyday users, Power users
- **Dependencies:** [UI-001](#ui-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — must respect GPU/battery budgets (animations, transparency). · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low
- **Competitors / precedents:** Zen, Arc, Vivaldi, Opera GX, Edge
- **Evidence:** Competitor precedent; visual preferences validated through community feedback.
- **Acceptance criteria:**
  - Respects OS reduced-motion
- **Origin:** H · **Duplicate of:** —
- **Limitations / notes:** Animation settings only affect Brumel UI, not web content animations.

<a id="ui-014"></a>

## UI-014 — Reduced motion

`Essential` · `Planned` · **P1** · Impact Medium · Complexity S · Phase 2 (Internal Alpha) · Pillar Everyday Tools · Epic EP-UI-01 (UI shell, design system and progressive discovery)

Honor OS reduced-motion and offer a browser-level switch.

- **Problem:** Motion can cause discomfort for vestibular disorders.
- **Use case:** A user disables all UI motion.
- **Segments:** Accessibility users
- **Dependencies:** [UI-001](#ui-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — must respect GPU/battery budgets (animations, transparency). · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low
- **Competitors / precedents:** Zen, Arc, Vivaldi, Opera GX, Edge
- **Evidence:** Competitor precedent; visual preferences validated through community feedback.
- **Acceptance criteria:**
  - All UI animations respect the setting
- **Origin:** H · **Duplicate of:** —
- **Limitations / notes:** Web content may ignore prefers-reduced-motion; Brumel can only reduce motion in its own UI and offer site-level overrides through Accessibility Studio.

<a id="ui-015"></a>

## UI-015 — Custom shortcuts

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity M · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-UI-02 (Themes and customization)

Remap keyboard shortcuts for browser actions.

- **Problem:** Default shortcuts conflict with apps or habits.
- **Use case:** A user remaps workspace switching to Alt+1..9.
- **Segments:** Everyday users, Power users
- **Dependencies:** [WRK-018](workspace.md#wrk-018)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — must respect GPU/battery budgets (animations, transparency). · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low
- **Competitors / precedents:** Vivaldi
- **Evidence:** Competitor precedent; visual preferences validated through community feedback.
- **Acceptance criteria:**
  - Conflict detection
  - Export
- **Origin:** H · **Duplicate of:** —
- **Limitations / notes:** Some shortcuts are reserved by the OS or by Chromium security UI (e.g. Guaranteed Exit) and cannot be remapped.

<a id="ui-016"></a>

## UI-016 — Command palette

`Flagship` · `Planned` · **P1** · Impact High · Complexity M · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-WRK-04 (Universal search, quick actions, split view and panels)

Tracked together with WRK-018 (Quick Actions).

- **Problem:** Power features are hidden in menus.
- **Use case:** Search-driven command palette for all actions.
- **Segments:** Power users, Knowledge workers, Students & researchers
- **Dependencies:** [WRK-018](workspace.md#wrk-018)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — UI and metadata only; unloaded tabs cost no renderer memory. · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low — organization metadata stored locally.
- **Competitors / precedents:** Vivaldi, Arc, Opera
- **Evidence:** Competitor precedent: popular in Arc, Vivaldi and Zen; demand to be validated with users.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of WRK-018
  - Use case verified: Search-driven command palette for all actions.
- **Origin:** H · **Duplicate of:** [WRK-018](workspace.md#wrk-018)
- **Limitations / notes:** Technical duplicate merged into WRK-018; kept as its own entry to preserve the use case and traceability.

<a id="ui-017"></a>

## UI-017 — Touch support

`Secondary` · `Planned` · **P2** · Impact Medium · Complexity M · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-UI-01 (UI shell, design system and progressive discovery)

Touch-friendly targets and gestures on touchscreen laptops/tablets.

- **Problem:** Small touch targets on convertibles.
- **Use case:** A user on a 2-in-1 navigates tabs by touch.
- **Segments:** Everyday users, Power users
- **Dependencies:** [UI-001](#ui-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — must respect GPU/battery budgets (animations, transparency). · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low
- **Competitors / precedents:** Zen, Arc, Vivaldi, Opera GX, Edge
- **Evidence:** Competitor precedent; visual preferences validated through community feedback.
- **Acceptance criteria:**
  - Touch mode with larger targets
- **Origin:** H · **Duplicate of:** —
- **Limitations / notes:** Chromium's touch UI on Windows/Linux is less mature than mobile; gestures may conflict with OS-level touch gestures.

<a id="ui-018"></a>

## UI-018 — Familiar default layout

`Essential` · `Planned` · **P0** · Impact High · Complexity S · Phase 2 (Internal Alpha) · Pillar Everyday Tools · Epic EP-UI-01 (UI shell, design system and progressive discovery)

Default layout close to mainstream browsers so new users feel at home; advanced layouts are opt-in.

- **Problem:** Radical defaults scare switchers.
- **Use case:** A Chrome user starts Brumel and immediately knows where everything is.
- **Segments:** Everyday users, Power users
- **Dependencies:** [UI-001](#ui-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — must respect GPU/battery budgets (animations, transparency). · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low
- **Competitors / precedents:** Zen, Arc, Vivaldi, Opera GX, Edge
- **Evidence:** Competitor precedent; visual preferences validated through community feedback.
- **Acceptance criteria:**
  - Default resembles mainstream layout
  - Advanced features off or subtle by default
- **Origin:** H · **Duplicate of:** —
- **Limitations / notes:** A familiar default hides Brumel's differentiators at first; discoverability depends on Progressive disclosure working well.

<a id="ui-019"></a>

## UI-019 — Progressive disclosure

`Essential` · `Planned` · **P1** · Impact High · Complexity M · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-UI-01 (UI shell, design system and progressive discovery)

Advanced features revealed gradually based on use and explicit choice, not all at once.

- **Problem:** Hundreds of features overwhelm users.
- **Use case:** After a user keeps 30+ tabs for a week, Brumel suggests vertical tabs once.
- **Segments:** Everyday users, Power users
- **Dependencies:** [UI-001](#ui-001)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — must respect GPU/battery budgets (animations, transparency). · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low
- **Competitors / precedents:** Zen, Arc, Vivaldi, Opera GX, Edge
- **Evidence:** Competitor precedent; visual preferences validated through community feedback.
- **Acceptance criteria:**
  - Suggestions rate-limited and dismissible forever
  - Local logic only, no telemetry required
  - The default-browser question is asked at most once, at first run, and never repeated
- **Origin:** H · **Duplicate of:** —
- **Limitations / notes:** Usage-based suggestions require local usage tracking; poorly timed suggestions feel like nagging, so frequency must be strictly limited.

<a id="ui-020"></a>

## UI-020 — Progressive Discovery

`Essential` · `Planned` · **P1** · Impact High · Complexity M · Phase 3 (Public Alpha) · Pillar Everyday Tools · Epic EP-UI-01 (UI shell, design system and progressive discovery)

Tracked together with UI-019 (Progressive disclosure).

- **Problem:** Hundreds of features overwhelm users.
- **Use case:** Discover new features according to the user's needs.
- **Segments:** Everyday users, Power users
- **Dependencies:** [UI-019](#ui-019)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — must respect GPU/battery budgets (animations, transparency). · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low
- **Competitors / precedents:** Zen, Arc, Vivaldi, Opera GX, Edge
- **Evidence:** Competitor precedent; visual preferences validated through community feedback.
- **Acceptance criteria:**
  - Covered by the acceptance criteria of UI-019
  - Use case verified: Discover new features according to the user's needs.
- **Origin:** R52-30 · **Duplicate of:** [UI-019](#ui-019)
- **Limitations / notes:** Technical duplicate merged into UI-019; kept as its own entry to preserve the use case and traceability.

<a id="ui-021"></a>

## UI-021 — Configuration Recipes

`Community` · `Research` · **P3** · Impact Medium · Complexity M · Phase 4 (Public Beta) · Pillar Everyday Tools · Epic EP-UI-02 (Themes and customization)

Share configurations (profiles, rules, layout) as files without personal data.

- **Problem:** Good setups cannot be shared easily.
- **Use case:** A user imports a 'Low-end laptop' recipe from the community.
- **Segments:** Everyday users, Power users
- **Dependencies:** [WRK-030](workspace.md#wrk-030), [ENG-039](engine.md#eng-039)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — must respect GPU/battery budgets (animations, transparency). · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low
- **Competitors / precedents:** Zen, Arc, Vivaldi, Opera GX, Edge
- **Evidence:** Competitor precedent; visual preferences validated through community feedback.
- **Acceptance criteria:**
  - Recipes contain no personal data (validated)
  - Preview before applying
  - Reversible
- **Origin:** R52-33 · **Duplicate of:** —
- **Limitations / notes:** Validating that a recipe contains no personal data is hard (URLs, names in rules); applying third-party recipes can weaken privacy settings.

<a id="ui-022"></a>

## UI-022 — Quiet New Tab page

`Essential` · `Planned` · **P1** · Impact High · Complexity S · Phase 2 (Internal Alpha) · Pillar Everyday Tools · Epic EP-UI-01 (UI shell, design system and progressive discovery)

A calm New Tab page with a search box, the user's own shortcuts and an optional resume strip, with no feed, no sponsored tiles and no remote content by default.

- **Problem:** Mainstream New Tab pages carry news feeds, sponsored tiles and remote content that add noise and network requests.
- **Use case:** A user opens a new tab and sees only the search box and the sites they pinned; nothing loads from the network until they type.
- **Segments:** Everyday users, Power users
- **Dependencies:** [UI-001](#ui-001), [UI-018](#ui-018)
- **Platforms:** Windows Planned · Linux Planned · macOS Deferred · Android Deferred
- **AI:** None · **Resource cost:** Low — must respect GPU/battery budgets (animations, transparency). · **Infrastructure cost:** None
- **Security risk:** Low
- **Privacy risk:** Low
- **Competitors / precedents:** Chrome, Edge, Brave, Vivaldi, Firefox
- **Evidence:** Competitor precedent: Firefox and Brave let users turn off New Tab content; Edge and Chrome ship feeds by default.
- **Acceptance criteria:**
  - No network request is made by the New Tab page itself until the user acts
  - No sponsored or remote content, on by default or otherwise
  - Every element can be hidden, including the shortcuts
  - Meets the design-system accessibility baseline in light, dark and forced-colours modes
- **Origin:** H · **Duplicate of:** —
- **Limitations / notes:** Upstream Chromium's New Tab page is tied to Google services; Brumel replaces it with its own WebUI page, which is a larger patch than restyling.
