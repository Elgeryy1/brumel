<!-- SPDX-License-Identifier: MPL-2.0 -->
# Interface mockups

> **Status: Research.** Static HTML mockups of Brumel's first screens. They fix layout,
> states and tokens for later Views and WebUI work. They are not product code, and the
> browser they show does not exist yet.

Open any file directly in a browser; nothing loads from the network. Each page has a theme
switch (system, light, dark and OLED) and a state sheet below the window. Add `?theme=dark`
to the address to open a page in one theme.

| Mockup | Surfaces | Catalog | Phase |
|---|---|---|---|
| [main-window.html](main-window.html) | Tab strip, toolbar, Clean Web button, New Tab page | UI-018, WRK-001, ENG-019, SHD-001, UI-022 | Internal Alpha |
| [vertical-tabs.html](vertical-tabs.html) | Vertical tab sidebar, per-site Clean Web panel | WRK-001, SHD-001, SHD-002, SHD-003, SHD-005, SHD-007 | Internal Alpha |
| [settings.html](settings.html) | Settings shell, Performance, Clean Web | ENG-033, ENG-019, ENG-011, SHD-001 to SHD-007 | Internal Alpha |
| [about.html](about.html) | About Brumel and the update states | CORE-004, CORE-051 | Technical Foundation |
| [modules.html](modules.html) | `chrome://brumel` module page | CORE-005 | Technical Foundation |
| [first-run.html](first-run.html) | First run, import and the default-browser question | CON-025, CORE-044, UI-003, UI-019 | Internal Alpha |

Rules the mockups follow:

- Every colour, font, space and motion value comes from
  [`../tokens/tokens.css`](../tokens/tokens.css); none is written in the pages.
- Sample content is marked as sample on each page. No figure is a measurement.
- Icons are one stroke set in [`_icons.svg`](_icons.svg), inlined into each page by
  `python3 scripts/design/inline_icons.py` because browsers block cross-file SVG references
  from local files.
- The Hallmark record (stamp, waivers and review outcome) is in the header of
  [`mockups.css`](mockups.css). Render-tier screenshots go to `.hallmark/`, which is not
  committed.

See [INTERFACE.md](../INTERFACE.md) for how each screen maps to Chromium.
