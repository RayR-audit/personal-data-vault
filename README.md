# Personal Data Vault (个人数据金库)

Local-first aggregator for your own digital life data.
把属于你自己的数据（应用使用、任务、聊天记录等）聚合到一个本地 SQLite 金库，一键导出，自用 AI 洞察。

## Why
- Your data, your disk. Local-first: nothing leaves your machine.
- Aggregate sources you already use (ActivityWatch, todo exports, chat archives) into one queryable store.
- One-command export (JSON / CSV) — portability by design.
- Optional AI insight reports generated locally from your own data.

## Status
🚧 v0 in active development (P1 timebox). See [docs/roadmap.md](docs/roadmap.md).

## Roadmap
- [ ] v0.1: ActivityWatch → SQLite aggregator
- [ ] v0.2: todo/task export ingestion
- [ ] v0.3: chat archive ingestion
- [ ] v0.4: one-command export (JSON/CSV)
- [ ] v0.5: local AI daily insight report

## Principles
1. Local-first — no cloud dependency, no telemetry.
2. You own the data — one-command full export, any time.
3. No lock-in — plain SQLite + plain files.

## License
MIT
