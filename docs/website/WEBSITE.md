# Website strategy

> **Status: In Development (static page only).** The first version of the site is a single
> static page in [`site/`](../../site/) that clearly says Brumel is in **Pre-development**.

## Hosting

| Decision | Choice | Why |
|---|---|---|
| Host | **GitHub Pages**, deployed by a GitHub Actions workflow from `site/` | Free, no server to maintain, the source is in the same repository, and every change is reviewed like code |
| URL | `https://elgeryy1.github.io/brumel/` | Free GitHub subdomain |
| Custom domain | **None for now** | Buying a domain requires the owner's explicit approval. See [NAME_CHECK.md](../research/NAME_CHECK.md) for the domain survey. |
| Build tooling | None. Hand-written HTML and CSS. | Fast, auditable, no dependency supply chain for a one-page site |

All URLs inside the site are **relative**, so the site works at the `/brumel/` sub-path and
will keep working if a custom domain is added later. The only absolute URLs are the Open
Graph image and page URL, which must be absolute.

## Principles

1. **Honest.** The site never shows a download button before signed builds exist. Every
   feature is labelled with its catalog status (Planned, Research, …).
2. **Private.** No analytics, no cookies, no third-party scripts, no remote fonts and no
   embeds. The page sets no cookies and makes no requests outside its own origin. If
   analytics are ever considered, the method must be privacy-preserving and documented in
   [PRIVACY.md](../privacy/PRIVACY.md) first.
3. **Fast.** One HTML file with inline CSS and a few small SVG files. No JavaScript is
   needed.
4. **Accessible.** Semantic landmarks, a skip link, visible focus, WCAG 2.2 AA contrast
   (tokens from [DESIGN_SYSTEM.md](../design/DESIGN_SYSTEM.md)), `prefers-color-scheme` and
   `prefers-reduced-motion` support, readable at 200% zoom and on 320 px wide screens.
5. **Consistent with the repository.** Copy is derived from the README and the docs. The
   repository remains the source of truth.

## Content outline

| Section | Phase 0 (now) | Later |
|---|---|---|
| Hero | Provisional mark, name, slogan, "Pre-development" badge, GitHub / roadmap / discussions buttons | Screenshot or short video of real builds |
| Philosophy | Optional by design, local-first, verifiable claims | Same |
| Five pillars | Efficiency, Memory, Clean Web, Trust, Everyday Tools | Linked to feature pages |
| Features | A selection of Planned and Research features with status chips | Status updates; "Available" only when it ships |
| Identity | Provisional logo | Final identity, press kit |
| Roadmap | Phase summary, current phase highlighted | Link to the live project board |
| Documentation | Links to the GitHub docs | Possibly a docs sub-site |
| Privacy and security | Principles and links to policies | Audit reports |
| Benchmarks | Not shown (no data) | Public results with raw data and methodology |
| Downloads | **Not shown.** A note warns that unofficial downloads are not from the project. | Signed builds, checksums, signatures, verification instructions |
| Contribute | Links to the contributing guide, discussions and good first issues | Same |
| Changelog | Link to CHANGELOG.md | Release notes |

## Deployment

The Pages deployment workflow lives in `.github/workflows/` (maintained with the rest of
CI). It:

1. triggers on pushes to `main` that touch `site/**`, and on manual dispatch;
2. uploads `site/` as the Pages artifact;
3. deploys with `actions/deploy-pages`, using pinned action SHAs and minimal permissions
   (`pages: write`, `id-token: write`, `contents: read`).

The repository's Pages source must be set to **GitHub Actions**
(Settings → Pages → Build and deployment → Source).

## Assets

`site/assets/` holds **copies** of the provisional branding assets so that the site is
self-contained: `mark.svg`, `mark-dark.svg`, `favicon.svg`, `favicon-180.png` and
`social-preview.png`. When the identity changes, update
[`assets/branding/`](../../assets/branding/) first and then copy the files again.

## Future options (not decided)

- A custom domain (needs the owner's approval and budget).
- A static site generator if the site grows to several pages (for example for devlogs). It
  must keep the no-tracking rule.
- Localised Spanish version.
