# Third-Party Notices

Brumel Browser is built on the work of many other open-source projects. This file
records which third-party material is in this repository, what we plan to depend on,
and how attribution will be produced for future binaries.

> **Current state (Pre-development):** this repository holds documentation,
> design proposals, project tooling and a few small scripts written for Brumel.
> **No third-party source code is vendored here yet.** Chromium is not
> committed to this repository and never will be (see
> [UPSTREAM_STRATEGY.md](docs/architecture/UPSTREAM_STRATEGY.md)).

## 1. Material currently included in this repository

| Component | Where | License | Notes |
|---|---|---|---|
| Contributor Covenant 2.1 | [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) | CC BY 4.0 | Adapted text; attribution kept in the file. |
| Mozilla Public License 2.0 text | [`LICENSE`](LICENSE) | License text, reproduced verbatim | Applies to Brumel-original files. |

Brand artwork in [`assets/branding/`](assets/branding/) was created for Brumel. It
contains no third-party marks. The candidate typefaces (Inter, Geist) are *referenced*
by name in the design documents but are **not** bundled.

## 2. Planned upstream dependencies

None of these is in the repository today. Each will add its notices when it is
first fetched, patched or redistributed.

| Component | Role in Brumel | License | Status |
|---|---|---|---|
| [Chromium](https://www.chromium.org/) | Browser engine and base application | BSD-3-Clause, plus hundreds of `third_party/` components under their own licenses (MIT, Apache-2.0, LGPL, MPL, ICU, zlib, others) | Planned (Phase 1) |
| [ungoogled-chromium](https://github.com/ungoogled-software/ungoogled-chromium) patches | Selected patches that remove Google services | BSD-3-Clause | Planned (Phase 1), patch by patch |
| [adblock-rust](https://github.com/brave/adblock-rust) | Candidate native content-blocking engine | MPL-2.0 | Research ([ADR-0011](docs/architecture/adr/README.md)) |
| Filter lists (for example EasyList, EasyPrivacy, uBlock filters) | Clean Web rule sets | Varies per list (CC BY-SA 3.0, GPL-3.0, others) | Research. Each list is checked before we ship it. |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Candidate local generative inference runtime | MIT | Research ([ADR-0008](docs/architecture/adr/README.md)) |
| [ONNX Runtime](https://github.com/microsoft/onnxruntime) | Candidate runtime for embeddings, OCR and speech | MIT | Research |
| Inter, Geist | Candidate UI and brand typefaces | SIL Open Font License 1.1 | Candidate, only if bundled |
| Small language and embedding models | Optional Brumel Nano component, downloaded separately | Varies: Gemma models use the *Gemma Terms of Use* (not an OSI license, includes a prohibited-use policy). Qwen3 small models use Apache-2.0. | Research. Model licenses are reviewed one by one in [LICENSING.md](docs/legal/LICENSING.md). |

## 3. How attribution will work in binaries

- **Chromium components.** Chromium generates its own credits page from the
  `README.chromium` and `LICENSE` files of every `third_party/` directory, using
  `tools/licenses/licenses.py`. Brumel builds will keep this mechanism, and the
  result will be shown at `brumel://credits` (the equivalent of `chrome://credits`).
  Removing or hiding upstream credits is not allowed.
- **Brumel-added components** (for example a content-blocking engine or an AI
  runtime) must ship the same metadata (`README.chromium`-style files with license
  and version). That way they appear in the generated credits automatically.
- **Separately downloaded components** (AI models, filter lists) carry their license
  and source in their component manifest. The browser shows this before download.
- **SBOM.** Every release is expected to publish a Software Bill of Materials
  (SPDX or CycloneDX). See [SECURITY.md](SECURITY.md).

## 4. Keeping this file accurate

1. Any pull request that adds, vendors, fetches or redistributes third-party
   material must update this file in the same PR.
2. The PR must state the component's license, version or commit, and source URL.
3. A component whose license is incompatible with
   [Brumel's licensing model](docs/legal/LICENSING.md) (MPL-2.0 for Brumel-original
   files, BSD-3-Clause for patches to Chromium-derived files) is rejected until the
   maintainer and, where needed, legal advice resolve it.
4. Before every release this file is reviewed against the generated credits and the
   SBOM.

If you think something here is missing or wrong, please open an issue or contact
the maintainer as described in [GOVERNANCE.md](GOVERNANCE.md).
