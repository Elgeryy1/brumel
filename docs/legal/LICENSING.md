# Licensing

> **Not legal advice.** This document records the project's licensing analysis and
> decisions. Where something needs a lawyer's review, it says so explicitly.

## 1. Decision (approved)

| Code | Licence | Status |
|---|---|---|
| **New, Brumel-original source files** (Brumel modules, WebUI pages, scripts, tools, docs code samples) | **MPL-2.0** | Approved by the owner on 2026-11-26 ([ADR-0004](../architecture/adr/)) |
| **Patches that modify Chromium-derived files** (`patches/`) | **BSD-3-Clause**, the same licence as the file being modified | Approved on 2026-11-26 |
| **Third-party code** (Chromium, ungoogled-chromium patches, other dependencies) | Their original licences, preserved | Always |
| **Documentation** | Covered by the repository licence (MPL-2.0) unless a file says otherwise | Provisional; CC BY 4.0 for docs may be considered later |
| **Name and logo** | **Not** licensed under MPL-2.0 or BSD-3-Clause; see [§7](#7-trademarks-name-and-logo) | Draft policy |

The repository's [`LICENSE`](../../LICENSE) file contains the MPL-2.0 text.
[`THIRD_PARTY_NOTICES.md`](../../THIRD_PARTY_NOTICES.md) lists third-party components and
their licences.

### Why this split

- **MPL-2.0 for Brumel's own files** is a *file-level* copyleft. If someone distributes a
  modified version of a Brumel file, they must publish their changes to that file, but they
  can combine it freely with code under other licences. That keeps Brumel's own
  improvements open without "infecting" Chromium or proprietary components. It is the
  licence Brave uses for brave-core and that Mozilla uses for Firefox. It has been tested in
  practice in browsers.
- **BSD-3-Clause for patches to Chromium files** keeps the modified files under a single
  licence (the one they already have) and keeps the door open to **upstreaming** fixes to
  Chromium, which accepts contributions under its BSD-style licence (along with Google's
  contributor licence agreement).
- **MPL-2.0 is compatible with the GPL family** through its "Secondary Licenses" clause
  (§3.3). This matters if Brumel is ever combined with GPL code, as long as no file is marked
  "Incompatible With Secondary Licenses".

## 2. Licences compared

| | BSD-3-Clause | MPL-2.0 | Apache-2.0 | GPL-3.0 |
|---|---|---|---|---|
| Type | Permissive | Weak (file-level) copyleft | Permissive | Strong copyleft |
| Must publish modifications when distributing | No | Yes, for modified MPL files | No | Yes, for the whole derived work |
| Can be combined with proprietary code | Yes | Yes, at file boundaries | Yes | No (for the combined work) |
| Explicit patent grant | No | Yes | Yes | Yes |
| Patent retaliation clause | No | Yes | Yes | Yes |
| Compatible with Chromium's BSD-3-Clause code | Yes (same) | Yes | Yes | Yes, but the combined work becomes GPL-3.0 |
| Compatible with GPL-3.0 | Yes | Yes (§3.3 Secondary Licenses) | Yes (GPLv3 only, not GPLv2) | Yes |
| Prevents closed forks of Brumel's own code | No | Partially (per file) | No | Yes |
| Precedent in browsers | Chromium, ungoogled-chromium, Thorium | Brave, Firefox | Some components | Helium |
| Effect on upstreaming to Chromium | None | Upstreamed code needs relicensing by its authors | Upstreamed code needs relicensing | Upstreamed code needs relicensing |

**Options considered and why they were not chosen:**

- **BSD-3-Clause everywhere.** This is the simplest option and identical to Chromium, but it
  allows anyone to ship a closed, rebranded copy of Brumel's own modules with no obligation
  to share improvements. It also has no explicit patent grant.
- **Apache-2.0.** A strong patent grant, but the same "closed fork" issue as BSD. It also
  mixes a third licence family into a BSD and MPL ecosystem.
- **GPL-3.0.** Gives the strongest openness guarantee, but makes the entire distributed
  browser a GPL-3.0 work. That complicates combination with some third-party components
  (for example proprietary CDMs, which are already separate components), limits who can
  build on Brumel, and adds compliance burden for a small project.

## 3. Compatibility with possible bases and sources

| Source | Licence (from GitHub metadata, 2026-11-26) | Can Brumel reuse it? | Conditions |
|---|---|---|---|
| Chromium | BSD-3-Clause (plus many third-party licences in `third_party/`) | Yes | Keep notices; generate the credits page |
| ungoogled-chromium | BSD-3-Clause | Yes, including selective patch import | Keep copyright notices in the imported patches |
| Brave (brave-core) | MPL-2.0 | Yes, file by file | Reused files stay MPL-2.0, and modifications to them must be published; follow Brave's trademark policy (no Brave name or logo) |
| adblock-rust (Brave) | MPL-2.0 | Yes | Same as above |
| Helium | GPL-3.0 | **Only if we accept GPL-3.0 obligations for the distributed browser** | **Default: do not import Helium code.** Learning from its public design and ideas is fine; copying code is not, unless a future ADR accepts GPL-3.0. |
| Thorium | BSD-3-Clause | Yes | Keep notices; review patch quality and security implications individually |

**Clean-room rule.** When a feature is inspired by a GPL-3.0 project, the implementation must
be written independently. Contributors must not copy GPL code into MPL or BSD files.

## 4. File headers (SPDX)

Every new Brumel source file starts with a copyright line and an SPDX licence identifier:

```cpp
// Copyright 2026 The Brumel Authors
// SPDX-License-Identifier: MPL-2.0
```

```ts
// Copyright 2026 The Brumel Authors
// SPDX-License-Identifier: MPL-2.0
```

```python
# Copyright 2026 The Brumel Authors
# SPDX-License-Identifier: MPL-2.0
```

Patches in `patches/` carry a header describing the change and the licence of the result:

```
Description: <what and why>
Upstream: <not applicable | submitted: <link> | imported from <project>@<commit>>
SPDX-License-Identifier: BSD-3-Clause
```

Patches imported from other projects (for example ungoogled-chromium) keep their original
author and copyright information in the patch header.

"The Brumel Authors" means the individual contributors who hold copyright in their
contributions. Contributors keep their copyright. Contributions are accepted under the
licence of the file they modify (inbound = outbound). See
[CONTRIBUTING.md](../../CONTRIBUTING.md) for the contribution process.

## 5. Third-party preservation and compliance

- Chromium ships hundreds of third-party components, each with its own `README.chromium` and
  licence file. Brumel builds must keep the generated credits page (`about:credits`, produced
  by Chromium's licence tooling) and must not strip licence files.
- [`THIRD_PARTY_NOTICES.md`](../../THIRD_PARTY_NOTICES.md) lists what the **repository itself**
  contains or depends on, and is updated with every new dependency.
- Release artefacts will include an **SBOM** (see [SECURITY.md](../../SECURITY.md)) listing
  components and licences.
- Copyleft components inside Chromium (for example LGPL-licensed parts of FFmpeg) carry
  obligations such as offering the corresponding source. Brumel's source plus the pinned
  upstream revision satisfy this. It will be verified per release.

### Codecs and DRM (needs legal review)

- **Proprietary codecs** (H.264, AAC, HEVC). Enabling them in the build is technically
  straightforward. Patent licensing for distributing decoders varies by jurisdiction and must
  be reviewed before public binaries ship. Hardware and OS decoders can reduce exposure.
  Status: Research; see [COMPATIBILITY.md](../architecture/COMPATIBILITY.md).
- **Widevine CDM** is proprietary and requires an agreement with Google. Brumel will not
  bundle or redistribute it without one. Status: Research.

## 6. AI model, filter list and font licences

### AI models (Brumel Nano)

Models are **not** part of the source tree. They are optional, separately downloaded
components, and each model's licence is shown before download.

| Model family | Licence | Notes |
|---|---|---|
| Gemma 3 (270M, 1B), EmbeddingGemma, FunctionGemma | **Gemma Terms of Use** (https://ai.google.dev/gemma/terms) | Not an OSI open-source licence. Includes a prohibited-use policy, and redistribution must pass the terms on. Needs review before we distribute weights from our own infrastructure. |
| Qwen3 (for example 0.6B) | Apache-2.0 | Permissive; keep the NOTICE file |
| Others | To be evaluated per model | A model is eligible only if its licence allows free use and redistribution as an optional download |

The runtimes llama.cpp (MIT) and ONNX Runtime (MIT) are permissive and compatible with both
MPL-2.0 and BSD-3-Clause.

### Filter lists (Clean Web)

Filter lists are **data** downloaded at runtime, but their licences still apply when we
redistribute or transform them:

| List | Licence (to be re-verified before use) |
|---|---|
| EasyList / EasyPrivacy | Dual-licensed GPL-3.0-or-later or CC BY-SA 3.0-or-later (per easylist.to) |
| uBlock Origin filter lists (uAssets) | GPL-3.0 |
| Other lists | Evaluated individually |

Brumel will not compile third-party lists into the binary under a different licence. Default
lists, their sources and their licences will be shown in settings.

### Fonts

Inter and Geist (and Geist Mono) are licensed under the **SIL Open Font License 1.1**. If
bundled, the `OFL.txt` must ship alongside them, and the fonts cannot be sold on their own.

## 7. Trademarks (name and logo)

The MPL-2.0 (§2.3) and BSD-3-Clause licences grant **no** trademark rights. The name
"Brumel", "Brumel Browser" and the Brumel logos are not covered by the code licences.

**Draft trademark guidelines** (to be finalised once the identity is final and the
[name check](../research/NAME_CHECK.md) is complete):

- **Allowed without asking:** referring to Brumel by name in articles, reviews, tutorials and
  comparisons; saying a product is "based on Brumel" or "compatible with Brumel";
  redistributing **unmodified** official builds under the Brumel name.
- **Not allowed without permission:** distributing **modified** builds under the Brumel name
  or logo, using the logo as your own product's icon, or implying official endorsement.
- **Forks** must change the name and logo, and must not use update servers or sync services
  that appear to be official Brumel ones.

## 8. Open items

- [ ] Legal review of the codec patent position before Public Alpha binaries.
- [ ] Widevine licensing inquiry (see [RESEARCH.md](../research/RESEARCH.md), H-10).
- [ ] Gemma Terms of Use review before Brumel distributes any Gemma weights.
- [ ] Decide whether documentation should move to CC BY 4.0.
- [ ] Finalise the trademark guidelines after identity and name clearance.
