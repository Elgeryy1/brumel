# Launch and visibility plan

> Brumel is in **Pre-development**. This plan is organised by **milestones**, not dates: we
> only talk publicly about things that exist. All post drafts live in [`posts/`](posts/) and
> are **published manually**. Nothing is posted automatically.

## Goals

1. Build a small, high-quality group of early followers who care about performance, privacy
   and control: people who will test, report and contribute.
2. Earn credibility through transparency: open plans, reproducible benchmarks, honest status.
3. Avoid the "vaporware browser" trap, where a project gets loud promises, a large launch spike
   and then silence.

## Audience

| Segment | What they care about | Where they are |
|---|---|---|
| Power users with many tabs | Memory, organisation, session recovery | r/browsers, YouTube, X |
| Privacy-conscious users | No telemetry, ad blocking, transparency | r/privacy, Bluesky, Hacker News |
| Developers | Chromium compatibility, DevTools, extensions, build quality | Hacker News, GitHub, X |
| Gamers and streamers | Background resource use during games | TikTok, YouTube, Reddit gaming communities |
| Owners of low-end laptops | Speed on 4–8 GB RAM, battery | YouTube, TikTok, Reddit |
| Chromium contributors and fork maintainers | Patch strategy, upstream hygiene | GitHub, Hacker News |

## Phased plan

### Phase 0 — Pre-development (now)

**What we have:** repository, documentation, catalog, roadmap, provisional identity, public
project board.

**What to post:**

- An "intro / building in public" post on X, Bluesky and a personal blog or devlog: why
  Brumel, the five pillars, what is deliberately *not* promised.
- A Reddit post asking for feedback (r/browsers). It must clearly say there is nothing to
  download, and invite people to Discussions.
- An optional *Ask HN* post ("What would make you switch browsers?") and **not** *Show HN*,
  because HN's Show rules require something people can try.

**Success signals:** thoughtful comments, issues or discussions with evidence, first
external contributors to the docs. Stars are not the goal.

### Phase 1 — Technical Foundation

**Trigger:** the first reproducible build from pinned upstream, with Brumel branding.

**Content:**

- Devlog: "Building Chromium from a pinned tag with a patch series", including real build
  times and disk use on the reference machines.
- A short video showing the build pipeline (screen recording, no hype).
- A post for Chromium-fork maintainers describing our patch tooling, inviting review.

### Phase 2 — Internal Alpha

**Trigger:** a daily-drivable internal build for maintainers and trusted testers.

**Content:**

- The first **benchmark report** with raw data (Brumel vs Chrome and others, same machine,
  same pages). Publish it whatever the result.
- Demo videos of features that work: vertical tabs, Clean Web blocking, session restore.
- Open a tester sign-up via a GitHub Discussion. Consider Discord or Matrix at this point.

### Phase 3 — Public Alpha

**Trigger:** signed, verifiable builds that the public can download, plus a working update
channel.

**Content:**

- **Show HN** with a runnable alpha.
- Reddit r/browsers launch post, YouTube walkthrough, TikTok short demos.
- Landing page "Download" section goes live, with checksums and signatures.

### Phase 4 — Public Beta

- Brumel Nano, workspaces and sync demos, each published only when it is real.
- Public benchmark dashboard.
- Product Hunt launch (one attempt, prepared well, no vote solicitation).

### Phase 5 — Version 1.0

- Coordinated 1.0 announcement: release notes, security process, roadmap for the future.
- Press kit (logo, screenshots, fact sheet with verified numbers only).

## Demo ideas

Each demo needs a **gate**: the condition that must be met before it can be published.

| Demo | Gate before publishing |
|---|---|
| Hundreds of tabs open with reduced memory | Only if the [benchmarks](../benchmarks/BENCHMARKS.md) prove it against Chrome under equal conditions, with the raw data linked |
| Recover a lost session (Browser Time Machine / Zero Loss) | Feature works in a public build |
| Native ad and tracker blocking (Clean Web) | Feature works; show the blocked counter and the page breakage rate honestly |
| Organise tabs with free local AI (Brumel Nano) | Runs fully offline; show the hardware used and the memory cost |
| Find something from history in natural language (Smart Memory) | Runs locally; disclose model size and latency |
| Compress a file directly when uploading (Smart Upload) | Works in a public build |
| Search for words inside a video (Video Search) | Works with local transcription; disclose limits |
| Find which extension slows the browser (Extension Doctor) | Diagnostic validated on real extensions, with attribution done fairly |
| Upload a file from your phone with a QR code (Mobile Upload) | Security review done; the transfer is end-to-end encrypted |
| Show every external connection the browser makes (Glass Box) | Log is complete for browser-initiated connections; method documented |
| Performance comparison with Chrome | Methodology published; same hardware, pages and extensions |
| Disabled features do not consume resources | Measured: memory and CPU with the feature on, off and never enabled |

## Content calendar by milestone

| Milestone | Devlog | Short video | Social thread | Reddit / HN | Other |
|---|---|---|---|---|---|
| Pre-development | #0001 intro (done), #0002 architecture choices | Logo exploration (optional) | Intro thread | r/browsers feedback post; Ask HN (optional) | GitHub Discussions open |
| Technical Foundation | First build, patch tooling | Build pipeline timelapse | Build milestone thread | r/chromium technical post | n/a |
| Internal Alpha | Benchmarks #1 (raw data) | 2–3 feature demos | Benchmark thread | r/browsers update | Tester sign-up |
| Public Alpha | Release notes, security model | Walkthrough | Launch thread | **Show HN**, r/browsers launch | Landing page downloads |
| Public Beta | Nano, sync, workspaces deep dives | Feature series | Beta thread | Updates | Product Hunt |
| 1.0 | 1.0 retrospective | Launch video | Launch thread | Launch posts | Press kit |

Cadence: aim for **one devlog per meaningful milestone**, not per week. Silence is better than
filler.

## Metrics that matter

**We track:** issues and discussions with real evidence, returning contributors, merged
external PRs, tester retention (from Internal Alpha onward), crash-free sessions, benchmark
reproducibility (others able to reproduce our numbers) and the time to ship upstream
security fixes.

**We do not optimise for:** stars, follower counts, impressions or upvotes. We look at them, but
they are never a goal.

## What not to do

- Do not say or imply that Brumel is ready, fast, private or secure before it is measured and
  audited.
- Do not post "Chrome killer" style copy or attack other browsers. We compare, credit and stay
  factual.
- Do not use undisclosed paid promotion, buy engagement, solicit votes or use multiple
  accounts.
- Do not post on behalf of the project from automation.
- Do not use screenshots of features that are mock-ups without labelling them as **Concept**.
- Do not share personal or infrastructure details of the maintainers.
