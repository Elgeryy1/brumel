# De-Googling audit

Status: **In Development** — first inventory, made from source code and patches. Nothing here has been checked against a running build yet. The network capture of a fresh profile is step 6 of the [Phase 1 plan](../development/PHASE1_PLAN.md) ([#72](https://github.com/Elgeryy1/brumel/issues/72)).

Related: [PRIVACY.md §3](PRIVACY.md#3-network-connections-and-google-service-replacements) · [COMPATIBILITY.md](../architecture/COMPATIBILITY.md) · [`patches/series`](../../patches/series) · issue [#69](https://github.com/Elgeryy1/brumel/issues/69) · catalog CORE-006

## Scope and method

- **Base:** Chromium 158.0.8127.88 as Brumel builds it: not Chrome-branded, with no Google API keys (`use_official_google_api_keys = false`, enforced by `scripts/build.py`) and `disable_fieldtrial_testing_config = true`.
- **Sources:** the pinned checkout, the ungoogled-chromium `158.0.8127.88-1` patches and their own descriptions, and Chromium's code where a claim depends on it.
- **"Patch in series"** means the patch is in [`patches/series`](../../patches/series) and applies to the pin together with the rest of the series (checked with `git apply`). It does **not** mean it has been built or that the connection is gone at runtime.
- **Not covered yet:** a network capture of a fresh profile, Linux-only services, and services reached only after the user signs in to something.

## Selection of ungoogled-chromium patches

Of the 110 patches in ungoogled-chromium `158.0.8127.88-1`, Brumel imports 15 for now. They all apply in order on top of the pin and touch only `src/`. The others are left out for these reasons:

| Left out | Reason |
|---|---|
| Patches that remove Safe Browsing (`fix-building-without-safebrowsing`, `inox-patchset/0001-…`, `iridium-browser/safe_browsing-*`, `remove-unused-preferences-fields`) | [PRIVACY.md](PRIVACY.md) does not allow removing Safe Browsing without a replacement (CORE-012). |
| `bromite/disable-fetching-field-trials` | Licensed GPL-3.0 (the Bromite repository), which is not compatible with Brumel's licensing ([ADR-0004](../architecture/adr/0004-licensing.md)). It is also not needed. In an unbranded build, `VariationsService` fetches no seed unless `--variations-server-url` is given (`IsFetchingEnabled()` in `components/variations/service/variations_service.cc`). |
| `block-trk-and-subdomains`, `disable-untraceable-urls`, `fix-learn-doubleclick-hsts`, `block-requests` | These rely on ungoogled-chromium's domain substitution, which Brumel does not use. |
| `replace-google-search-engine-with-nosearch` | The default search engine is a product decision: the user chooses it on first run ([PRIVACY.md](PRIVACY.md)). |
| `disable-webstore-urls`, `extensions-manifestv2` | They conflict with Chrome Web Store compatibility (CORE-022). |
| `disable-ai`, `disable-privacy-sandbox`, `doh-changes`, `remove-f1-shortcut`, `move-js-optimizer-unfamiliar-sites` | Not yet reviewed. Some depend on patches left out above. |
| `extra/*` (flags and UI changes) | Product features, not removals of Google services. Decided per feature. |
| `upstream-fixes/*` | Build fixes for configurations Brumel does not use yet. |

The imported patches keep their header and license and gain an `Origin:` line. The ungoogled-chromium patches are BSD-3-Clause. The `inox-patchset/` patches are BSD-2-Clause ([THIRD_PARTY_NOTICES.md](../../THIRD_PARTY_NOTICES.md)).

## Inventory

State legend: **Patch in series** (applies, not built) · **Upstream default** (already off in an unbranded build without keys, verified in the source) · **Kept** (needed and deliberate) · **Gap** (still contacts Google; work is listed) · **To verify** (unknown until the network capture).

| Service | What Chromium does | How Brumel handles it | State |
|---|---|---|---|
| Google API keys | Many services authenticate with a key compiled into the build | No keys. `build.py` refuses profiles that set keys or leave `use_official_google_api_keys` enabled | Upstream default + guard |
| Google account sign-in (Gaia) | Sign-in and token fetches to `accounts.google.com` | `core/ungoogled-chromium/disable-gaia.patch` | Patch in series |
| Google Sync | Syncs browser data through the signed-in Google account | Needs sign-in and keys, so it is not reachable. Brumel Connect replaces it later (PRIVACY.md §6) | To verify |
| Safe Browsing | Update and hash-check requests to `safebrowsing.googleapis.com`. Without a key the request has no `&key=` parameter (`v5_update_protocol_manager.cc`) | **Kept** in the code. Whether Google answers requests without a key is not verified. If it does not, internal builds have **no Safe Browsing protection** until CORE-012 provides a replacement | Gap / To verify |
| Crash reporting | Crashpad uploads and background requests to `clients2.google.com` | `core/ungoogled-chromium/disable-crash-reporter.patch`. An opt-in Brumel endpoint is CORE-011 | Patch in series |
| Google Cloud Messaging (push) | Keeps a connection to Google's GCM servers for push messages | `core/ungoogled-chromium/disable-gcm.patch`. Side effect: Web Push through Google is gone | Patch in series |
| Domain Reliability | Sends reliability beacons about requests to Google properties | `core/ungoogled-chromium/disable-domain-reliability.patch` (also removes the preloaded domain list) | Patch in series |
| Network time | Asks a Google server for the time, to detect a wrong system clock | `core/ungoogled-chromium/disable-network-time-tracker.patch`. Certificate checks still use the system clock; only the "your clock is wrong" detection gets weaker | Patch in series |
| Field trials (variations) | Downloads experiment seeds from `clientservices.googleapis.com` | Not fetched in unbranded builds without `--variations-server-url` (source checked). The testing config is off through `disable_fieldtrial_testing_config` | Upstream default |
| Google host detection | Google-specific behavior for Google sites, such as extra request headers and URL throttles | `core/ungoogled-chromium/disable-google-host-detection.patch` | Patch in series |
| Autofill server | Downloads form-field predictions from Google | `core/inox-patchset/0003-disable-autofill-download-manager.patch` | Patch in series |
| Updater pings | The Chromium updater reports usage pings | `core/inox-patchset/0015-disable-update-pings.patch`. Brumel's own updater is CORE-051 | Patch in series |
| RLZ (promotion tracking) | Tracks installation and search promotions | `core/inox-patchset/0021-disable-rlz.patch` | Patch in series |
| Profile avatars | Downloads profile pictures from `www.gstatic.com` | `core/ungoogled-chromium/disable-profile-avatar-downloading.patch` | Patch in series |
| Reader mode fonts | DOM Distiller loads fonts from `fonts.googleapis.com` | `core/ungoogled-chromium/disable-fonts-googleapis-references.patch` | Patch in series |
| WebRTC logs | Uploads WebRTC diagnostic logs to Google | `core/ungoogled-chromium/disable-webrtc-log-uploader.patch` | Patch in series |
| Media Engagement preload | Ships a pre-built list of sites allowed to autoplay | `core/ungoogled-chromium/disable-mei-preload.patch` | Patch in series |
| Search tracking parameter | Adds a navigation-source parameter to search URLs | `core/ungoogled-chromium/remove-navigation-source-param.patch` | Patch in series |
| Translate | Page translation through Google's translation service | `core/ungoogled-chromium/toggle-translation-via-switch.patch`: off unless `--translate-script-url` is given. Local translation is CORE-013 | Patch in series |
| Component updater | Downloads components (for example CRLSets and certificate data) from Google's update servers | Not changed yet. A Brumel component server is Research in PRIVACY.md | Gap |
| Spellcheck dictionaries | Downloads Hunspell dictionaries from Google on demand | Not changed yet. Hosting is CORE-014 | Gap |
| Default search engine and suggestions | Google is the default, with suggestions on | The user chooses on first run (Planned) | Gap |
| Chrome Web Store | Extension installs and update checks go to Google | Kept for compatibility (CORE-022). Requests start from the user's extensions | Kept |
| AI features (Gemini in Chrome, on-device model downloads) | Downloads models and talks to Google AI services when enabled | Not reviewed yet (`disable-ai` is not imported) | To verify |
| Privacy Sandbox | Topics and related APIs, with Google-operated lists | Not reviewed yet (`disable-privacy-sandbox` is not imported) | To verify |
| Cast / Media Router discovery | mDNS and DIAL discovery on the local network | Not changed. ungoogled-chromium builds with `enable_mdns = false` and `enable_service_discovery = false`. PRIVACY.md has this as Research | To verify |
| Hangouts services extension | A built-in component extension for Google Meet and Hangouts | Not changed. ungoogled-chromium builds with `enable_hangout_services_extension = false` | Gap |

## Strings that become untrue

Some user-visible strings describe Google services that these patches remove (for example "Chromium uses Google servers" for private prefetch). `scripts/rebrand.py` changes only the product name ([ADR-0015](../architecture/adr/0015-branding-without-string-patches.md)). Correcting statements like these is a follow-up, done when each feature is reviewed.

## Next steps

1. Build the series and smoke-test it (Phase 1, step 3).
2. Capture the network traffic of a fresh profile and of a short browsing session. Replace every **To verify** with what was observed (step 6, [#72](https://github.com/Elgeryy1/brumel/issues/72)).
3. Decide on the GN switches ungoogled-chromium uses (`enable_mdns`, `enable_service_discovery`, `enable_hangout_services_extension`, `enable_reporting`), taking compatibility into account.
4. Review the patches not imported yet, starting with `disable-ai` and `disable-privacy-sandbox`.
