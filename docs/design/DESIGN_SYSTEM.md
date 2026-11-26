# Brumel Design System

> **Status: Research / provisional.** This is the first version of the design system. The
> visual identity is provisional ([branding assets](../../assets/branding/README.md)). No
> browser UI has been built yet, so every token below is a starting point that will be
> checked against real Chromium Views and WebUI surfaces in Phase 1 and Phase 2.

## 1. Design intent

Brumel's slogan is **Less noise. More control.** The interface has to deliver on it:

- **Quiet by default.** At first launch the browser should look and behave like a familiar
  browser: tab strip, omnibox, back/forward. Nothing flashes, nags or animates without a
  reason.
- **Powerful on request.** Advanced capabilities (vertical tabs, workspaces, budgets,
  Brumel Nano, Glass Box…) appear through **progressive disclosure**. You find them in
  context, through the command palette or in settings. They are never pushed by pop-ups.
- **Honest.** Every indicator tells the truth: a suspended tab looks suspended, and a
  blocked request is counted where you can see it. A feature that is off really is off.
- **Calm motion.** Motion explains change and is never decoration. It respects the OS
  "reduce motion" setting by default.
- **Accessible from day one.** Contrast, keyboard access and screen-reader support are
  acceptance criteria, not polish.

## 2. Identity

| Element | Value | Notes |
|---|---|---|
| Name | Brumel / Brumel Browser | "Brumel" alone in UI; "Brumel Browser" in stores and installers |
| Mark | Proposal 03 "Haze" (provisional) | A disk dissolving into two bands of mist |
| Slogan | Less noise. More control. | Provisional |
| Voice | Plain, precise, calm | No hype, no exclamation marks, no fear-based copy |

### Logo usage

- Use `logo/mark.svg` on light surfaces, `logo/mark-dark.svg` on dark surfaces and
  `favicon.svg` (the tile) wherever the background is unknown (taskbars, docks, store
  listings, social cards).
- Leave clear space of at least ¼ of the mark width on every side.
- Minimum size: 16 px for the tile and 20 px for the bare mark.
- Do not stretch, rotate, outline, add effects to, or recolour individual bands outside
  the palette.

## 3. Colour

### 3.1 Brand palette

| Token | Hex | Use |
|---|---|---|
| `graphite` | `#11151C` | Primary ink on light, base surface on dark |
| `mist` | `#9AB9E8` | Accent on dark surfaces, focus and selection highlights |
| `slate` | `#56677F` | Secondary text on light, borders, inactive icons |
| `cloud` | `#F4F6FA` | Base surface on light, primary ink on dark |

### 3.2 Derived tokens (provisional)

| Token | Hex | Why it exists |
|---|---|---|
| `slate-200` | `#7F93AE` | Slate is too dim on Graphite for structural elements |
| `slate-300` | `#8C9BB0` | Secondary text on dark surfaces |
| `mist-700` | `#3B5F95` | Accent that passes AA as text or icon on light surfaces (Mist itself does not) |
| `oled-black` | `#000000` | OLED theme base surface |

### 3.3 Measured contrast (WCAG 2.x relative luminance)

These ratios were computed with the WCAG 2.x formula and are not estimates.

| Foreground on background | Ratio | AA normal text (4.5) | AA large / UI (3.0) |
|---|---|---|---|
| Graphite on Cloud | 16.91 | Pass | Pass |
| Graphite on White | 18.29 | Pass | Pass |
| Slate on Cloud | 5.33 | Pass | Pass |
| Slate on White | 5.77 | Pass | Pass |
| Mist 700 on Cloud | 5.96 | Pass | Pass |
| Mist 700 on White | 6.45 | Pass | Pass |
| **Mist on Cloud** | **1.85** | **Fail** | **Fail** |
| Cloud on Graphite | 16.91 | Pass | Pass |
| Mist on Graphite | 9.13 | Pass | Pass |
| Slate 300 on Graphite | 6.47 | Pass | Pass |
| Slate 200 on Graphite | 5.83 | Pass | Pass |
| **Slate on Graphite** | **3.17** | **Fail** | Pass (non-text only) |
| Cloud on OLED black | 19.41 | Pass | Pass |
| Mist on OLED black | 10.48 | Pass | Pass |
| Slate 300 on OLED black | 7.43 | Pass | Pass |

**Rules that follow from the measurements:**

- Never use `mist` for text, icons or focus rings on light surfaces. Use `mist-700` there.
- Never use `slate` for text on dark surfaces. Use `slate-300`.
- Focus indicators need at least 3:1 against **both** adjacent colours (WCAG 2.2 SC 2.4.11 / 2.4.13).

### 3.4 Themes

| Theme | Surface | Raised surface | Primary text | Secondary text | Accent |
|---|---|---|---|---|---|
| Light | `cloud` | `#FFFFFF` | `graphite` | `slate` | `mist-700` |
| Dark | `graphite` | `#1A202A` | `cloud` | `slate-300` | `mist` |
| OLED (pure black) | `oled-black` | `#0B0D11` | `cloud` | `slate-300` | `mist` |
| System accent | Follows the OS accent colour when the user opts in (Windows accent, GTK/KDE accent where available); contrast is re-validated at runtime, falling back to the brand accent when it fails |

OLED theme notes (feature OLED Protection, see the [feature catalog](../product/FEATURES.md)):
the theme uses true black backgrounds and can optionally dim or auto-hide static chrome
elements after inactivity. Raised surfaces stay slightly lifted so that they remain
distinguishable.

Dynamic themes (colour extracted from the page or the wallpaper) are **Planned**. They must
pass the same contrast checks before they are applied.

## 4. Typography

| Role | Typeface | Licence | Notes |
|---|---|---|---|
| UI (browser chrome) | **System UI font** (Segoe UI Variable on Windows, the system sans on Linux) | n/a | Native Views surfaces follow the OS for familiarity, hinting and language coverage |
| Brand, WebUI headings, website | **Inter** (candidate) or **Geist** (candidate) | SIL OFL 1.1 (both) | The final pick depends on rendering tests at small sizes and on script coverage |
| Code, DevTools-adjacent tools | System monospace; **Geist Mono** (candidate, OFL 1.1) | | |

Type scale for WebUI pages, in px, on a 1.2 ratio rounded to the 4 px grid where possible:
12 · 13 (base UI) · 14 · 16 · 20 · 24 · 32 · 40.
Line height is 1.4 for UI text and 1.6 for long-form text. Body text weight is 400, emphasis
is 500–600, and 700 is never used for UI.

Fonts will only be bundled if WebUI needs them. A bundled font must ship with its licence
and be listed in [THIRD_PARTY_NOTICES.md](../../THIRD_PARTY_NOTICES.md).

## 5. Layout tokens

| Token | Value |
|---|---|
| Base grid | 4 px |
| Spacing scale | 2, 4, 8, 12, 16, 24, 32, 48, 64 |
| Radius | `sm` 4 · `md` 8 · `lg` 12 · `xl` 16 · `full` 9999 |
| Tab strip height | Inherited from Chromium in "familiar" density; reduced in compact density |
| Hit targets | ≥ 24 × 24 px (WCAG 2.2 SC 2.5.8); ≥ 32 px in touch mode |

**Density modes:**

- **Comfortable** is the default and stays close to Chromium's metrics.
- **Compact** uses smaller paddings and a thinner toolbar.
- **Touch** uses larger targets and is enabled automatically on touch-first devices when the OS reports it.

## 6. Motion

| Token | Duration | Easing | Use |
|---|---|---|---|
| `instant` | 0 ms | n/a | When reduce-motion is on, or for state that must feel immediate |
| `quick` | 120 ms | `cubic-bezier(0.2, 0, 0, 1)` | Hover, press, small toggles |
| `standard` | 200 ms | `cubic-bezier(0.2, 0, 0, 1)` | Panels, popovers, tab moves |
| `gentle` | 320 ms | `cubic-bezier(0.3, 0, 0, 1)` | Large layout changes (split view, sidebar) |

Motion rules:

- Respect `prefers-reduced-motion` and the OS settings. With reduced motion, transitions become cross-fades of 120 ms or shorter, or happen instantly.
- No looping animation in the browser UI. The only exception is a progress indicator for real work in progress.
- Animations can be configured in settings. "Off" is a valid choice and is respected everywhere.

## 7. Iconography

- Stroke icons on a 16 px and 20 px grid with a 1.5 px stroke, rounded caps and joins, built
  from simple geometry that echoes the mark.
- Where Chromium already has a recognisable icon (reload, downloads, extensions), keep the
  same **metaphor** for familiarity even if the drawing changes.
- Status icons always come with text or an accessible name. Colour is never the only signal.
- Icons are drawn as vector icons (`.icon` vector format for Views, SVG for WebUI) so that
  they scale crisply and can be themed.

## 8. Interface principles

1. **Familiar by default.** A Chrome user can browse in Brumel without a tutorial.
2. **Progressive disclosure.** A feature shows up when it is relevant, offered once and
   then easy to dismiss forever. This is the Progressive Discovery feature in the catalog.
3. **One way to undo.** Destructive actions (closing groups, clearing data, Smart Optimize)
   offer an undo, which is the Universal Undo feature.
4. **No dark patterns.** No confirmshaming, no default-on upsells, no fake urgency, no
   pre-ticked consent.
5. **Visible state.** Suspended tabs, blocked items, active budgets and AI activity are all
   visible and explainable ("why is this happening?").
6. **Everything optional can be hidden.** Sidebar, buttons, toolbars, badges and counters
   can all be hidden.
7. **Keyboard first, mouse and touch friendly.** Every action can be reached from the
   command palette.

## 9. Implementation notes (Chromium)

- **Native browser chrome (Views).** Brumel defines a colour mixer pipeline (`ui/color`)
  with Brumel colour IDs that map to these tokens, and does not hard-code colours. Themes
  are implemented as color mixers so that they keep working with Chromium's theme and high
  contrast handling.
- **Internal pages (WebUI).** TypeScript and Lit, in line with Chromium's WebUI stack. The
  tokens are exposed as CSS custom properties (`--brumel-color-surface`, …) and kept in sync
  with the `ui/color` values. No external frameworks or CDNs.
- **Windows Mica and transparency.** Planned, behind a setting. Text contrast must hold when
  the effect is unavailable or disabled (battery saver, remote desktop, high contrast).
- **Forced colors / high contrast mode** must be honoured on every surface. WebUI uses
  system colour keywords under `@media (forced-colors: active)`.
- **Custom CSS** (controlled personalisation) is applied only to Brumel's own WebUI surfaces
  inside a constrained scope. It is never injected into web content or into security
  surfaces such as permission prompts, the omnibox security indicator or the download
  warnings.

## 10. Accessibility baseline (acceptance criteria for any UI change)

- Text meets WCAG 2.2 AA contrast (4.5:1, or 3:1 for large text and UI components).
- Full keyboard operability with a visible focus indicator.
- Accessible names and roles on every control, checked with the Windows Narrator, NVDA and
  Orca screen readers.
- Respect for OS text scaling up to 200% without clipping.
- Respect for reduce-motion, high-contrast or forced-colours, and reduced-transparency settings.
- No information conveyed by colour alone.

Accessibility Studio, adaptive reading options and reduced visual stimulation are product
features tracked in the [feature catalog](../product/FEATURES.md). The baseline above applies
to everything, whether or not those features are enabled.
