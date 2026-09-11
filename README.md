# Personal Data Vault (个人数据金库)

> Your data, your vault. — 把数据的主权还给个人。

**Personal Data Vault** is a local-first, open-source tool that returns data ownership to individuals:
it aggregates the digital traces you already generate every day — screen time, tasks, chat archives —
into **one private SQLite vault on your own disk**. You own it, query it, and export it on your own terms.

**Personal Data Vault** 是一个把数据所有权还给个人的本地优先开源工具：
它把你每天都在产生、却被散落在各个 SaaS 里的数字痕迹——屏幕时间、任务、聊天记录——
聚合进**一块属于你自己的本地 SQLite 金库**。聚合、自托管、变现，方式由你决定。

## Why

Every click you make feeds someone else's model. Your activity data sits in dozens of silos —
productivity apps, trackers, platforms — where you can see fragments of it but never truly hold it.

Personal Data Vault flips that:

- **Your data, your disk.** Local-first: nothing leaves your machine. No cloud, no telemetry, no account.
- **One vault, many sources.** Aggregate ActivityWatch, todo/task exports, chat archives and more into a single queryable store.
- **One-command export.** JSON / CSV anytime — portability by design, no lock-in.
- **Own AI insights.** Optional daily insight reports generated locally from your own data.

## Status

🚧 **v0.1 working** — aggregator (ActivityWatch + task source → SQLite) and daily insight prototype are implemented and running daily.

## Quick Start

```bash
# sync all sources into the local vault (default: last 7 days)
python aggregate.py

# generate an insight report
python insight.py

# export everything to JSON
python aggregate.py --export json
```

## Roadmap

- [x] v0.1: ActivityWatch + task ingestion → SQLite
- [ ] v0.2: chat archive ingestion
- [ ] v0.3: one-command full export (JSON / CSV)
- [ ] v0.4: local AI daily insight report (narrated)
- [ ] v0.5: optional "data on your terms" — share only what you choose, only when you choose

## Principles

1. **Local-first** — no cloud dependency, no telemetry, no sign-up.
2. **You own the data** — one-command full export, any time, no questions asked.
3. **No lock-in** — plain SQLite + plain files. Delete the folder, everything is gone.
4. **Consent over extraction** — sharing (if ever) is opt-in, per-source, revocable. The default is private forever.

## License

MIT
