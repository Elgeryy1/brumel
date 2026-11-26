# Compatibility

Status: **Planned** — expectations and research for a browser that does not exist yet. Nothing below has been tested on a Brumel build. Items marked *to be verified* need confirmation during Phase 1.

Related: [Architecture](ARCHITECTURE.md) · [Chromium Bases](../research/CHROMIUM_BASES.md) · [Privacy §3](../privacy/PRIVACY.md) · [Licensing](../legal/LICENSING.md)

## 1. Compatibility goal

Brumel aims for **Chrome-level web compatibility**: if a site works in the matching Chrome stable version, it should work in Brumel. Brumel achieves this by shipping the same Blink and V8 as Chromium stable and not modifying the engine. Differences come only from:

1. Features Google provides to Chrome but not to Chromium builds.
2. Privacy features Brumel enables (blocking, anti-fingerprinting) — which can break sites and therefore need per-site controls and a repair path (Self Repair).
3. Bugs in Brumel patches.

## 2. Chromium vs Google Chrome

| Capability | In Chromium source | In Chrome only / Google-provided | Brumel position |
| --- | --- | --- | --- |
| Blink, V8, web platform features | Yes | — | Inherited, unchanged |
| DevTools | Yes | — | Inherited |
| PDF viewer (PDFium) | Yes | — | Inherited |
| Printing, print preview | Yes | Cloud print (discontinued) | Inherited |
| Hunspell spellcheck | Yes (dictionaries downloaded from Google) | Enhanced spellcheck (cloud) | Local dictionaries via Brumel mirror; no cloud spellcheck |
| Password manager (local) | Yes | Google Password Manager cloud sync, passkey sync via Google account | Local password manager; sync Deferred |
| Sync | Client code yes | Google Sync servers; Google restricted Chrome Sync and other private APIs for third-party Chromium builds in March 2021 | Replaced by Brumel Connect |
| Safe Browsing | Client code yes | Google Safe Browsing service (API terms apply) | Research: privacy-preserving replacement or proxy; protection must not be dropped |
| Translate | UI yes | Google Translate endpoint | Local translation models (Research); optional cloud |
| Widevine CDM | Integration hooks | CDM binary and license from Google | See §4 |
| Proprietary codecs | Supported via build flags | Chrome builds with them enabled | See §5 |
| Cast / Media Router | Code yes | Google Cast ecosystem | See §6 |
| Auto-update | Open-source updater exists (`chrome/updater`) | Google Update servers | Own update service ([ADR-0012](adr/0012-update-system.md)) |
| Crash reporting | Crashpad yes | Google crash servers | Opt-in Brumel endpoint |
| Chrome Web Store | Store is a website | Integration tuned for Chrome | See §3 |

## 3. Extensions

- **Chrome Web Store**: installing extensions from the Chrome Web Store generally works in Chromium-based browsers (Brave, Vivaldi, Edge, Opera use it or allow it). ungoogled-chromium removes parts of the integration and needs extra handling; Brumel will keep or restore Web Store installation and updates (to be verified against the imported ungoogled patches).
- **Manifest V3** is the supported extension platform upstream. Brumel supports MV3 fully.
- **Manifest V2**: upstream Chromium has been phasing out MV2 and removing the underlying code paths. Keeping MV2 working would require carrying increasingly large patches, which conflicts with the patch budget ([Upstream Strategy §5](UPSTREAM_STRATEGY.md)). Status: **Research**, leaning toward not supporting MV2. Brumel's native content blocking ([ADR-0011](adr/0011-native-content-blocking.md)) reduces dependence on MV2 blockers.
- Extension-related Brumel features (Extension Doctor, Extension Firewall, Extension Passport, On-Demand Extensions) build on Chromium's runtime host permissions and task manager metrics and must not break extension APIs.

## 4. DRM (Widevine)

- Streaming services that use Encrypted Media Extensions typically require Widevine.
- Shipping Widevine requires an agreement with Google. Protected playback at higher resolutions on Windows (and macOS) additionally requires **VMP (Verified Media Path)** signing of the browser binaries through Google's process.
- Some Chromium forks rely on the Widevine component downloaded at runtime; without VMP signing, many services limit resolution or refuse playback. Behavior differs per service and must be tested.
- Linux builds can load the Widevine component more easily, but service support still varies.

Brumel position: **Research**. Apply for Widevine licensing when there is a public build worth distributing; until then, document limitations clearly. No claims of Netflix/Disney+/etc. support until verified.

## 5. Codecs

| Codec | Royalty status (simplified, not legal advice) | Chromium build | Brumel plan |
| --- | --- | --- | --- |
| VP8, VP9, AV1, Opus, Vorbis, FLAC | Royalty-free | Always included | Included |
| H.264 (AVC), AAC | Patent pools exist | Requires `proprietary_codecs=true` and `ffmpeg_branding="Chrome"` | Research: enable with legal review; many forks ship with them; OS decoders can sometimes be used |
| HEVC (H.265) | Multiple patent pools | Chromium can use platform (OS/hardware) decoders | Hardware/OS decode only where available, to be verified |
| MP3 | Patents expired | Included | Included |

Hardware decode (GPU) is inherited from Chromium (D3D11 video decoder on Windows, VA-API on Linux — Linux support varies by GPU and driver).

Brumel will publish a codec matrix per platform once builds exist. The legal assessment belongs in [Licensing](../legal/LICENSING.md).

## 6. Cast

Chromium contains Media Router code to discover and cast to Google Cast devices. Behavior in non-Google builds varies: Cast relies on Google's ecosystem, and some forks disable it, others keep it optional. Brumel: **Research**, opt-in, local network only, only if it works without Google account integration and without violating terms.

## 7. Passkeys and WebAuthn

- WebAuthn and passkeys are part of the web platform in Chromium.
- **Platform authenticators** work through the OS: Windows Hello on Windows; on Linux, platform passkey support is limited and depends on the desktop environment (to be verified).
- Security keys (USB/NFC FIDO2) work as in Chromium.
- Hybrid (phone as authenticator via QR/Bluetooth) is in Chromium; behavior without Google services to be verified.
- Google Password Manager passkey sync is not available; Brumel does not sync passkeys (Deferred with password sync).

## 8. Other inherited capabilities

| Capability | Expectation |
| --- | --- |
| PWAs (installable web apps) | Inherited; Web App Dock builds on it |
| Picture-in-Picture, Document PiP | Inherited |
| Hardware acceleration (GPU raster, WebGL, WebGPU) | Inherited; WebGPU availability per platform as upstream |
| Screen capture, getDisplayMedia | Inherited |
| Secure DNS (DoH) | Inherited; Brumel offers a provider list without a default third-party dependency (Research which default) |
| HTTPS-First / HTTPS-Only | Inherited |
| Import/export of user data | Inherited importers + Brumel Migration Assistant |
| Accessibility (screen readers) | Inherited; Brumel UI must not regress it |

## 9. Site compatibility process (planned)

1. **Report**: issue template "Site compatibility" with URL, steps, Brumel version, Chrome version comparison, and whether Shield features were active.
2. **Triage**: reproduce in matching Chromium/Chrome; classify as upstream bug, Brumel patch bug, blocking/anti-fingerprinting breakage or Google-only service.
3. **Fix**: patch, filter-list exception, per-site setting default, or upstream report.
4. **Self Repair**: in-browser flow that disables Shield features for a site one at a time to identify the cause, and lets the user submit an anonymous report (opt-in).
5. **Regression**: a curated set of popular sites runs in automated smoke tests per release (Research: tooling and legal considerations of automated testing against third-party sites; prefer recorded replays).
