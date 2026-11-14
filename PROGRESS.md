# PPL-Tracker — Progress Notes

**Read this first when starting any work on the app. Update it at the END of every work session and commit it with the feature.**

## Ground rules (do not lose these)
- Single-file app: everything lives in `index.html`.
- Publish pipeline: edit `index.html` → `node --check` extracted script → browser selftest → `git add/commit/push` → GitHub Pages (~1–2 min) → `cp index.html 'C:\Users\jamie\iCloudDrive\PPL-Tracker\Workout Tracker.html'` → verify sha256 match.
- Version tag: `App v3.x` shown in homeView — bump it with every release.
- Local test: `python -m http.server 8347` + call `selftest()` in the browser.
- **Update this file before committing the feature** (fill "In progress" into "Shipped", note anything deferred).

## Shipped
- v3.3 — Exercise Library: browse all swappable moves by focus (video + how-to), add to any day; EXLIB single source of truth (50+ moves); swap modal redesigned (same focus first, per-move how-to preview).
- v3.2 — Stats tab: streaks (current/best weeks), total volume & gym time, this-week summary, 8-week volume chart, day-of-week chart (plan days highlighted), per-focus table.
- v3.1 — Structured cardio logging: machine select, time, per-machine metrics.
- v3.0 — Exercise alternatives, how-to guides with verified videos, extra exercises/sets, workout timer, version tag.

## In progress (clear this when shipped)
- *(nothing currently — start a work item here with: what, why, state so far, next step)*

## Deferred / backlog (user-approved "down the line")
- **Username/password login.** App is serverless (per-device localStorage), so real login needs a backend (e.g. Supabase/Firebase free tier). Main benefit: cross-device sync of workout data. Not started.

## Gotchas learned
- iCloud copy path uses single quotes in bash: `cp index.html 'C:/Users/jamie/iCloudDrive/PPL-Tracker/Workout Tracker.html'`.
- Native Windows tools take forward-slash native paths, not MSYS `/c/...` paths.
