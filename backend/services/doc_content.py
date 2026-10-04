"""Full in-app document content for the Documentation Hub.

Each catalog entry in ``doc_service.RAW_DOCUMENTS`` maps to a complete,
self-contained markdown document here, served by ``GET /api/v1/docs/{doc_id}``
and rendered inside the in-app documentation reader.
"""

DOCUMENT_CONTENT: dict[str, str] = {
    "github-docs-home": """\
## Overview

GitHub Docs is the official, always-current reference for everything on the
platform: repositories, pull requests, Actions, security, administration, and
more. Think of it as the map for the entire GitHub landscape — if you are ever
lost, the answer is almost always one search away.

## What lives inside

- **Get started** — account setup, Git installation, and the core workflow.
- **Repositories** — creating, configuring, and managing projects.
- **Pull requests & issues** — proposing, reviewing, and tracking changes.
- **Actions** — automating builds, tests, and deployments with CI/CD.
- **Codespaces** — instant, cloud-hosted development environments.
- **Security** — Dependabot, secret scanning, and branch protection.

## How to use it well

1. Use the search bar before asking in forums — official docs rank first.
2. Check the version selector at the top of every page (Free/Pro/Team/Enterprise)
   so instructions match your account.
3. Bookmark the changelog page to stay current with platform updates.

## Key takeaways

> The official docs are the single source of truth. Tutorials age, blog posts
> drift — GitHub Docs tracks every feature release.

- Every page has a **"Was this helpful?"** control; feedback really shapes docs.
- Pages include **rest-API examples** you can copy straight into `curl`.
- Printable and translatable versions exist for most pages.
""",
    "hello-world-quickstart": """\
## Overview

GitHub's official 10-minute introduction. In one sitting you will create a
repository, make a branch, commit a change, and open a pull request — the exact
sequence you will repeat for the rest of your open source life.

## Step 1 — Create a repository

1. Click the **+** in the top-right corner, choose **New repository**.
2. Name it `hello-world`, add a short description, tick **Add a README**.
3. Click **Create repository**.

A repository is the container for your project: files, folders, history, and
discussion all live inside it.

## Step 2 — Create a branch

Branches let you work without touching the default branch.

- Open your new repo, click the **branch selector** (`main`).
- Type `readme-edits`, press **Create branch**.

Now two independent copies of the project exist: `main` (the truth) and
`readme-edits` (your playground).

## Step 3 — Make and commit a change

1. Open `README.md` and click the pencil icon.
2. Edit a line or two.
3. Write a commit message like `Improve intro paragraph`, press
   **Commit changes**.

A commit is a labeled snapshot — small, frequent commits make history easy to
read and easy to revert.

## Step 4 — Open a pull request

Click **Compare & pull request**, describe what changed, and open it. A PR is a
proposal: *please review and merge these changes*. You can comment, request
review, and iterate with commits until it is merged.

## Key takeaways

```text
create repo -> branch -> commit -> pull request -> merge
```

> The whole loop above happens on GitHub without installing anything — the same
> flow scales from hello-world to a codebase with thousands of contributors.
""",
    "github-quickstart-newcomers": """\
## Overview

This is the daily-driver guide: install Git, connect it to GitHub, and adopt
the clone → branch → commit → push → pull-request loop used by nearly every
open source project.

## Set up Git locally

```bash
# 1. Download Git from git-scm.com, then verify
git --version

# 2. Identify yourself (name + email appear on every commit)
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## Authenticate with GitHub

Modern Git uses the credential manager bundled with Git for Windows / macOS:

- **HTTPS** — push and you are prompted; Git stores the token.
- **SSH** — generate a key and add it under *Settings → SSH and GPG keys*:

```bash
ssh-keygen -t ed25519 -C "you@example.com"
cat ~/.ssh/id_ed25519.pub   # paste this into GitHub
```

## The everyday workflow

```bash
git clone https://github.com/owner/repo.git   # get a local copy
cd repo
git switch -c my-feature                      # new branch
# ...edit files...
git add .                                     # stage changes
git commit -m "Add my feature"                # snapshot
git push -u origin my-feature                 # publish branch
```

Then open the pull request on GitHub, respond to review feedback with more
commits, and delete the branch after merge.

## Key takeaways

- `pull` before you `push` to stay in sync with upstream work.
- One branch = one idea; small branches merge fast and conflict rarely.
- Commit messages are documentation: write them for the person reading in a
  year (often you).
""",
    "set-up-git": """\
## Overview

Official instructions for installing Git and telling it who you are. Every
commit you make carries this identity, so it is worth five careful minutes.

## Install Git

| Platform | Command / Source |
| --- | --- |
| Windows | [Git for Windows](https://git-scm.com/download/win) (includes Git Bash) |
| macOS | `brew install git` or `xcode-select --install` |
| Linux | `sudo apt install git` / `sudo dnf install git` |

Verify:

```bash
git --version
```

## Configure identity and defaults

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global core.editor "code --wait"   # VS Code as commit editor
```

> Tip: set the email to a GitHub **noreply** address
> (`ID+username@users.noreply.github.com`) to keep your personal inbox private
> while commits still link to your profile.

## Connect to GitHub

1. **HTTPS** — easiest; Git Credential Manager stores a browser-obtained token.
2. **SSH** — best for frequent pushes:

```bash
ssh-keygen -t ed25519 -C "you@example.com"
eval "$(ssh-agent -s)" && ssh-add ~/.ssh/id_ed25519
ssh -T git@github.com          # should greet you by username
```

3. **GitHub CLI** — `gh auth login` configures both HTTPS and credential
   helpers in one step.

## Key takeaways

- `git config --global --list` shows everything you have set so far.
- Per-repo overrides win: drop `--global` inside a project.
- Windows users: keep line endings consistent with
  `git config --global core.autocrlf true`.
""",
    "how-to-contribute-guide": """\
## Overview

The classic Open Source Guides essay answering the biggest question of all:
*"I want to help — but how?"* It reframes contribution as something far wider
than code.

## Why people contribute

- To learn real-world engineering and tooling.
- To meet mentors and grow a public portfolio.
- To fix the bug that annoyed them and give back.
- To shape the software they depend on.

## Anatomy of a good first contribution

1. **Read the README and CONTRIBUTING file** — every project defines its own
   process; following it signals respect.
2. **Watch how the maintainers behave** in issues and PRs; mirror their norms.
3. **Start small and true**: fix a typo, clarify a doc, add a failing test.
   Small verified PRs build the trust that unlocks bigger ones.
4. **Communicate before you build** for anything non-trivial: open an issue,
   outline your plan, get a maintainer's nod.

## Contribution types that matter

- Documentation fixes and translations.
- Bug reports with clean reproduction steps.
- Design, accessibility, and UX feedback.
- Test coverage, CI improvements, and release management.
- Answering newcomer questions in discussions.

## Finding a project

> Contribute to software **you already use** — your motivation and context will
> be better than any trending-project list can offer.

Check `good first issue` labels, project activity (recent commits are a sign of
a live project), and the responsiveness of maintainers.

## Key takeaways

- A contribution is judged by its usefulness, not its size.
- Always read the contributing guide before the first PR.
- The opensource.guide page itself is on GitHub — you can fix it via PR.
""",
    "first-contributions": """\
## Overview

A famous hands-on repository that walks absolute beginners through making a
real pull request in minutes. It exists purely for practice — breaking it is
impossible and encouraged.

## What you will do

1. **Fork the repository** — creates `you/first-contributions`.
2. **Clone it locally:**

```bash
git clone https://github.com/you/first-contributions.git
cd first-contributions
git switch -c add-your-name
```

3. **Edit `Contributors.md`** — add your name to the list.
4. **Stage, commit, push:**

```bash
git add Contributors.md
git commit -m "Add <Your Name> to contributors list"
git push -u origin add-your-name
```

5. **Open the pull request** on GitHub and submit it.

The repo's automation responds, your PR gets merged, and you have exercised
fork → branch → edit → commit → push → PR with zero risk.

## Why the flow matters

The exact same mechanics are used for contributions to Python, Kubernetes, or
any project. Practicing once on a sandbox removes the fear when it counts.

## Key takeaways

- Fork + clone is the standard for projects you cannot push to directly.
- Your name lands in the contributors list with a real merged PR in your
  history — an icebreaker for the next contribution.
- Translated versions of the guide exist in dozens of languages.
""",
    "pro-git-book": """\
## Overview

*Pro Git* is the complete, free, official book on Git, written by Scott Chacon
and Ben Straub and maintained at git-scm.com. If Git feels like magic, this
book turns it into machinery you can trust.

## Chapters that pay off fastest

- **Chapter 2 — Git Basics**: commits, staging, history, remotes, tagging.
- **Chapter 3 — Branching**: what a branch really is (a movable pointer),
  merging, rebase, and remote-branch mechanics.
- **Chapter 7 — Git Tools**: stash, interactive rebase, bisect, submodules,
  hooks, and more.
- **Chapter 10 — Internals**: object model (blob/tree/commit/tag), refs, and
  packfiles for the truly curious.

## Reading path for daily work

```text
Start at 2.1 -> 2.5, jump to 3.1-3.5, keep 7.x as a tool reference.
```

## Why it clicks

Git's model is simple underneath: a directed acyclic graph of snapshots plus
three areas (working tree, index, repository). Once you see commits as
immutable snapshots, merge conflicts and rebases stop being scary and start
being arithmetic.

## Key takeaways

- The full book is free online in many languages; the source is on GitHub.
- `git help <command>` opens the same material locally.
- Second edition (v2) tracks modern Git including `switch`/`restore`.
""",
    "git-reference-docs": """\
## Overview

The complete command reference for every Git subcommand, straight from the
Git project. This is the authority: options, defaults, exit codes, examples.

## Making the reference usable

The pages are dense, so pair them with these habits:

1. Read the **SYNOPSIS** block first — it is the command's shape.
2. Scan **OPTIONS** for the flag you half-remember; descriptions are precise.
3. Jump to **EXAMPLES** at the bottom — most pages end with copy-paste
   recipes.

## Commands worth knowing cold

```bash
git status       # what changed, what is staged
git log --oneline --graph --all   # history as a picture
git diff [--staged]               # exact edits, line by line
git restore [--staged] <file>     # unstage / discard safely
git switch -c <name>              # create + enter a branch
git bisect                        # binary-search the commit that broke it
git stash [pop]                   # park work mid-task
```

## Faster lookups

- `git help everyday` — the seven-command daily cheat sheet.
- `git help workflows` — central / fork / topic-branch patterns.
- `git help tutorial` — a guided mini-course straight from the source.

## Key takeaways

> Everything you read in blog posts is a summary of these pages. Going to the
> reference first removes outdated advice from the equation.

- Docs match your installed version — run `git --version` and read the same
  version on git-scm.com to avoid flag drift.
""",
    "learn-git-branching": """\
## Overview

An interactive visual playground that teaches Git branching by letting you
*see* commits, branches, and rebases as living graphs. Widely considered the
fastest way to build a correct mental model of Git.

## How it works

- The screen shows your commit graph in real time.
- You type real Git commands (`git commit`, `git branch`, `git rebase`).
- Levels challenge you to reach a target graph — the robot rebuilds every
  scenario so you can experiment freely.

## Learning path

1. **Main sequence**: commit basics → branching → merging → rebase → detached
   HEAD → relative refs (`^` and `~`) → reverting.
2. **Remote sequence**: clone, fetch, pull, push, tracking branches, force-push
   dangers — the exact choreography behind team workflows.

## Concepts it finally makes obvious

- A branch is just a **label on a commit** — nothing is copied.
- Merge creates a commit with two parents; rebase *replays* commits on top of
  another base, producing linear history.
- `git pull` = fetch + merge; `git pull --rebase` avoids the merge bubble.

## Key takeaways

> Ten minutes of visual rebasing teaches more than a week of `git push
> --force` archaeology.

- The site has no login and saves progress locally; every level is repeatable.
- Advanced levels cover cherry-picking, tags, and `git describe`.
""",
    "resolving-merge-conflict": """\
## Overview

A merge conflict happens when two branches change the same lines differently
and Git cannot choose. It is normal, not an error — this official guide walks
through resolving one on the command line.

## Why conflicts happen

- Two people edit the same lines of one file.
- A branch and its base both edit imports at the top of a file.
- A file is deleted on one branch and edited on the other.

## Resolving step by step

1. **Start the merge** — Git stops at the conflict:

```bash
git pull origin main
# CONFLICT (content): Merge conflict in app.py
```

2. **Inspect the markers** inside the file:

```text
<<<<<<< HEAD
your branch's version
=======
their version from main
>>>>>>> main
```

3. **Edit the file** so it contains the correct final version — keep one side,
   blend both, or write something new. Delete the marker lines.
4. **Mark resolved and commit:**

```bash
git add app.py
git commit            # completes the merge
```

5. **Verify** with the project's tests before pushing the merge.

## Tools that make it easier

- `git diff` shows only conflicted hunks during a merge.
- VS Code offers **Accept Current / Incoming / Both** buttons in-editor.
- `git merge --abort` returns you to the pre-merge state if things go wrong.

## Key takeaways

> A conflict means two humans cared about the same lines. Resolution is a
> decision about intent, not a mechanical edit.

- Pull frequently from upstream so conflicts stay small and frequent instead
  of large and rare.
- Conflicts during rebase are resolved with `git add` + `git rebase
  --continue`.
""",
    "undoing-things-git": """\
## Overview

Git lets you fix mistakes at every stage — as long as nothing was pushed to a
shared branch. This book chapter maps each scenario to the right command.

## The last commit isn't right

```bash
git commit --amend                        # fix the message
git commit --amend --no-edit              # add forgotten staged changes
git restore --staged file.txt             # unstage (keep edits)
git restore file.txt                      # discard local edits (destructive)
```

> If the commit is already pushed to a shared branch, do **not** amend — that
> rewrites history everyone depends on. Add a follow-up commit instead.

## Undo commits safely

```bash
git revert <sha>     # create a commit that INVERTS an old one — safe
git reset --soft HEAD~1   # move back, keep changes staged
git reset --hard HEAD~1   # move back, discard changes — local only!
```

`revert` is the team-friendly choice: history stays append-only, and the undo
is itself reviewable.

## Rescue operations

- `git reflog` — a log of where HEAD has been; any entry can be checked out.
- `git stash` — park half-done work, `git stash pop` to restore it.
- `git reset --hard origin/main` — restore your branch to the remote truth.

## Key takeaways

- Unpushed history is yours to rewrite; pushed history is the team's.
- `--soft` keeps changes, `--mixed` unstages, `--hard` deletes — read twice.
- The reflog makes almost any Git disaster recoverable for ~90 days.
""",
    "rewriting-history-git": """\
## Overview

The power-tools chapter: interactive rebase, cherry-pick, and amend for
shaping clean, reviewable history — plus the caveats that come with rewriting
branches other people can see.

## Interactive rebase

```bash
git rebase -i HEAD~3
```

Opens an editor listing three commits with verbs:

- `pick` — keep as-is.
- `reword` — change the message.
- `squash`/`fixup` — fold into the previous commit.
- `drop` — remove it entirely.

Typical use: turn *"wip", "fix typo", "final"* into one clean, meaningful
commit before opening the PR.

## Cherry-picking

```bash
git cherry-pick <sha>   # copy one commit onto the current branch
```

Perfect for hotfixing a single change onto a release branch.

## The golden rule

> Never rewrite commits that exist on a branch others may have pulled. Once
> your PR has reviewers' comments, prefer follow-up commits or explicit
> `git push --force-with-lease` after announcing it.

```bash
git push --force-with-lease   # refuses to clobber remote work you never saw
```

## Key takeaways

- Rebase locally before sharing; merge afterwards.
- `filter-repo` can scrub secrets from history — but rotate credentials too.
- Clean history is a courtesy: `git bisect` and future debugging depend on it.
""",
    "understanding-github-flow": """\
## Overview

GitHub Flow is the lightweight, branch-based workflow behind most open source
projects: small branches, short-lived changes, everything through pull
requests. No release branches, no ceremony — just a disciplined loop.

## The six steps

1. **Create a branch** from the default branch. Name by topic:
   `fix/login-timeout`, `feat/dark-mode`.
2. **Add commits** — small and frequent, each with a clear message.
3. **Open a pull request** early — even before the work is finished — to share
   progress and invite early feedback.
4. **Discuss and review code** — respond to comments, push additional commits,
   keep conversations on specific lines.
5. **Merge after approval** and required checks (CI tests passing, reviews
   done).
6. **Delete the branch** — merged code is safe on main; deleting prevents
   stale-branch confusion.

## Why it works for distributed teams

- `main` is always deployable — every merge keeps it green.
- Pull requests are the review, discussion, and audit trail in one place.
- Branch protection rules can enforce tests and reviews before merge.

## Deploy-first culture

> GitHub Flow assumes you can deploy what you merge. Feature flags and preview
> environments let you merge daily while controlling what users see.

## Key takeaways

- One branch, one purpose, short life — measured in days, not weeks.
- The PR is the unit of collaboration, not the commit.
- If `main` breaks, revert forward with a new PR rather than patching hotfix
  branches.
""",
    "about-issues": """\
## Overview

Issues are GitHub's lightweight tracker for bugs, feature ideas, tasks, and
discussion — where nearly every open source contribution begins.

## What an issue is for

- **Bug reports** — something broke, with steps to reproduce.
- **Feature requests** — a problem worth solving, described as a user story.
- **Meta tasks** — "upgrade dependency", "split this module".
- **Discussion** — proposals that need consensus before code exists.

## Filing an issue people can act on

1. Search existing issues first — your bug may be known.
2. Use the project's issue templates (bug / feature forms).
3. Include: expected behavior, actual behavior, minimal reproduction steps,
   versions, and logs.
4. One topic per issue — a checklist of ten bugs is ten issues.

## The maintainer's lifecycle

```text
Open -> Triage (labels: bug, triage, good first issue)
     -> Assigned / planned
     -> PR linked ("Fixes #123")
     -> Closed automatically when the PR merges
```

## Power features

- **Labels & milestones** organize a busy backlog.
- **Task lists** inside an issue track sub-work.
- **Issue forms** enforce structure for bug reports.
- **Convert to discussion** moves open-ended threads out of the backlog.

## Key takeaways

- A great bug report is half the fix: reproduction steps are the currency.
- Reference issues in commits/PRs (`Fixes #42`) to auto-close them.
- Issues are documentation of *why* code changed — write them for posterity.
""",
    "github-actions-docs": """\
## Overview

GitHub Actions is the built-in CI/CD engine: workflows defined as YAML in your
repository, running on GitHub's servers on every push, PR, or schedule.

## Core concepts

- **Workflow** — one `.yml` file under `.github/workflows/`.
- **Event** — what triggers it: `push`, `pull_request`, `schedule`, `release`.
- **Job** — a set of steps running on a fresh virtual machine (or matrix).
- **Step** — a shell command or a reusable **Action** from the Marketplace.

## A minimal CI workflow

```yaml
name: CI
on:
  push:
    branches: [main]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: pytest -q
```

## Patterns worth adopting

- **Matrix builds** — test across versions with `strategy: matrix`.
- **Caching** — `actions/cache` for dependencies; minutes matter.
- **Secrets** — store tokens in repo settings; never commit them.
- **Concurrency** — cancel superseded runs on the same branch.

## Security essentials

> Pin third-party actions to a full commit SHA, not `@main` — a tag can be
> moved, a SHA cannot.

- Least-privilege `permissions:` blocks per job.
- Avoid `pull_request_target` with checkout of untrusted code.

## Key takeaways

- Public repos run Actions free — CI costs nothing for open source.
- The workflow file is versioned with the code it tests.
- `act` runs workflows locally for faster iteration.
""",
    "about-readmes": """\
## Overview

The README is your project's front door: the first file every visitor sees on
the repo page, and the reason they stay or leave. GitHub renders it right
below the file list.

## The essential skeleton

```markdown
# Project Name
One-sentence pitch: what it does and for whom.

## Install
pip install project-name

## Quick start
Minimal runnable example — copy, paste, works.

## Docs & Support
Links: full docs, issue tracker, discussions.

## Contributing
Point to CONTRIBUTING.md and the code of conduct.

## License
MIT — see LICENSE.
```

## Details that separate good from great

- A **screenshot or GIF** above the fold for anything visual.
- **Badges** (build status, version, license) in a single compact row.
- A **requirements section** instead of assuming.
- A **FAQ** fed by real recurring issues.

## Mechanics on GitHub

- Place the file at the repo root as `README.md` (Markdown).
- A `README` in the `.github` folder works for people who dislike root clutter.
- Adding `docs/` and committing a `README.md` creates an instant **project
  site** via Pages.

## Key takeaways

> Write the README for the visitor who arrived by accident and must decide in
> ten seconds whether this project is for them.

- Show, don't tell: one runnable snippet beats three paragraphs of prose.
- Keep install instructions tested — a broken quickstart loses everyone.
""",
    "securing-your-repo": """\
## Overview

Security features GitHub gives every repository for free: automated dependency
updates, secret scanning, and branch protection. Turning them on takes
minutes and prevents the most common breach patterns.

## Dependabot

- **Alerts** — flags vulnerable dependencies with severity and fix versions.
- **Security updates** — opens upgrade PRs automatically.
- **Version updates** — keeps everything current on a schedule:

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: pip
    directory: "/"
    schedule:
      interval: weekly
```

## Secret scanning

Pushes containing known token formats are blocked or alerted; partners
(gitHub, AWS, Slack, OpenAI…) are notified to revoke leaked credentials
automatically.

> If a secret ever lands in history, rotate it **first**, then clean history —
> removal without rotation protects nobody.

## Branch protection & rulesets

- Require PR reviews and passing status checks before merge.
- Require signed commits; disallow force pushes.
- Mark `main` (and release branches) as protected via rulesets.

## Extra layers

- **Code scanning** (CodeQL) finds injection, XSS, and query flaws in code.
- **Security policy** (`SECURITY.md`) gives reporters a private channel.
- **Dependency review** on PRs shows license and vulnerability deltas.

## Key takeaways

- Enable Dependabot + secret scanning on every repo the day you create it.
- Branch protection converts good intentions into enforced process.
- Security is continuous: alerts are worthless if nobody triages them.
""",
    "about-pull-requests": """\
## Overview

A pull request is the conversation around a proposed change: the diff, the
review, the discussion, and the record of why the change happened. Master the
concept and the mechanics follow.

## What a PR contains

- **Commits** from a source branch, shown as a reviewable diff.
- **Description** — what changed, why, how to test.
- **Review thread** — line comments, approvals, requested changes.
- **Checks** — CI results and required status gates.

## How review and merge work

1. Reviewers see the diff with line-level commenting.
2. They respond: *Approve*, *Request changes*, or *Comment*.
3. Authors push fixes; discussions resolve inline.
4. When checks pass and approvals arrive, someone with access clicks merge:

| Strategy | History shape | Use when |
| --- | --- | --- |
| Merge commit | true graph preserved | want complete history |
| Squash | one clean commit per PR | noisy WIP commits |
| Rebase | linear, one commit each | curated linear history |

## PRs as documentation

> `git blame` answers *which commit*; the PR answers *why*, *who agreed*, and
> *what alternatives were rejected*.

## Key takeaways

- Small PRs (≤ ~400 changed lines) get meaningfully better reviews.
- Draft PRs signal intent without requesting review.
- Every PR should be traceable to an issue or a clear motivation.
""",
    "creating-pull-request": """\
## Overview

The official walkthrough for proposing changes — from a branch in the same
repository or from a fork when you lack write access (the usual open source
case).

## From a branch in your repo

1. Push your work: `git push -u origin feat/my-change`.
2. GitHub offers **Compare & pull request**; otherwise open *Pull requests →
   New*.
3. Set base: `main` ← compare: `feat/my-change`.
4. Write the description, link the issue (`Closes #42`), submit.

## From a fork (contributing to others)

```bash
# 1. Fork on GitHub, then:
git clone https://github.com/you/their-project.git
cd their-project
git remote add upstream https://github.com/owner/their-project.git
git fetch upstream && git switch -c fix-typo upstream/main
# 2. Commit your change, then push to YOUR fork
git push -u origin fix-typo
# 3. Open the PR: head = you:fix-typo, base = owner:main
```

## Writing the description

- **What** — one paragraph summary of the change.
- **Why** — link the issue; state the user-visible benefit.
- **How tested** — tests added, manual steps performed.
- **Screenshots** for UI changes (before/after).

## After opening

- Watch CI; fix failures promptly.
- Push follow-up commits in response to review — the PR updates automatically.
- Keep the branch focused: unrelated work belongs in another PR.

## Key takeaways

> Open the PR early as a draft — early feedback beats a perfect surprise.

- Sync with upstream (`git fetch upstream && git rebase upstream/main`) before
  asking for final review.
- Deleting the branch after merge is safe and tidy.
""",
    "reviewing-changes-prs": """\
## Overview

Code review is where quality, knowledge-sharing, and community health happen.
This guide covers reviewing *politely and effectively* — a skill for both
sides of the PR.

## Reviewer workflow

1. Read the PR description and linked issue first — context before diff.
2. Skim the **Files changed** tab for overall shape.
3. Review line by line, starting with tests: do they verify the claim?
4. Submit structured feedback: **Comment / Approve / Request changes**.

## High-value review comments

- Distinguish **blocking** (bugs, security, missing tests) from **nits**
  (style, naming) — label nits as nits.
- Ask questions instead of issuing verdicts: *"What happens if this list is
  empty?"* teaches more than *"add a guard"*.
- Suggest concrete fixes with code blocks reviewers can apply directly.
- Say what you liked — reviews that only criticize burn people out.

## Tone for open source

> Write every comment for the contributor who will read it with no tone of
> voice. Critique the code, praise the effort, assume good faith.

```text
Blocking: unhandled None here — input can be empty per #42.
Nit (optional): name could be `retry_count` to match the config key.
Nice: the regression test pins exactly the bug we hit.
```

## The author's side

- Respond to every comment; resolve threads as you fix them.
- Push small commits rather than force-pushing mid-review.
- Disagree in writing with reasons — the thread is the record.

## Key takeaways

- Fast first response matters more than perfect first response.
- Approvals express confidence, not perfection.
- Reviews are mentoring: the reviewer's job is a better contributor, not just
  better code.
""",
    "requesting-pr-review": """\
## Overview

Asking for review is a skill: the right reviewers, a clear summary, and
managed momentum are what keep a PR moving instead of rotting for weeks.

## Choosing reviewers

- **Code owners** are auto-requested when their paths change (CODEOWNERS
  file).
- Prefer 1–2 relevant reviewers; mass-assignment diffuses accountability.
- For ambiguous areas, comment `@maintainer` with a specific question instead
  of a blanket request.

## Making the PR easy to review

1. Title states the outcome: *"Fix NPE when repo has no README (#123)"*.
2. Description covers what / why / how tested.
3. CI green **before** you ask for eyes.
4. `Draft` until it is actually ready — drafts tell reviewers to wait.

## Keeping momentum

```text
Day 0  open PR (draft) -> CI green -> mark Ready -> request review
Day 2  no response? friendly nudge referencing their expertise
Day 5  maintainer busy? offer to split scope or pair on the review
```

- Reply to every comment; push fixes as small commits.
- Re-request review after substantive changes (the checkmark resets).

## Receiving a request changes

> A "Request changes" review is engagement, not rejection. Address it, push,
> and the same reviewer usually approves quickly.

## Key takeaways

- Reviewers review momentum: green checks and clear descriptions get read
  first.
- Small, focused PRs are reviewed in minutes, not days.
- After merge, thank reviewers — it sustains the community.
""",
    "keeping-branch-in-sync": """\
## Overview

Long-lived branches drift from `main` and collect painful conflicts. This
official guide covers keeping forks and branches current: syncing a fork,
rebasing onto upstream, and updating a PR branch.

## Sync your fork

```bash
git fetch upstream
git switch main
git merge --ff-only upstream/main     # fast-forward, no merge bubble
git push                              # update your fork on GitHub
```

On the GitHub UI, the **Sync fork** button on your fork's page does the same
in one click.

## Rebase a feature branch onto latest main

```bash
git switch feat/my-change
git fetch upstream
git rebase upstream/main
# resolve conflicts per commit, then:
git push --force-with-lease
```

Your PR shows only your own commits on top of current `main` — reviewers see
small diffs instead of giant merge bubbles.

## Alternative: merge main into the branch

```bash
git merge upstream/main   # safe, preserves history, adds a merge commit
```

Choose merge when the branch is shared or history rewriting would be rude;
choose rebase for solo, linear-history projects.

## Habits that prevent drift

- Sync `main` **before** starting new work each day.
- Keep feature branches small and short-lived (days, not weeks).
- Never let a PR sit while `main` moves fifty commits ahead.

## Key takeaways

> A fresh branch on top of current `main` is the cheapest conflict prevention
> there is.

- `--ff-only` is a safety net: it refuses surprising merges.
- Force-push only your own PR branches, and only with `--force-with-lease`.
""",
    "building-welcoming-community": """\
## Overview

Projects live and die by their communities. This official guide covers the
levers that turn a repo into a place people want to return to.

## The four foundational documents

1. **README** — sets expectations for what the project is.
2. **CONTRIBUTING.md** — how to participate, step by step.
3. **Code of Conduct** — behavioral standards and enforcement.
4. **LICENSE** — the legal terms underneath it all.

Each reduces friction for newcomers and decisions for maintainers.

## What welcoming looks like in practice

- Respond to first-time issues and PRs within days — even "thanks, looking!".
- Maintain `good first issue` labels that are actually small and well-specified.
- Pair labels with CONTRIBUTING pointers so new contributors know the drill.
- Celebrate contributions in release notes and READMEs.

## Growing the right way

> Communities scale through processes, not heroics: templates, labels, docs,
> and clear ownership let strangers collaborate without gatekeeping.

- Document decisions publicly (issues, discussions, RFCs).
- Create maintainer paths: triage → reviewer → committer, with criteria.
- Use GitHub **discussions** for open-ended conversation; keep issues for work.

## Handling conflict

- Enforce the code of conduct consistently — selective enforcement is worse
  than none.
- Keep debates on technical merit; move personal disputes to private contact.

## Key takeaways

- Newcomers judge a project by the *responsiveness*, not the code quality.
- Every automated nicety (templates, bots, labels) is maintainer time saved.
- A friendly culture is a security feature — more eyes, more honesty.
""",
    "code-of-conduct-adding": """\
## Overview

A code of conduct states the behavioral expectations of your community and
what happens when they are violated. GitHub offers the **Contributor
Covenant** as a one-click template in the community standards checklist.

## Why every project needs one

- Sets explicit norms — "professional and respectful" is too vague to enforce.
- Gives maintainers a fair, pre-agreed process for handling conflict.
- Signals to underrepresented contributors that harassment has consequences.

## Adding one to your repository

1. Open **Issues** → nothing to see; instead go to the repo and click
   **Community standards** (right sidebar, "About" area).
2. Click **Add code of conduct**.
3. Choose the Contributor Covenant (or Citizen Code of Conduct).
4. Fill in contact email(s), commit to the repo root as `CODE_OF_CONDUCT.md`.

## What the Contributor Covenant contains

- **Promise**: welcoming, inclusive behavior as the standard.
- **Standards**: harassment, trolling, personal attacks, publishing others'
  private info — all prohibited with examples.
- **Responsibilities**: maintainers may remove, ban, or edit comments.
- **Scope**: project spaces *and* public spaces when representing the project.

## Enforcement that works

> A code of conduct without enforcement is decoration. Publish who enforces,
> how reports are handled, and apply consequences consistently.

- Create a private reporting channel (an email alias works).
- Acknowledge reports within a few days.
- Document outcomes in aggregate, never naming victims.

## Key takeaways

- Put the contact email in the file itself; missing contacts stall reports.
- The checklist turns green on your repo page when standards are in place —
  a visible trust signal.
""",
    "towns-governance-oss": """\
## Overview

How do open source projects actually decide things? This Open Source Guides
chapter maps the governance models used by real projects, from benevolent
.dictators to foundation-run collectives.

## Common models

- **BDFL (Benevolent Dictator for Life)** — one trusted person makes final
  calls (historically: Python). Clear, fast, key-person risk.
- **Meritocracy / consensus** — long-time contributors earn decision weight
  (historically: Apache). Slow but stable.
- **Liberal contribution** — the most active contributors *are* the decision
  makers by doing (e.g. many Node modules). Lightweight, low ceremony.
- **Foundation stewardship** — legal and trademark ownership lives with an
  independent foundation (Kubernetes/CNCF, Rust Foundation). Neutral ground
  for corporate contributors.

## What healthy governance documents

- **Who decides what**: daily maintenance (committers) vs direction (RFCs) vs
  identity (foundation board).
- **How to become a maintainer** — concrete criteria, not vibes.
- **Conflict resolution** — an escalation path that does not depend on shouting
  the loudest.

## Formal decision tools

- **RFC process** — proposals as documents, feedback windows, final decision
  recorded (Rust, React style).
- **Voting** — lazy consensus by default; formal votes when deadlocked.

## Choosing for your project

> Start simple (liberal contribution), write down what already happens, and
> formalize only when growth forces it. Governance follows reality, not the
> other way around.

## Key takeaways

- Every project is governed — the only question is whether it is written down.
- Unwritten rules advantage insiders; written rules welcome newcomers.
- When a project outgrows its founder, a foundation is the classic off-ramp.
""",
    "getting-paid-oss": """\
## Overview

Can open source work pay? Yes — through sponsorships, grants, employment,
platforms, and paid hosting of free software. This guide surveys the honest
paths and their trade-offs.

## The main models

- **Sponsorships** — GitHub Sponsors, Patreon, Open Collective: many small
  recurring donations. Works best with visible, consistent output.
- **Grants & fellowships** — NLnet, Mozilla, Prototype Fund: project-based
  funding with applications and reports.
- **Employment** — companies hire maintainers of software they depend on; the
  most common way maintainers get paid.
- **Paid support/hosting** — open core or managed-cloud models (the GitLab /
  Supabase pattern) once a project has product-market fit.
- **Bounties** — issue-level funding via Algora/Polar-style platforms.

## Practical advice

1. Build proof of usefulness first: users, stars, release cadence, issue
   activity.
2. Make giving easy: Sponsors button, transparent funding goals, an Open
   Collective for communal projects.
3. Document what money funds — "maintainer hours for triage" beats "support
   the project".
4. Beware burnout economics: occasional large donations end; steady, modest
   income lasts.

## Sustainability reality check

> Funding follows the value created for others. The more your project is
> load-bearing for real businesses, the more leverage you have when asking.

## Key takeaways

- Most maintainers get paid via employment or grants, not donations.
- Transparency about funding builds trust with contributors.
- Never let a single sponsor become your only income stream.
""",
    "finding-users-project": """\
## Overview

Code published is not code used. This guide covers finding and growing the
user base your project deserves — honestly, without growth-hacking.

## Seed the first hundred users

- **Go where the problem lives**: subreddits, Discords, HN, dev.to, relevant
  mailing lists. Share as a solution, not an ad.
- **Write the launch post**: the problem, why existing tools fail, a GIF of
  the fix. One good post beats ten tweets.
- **Ask your network**: teammates, classmates, and prior communities are the
  first real users.
- **Interoperate**: plugins, integrations, and docs for adjacent tools put you
  in existing workflows.

## Make adoption effortless

- A README with a 60-second quickstart (install → run → visible result).
- Reproducible examples and a demo deployment.
- Semantic versioning + a changelog so upgraders trust you.

## Retention beats acquisition

> Users stay for responsiveness. Answer every issue; ship the fix you promised.
> A project with kind, fast maintainers markets itself.

- Add a **testimonial or users list** when companies adopt you (ask!
  permission matters).
- Track adoption signals beyond stars: clones, package downloads, issue
  authors, repeat contributors.

## Key takeaways

- Distribution is a feature: budget time for it like code.
- Ten engaged users who file bugs are worth a thousand who star and leave.
- Say what the project is *for* as loudly as what it does.
""",
    "documentation-system-divio": """\
## Overview

The DIVIO documentation framework — the four-quadrant model that separates
**tutorials, how-to guides, reference, and explanation**. Once internalized,
it explains why docs feel broken and how to fix them.

## The four quadrants

| Quadrant | Serves | Form | Test |
| --- | --- | --- | --- |
| Tutorial | learning | a lesson, guaranteed success | does it work for a novice? |
| How-to | goals | recipe for a real task | does it solve the task? |
| Reference | information | dry, accurate, complete | is it correct & findable? |
| Explanation | understanding | essay, discussion, context | does it deepen insight? |

## Why mixing them fails

- A tutorial that digresses into architecture theory loses the learner.
- Reference pages that try to teach become both unscannable and unreliable.
- How-tos that explain at length stop being recipes.

Each type answers a different question: *learning / doing / looking /
understanding*.

## Applying it to your project

```text
docs/
  tutorial.md      # first 15 minutes, zero assumptions
  howto/           # deploy, configure, migrate — task by task
  reference/       # API, config flags, generated from source where possible
  explanation/     # why we chose queues over streams; architecture notes
```

## Writing discipline

> Tutorials must be **tested end-to-end by a fresh machine**. Reference must
> be **generated or linted against reality**. Explanation is allowed to have a
> point of view.

## Key takeaways

- Diagnose complaints ("docs are bad") by asking *which quadrant* is missing.
- Structure your docs tree by quadrant, not by feature.
- The full essay is short and worth reading twice.
""",
    "writing-on-github": """\
## Overview

GitHub Flavored Markdown (GFM) is the dialect behind READMEs, issues, PRs,
and comments. This official reference covers formatting that goes beyond
plain Markdown.

## The everyday toolkit

```markdown
**bold** and *italic* and `inline code`

- [ ] task list item      # renders with checkboxes
- [x] done item

> blockquote for quotes and callouts

| Column | Value |   # tables, GFM extension
| --- | --- |
| a | b |
```

## Alerts (the big one)

```markdown
> [!NOTE]    Useful context the reader should keep in mind.
> [!TIP]     A shortcut or trick.
> [!IMPORTANT] Critical information.
> [!WARNING]  Risk of data loss or breakage.
> [!CAUTION]  Danger — proceed carefully.
```

They render as colored callout boxes in issues, PRs, and READMEs.

## Code and diffs

````markdown
```diff
- removed_line
+ added_line
```
````

Syntax highlighting works for hundreds of languages; ` ```console ` and
` ```shell ` style output beautifully.

## Collaboration extras

- `@mention` people and teams; `#123` references issues/PRs.
- `<!-- comment -->` hides notes from rendered output.
- Collapse long sections with `<details>` for giant logs.

## Key takeaways

- Learn the alerts and task lists first — biggest visual payoff.
- Tables and details make issues readable at scale.
- Everything here works in READMEs too — use callouts for warnings.
""",
    "starting-open-source-project": """\
## Overview

A launch checklist for turning a personal repo into a project strangers can
use and contribute to — from licensing to community files to first release.

## The pre-launch checklist

1. **LICENSE** — without one, *all rights reserved* applies and nobody can
   legally use it. Pick MIT/Apache-2.0/GPL per your goals.
2. **README** — pitch, quickstart, requirements, support links.
3. **CONTRIBUTING.md** — how to set up, test, and submit PRs.
4. **CODE_OF_CONDUCT.md** — one click from the community standards checklist.
5. **Issue/PR templates** — structured input from day one.
6. **CI** — a workflow that runs tests on every PR; it IS your review aid.

## Decide early

- **Name & identity** — searchable, unique, ideally available on PyPI/npm.
- **Scope** — what the project will *not* do. Write it in the README.
- **Maintenance promise** — response times and deprecation policy, even as
  simple sentences.

## First release mechanics

```bash
git tag -a v0.1.0 -m "First usable release"
git push origin v0.1.0
```

Then create a GitHub **Release** with notes. Early versions should be
explicitly honest: `0.x` means APIs may move.

## Marketing with integrity

> Post the launch story where your users gather; show the problem being
> solved. Reply to every early comment — the first week shapes the community.

## Key takeaways

- Launch readiness is documentation + license + CI, not feature count.
- Set expectations (scope, maturity) before users set them for you.
- Ship v0.1.0 to five real users; feedback beats more features.
""",
    "semantic-versioning": """\
## Overview

SemVer is the `MAJOR.MINOR.PATCH` contract that lets software depend on
software without reading source code. The version number itself communicates
what changed.

## The contract

Given version `MAJOR.MINOR.PATCH`:

- **MAJOR** — incompatible API changes.
- **MINOR** — backwards-compatible functionality.
- **PATCH** — backwards-compatible bug fixes.

Pre-release builds append `-alpha.1`, `-rc.2`; build metadata appends
`+build.5`. Once released, a version is immutable — fix mistakes by shipping a
new version.

## Version bump decisions

```text
Added a function, old code still works?      -> MINOR
Changed a function's signature?              -> MAJOR
Fixed a crash, API untouched?                -> PATCH
Deprecated (but still working) an API?       -> MINOR + docs
Removed the deprecated API?                  -> next MAJOR
```

## In dependency ecosystems

- npm caret `^1.2.3` allows MINOR+PATCH; tilde `~1.2.3` PATCH only.
- Python constraints `~=1.2` behave like caret.
- Lockfiles pin exact trees while the manifest expresses intent.

## Practical guidance

> Before `1.0.0`, breaking changes may ride in MINOR bumps — but the first
> real user is the moment to go `1.0.0` and start honoring the contract.

## Key takeaways

- SemVer is communication: it answers "is upgrading safe?" without a diff.
- Deprecate → wait → remove; never break silently.
- Automate bumps with conventional-commit tooling where possible.
""",
    "keep-a-changelog": """\
## Overview

A changelog is a human-curated file at the project root — `CHANGELOG.md` —
listing notable changes per version, newest first. *Keep a Changelog* defines
the format almost everyone copies.

## The file skeleton

```markdown
# Changelog
All notable changes to this project will be documented in this file.

## [1.2.0] - 2026-09-15
### Added
- Dark mode support (#231)
### Changed
- Config now reads `osad.toml` (was `osa.conf`)
### Fixed
- Crash when repo had no README (#240)

## [Unreleased]
### Added
- (work in progress)
```

## The section vocabulary

- **Added** — new features.
- **Changed** — changes to existing behavior.
- **Deprecated** — soon-to-be-removed features.
- **Removed** — removed features (replaces deprecations).
- **Fixed** — bug fixes.
- **Security** — vulnerability fixes.

## Principles

1. **Humans first** — written for users, not auto-dumped from git log.
2. **Unreleased section** — always open, commits land there as they merge.
3. **Same-day dates** — `YYYY-MM-DD` for every release.
4. **Don't log every commit** — log what users *feel*.

## Changelog vs release notes

> The changelog is the durable file; GitHub Releases are its per-version
> announcement. Many projects paste each changelog entry into its Release —
> both audiences are served.

## Key takeaways

- Write the entry **when you merge**, not the night before a release.
- PR titles + conventional commits can draft entries; curate before shipping.
- Link every entry to its issue/PR for the curious.
""",
    "conventional-commits": """\
## Overview

Conventional Commits is a lightweight spec for commit messages:
`type(scope): description`. Machines can read it — versions, changelogs, and
releases become automation instead of chores.

## The format

```text
<type>(<scope>): <short summary>

[optional body]

[optional footer(s)]
```

Common types: `feat`, `fix`, `docs`, `refactor`, `perf`, `test`, `build`,
`ci`, `chore`, `revert`.

## Examples

```text
feat(auth): add GitHub OAuth login flow
fix(parser): handle empty README without crash
feat(api)!: require token in Authorization header   # ! = breaking

docs: rewrite contribution guide
chore(deps): bump fastapi to 0.141.1
```

Breaking changes use `!` before the colon or a `BREAKING CHANGE:` footer
explaining the migration.

## What automation unlocks

- **Version bump**: any `feat` -> MINOR, any `fix` -> PATCH, breaking -> MAJOR
  (semantic-release / release-please do this).
- **Changelog**: grouped by type, with scopes and links.
- **Review filters**: `git log --grep "^fix"` isolates fixes instantly.

## Rules that matter

1. Commit types are nouns from the fixed list — no surprises.
2. Summary: imperative mood, ≤ ~72 chars, no trailing period.
3. Breaking changes are always explicit (`!` or footer).
4. Squash merges keep the convention clean at the merge-commit level.

## Key takeaways

> Conventional Commits trades five seconds of typing for a versioned,
> changelogged, machine-readable history.

- Pair with squash merges so one PR = one conventional commit.
- Many repos enforce the format with commitlint + a CI hook.
""",
    "google-summer-of-code": """\
## Overview

Google Summer of Code (GSoC) is the flagship program paying contributors to
work on open source: a full-time, remote, mentorship-based internship-style
program run annually by Google with hundreds of participating organizations.

## How it works

1. **Organizations apply** and are selected (Feb–Mar).
2. **Contributors apply** with project proposals (Mar–Apr).
3. **Community bonding** — accepted contributors meet mentors and set up.
4. **Coding periods** with evaluations and stipend payments (typically May–
   August).
5. **Final evaluation** — mentors assess outcomes; contributors submit code.

Stipends are sized by project difficulty and contributor location.

## Eligibility (typical year)

- Anyone new to the program — students and non-students alike — 18+.
- First-time contributors to GSoC get priority for slots.

## What a winning proposal contains

- **The problem** and why it matters to that org's users.
- **Deliverables** broken into mid-term and final milestones.
- **Timeline** weekly, with buffer for exams and review cycles.
- **Prior work**: merged PRs with the org **before** applying — the single
  strongest predictor of acceptance.

## Preparation timeline that works

```text
Nov–Jan  pick 2–3 orgs, join their community, fix small issues
Feb      watch the orgs list, engage on the project channel
Mar      draft proposal, get mentor feedback before submitting
Apr      submit early; polish, don't procrastinate
```

## Key takeaways

> Accepted GSoC contributors almost always started contributing months before
> proposals opened. The program selects for community fit, not just code.

- Contributions during the application window are read as a preview of the
  summer.
- Past projects and proposals are public — study successful ones.
""",
    "hacktoberfest": """\
## Overview

Hacktoberfest is DigitalOcean's month-long (October) open source celebration:
register, submit qualifying pull requests, earn a digital reward and tree
planted in your name. It is the most beginner-friendly doorway into open
source.

## How participation works (typical year)

1. **Register** at hacktoberfest.com with your GitHub account (late Sept–
   October).
2. **Submit PRs/MRs** to any participating repository during October.
3. **Qualify**: a small number of accepted, non-spammy PRs (e.g. 4 in recent
   years; check the current rules).
4. Maintainers mark PRs valid/spam; only valid ones count.

## Rules that matter

- PRs must be to **public repos**, and count when merged or approved.
- **Spam is banned**: no `fix typo` raids on tiny-word lists, no automated
  translations. Maintainers label spam and it can disqualify you.
- Some repos are **Hacktoberfest-labeled** or opt-in only — check the topic.

## Finding good projects

- `topic:hacktoberfest` on GitHub — repos that explicitly welcome it.
- The official **profile-generator** repo: add your card, get a real merged
  PR in minutes.
- Projects you already use — issues marked `good first issue`.

## Beyond the PR count

> The reward is the excuse; the habit is the prize. October is a forcing
> function: one month of reading CONTRIBUTING.md, filing clean PRs, and
> talking with maintainers.

## Key takeaways

- Quality > quantity: four thoughtful PRs beat twenty drive-by typos.
- Use it to start a project relationship, not to farm rewards.
- Maintainers: prepare issues, label them, enable only what you can review.
""",
    "outreachy": """\
## Overview

Outreachy provides **paid, remote internships** in open source specifically
for people subject to systemic bias and impacted by underrepresentation in the
industry. Twice a year, ~3 months, stipend-funded, with dedicated mentors.

## Who it serves

- Applicants who are women (cis and trans), trans men, nonbinary people, and
  cis men of color underrepresented in tech in their region — full eligibility
  details on the site.
- No student requirement; career-changers welcome.

## The application process

1. **Initial application** (about a month before internships start).
2. **Eligibility check** and demographic screening.
3. **Contribution phase** — 10 days to 2 weeks working on a real task with a
   mentor from a participating community.
4. **Final application** for that project; mentors select interns.

The contribution phase IS the interview: show communication, responsiveness,
and steady progress.

## What interns do

- A project chosen with their mentor (code, docs, design, research, or
  translation depending on the community).
- Weekly check-ins and a final report; many interns continue after the
  internship ends.

## Preparing a strong application

- Read the project's docs and recent issues before contacting mentors.
- Pick **one** project and go deep rather than sampling five.
- Ask questions early and specifically; mentors read engagement as signal.

## Key takeaways

> Outreachy's slogan — "treat each applicant as a future colleague" — extends
> to applicants: act like a colleague from your first message.

- Stipends and dates differ per cohort — always check the current round.
- Alumni often become maintainers; the pipeline is real.
""",
    "github-campus-experts": """\
## Overview

GitHub Campus Experts are student leaders who build open source, technical,
and community programs on their campuses with GitHub's training and support —
public speaking, community organizing, and technical writing included.

## What Experts get

- **Training** from GitHub in community leadership, event design, and public
  speaking.
- Direct lines to GitHub staff, swag, and program recognition.
- A global network of hundreds of student leaders to exchange playbooks with.

## What Experts do

- Run campus events: Git/GitHub workshops, Hacktoberfest chapters, open source
  days.
- Grow local communities around open source and GitHub Education tools.
- Publish guides and resources for other students.

## Eligibility and application

- You must be a **student**, 18+, at a degree-granting institution, with at
  least two semesters (or equivalent) remaining.
- Applications open periodically; the process includes a written application
  and an interview, plus a sample of community or technical leadership.

## Building the case for yourself

```text
Show, don't promise: an existing club, a workshop you ran,
a repo of your campus community's resources — evidence beats intent.
```

## Key takeaways

- Campus Experts is a *leadership* program that uses open source as its
  medium — apply if organizing energizes you.
- Pair it with the Student Developer Pack to fund the community you build.
- Terms are time-boxed and renewable; plan continuity with your successor.
""",
    "github-student-pack": """\
## Overview

The GitHub Student Developer Pack bundles dozens of free tools, credits, and
services for verified students — GitHub Copilot, cloud credits, domains,
IDEs, design tools, and more. It is the fastest way to turn a student account
into a professional development environment.

## Signature benefits

- **GitHub Copilot Pro** — free while you are verified.
- **Cloud credits** — DigitalOcean, Heroku, Azure, and more.
- **Domains** — free `.me` / `.tech` domain for a year.
- **Developer tools** — JetBrains IDEs, Termius, GitKraken, Sentry, and many
  others.

## How to get verified

1. Go to education.github.com/pack and click sign up.
2. Provide **proof of enrollment**: student ID, enrollment letter, or
   transcript with dates and institution name visible.
3. Enable **location access** and camera verification when asked.
4. Verification usually completes within days; re-verification is periodic.

## Making the most of it

- Use Copilot on a real project — learning accelerates on live code.
- Deploy something with your cloud credits: a portfolio site or your open
  source project's demo.
- Register the free domain and host docs there with GitHub Pages.

## For teachers

> GitHub Classroom and the Teacher Toolbox give educators free team
> management, autograding, and tools for courses.

## Key takeaways

- Verification requires enrollment proof — prepare documents first.
- Most benefits are annual; set renewal reminders.
- The pack is a sandbox: use it to ship something real, not just collect
  offers.
""",
    "choose-an-open-source-license": """\
## Overview

Choose a License is GitHub's interactive chooser that walks you to the right
license in three questions. The one legal file every open source project
needs, chosen correctly.

## The shortlist

- **MIT** — do anything, keep the copyright notice. The default for maximal
  adoption.
- **Apache-2.0** — MIT plus an explicit patent grant and contribution terms.
  Preferred by enterprises.
- **BSD-3** — like MIT, plus a no-endorsement clause.
- **GPL-3.0 / LGPL** — strong copyleft: derivatives must stay open under the
  same license.
- **AGPL-3.0** — copyleft that reaches server-side use; defeats the SaaS
  loophole.
- **MPL-2.0** — file-level copyleft, a middle path.
- **Unlicense / CC0** — public domain dedication.

## The three chooser questions

1. **Do you want others to share improvements back?** -> copyleft (GPL family)
   if yes, permissive (MIT/Apache) if no.
2. **Does your community care about patents?** -> Apache-2.0.
3. **Do you want maximum simplicity?** -> MIT.

## What happens with NO license

> A repo without a license is *all rights reserved*. Nobody may legally copy,
> modify, or redistribute it — and most companies will not touch it.

## Applying it

```text
Add LICENSE (or LICENSE.txt) at the repo root with the full text,
optionally a SPDX identifier in package metadata: "license": "MIT"
```

## Key takeaways

- Never write your own license text; use a vetted one.
- License choice is community strategy, not just legalese.
- The chooser links each option to its full text and usage stats.
""",
    "licensing-a-repository": """\
## Overview

The official GitHub how-to for placing a license in your repository and what
it legally means — including how GitHub detects and displays your license.

## Where the license file goes

- Repo root, named `LICENSE` or `LICENSE.md` (also `LICENSE.txt`,
  `COPYING`).
- GitHub's licensee tool detects it and shows the license name with a link to
  its details in the file list header.

## Choosing and adding via GitHub UI

1. On your repo, click **Add file → Create new file**.
2. Type `LICENSE` as the filename.
3. A **Choose a license template** button appears — pick MIT, Apache-2.0,
   GPL-3.0, etc.
4. Review, fill in the year and name, commit.

## What the license does and does not do

| It grants | It does not grant |
| --- | --- |
| Use, copy, modify, distribute | Trademark rights |
| (Apache/GPL) patent rights | Warranty — software is "as is" |
| For contributors: terms for their patches | Liability for damages |

## Special cases

- **Your company owns the code?** Get legal sign-off before open-sourcing.
- **Forking** — the fork inherits the license; your changes are bound by it.
- **Multiple licenses** — some projects dual-license (e.g. MIT OR Apache-2.0)
  to ease downstream choices.
- **Private dependencies** — check that their licenses permit your use.

## Key takeaways

- Public + no license = unusable by others, whatever the README promises.
- Contributors own their additions — the project license covers their
  contributions only if they agreed to it (see CONTRIBUTING / CLA).
- License files are for lawyers and licensees alike; keep the full text,
  never a summary.
""",
    "github-support": """\
## Overview

GitHub Support is the official help portal for account, billing, and platform
issues that community forums cannot solve — data recovery, account access,
billing disputes, security reports.

## What support handles

- **Account access** — lost 2FA devices, account recovery, compromised
  accounts.
- **Billing** — charges, refunds, sponsorship and Actions spending questions.
- **Platform problems** — suspected outages (after checking githubstatus.com),
  data loss, repository corruption.
- **Trust & safety escalations** — impersonation, sensitive content reports.
- **Security reports** — via GitHub's private vulnerability disclosure
  (security.github.com), not the public ticket queue.

## How to file effectively

1. Sign in at support.github.com (Premium/Enterprise plans get faster SLAs).
2. Pick the closest category; the form asks for precise context.
3. Include: affected repo/account names, exact timestamps (UTC), error
   messages, request IDs if shown.
4. For 2FA lockouts, use the recovery codes you saved at setup — that is the
   fastest path, no ticket needed.

## Before you file

- **githubstatus.com** — live incident and maintenance status.
- **GitHub Community forum** — product questions answered by users and staff.
- **docs.github.com** — configuration issues are usually documented.

## Enterprise and education

> Enterprise Cloud/Server contracts include dedicated support with response
> SLAs; Campus programs route education questions through a dedicated portal.

## Key takeaways

- Save your 2FA recovery codes offline; support cannot bypass 2FA for you.
- Security issues never go to public tickets — use coordinated disclosure.
- Support is for *GitHub problems*, not for problems in your own code.
""",
    "github-community-forum": """\
## Overview

The GitHub Community forum (github.community) is where GitHub users ask and
answer product questions, share feedback directly with GitHub staff, and find
feature announcements outside the issue tracker.

## When to use the forum

- **Product how-to questions** that are not code-specific enough for Stack
  Overflow: workflows, permissions, Pages, Copilot plans.
- **Feature requests and feedback** — GitHub staff actively read the
  *Feedback* category.
- **Announcements** — changes to Actions pricing, Dependabot behavior, new
  features, and betas.

## What belongs elsewhere

| You need | Go to |
| --- | --- |
| Code-level debugging help | Stack Overflow |
| Repository-specific bugs | That project's issues |
| Platform outages | githubstatus.com |
| Account/billing problems | support.github.com |

## Asking questions that get answered

1. Search first — many answers exist, often from years past.
2. Title with the specific feature: *"Branch protection: require review from
   Code Owner only for /docs paths?"*
3. Share minimal context: what you tried, what happened, what you expected.
4. No secrets or tokens in screenshots.

## Etiquette

> The forum is staffed largely by volunteers and community members. Mark the
> accepted solution; a follow-up that closes the loop helps the next searcher.

## Key takeaways

- Forum answers sometimes include GitHub staff — a better channel for feature
  feedback than random tweets.
- Answers are indexed: a well-asked question becomes the reference for
  everyone after you.
""",
    "reporting-abuse-spam": """\
## Overview

GitHub's Community Guidelines define what is not allowed on the platform and
the official channels for reporting abuse, spam, and harmful content.

## What is reportable

- **Harassment and hate speech** targeting individuals or groups.
- **Spam** — fake accounts, link farms, star/ crypto scams, comment spam.
- **Malicious content** — malware repos, phishing pages, credential theft.
- **Impersonation** — accounts or repos pretending to be real people/orgs.
- **Sensitive or illegal content** — incl. non-consensual imagery, doxxing.

## How to report

1. **Report a user**: profile → About → **Report user**; pick the violation
   category.
2. **Report a repository / issue / comment**: the **...** menu → *Report*
   (same flow, content-scoped).
3. **DMCA**: github.com/github/dmca for copyright takedowns.
4. **Security**: suspected malware or credential phishing can also go to
   GitHub Security Lab / private reporting.

Reports go to GitHub Trust & Safety; you may remain anonymous for some
categories.

## The Community Guidelines in one line each

- Be excellent to each other — no harassment, doxxing, or threats.
- No spam, scams, or artificially inflated metrics.
- Content must be lawful; copyright is enforced via DMCA.
- Impersonation and misrepresentation are prohibited.

## Protecting yourself first

> Block first, report second — blocking instantly cuts off a harasser's
> ability to interact with you on the platform.

- Enable 2FA and review your security log for session anomalies.
- Limit profile details if you are being targeted.

## Key takeaways

- Reporting works: Trust & Safety acts on valid reports and can remove
  content, suspend accounts, and cooperate with law enforcement.
- For coordinated harassment, keep evidence before blocking.
- The guidelines apply everywhere on GitHub — repos, issues, profiles,
  usernames.
""",
    "github-status": """\
## Overview

githubstatus.com is GitHub's live service dashboard: current incidents,
planned maintenance, and 90-day uptime history for every major subsystem.
Check here before debugging an outage on your side.

## What is tracked

- **Git operations** — pushes, pulls, clones (usually the last thing to break).
- **Web & API** — github.com, REST, GraphQL, webhooks.
- **Actions** — workflow runs, runners, artifact/ caching backends.
- **Packages** — npm, PyPI, Maven, NuGet registries.
- **Codespaces, Pages, Copilot, Search** — each has its own component.

## Reading the page

- **Green banner** = all systems operational (the usual state).
- **Active incident** — ongoing problem, with a timeline of investigation /
  identification / monitoring / resolution updates.
- **Planned maintenance** — scheduled windows where some services degrade;
  usually announced days ahead.
- Each incident links its post-mortem when published.

## Incident response pattern

```text
Symptom: CI suddenly fails on git fetch, or Actions queue stalls.
Step 1  open githubstatus.com — is an incident live?
Step 2  subscribe to updates (Subscribe to Updates button -> email/SMS/RSS)
Step 3  check @githubstatus on X for real-time notices
Step 4  if status is green and your problem persists -> support ticket
```

## Automating checks

> The status page exposes an RSS/Atom feed and API (www.githubstatus.com/api
> — see status.openpage / Atlassian Statuspage conventions) so your on-call
> tooling can watch it for you.

## Key takeaways

- Green status with persistent failure = your problem (network, proxy,
  credentials) — but file it, history shows real incidents that were reported
  first by users.
- Webhook deliveries failing with timeouts are often a GitHub-side incident:
  check status before re-sending.
- Subscribe to updates during an active incident instead of refreshing.
""",
    # __MORE_DOCS__
}
