# ADR-0015: Branding through GN arguments and generated strings

- Status: Accepted (provisional)
- Date: 2026-11-27
- Deciders: @Elgeryy1
- Related: [ADR-0003](0003-patch-based-repository.md), [ADR-0013](0013-git-backed-patch-tooling.md), [`patches/README.md`](../../../patches/README.md), [Building](../../development/BUILDING.md), issue [#68](https://github.com/Elgeryy1/brumel/issues/68), catalog CORE-004

## Context

A Chromium build calls itself "Chromium" in three places:

1. **Version resources and installers.** They read `COMPANY_FULLNAME`, `PRODUCT_FULLNAME`, `COPYRIGHT` and similar keys from a `BRANDING` file.
2. **User-visible strings.** In the pinned 158.0.8127.88 checkout, `chrome/app/chromium_strings.grd`, its `settings_chromium_strings.grdp` part and `components/components_chromium_strings.grd` name the product in 702 English messages. Their 81 translation files (`.xtb`) name it in about 47,000 translated lines.
3. **Platform identity.** These are the Windows install modes (user data directory, registry keys, COM class IDs), the Linux profile directory and the icons. They live in C++ constants and binary files.

[ADR-0003](0003-patch-based-repository.md) keeps patches small and reviewable. A patch for item 2 would add tens of thousands of lines, and it would conflict on every upstream update that touches a translation. There is also a technical trap. GRIT finds each translation through a fingerprint of the English text. If the English text changes and the translations are not renamed, every language silently falls back to English.

## Decision

- **`BRANDING` without a patch.** `branding_file_path` is a GN argument. Brumel's own `BRANDING` lives in `src/branding/` and reaches the checkout as `//brumel/branding/BRANDING` through `scripts/overlay.py sync`. `config/gn/_common.gn` points every profile at it. `build.py` refuses to generate a profile whose `//brumel` files are missing. `version.py` accepts only `KEY=VALUE` lines, so the license notice of `BRANDING` is in a `BRANDING.license` file next to it.
- **Strings are generated, not patched.** `scripts/rebrand.py apply` rewrites the three string files and their translations in the checkout. It always starts from the committed content (`git show HEAD:`), so it is repeatable and gives the same result every time.
  - It asks the checkout's own GRIT (`src/tools/grit`) for the message IDs before and after the change, and renames each translation to its new ID. It never has to guess GRIT's fingerprint.
  - It replaces "Chromium" with "Brumel", including inflected or prefixed forms in translations (`Chromiumin`, `iChromium`) and names with a menu accelerator inside them (`Chr&amp;omium`).
  - Some translations say "Chrome" where the English says "Chromium". They are rebranded too, unless the English message itself mentions Chrome (for example the Chrome Web Store).
  - **Attribution stays.** These are kept as they are: the company name and copyright messages (`IDS_ABOUT_VERSION_COMPANY_NAME`, `IDS_ABOUT_VERSION_COPYRIGHT`), the phrase "The Chromium Authors", the link to the Chromium project on the about page, placeholder contents, and other products (ChromiumOS, Chromebook).
  - The changes stay uncommitted in the checkout, so `patches.py refresh` never exports them. `rebrand.py revert`, or `patches.py apply --reset`, restores the files before patches are applied again.
- **Platform identity goes in small patches.** Install modes, profile directories and icons go in `patches/brumel/branding/`. Each patch stays reviewable and has one purpose.

Order in a checkout: `patches.py apply`, then `overlay.py sync`, then `rebrand.py apply`, then `build.py`.

## Consequences

- Positive: rebranding about 47,000 strings costs zero patch lines and no rebase conflicts. A new upstream version is rebranded by running the script again.
- Positive: translations stay. In a dry run against the pinned checkout, 682 messages of `chromium_strings` and 20 of `components_chromium_strings` changed. 47,223 translations were renamed to match.
- Negative: about 0.7% of the renamed translations still show the upstream name. Measured: 314 of them, mostly Hindi and Nepali (the name is transliterated as क्रोमियम), Czech declensions (`Chromiu`, `Chromia`) and a few Japanese and Zulu forms. Grammar around the new name is not adjusted (for example Hungarian vowel harmony). Native-speaker review is a follow-up.
- Negative: the build depends on one more preparation step. `build.py` cannot check that it ran. The about page or the window title shows it at once.
- Negative: the product name keeps Chromium's string IDs (`IDS_*`), so Brumel strings that are not about the product name still come from upstream, including statements about Google services that de-Googling patches make untrue. The de-Googling audit ([#69](https://github.com/Elgeryy1/brumel/issues/69)) tracks those.

## Alternatives considered

- **One large strings patch.** Rejected. It would be tens of thousands of lines, conflict on every translation update and hide real changes in review.
- **Rebranding only the English file.** Rejected. Every translation would be dropped, because its ID would no longer match.
- **Copies of the string files under `//brumel` and a GN hook pointing GRIT at them.** Not chosen for now. Other tools read the same files by path (installer strings, Linux packaging), so each consumer would need a hook patch. It remains an option if leaving uncommitted changes in the checkout causes problems.
- **`is_chrome_branded` or `branding_path_component`.** Rejected. These switch to Google Chrome branding and Google-internal resources, which Brumel must not use.

## Revisit when

- Upstream moves these strings to another format or a single file.
- Translators or users report wrong grammar in a language often enough to need per-language rules.
- The uncommitted rebrand step causes mistakes in the patch workflow.
