# PPL-Tracker — Progress Notes

**Read this first when starting any work on the app. Update it at the END of every work session and commit it with the feature.**

## Ground rules (do not lose these)
- Single-file app: all APP code lives in `index.html`. Since v3.5 it is a **PWA**, so the repo also carries a small PWA shell: `manifest.json`, `sw.js`, `icons/{icon-192,icon-512,apple-touch-icon}.png`. The app itself never moves out of `index.html`.
- Publish pipeline: edit `index.html` → `node --check` extracted script **and** `node --check sw.js` → browser selftest (now reports `pwa:"ok"`) → `git add/commit/push` → GitHub Pages (~1–2 min) → sync to iCloud (see below) → verify sha256 match on the main file.
- iCloud sync (all 4 PWA pieces so the local copy also installs with icons):
  - `cp index.html 'C:\Users\jamie\iCloudDrive\PPL-Tracker\Workout Tracker.html'`
  - `cp manifest.json sw.js 'C:\Users\jamie\iCloudDrive\PPL-Tracker\'` and copy the `icons/` folder there too.
  - Note: the iCloud copy opens via `file://`, so the service worker (offline) is **skipped there by design**; the full offline+install PWA lives on the **GitHub Pages** URL (`https://jamienorwood1989-afk.github.io/ppl-tracker/`).
- Version tag: `App v3.x` shown in homeView — bump it with every release.
- Local test: `python -m http.server 8347` + call `selftest()` in the browser (localhost is treated as https, so the SW does register and you can confirm offline caching).
- **Update this file before committing the feature** (fill "In progress" into "Shipped", note anything deferred).

## Shipped
- v3.5.1 — Bugfix: History session cards were broken (user: "history tab only shows personal records and top lifts"). In `histListView`, `h += '<div…>' + top ? (A) : (B)` — `+` binds tighter than `? :`, so for any session with weighted lifts the whole card HTML (wrapper, date, onclick, volume, closing tags) was dropped and only dangling `top lift Xkg · ` text rendered. Fixed by parenthesizing both ternaries (only occurrence of the `+cond?` pattern in file, confirmed by grep). Selftest now renders `histListView()` + `histDetailView()` and asserts a tappable `openHist()` card, `kg volume`, and `exportSessionPdf(` button exist — this bug class can't ship silently again. Version tag `App v3.5.1`; SW cache `ppl-v3.5.1` (installed PWAs fetch the fix on next open). Verified end-to-end in browser: card → tap → full detail → Export to PDF → 2 KB PDF.
- v3.5 — PWA: installable app + offline. Added `manifest.json` (standalone, theme `#0b0f14`), `sw.js` (app-shell cache, versioned `ppl-v3.5.1`), generated icons (barbell + "PPL", matched to app palette), `theme-color`/`apple-*` meta, manifest + apple-touch-icon links, and a guarded `serviceWorker.register('sw.js')` (only on https/localhost, silently skipped on `file://`). Selftest gained `pwa:"ok"`. Verified in browser: SW **activated**, all 5 shell entries cached, **offline reload renders the full app**.
- v3.4 — PDF export: self-contained writer (zero deps). "⬇ Export program to PDF" (plan tab) and "⬇ Export to PDF" per past session. Multi-page A4, Helvetica/WinAnsi, real xref table; in-app `pdfValidate` selftest (validator off-by-one found via selftest, fixed). Verified: node xref/stream-length checks + text decode (71 text ops, 2 pages, all exercises present).
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
