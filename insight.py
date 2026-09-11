#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
personal-data-vault :: daily insight (self-use prototype)
Reads data/vault.db, prints a plain insight report. (AI-narrated version comes later.)

Usage: python insight.py [--days 1]
"""
import argparse
import sqlite3
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DB = ROOT / "data" / "vault.db"
OUT = ROOT / "out"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=1)
    args = ap.parse_args()
    if not DB.exists():
        print("vault.db not found — run aggregate.py first")
        return
    conn = sqlite3.connect(DB)
    since = (datetime.now(timezone.utc) - timedelta(days=args.days)).strftime("%Y-%m-%dT%H:%M")

    print(f"# Data Vault Insight · last {args.days}d · generated {datetime.now():%Y-%m-%d %H:%M}\n")

    # screen time by app
    rows = conn.execute(
        "SELECT app, SUM(duration_s)/3600.0 h, COUNT(*) n FROM app_events "
        "WHERE ts >= ? GROUP BY app ORDER BY 2 DESC LIMIT 15", (since,)).fetchall()
    total_h = sum(r[1] for r in rows)
    print(f"## Screen time (tracked): {total_h:.1f}h\n")
    for app, h, n in rows:
        bar = "#" * max(1, int(h * 4))
        print(f"- {app:<30} {h:5.2f}h {bar}")

    # task throughput
    done = conn.execute(
        "SELECT project, COUNT(*) FROM tasks WHERE status='completed' AND completed_at >= ? "
        "GROUP BY project ORDER BY 2 DESC", (since,)).fetchall()
    print(f"\n## Tasks completed: {sum(r[1] for r in done)}\n")
    for p, n in done:
        print(f"- {p}: {n}")

    open_cnt = conn.execute("SELECT COUNT(*) FROM tasks WHERE status='open'").fetchone()[0]
    print(f"\n## Open tasks total: {open_cnt}")

    # focus ratio (active vs total tracked)
    act = conn.execute(
        "SELECT SUM(duration_s) FROM app_events WHERE app='(active)' AND ts >= ?", (since,)).fetchone()[0] or 0
    if total_h > 0:
        print(f"\n## Active (not-afk) ratio: {act/3600:.1f}h / {total_h:.1f}h = {act/3600/total_h*100:.0f}%")

    conn.close()


if __name__ == "__main__":
    main()
