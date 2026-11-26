# Launch post drafts (English)

> **DRAFT. Do not auto-publish.** These are drafts for manual publication by the maintainer.
> Before posting, check that every statement still matches the current
> [project status](../../../README.md) and the [launch plan](../LAUNCH_PLAN.md). Phase 0 posts
> must make clear that **there is nothing to download yet**.

---

## 1. Reddit — r/browsers (Phase 0, feedback request)

**Title:** I'm starting an open-source Chromium-based browser focused on efficiency, privacy and not losing your stuff. There's nothing to download yet, so I'd like your critique of the plan.

**Body:**

Hi r/browsers,

I've started **Brumel**, an open-source browser based on Chromium. It's in **pre-development**:
no builds, no binaries, only a public plan. I'm posting now because I'd rather get the plan
right than polish a launch.

What I'm aiming for:

- **Efficiency.** Use fewer resources when your machine needs them, for example during a
  game, on battery or on a low-RAM laptop, without disabling Chromium's sandboxing or site
  isolation.
- **Memory.** Don't lose tabs, sessions, drafts or the context of what you were doing.
- **Clean Web.** Native ad and tracker blocking, with no sponsored junk of our own.
- **Trust.** No mandatory telemetry, no mandatory account, and a log showing every
  connection the browser itself makes.
- **Everyday tools.** Small things browsers should already do: compress a file when uploading
  it, export a table to CSV, search inside a video.

Optional local AI (small models running on your own machine) is part of the plan, but it's
off by default and never required.

What I'm **not** promising: dates, magic RAM numbers or "Chrome killer" anything. Performance
claims will only appear with a reproducible benchmark and raw data.

Everything is public: roadmap, feature catalog with IDs and statuses, architecture decisions
and threat model.

- Repo: https://github.com/Elgeryy1/brumel
- Discussions: https://github.com/Elgeryy1/brumel/discussions

I'd especially like to hear **what makes you stay with or leave your current browser**, and
which of the planned features you think are pointless.

---

## 2. Reddit — r/chromium (Phase 1, technical)

**Title:** Maintaining a small Chromium fork with a patch series: our approach (feedback welcome)

**Body:**

We're setting up Brumel as a patch-based Chromium derivative. We pin upstream stable tags,
keep our changes as an ordered patch series, selectively import ungoogled-chromium patches and
script everything so that rebases are reproducible. Our upstream strategy doc covers how we
plan to ship security updates quickly and what we deliberately avoid touching.

Doc: https://github.com/Elgeryy1/brumel/blob/main/docs/architecture/UPSTREAM_STRATEGY.md

If you maintain a fork, I'd value your comments on patch granularity, rebase tooling and CI
cost.

*(Only post once the first reproducible build exists. Include real build time and disk numbers.)*

---

## 3. Hacker News

### 3a. Phase 0: Ask HN (optional)

**Title:** Ask HN: What would actually make you switch browsers in 2026?

**Body:** I'm planning an open-source Chromium-based browser (pre-development, nothing to
run yet; plan at github.com/Elgeryy1/brumel). Before writing code, I want to stress-test the
priorities: resource use, session and data recovery, native blocking, transparency about
the browser's own network connections. What's missing from Chrome, Firefox, Brave, Vivaldi,
Arc or Zen that you'd switch for, and what would make you distrust a new browser immediately?

### 3b. Public Alpha: Show HN (DO NOT USE before a runnable build exists)

**Title:** Show HN: Brumel – an open-source Chromium browser built around efficiency and control

**Body:** Brumel is a Chromium-based browser. This alpha includes: [list ONLY features that
work in the build]. Builds are signed and checksummed: [link]. Benchmarks with raw data and
method: [link]. Known gaps: [honest list]. I'm happy to answer questions about the patch
strategy, the security model or anything else.

---

## 4. X and Bluesky thread (Phase 0)

1/ I'm building **Brumel**, an open-source, Chromium-based browser. Slogan: *Less noise. More control.* It's in pre-development: no builds yet, only a public plan. 🧵

2/ The idea: a browser can have hundreds of features without all of them running all the time. Anything optional can be fully switched off, and when it's off it should cost nothing.

3/ Five pillars: Efficiency, Memory (never lose your context), Clean Web (native blocking), Trust (no mandatory telemetry or account) and Everyday Tools.

4/ Local AI is optional, free and runs on your device. It helps with things like grouping tabs or finding something in your history. It's off by default and never required.

5/ No dates and no magic RAM numbers. Performance claims will only come with a reproducible benchmark and raw data.

6/ The roadmap, feature catalog, architecture decisions and threat model are all public. Feedback welcome: github.com/Elgeryy1/brumel

---

## 5. Short video script: TikTok, YouTube Shorts (Phase 0 devlog, about 45 s)

**[0–3 s]** On screen: a browser with 80 tabs, task manager showing high memory.
**Voice:** "Your browser shouldn't fight your computer."

**[3–12 s]** Cut to the repository and the roadmap.
**Voice:** "I'm starting Brumel, an open-source browser based on Chromium. There's nothing to download yet. I'm building it in public, from day one."

**[12–30 s]** Quick cuts of the five pillars as text cards.
**Voice:** "Use fewer resources when you're gaming or on battery. Never lose a session. Block ads natively. No mandatory telemetry or account. And small tools that fix everyday annoyances."

**[30–40 s]** The logo exploration sheet.
**Voice:** "Even the logo is still a draft. Tell me which one you'd pick."

**[40–45 s]** End card: "Brumel: Less noise. More control. Link in bio."

> Rule: never show a mock-up as a working feature. Label concept footage as **Concept**.

---

## 6. Product Hunt (Public Beta or later, DO NOT USE earlier)

**Tagline:** An open-source Chromium browser that stays out of your way.

**Description:** Brumel is a Chromium-based browser focused on efficiency, never losing your
context, native ad blocking and verifiable privacy. [Feature list limited to what ships in
the beta.] Free, open source, no account required.

**First comment (maker):** Why I built it, what's deliberately not included, benchmark link
with raw data, known limitations.
