# job-hunter

**TL;DR:** Система мониторинга и трекинга вакансий. Монорепо координирует субмодули.

> **Стек**: n8n (scraping), Kotlin + Spring Boot (API + Telegram bot), React (UI), PostgreSQL

---

## Руководство для AI

### Работа с субмодулями
**ВАЖНО:** Перед изменением субмодуля — прочитай его `CLAUDE.md`:
```
n8n/CLAUDE.md        — n8n workflows, скрапинг
api/CLAUDE.md        — Kotlin backend, Telegram bot
ui/CLAUDE.md         — React frontend
```

### Глобальные правила
- **Atomic commits**: Один коммит = одна законченная единица работы
- **Cross-repo awareness**: Изменения часто затрагивают несколько субмодулей
- **No secrets in code**: Секреты через .env (gitignored), Doppler, K8s Secrets
- **Язык**: Документация — русский, код/комментарии/коммиты — английский

---

## Структура

```
job-hunter/
  n8n/          # Scraping workflows (субмодуль)
  api/          # Kotlin Spring Boot + Telegram bot (субмодуль, позже)
  ui/           # React frontend (субмодуль, позже)
```

## Архитектура

```
n8n (scraping)  →  POST /api/jobs/ingest  →  Kotlin API  →  Telegram Bot
DOU, Djinni,                                     ↓              ↓
Indeed                                       PostgreSQL     Push уведомления
                                                 ↑
                                              React UI
```

## Работа с субмодулями

### Клонирование
```bash
git clone --recurse-submodules git@github.com:mshykhov/job-hunter.git
```

### Обновление
```bash
git submodule update --remote --merge
```

### Изменение субмодуля
```bash
cd n8n
git add . && git commit -m "feat: description"
git push origin master

cd ..
git add n8n
git commit -m "chore: update submodule n8n"
git push
```

## Добавление нового субмодуля

| Шаг | Действие |
|-----|----------|
| 1 | Создать репо `job-hunter-{name}` на GitHub |
| 2 | `git submodule add git@github.com:mshykhov/job-hunter-{name}.git {name}` |
| 3 | Commit + push монорепо |
| 4 | Для деплоя: Helm chart в smhomelab/deploy |

## Git соглашения

```
{type}: {описание}

Типы: feat, fix, docs, chore, refactor, test, ci
```
