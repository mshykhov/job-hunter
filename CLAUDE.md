# job-hunter

**TL;DR:** Job vacancy monitoring and tracking system. Monorepo coordinating submodules.

> **Stack**: n8n (scraping), Kotlin + Spring Boot (API + Telegram bot), React (UI), PostgreSQL

---

## Portfolio Project

**This is a public portfolio repository.** All code, documentation, commits, and architectural decisions must demonstrate professional-level engineering.

### Quality Standards
- **Clean, readable code** — naming, structure, formatting at production level
- **Meaningful commits** — conventional commits, clear messages, atomic changes
- **README** in every submodule — description, architecture, quick start
- **No junk** — no TODO-hacks, commented-out code, or temporary solutions in master
- **No AI mentions** — commits and code must not reference AI generation
- **No Co-Authored-By** — never add Co-Authored-By, Signed-off-by, or any trailer referencing Claude/AI
- **English only** — all code, comments, commits, README, CLAUDE.md in English

---

## AI Guidelines

### Submodule Awareness
**IMPORTANT:** Read the submodule's `CLAUDE.md` before making changes:
```
n8n/CLAUDE.md        — scraping workflows
api/CLAUDE.md        — Kotlin backend, Telegram bot
ui/CLAUDE.md         — React frontend
```

### Rules
- **Atomic commits** — one commit = one completed unit of work
- **Cross-repo awareness** — changes often span multiple submodules
- **No secrets in code** — secrets via .env (gitignored), Doppler, K8s Secrets
- **Conventional commits** — `feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, `test:`, `ci:`

---

## Structure

```
job-hunter/
  n8n/          # Scraping workflows (submodule)
  api/          # Kotlin Spring Boot + Telegram bot (submodule, coming soon)
  ui/           # React frontend (submodule, coming soon)
```

## Architecture

```
n8n (scraping)  →  REST API  →  Kotlin API  →  Telegram Bot
DOU, Djinni,                        ↓              ↓
Adzuna                          PostgreSQL     Push notifications
                                     ↑
                                  React UI
```

## Working with Submodules

### Clone
```bash
git clone --recurse-submodules git@github.com:mshykhov/job-hunter.git
```

### Update
```bash
git submodule update --remote --merge
```

### Adding a New Submodule

| Step | Action |
|------|--------|
| 1 | Create repo `job-hunter-{name}` on GitHub |
| 2 | `git submodule add git@github.com:mshykhov/job-hunter-{name}.git {name}` |
| 3 | Commit + push monorepo |
| 4 | For deployment: Helm chart in smhomelab/deploy |
