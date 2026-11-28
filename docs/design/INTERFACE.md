<!-- SPDX-License-Identifier: MPL-2.0 -->
# Brumel Interface Design

> **Status: Research.** No Brumel interface has been built. This document turns the
> [design system](DESIGN_SYSTEM.md) into screens and explains how each screen reaches
> Chromium as a small patch. The mockups are static HTML; they fix layout, states and
> tokens, not final code. Chromium file paths below are **to be verified** against the
> pinned version (`config/upstream.json`) before any patch is written.

## 1. What this covers

| Piece | Where | Source of truth |
|---|---|---|
| Surface inventory | [UI_INVENTORY.md](UI_INVENTORY.md) | [surfaces.json](surfaces.json) + the [feature catalog](../product/catalog/features.json) |
| Tokens | [tokens/tokens.css](tokens/tokens.css), [tokens/CONTRAST.md](tokens/CONTRAST.md) | [tokens/brumel.tokens.json](tokens/brumel.tokens.json) |
| Mockups | [mockups/](mockups/README.md) | The HTML files themselves |
| Principles, palette, type | [DESIGN_SYSTEM.md](DESIGN_SYSTEM.md) | That document |

Regenerate and check everything with:

```sh
python3 scripts/design/render_surfaces.py --check
python3 scripts/design/render_tokens.py --check
python3 scripts/design/inline_icons.py --check
```

## 2. How the interface is built in Chromium

Brumel keeps Chromium's split ([ADR-0005](../architecture/adr/0005-native-ui-no-electron.md)):

- **Native chrome (Views, C++).** The window frame, tab strip, toolbar, omnibox, bubbles,
  infobars and permission prompts. Colours come from the `ui/color` pipeline, so Brumel adds
  a colour mixer instead of hard-coding colours, and themes, high contrast and the OS accent
  keep working.
- **Internal pages (WebUI, TypeScript and Lit).** Settings, history, downloads, the New Tab
  page and every Brumel page. They read the tokens as CSS custom properties
  (`--brumel-color-*`, `--brumel-space-*`). No external framework, font or CDN.
- **Installer and OS integration.** Icons, the uninstall dialog and desktop entries.

Every change is a patch in `patches/` or new code under `//brumel` through the source
overlay. Native Brumel views live under `//brumel/browser/ui/views/`; WebUI pages under
`//brumel/browser/resources/`. Upstream files get the smallest hook that works.

**Security surfaces stay upstream.** The omnibox security indicator, permission prompts,
download warnings, security interstitials and credential bubbles keep Chromium's layout and
wording. Brumel changes them only through the colour mixer, never through custom CSS or new
layout ([DESIGN_SYSTEM.md § 9](DESIGN_SYSTEM.md#9-implementation-notes-chromium)). No design
here disables or weakens a mitigation.

## 3. Tokens

[brumel.tokens.json](tokens/brumel.tokens.json) holds the brand primitives from the design
system and **semantic roles** that surfaces use: `frame`, `toolbar`, `surface`, `raised`,
`hover`, `selected`, `ink`, `ink-muted`, `accent`, `accent-fill`, `accent-fill-hover`,
`on-accent`, `focus`, `control-border`, `divider`, `danger`, `warning` and `success`. Each
role has a value in the light, dark and OLED themes, and a forced-colours mapping to CSS system
colours.

`render_tokens.py` measures every required pair with the WCAG 2.x formula and fails if one
falls short: 4.5:1 for text, 3:1 for focus rings and control borders. The results are in
[CONTRAST.md](tokens/CONTRAST.md). Two rules from the design system carry over: Mist is never
text on light surfaces (`accent` is Mist 700 there), and Slate is never text on dark
surfaces (`ink-muted` is Slate 300 there).

### Mapping roles to Views colour IDs

A Brumel mixer (`//brumel/browser/ui/color/brumel_color_mixer.cc`, registered with one line in
Chromium's mixer list) defines Brumel colour IDs from the roles and points the upstream IDs at
them. The upstream IDs below are the likely targets and must be checked on the pinned version.

| Role | Brumel colour ID | Upstream IDs it feeds (to verify) |
|---|---|---|
| `frame` | `kColorBrumelFrame` | `kColorFrameActive`, `kColorFrameInactive`, `kColorTabBackgroundInactiveFrameActive` |
| `toolbar` | `kColorBrumelToolbar` | `kColorToolbar`, `kColorTabBackgroundActiveFrameActive` |
| `hover` | `kColorBrumelHover` | `kColorTabBackgroundInactiveHoverFrameActive`, `kColorToolbarInkDrop` (as a base) |
| `ink`, `ink-muted` | `kColorBrumelInk`, `kColorBrumelInkMuted` | `kColorTabForegroundActiveFrameActive`, `kColorTabForegroundInactiveFrameActive`, `kColorToolbarButtonIcon` |
| `focus` | `kColorBrumelFocus` | `kColorFocusableBorderFocused` |
| `raised` | `kColorBrumelRaised` | `kColorBubbleBackground`, `kColorDialogBackground` |
| `control-border` | `kColorBrumelControlBorder` | `kColorTextfieldOutline` |
| `accent`, `accent-fill`, `on-accent` | `kColorBrumelAccent`, `kColorBrumelAccentFill`, `kColorBrumelOnAccent` | `kColorButtonBackgroundProminent`, `kColorButtonForegroundProminent`, `kColorLinkForeground` |

WebUI already reads many upstream colours as CSS variables (`--color-*` generated from
`ui/color`). Where an upstream WebUI page is only restyled, the mixer is enough; Brumel pages
import `tokens.css` as well so they share one vocabulary.

## 4. The main window

Mockups: [main-window.html](mockups/main-window.html) and
[vertical-tabs.html](mockups/vertical-tabs.html).

- **Familiar by default** (UI-018). Horizontal tabs on top, back, forward and reload, the
  omnibox, then Clean Web, extensions, downloads, the profile and the menu. Vertical tabs are
  opt-in (WRK-001) and extend Chromium's own vertical tab strip.
- **Metrics.** Tabs 34 px tall in a 42 px strip, toolbar 40 px with 32 px buttons and a 44 px
  hit target, omnibox 32 px. The tab strip keeps its right end free for the Windows caption
  buttons (138 px in the mockup; the real value comes from the OS). The vertical sidebar is
  248 px and collapses.
- **Honest tab state, the signature.** A suspended tab (ENG-019) keeps its title and place,
  its favicon sits in a dashed ring, its title turns muted and its accessible name says
  "suspended". Chromium already marks discarded tabs; Brumel restyles that marker rather than
  adding a new one. Pinned, muted and grouped tabs are told apart by shape, an icon and text,
  never by colour alone.
- **Clean Web button** (S-WIN-07). Shows a count only when something was blocked on the
  page, says "Off" when the user turned Clean Web off for the site, and opens a per-site panel
  that names each kind of item blocked. Built as a toolbar action through Chromium's actions
  framework, so the toolbar patch is a registration, not a new layout.
- **Bubbles.** One raised surface, 12 px radius, a hairline, one shadow token. Every bubble
  has a heading, the state in words, and at most one primary action.

## 5. Internal pages

Mockups: [settings.html](mockups/settings.html), [about.html](mockups/about.html),
[modules.html](mockups/modules.html) and the New Tab page inside
[main-window.html](mockups/main-window.html).

- **Settings shell** (S-WEB-02). Chromium's settings page with Brumel sections added through
  its route list and menu. A 240 px side navigation that becomes a scrolling row under
  60rem, a search field, and a 760 px column.
- **Groups and rows.** A section is a heading, one sentence, then one raised panel whose rows
  are split by hairlines. Choices with consequences are radio rows with a sentence each;
  simple on/off settings are switches with a label and a description tied by
  `aria-describedby`. Never a card inside a card.
- **Data regions have four states:** loading (a skeleton in the shape of the rows), empty
  (what belongs there and the one action that fills it), error (what broke, what Brumel does
  about it and a retry) and full. Each mockup carries a state sheet below the window.
- **Undo, not confirmation.** Changing a profile or turning a feature off happens at once and
  offers undo (MEM-020); destructive actions on data confirm.
- **New Tab page** (UI-022). A search field, the user's own shortcuts and a quiet
  "Customize" action. No feed, no sponsored tiles, no request until the user acts.
- **chrome://brumel** (CORE-005). Lists modules with the three gates from
  [MODULE_SYSTEM.md](../architecture/MODULE_SYSTEM.md) and whether an instance exists. A
  Phase 1 build shows the empty state, because no optional module is compiled in yet.

## 6. First run

Mockup: [first-run.html](mockups/first-run.html). Three steps at most, no account
(CON-025): the look (theme and tab layout), an optional import (CORE-044), and the finish,
where the default-browser question is asked once and never again (UI-019). It replaces the
sign-in steps of Chromium's first-run flow. The Windows installer stays silent, as Chromium's
`mini_installer` is, so first run carries all the setup.

## 7. Patch plan for the first screens

Hooks to verify on the pinned Chromium before writing patches. "New" means code under
`//brumel` reached through the overlay.

| Surface | Upstream hook (to verify) | Brumel change | Size |
|---|---|---|---|
| Colours everywhere (S-WIN-01, S-WIN-03) | `chrome/browser/ui/color/chrome_color_mixers.cc` | Register the Brumel mixer | One line plus new code |
| Suspended tab state (S-WIN-01) | `chrome/browser/ui/views/tabs/tab_icon.cc` | Restyle the discard marker as a dashed ring | Small |
| Clean Web button (S-WIN-07) | `chrome/browser/ui/actions/`, toolbar action registration | New action and bubble view | Small hook, new code |
| Settings sections (S-WEB-04, S-WEB-05) | `chrome/browser/resources/settings/route.ts`, settings menu | New Lit pages | Small hook, new code |
| About page (S-WEB-17) | `chrome/browser/resources/settings/about_page/` | Strings via the branding script (ADR-0015); channel row | Small |
| Module page (S-WEB-18) | `chrome/browser/ui/webui/chrome_web_ui_configs.cc` | Register `chrome://brumel` (patch `0004-register-webui`) | One line plus new code |
| New Tab page (S-WEB-01) | `chrome/browser/search/` and the New Tab page WebUI | Point the NTP at a Brumel WebUI page | Medium: the riskiest patch here |
| First run (S-INS-04) | `chrome/browser/ui/webui/intro/` | Replace the sign-in step with the three Brumel steps | Medium |

## 8. Accessibility and motion

Every mockup meets the [design-system baseline](DESIGN_SYSTEM.md#10-accessibility-baseline-acceptance-criteria-for-any-ui-change):
measured contrast in light, dark and OLED, a visible focus ring on every control, keyboard
access, accessible names on icon buttons, state in words as well as colour, forced-colours
rules and reduced motion. Motion uses the `quick` and `standard` tokens on colour and
transform only, and drops to zero under `prefers-reduced-motion`.

The mockups were checked with Hallmark's `sloplint` (static and render tiers, app scope) and
a finish review in fresh context; the record sits in the header of
[mockups.css](mockups/mockups.css). That is a check of the mockups, not of Brumel: the
product still needs its own audit with Narrator, NVDA and Orca (Public Beta exit criteria).

## 9. Open questions

1. **New Tab page patch size.** Replacing the upstream page may touch Google-specific code
   that ungoogled-chromium already removes. Measure before committing to it.
2. **Command palette** (WRK-018). Native popup or a WebUI bubble hosted in Views.
3. **Resource monitor** (ENG-031). Extend the native task manager or build a WebUI page.
4. **Brand typeface.** Chrome uses the system font. Inter or Geist for WebUI headings is
   decided after rendering tests, and only if the gain is worth bundling a font.
5. **Final logo and icon set.** The mark is provisional; app icons wait for it.
