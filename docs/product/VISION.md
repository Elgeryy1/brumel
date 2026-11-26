# Brumel Vision

> **Status:** Pre-development. This document describes intent, not shipped software.
> No Brumel build exists yet, and every capability below is Planned, Research or
> Experimental unless stated otherwise.

## Mission

**Build a browser that gives people back control of their attention, their
computer's resources and their data, without asking them to give up the
compatibility of the modern web.**

*Less noise. More control.*

## Why another browser?

Most people now spend a large part of the working day inside a browser. It is where
they write, study, buy, bank, watch, play and keep in touch. Yet the browser often
works against them in small ways that add up:

1. **Noise.** Ads, trackers, cookie walls, autoplaying media, notification prompts,
   pop-ups, hijacked back buttons and infinite feeds compete for attention. Much of
   this is not content. It is friction someone else profits from.
2. **Wasted resources.** Dozens of background tabs keep timers, animations and
   scripts running. Laptops heat up, fans spin, batteries drain, and a game or a
   video call stutters because a forgotten tab is still busy. Users have little
   visibility and fewer tools to act.
3. **Lost context.** A crash, an update, an accidentally closed window or an expired
   session can wipe out work in progress. Half-written forms, a research session
   spread over forty tabs, the page you read last week but cannot find: browsers
   still lose things that matter.
4. **Surveillance as a default.** Telemetry, mandatory accounts, cloud-only features
   and opaque background connections are treated as normal. Users cannot easily
   check what their browser sends, or to whom.
5. **Lock-in.** Data, workflows and settings are hard to take elsewhere. Switching
   browsers feels like moving house.

Each of these problems has partial answers somewhere: one browser blocks ads well,
another organizes tabs beautifully, a third manages resources aggressively. Brumel's
bet is that these answers can live in **one coherent, efficient browser**. Features
that are not in use should cost nothing, and the user stays in charge.

## Core philosophy

> **A browser can offer hundreds of features without running all of them all the
> time.**

This is the most important engineering principle in Brumel. Every optional feature
must:

- be **off, dormant or lazily loaded** until it is needed;
- be **fully disableable**, which means its code paths, timers, storage and network
  activity actually stop, not just its UI being hidden;
- have a **measurable cost** that Brumel can show to the user and that we track in
  [benchmarks](../benchmarks/BENCHMARKS.md).

### Principles

| Principle | What it means in practice |
|---|---|
| **Compatibility first** | Chromium engine, Chromium extension support, standards behavior. If a site works in Chrome it should work in Brumel. Exceptions are documented in [COMPATIBILITY.md](../architecture/COMPATIBILITY.md). |
| **Security is not negotiable** | Sandboxing, site isolation and exploit mitigations are never disabled to win benchmarks. Upstream security fixes are shipped fast. See [SECURITY.md](../../SECURITY.md). |
| **Privacy by design** | No mandatory telemetry, accounts or subscriptions for essential features. Optional diagnostics are opt-in and auditable. See [PRIVACY.md](../privacy/PRIVACY.md). |
| **Local-first** | Features work on the device by default. Sync is optional, end-to-end encrypted and self-hostable. |
| **Efficiency with honesty** | Resource savings must come from smarter scheduling, not from breaking pages or weakening isolation. Claims require reproducible measurements. |
| **Simple by default, deep on demand** | A familiar interface out of the box. Power features are revealed progressively, never forced. |
| **Free, local AI that stays in its lane** | Optional, downloadable, isolated, and used only where it beats deterministic code. Never a gatekeeper and never in charge of security decisions. |
| **Verifiable transparency** | Users can see what the browser connects to and why (*Glass Box*). The source code, the decisions and the roadmap are public. |
| **Data portability** | Everything Brumel stores can be exported in open formats (*Exit Freedom*). |
| **No invasive monetization** | No ads of our own injected into pages or the UI, no sponsored content in the new tab page by default, no selling of user data. |

## The five pillars

Brumel is organized around five user-facing pillars. They structure the
[feature catalog](FEATURES.md), the roadmap and the way we talk about the product.

### 1. Efficiency: get the most out of every machine

The browser should adapt to the computer, not the other way around. Brumel Engine
plans to schedule background work, discard or throttle idle tabs, respect thermal and
battery state, step aside when the user is gaming, and explain its decisions.
Equally important is what Efficiency does **not** mean: no disabling site isolation,
no unsafe flags, no stripping of features that pages rely on.

### 2. Memory: never lose information or context

Sessions, tabs, drafts, downloads and reading positions are valuable work. Brumel
Memory aims for *zero loss*: robust session recovery, a browser "time machine",
draft protection, and local search over what you have chosen to keep. All of it stays
on the device unless you sync it, encrypted.

### 3. Clean Web: browse without invasive ads and needless friction

Native, efficient blocking of ads and trackers. Help with cookie banners, pop-ups,
autoplay, notification spam and manipulative patterns, plus a guaranteed way out of
hostile pages. Clean Web favors precision over aggression: when a site breaks, the
fix should be one click away and explained.

### 4. Trust: privacy and security you can verify

Trust is earned through evidence: a public threat model, reproducible builds where
feasible, signed updates, an SBOM, a transparent log of connections the browser
itself makes, and controls over what extensions can do. Brumel should be a browser
whose claims a skeptical expert can check.

### 5. Everyday Tools: solve daily problems where they happen

Compress an image before you upload it. Export a table to CSV. Find the word someone
said in a video. Send a file from your phone without installing anything. Many small,
frequent tasks currently need an extension, a website of unknown trustworthiness, or
a separate app. Brumel can handle many of them locally, privately and with no
background cost when unused.

### Cross-cutting: Brumel Nano

**Brumel Nano** is an optional local AI layer: small models for classification,
embeddings, extraction, OCR, speech and, where quality allows, summarization. It
supports features across all five pillars (grouping tabs, semantic search over your
history, tagging downloads) but it is **not the product's identity** and never
required. Deterministic algorithms come first whenever they are faster and more
reliable. Nano runs in an isolated process without network access, loads on
demand, unloads when idle, and can be removed entirely. Users who prefer a cloud
model can bring their own provider (BYOK). See
[AI_ARCHITECTURE.md](../architecture/AI_ARCHITECTURE.md).

## What we learn from other browsers

Brumel stands on the shoulders of excellent work. We study each of these products
for what it does well. We are not cloning any of them.

| Browser | What we learn from it |
|---|---|
| **Google Chrome** | Web compatibility, extension ecosystem, the security engineering and release discipline of Chromium. |
| **Brave** | Native, efficient content blocking and a privacy-first stance, built while maintaining a large Chromium patch set at scale. |
| **Vivaldi** | Productivity depth and customization for power users. |
| **Arc** | Rethinking tab organization: spaces, sidebars, ephemeral tabs. |
| **Zen Browser** | Calm, refined aesthetics and a focused interface. |
| **Microsoft Edge** | Pragmatic resource management (sleeping tabs, efficiency modes) and OS integration. |
| **Opera GX** | Giving users explicit control over CPU, RAM and network budgets. |
| **Firefox** | Session and identity isolation (containers), and a long record of privacy advocacy. |
| **Safari** | Energy efficiency and the discipline of simplicity. |
| **Helium** | Lightness and how far careful de-Googling of Chromium can go. |

Our differentiation comes from **integration and restraint**: combining these ideas
in one coherent design, making each one cost nothing when off, and proving the
results with public, reproducible measurements.

## Who Brumel is for

| Segment | What they need from Brumel |
|---|---|
| Everyday users | A familiar, fast, clean browser that does not lose their stuff. |
| Power users and tab hoarders | Hundreds of tabs without hundreds of loaded pages; workspaces, trees and fast search. |
| Students and researchers | Reading queues, highlights, copy-with-source, semantic recall of what they read. |
| Developers | Strong DevTools (from Chromium), per-workspace profiles and proxies, and later dedicated tools. |
| Gamers and streamers | A browser that steps aside when a game or a stream needs the hardware. |
| Privacy-conscious users | Blocking, anti-fingerprinting, transparent connections, no mandatory accounts. |
| Users on modest hardware | A low-end mode that keeps 4–8 GB machines usable. |
| Users with accessibility needs | Readable, adjustable, low-stimulus browsing and local dictation and captions. |

Initial platforms are **Windows and Linux (x64)**. macOS is Deferred, and Android is
part of the Future phase. See [ROADMAP.md](../../ROADMAP.md).

## What Brumel will not do

- **No Electron** or other web-wrapper shell. Brumel is native Chromium.
- **No disabling** of sandboxing, site isolation or mitigations to look faster.
- **No mandatory** telemetry, account, subscription or cloud AI for essential
  features.
- **No injected ads** of our own, no affiliate-link rewriting, no selling of data.
- **No AI in charge** of security-critical decisions, and no autonomous agent
  acting on your behalf without a capability-based security model and explicit
  confirmation.
- **No invented numbers.** No fake benchmarks, users, stars or downloads in our
  communication.
- **No promises of proprietary services** we cannot legally use or redistribute
  (for example Google Sync, or Widevine without a license).
- **No feature bloat by default.** A capability enters the default experience only
  if it earns its place.

## How we will measure success

Success criteria will be refined as the project matures. Initial criteria:

1. **Security parity:** Brumel stable ships upstream Chromium security fixes within
   a defined, published window (target defined in
   [UPSTREAM_STRATEGY.md](../architecture/UPSTREAM_STRATEGY.md)).
2. **Compatibility:** the web compatibility test suite and the top-sites smoke tests
   pass at a rate comparable to an equivalent Chromium build.
3. **Efficiency, demonstrated:** reproducible benchmarks show measurable savings in
   memory, CPU and energy against a comparable Chromium configuration, under
   identical conditions. Our current targets (around 20–40% less RAM and 15–30% less
   energy in multi-tab scenarios) are **hypotheses to test, not results**.
4. **Zero-cost-when-off:** benchmarks show that disabled modules add no measurable
   idle CPU, memory or network activity.
5. **Trust:** every connection initiated by the browser is documented and visible
   in Glass Box, and the threat model is reviewed before each phase transition.
6. **Community:** external contributors take part in research, design and code, and
   governance evolves beyond a single maintainer as described in
   [GOVERNANCE.md](../../GOVERNANCE.md).

## Current status

Brumel is in **Phase 0: Pre-development**. The work right now is definition:
documentation, research, architecture decisions, the feature catalog and the
project's identity. There is **no public build** and there will be none until the
technical foundation (reproducible upstream builds, signed updates) is in place.
Follow progress in the [roadmap](../../ROADMAP.md) and in
[GitHub Discussions](https://github.com/Elgeryy1/brumel/discussions).
