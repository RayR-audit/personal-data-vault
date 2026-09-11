# Roadmap

## P1 Timebox (2026-09-09 ~ 09-15)
Acceptance (7-day): 7 consecutive days of self dogfood data + actually reading the daily insight,
OR >= 1 substantive buyer-probe reply. Neither => stop.

- [x] D1 (done 09-11): repo skeleton, ActivityWatch v0.13.2 installed & running (dogfood started)
- [x] D3-5 (done 09-11, early): aggregate.py v0.1 — ActivityWatch + Dida365 -> SQLite, tested (1,145 tasks + live AW events ingested)
- [x] D6-7 partial: insight.py report prototype tested; buyer probe list NOT started
- Push to GitHub pending: needs repo created on RayR-audit account (no API token for that identity; SSH key auth verified)
- D3-5: aggregator script: ActivityWatch + todo export -> local SQLite (v0)
- D6-7: AI daily insight prototype (self-use) + buyer probe list (10 targets, 2-3 probes sent, receipts required)

## Guardrail
MECIP milestone slip (9/12 draft, 10-05 delivery) => freeze this line.

## Identity hygiene
- git identity fixed at repo level: rayr-audit <farbank@pm.me>
- never use the host's main GitHub credentials for this repo
- if the project gets its own brand later: repo transfer (keeps stars/issues)
