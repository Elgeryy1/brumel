# Brumel branding assets

> **Status: provisional.** Everything in this folder is an early exploration made during
> Pre-development. The logo, wordmark and palette are **not final** and may change after
> community feedback, a proper trademark search and a professional design review.
> See [`docs/design/DESIGN_SYSTEM.md`](../../docs/design/DESIGN_SYSTEM.md) for tokens and usage,
> and [`docs/research/NAME_CHECK.md`](../../docs/research/NAME_CHECK.md) for the name check.

## Concept

*Brumel* comes from *bruma*, the Spanish word for mist. The identity should feel like
mist: quiet, light and fluid. It should feel calm rather than loud, and still be clear
at the size of a browser tab. We avoided the usual browser clichés on purpose: no globes,
no orbit rings, no flames or animals, no "AI sparkle" stars, no heavy gradients and no 3D
effects.

Palette (provisional):

| Token | Hex | Role |
|---|---|---|
| Graphite | `#11151C` | Primary ink, dark surfaces |
| Mist Blue | `#9AB9E8` | Accent, the single "breath of colour" |
| Slate | `#56677F` | Secondary ink, quiet structure |
| Cloud | `#F4F6FA` | Light surfaces, ink on dark |

Derived tints such as `#7F93AE` (Slate 200) and `#8C9BB0` (Slate 300) are used only where
plain Slate is too dim on Graphite. See the design system for contrast ratios.

## The five proposals

All marks use a `0 0 64 64` view box and are plain SVG paths and shapes, with no filters,
no raster images and no gradients. Each proposal comes in three variants:

- `mark-light.svg` is for light backgrounds.
- `mark-dark.svg` is for dark backgrounds.
- `mark-mono.svg` is a single colour (Graphite). You can recolour it freely as long as the
  contrast stays sufficient.

The contact sheet [`proposals/overview.svg`](proposals/overview.svg) shows every proposal at
128, 32 and 16 px on light and dark backgrounds.

| # | Name | Concept | Strengths | Weaknesses | 16 px legibility |
|---|---|---|---|---|---|
| 01 | [Drift](proposals/01-drift/) | Abstract: three layers of mist that thin out as they drift forward on a diagonal, ending in a droplet | Calm, light, conveys movement and "less noise" | Close to generic "text/menu" glyphs, so it is weak as an app icon | Fair (reads as lines) |
| 02 | [Monogram](proposals/02-monogram/) | A geometric **B** with a short trail of mist leaving its waist | Very legible, easy to own once known, works as a letter in UI | Letter marks are common in software, and the B alone says little about the product | Excellent |
| 03 | [Haze](proposals/03-haze/) | A disk (the page and the light) dissolving into two drifting bands of mist | Distinctive silhouette, calm, timeless, unlike existing browser logos, scales from 16 px to billboard | The banded disk is a known "sunset" motif in retro design, so it needs care to avoid looking derivative | Very good (disk plus one band survive) |
| 04 | [Wake](proposals/04-wake/) | Two curves meeting at a point, like the wake behind a boat: navigation and forward motion | Dynamic, communicates navigation | Reads like a "fast-forward" or "greater than" glyph and is less calm | Good |
| 05 | [Settle](proposals/05-settle/) | A noisy wave that settles into a straight, controlled line ending in a dot: *Less noise. More control.* | Tells the product story literally, very original | Wide aspect ratio, too detailed for 16 px, can look like an audio or slider icon | Poor |

## Provisional primary: 03 Haze

**Haze** is used for now in the README, the favicon, the social preview and the landing
page. We chose it for these reasons:

1. **It holds up at 16 × 16 px.** The upper disk and the first mist band stay distinct in a
   browser tab (see `favicon-16.png`).
2. **It carries the name.** A light source seen through *bruma* (mist) expresses
   "less noise" without words.
3. **It is unlike other browser marks.** Major browsers use globes, rings, swirls,
   animals or compasses. A banded disk sits in a different visual space.
4. **It is calm and premium without looking corporate.** It is built from one circle and two
   offsets, and it can be drawn in a single colour.

Still open before this becomes final: a wider review of similarity to existing marks
(retro "sunset" logos), testing on the Windows taskbar and Linux docks, and community
feedback in GitHub Discussions.

## Files

| File | Use |
|---|---|
| `logo/mark.svg` | Primary mark, for light backgrounds |
| `logo/mark-dark.svg` | Primary mark, for dark backgrounds |
| `logo/mark-mono.svg` | Single-colour mark |
| `logo/wordmark-light.svg`, `logo/wordmark-dark.svg` | Mark plus "Brumel" lockup |
| `favicon.svg` | Tile icon (Graphite rounded square) for tabs and app icons |
| `favicon-16.png`, `favicon-32.png`, `favicon-180.png`, `favicon-512.png` | Raster exports of the tile |
| `banner.svg` | README banner, 1280 × 320 |
| `social-preview.svg`, `social-preview.png` | GitHub and Open Graph social preview, 1280 × 640 |
| `proposals/**` | The five explorations and the contact sheet |
| `../icon.svg` | Project icon used by tooling (same tile as the favicon) |

The PNG files were rasterised from the SVG sources with a headless Chromium-based browser and
downscaled with Lanczos resampling.

**Upload the social preview by hand.** GitHub has no API for the repository social image.
Go to **Settings → General → Social preview → Upload an image** and choose
`social-preview.png`.

## Typography and fonts

The wordmarks use SVG `<text>` with the font stack
`Inter, Geist, 'Segoe UI', system-ui, sans-serif`. On a machine without Inter or Geist, the
text falls back to a system font, so the wordmarks look slightly different depending on where
they are rendered. Before the identity is final, the wordmark will be **converted to outlines**
so that it renders identically everywhere.

- **Inter**, by Rasmus Andersson, is licensed under the SIL Open Font License 1.1.
- **Geist**, by Vercel, is licensed under the SIL Open Font License 1.1.

Neither font is bundled in this repository yet. If one is added, its `OFL.txt` must be
included and the font listed in [`THIRD_PARTY_NOTICES.md`](../../THIRD_PARTY_NOTICES.md).

## Usage rules (provisional)

- Keep clear space around the mark equal to at least ¼ of its width.
- Do not rotate, skew or outline the mark, and do not add shadows, glows or gradients.
- Do not recolour individual bands outside the palette. Use the mono variant when only one
  colour is available.
- Minimum size: 16 px for the tile icon and 20 px for the bare mark.
- On busy photographs, use the tile version (`favicon.svg`) rather than the bare mark.

The name "Brumel" and the logo are **not** covered by the project's source-code licences.
See [`docs/legal/LICENSING.md`](../../docs/legal/LICENSING.md#trademarks-name-and-logo).
