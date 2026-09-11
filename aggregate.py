#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
personal-data-vault :: aggregator
Pull local data sources into one local SQLite vault. Nothing leaves the machine.

Sources (v0.1):
  - ActivityWatch (window + afk events) via local REST API :5600
  - Dida365 (TickTick) completed tasks via open API (optional; needs DIDA365_MCP_TOKEN)

Usage:
  python aggregate.py                 # sync all sources, last 7 days
  python aggregate.py --days 30      # custom lookback
  python aggregate.py --source aw    # single source
  python aggregate.py --export json  # export vault to out/vault_export.json

DB default: ./data/vault.db  (gitignored)
"""
import argparse
import json
import os
import sqlite3
import subprocess
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "data" / "vault.db"
AW_API = "http://localhost:5600"

SCHEMA = """
CREATE TABLE IF NOT EXISTS app_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT NOT NULL,             -- 'activitywatch'
    bucket TEXT NOT NULL,
    ts TEXT NOT NULL,                 -- ISO8601 UTC
    duration_s REAL NOT NULL DEFAULT 0,
    app TEXT,
    title TEXT,
    UNIQUE(source, bucket, ts)
);
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT NOT NULL,             -- 'dida365'
    external_id TEXT NOT NULL,
    title TEXT,
    project TEXT,
    status TEXT,
    completed_at TEXT,
    UNIQUE(source, external_id)
);
CREATE TABLE IF NOT EXISTS sync_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts TEXT NOT NULL,
    source TEXT NOT NULL,
    events_written INTEGER NOT NULL,
    detail TEXT
);
CREATE INDEX IF NOT EXISTS idx_app_events_ts ON app_events(ts);
CREATE INDEX IF NOT EXISTS idx_app_events_app ON app_events(app);
"""


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f+00:00")


def get_db() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.executescript(SCHEMA)
    return conn


def http_json(url: str, timeout: int = 15):
    with urllib.request.urlopen(url, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


# ---------------- ActivityWatch ----------------

def sync_activitywatch(conn: sqlite3.Connection, days: int) -> int:
    buckets = http_json(f"{AW_API}/api/0/buckets/")
    start = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%dT%H:%M:%S")
    total = 0
    for name, b in buckets.items():
        if b["type"] not in ("currentwindow", "afkstatus"):
            continue
        url = f"{AW_API}/api/0/buckets/{name}/events?start={start}&limit=-1"
        try:
            events = http_json(url)
        except Exception as e:
            print(f"[aw] bucket {name} fetch failed: {e}", file=sys.stderr)
            continue
        rows = []
        for ev in events:
            data = ev.get("data") or {}
            if b["type"] == "currentwindow":
                rows.append(("activitywatch", name, ev["timestamp"],
                             ev.get("duration", 0) or 0,
                             data.get("app"), data.get("title")))
            else:  # afk events: keep not-afk time as app='(active)', title=None
                status = data.get("status")
                if status == "not-afk":
                    rows.append(("activitywatch", name, ev["timestamp"],
                                 ev.get("duration", 0) or 0, "(active)", None))
        conn.executemany(
            "INSERT OR IGNORE INTO app_events(source,bucket,ts,duration_s,app,title) "
            "VALUES(?,?,?,?,?,?)", rows)
        total += len(rows)
        print(f"[aw] {name}: {len(rows)} events")
    return total


# ---------------- Dida365 (optional) ----------------

def _dida_token() -> str:
    env_file = Path(os.path.expandvars(r"%LOCALAPPDATA%\hermes\.env"))
    tok = os.environ.get("DIDA365_MCP_TOKEN", "")
    if not tok and env_file.exists():
        for line in env_file.read_text(encoding="utf-8", errors="ignore").splitlines():
            if line.startswith("DIDA365_MCP_TOKEN="):
                tok = line.split("=", 1)[1].strip()
                break
    return tok


def _dida_curl(url: str, tok: str) -> str:
    if not tok.startswith("Bearer"):
        tok = "Bearer " + tok
    args = ["curl.exe", "-s", "-m", "30",
            "--resolve", "open.dida365.com:443:54.223.186.2",
            url, "-H", "Authorization: " + tok]
    r = subprocess.run(args, capture_output=True, text=True, timeout=40)
    return r.stdout


def sync_dida(conn: sqlite3.Connection, days: int) -> int:
    """Dida365 open API: no completed-only endpoint; /project/{id}/data returns all
    tasks (open + completed-in-window). status: 0=normal, 2=completed(-1=abandoned)."""
    tok = _dida_token()
    if not tok:
        print("[dida] no token, skip")
        return 0
    raw = _dida_curl("https://open.dida365.com/open/v1/project", tok)
    try:
        projects = json.loads(raw)
    except Exception:
        print(f"[dida] project list failed: {raw[:120]}", file=sys.stderr)
        return 0
    since_dt = datetime.now(timezone.utc) - timedelta(days=days)
    total = 0
    for p in projects:
        if p.get("kind") == "NOTE":
            continue
        raw = _dida_curl(
            f"https://open.dida365.com/open/v1/project/{p['id']}/data", tok)
        try:
            payload = json.loads(raw)
        except Exception:
            continue
        rows = []
        for t in payload.get("tasks", []) or []:
            comp = t.get("completedTime")
            status = {0: "open", 2: "completed", -1: "abandoned"}.get(
                t.get("status", 0), str(t.get("status")))
            # keep task if open, or completed within the lookback window
            keep = status == "open"
            if comp:
                try:
                    keep = keep or (datetime.strptime(comp[:19], "%Y-%m-%dT%H:%M:%S")
                                    .replace(tzinfo=timezone.utc) >= since_dt)
                except ValueError:
                    keep = True
            if keep:
                rows.append(("dida365", t.get("id"), t.get("title"),
                             p.get("name"), status, comp))
        if rows:
            conn.executemany(
                "INSERT OR IGNORE INTO tasks(source,external_id,title,project,status,completed_at) "
                "VALUES(?,?,?,?,?,?)", rows)
        total += len(rows)
        print(f"[dida] project {p.get('name')}: {len(rows)} tasks")
    return total


# ---------------- Export ----------------

def export_json() -> Path:
    out_dir = ROOT / "out"
    out_dir.mkdir(exist_ok=True)
    conn = get_db()
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out = out_dir / f"vault_export_{stamp}.json"
    data = {
        "exported_at": now_iso(),
        "app_events": [dict(zip([c[0] for c in cur.description], row))
                       for cur in [conn.execute("SELECT * FROM app_events")] for row in cur.fetchall()],
        "tasks": [dict(zip([c[0] for c in cur.description], row))
                  for cur in [conn.execute("SELECT * FROM tasks")] for row in cur.fetchall()],
    }
    out.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"export -> {out}")
    return out


# ---------------- Main ----------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--source", choices=["aw", "dida", "all"], default="all")
    ap.add_argument("--export", choices=["json"], default=None)
    args = ap.parse_args()

    conn = get_db()
    results = {}
    if args.source in ("aw", "all"):
        try:
            results["activitywatch"] = sync_activitywatch(conn, args.days)
        except Exception as e:
            print(f"[aw] sync failed: {e}", file=sys.stderr)
            results["activitywatch"] = 0
    if args.source in ("dida", "all"):
        try:
            results["dida365"] = sync_dida(conn, args.days)
        except Exception as e:
            print(f"[dida] sync failed: {e}", file=sys.stderr)
            results["dida365"] = 0

    conn.executemany("INSERT INTO sync_log(ts,source,events_written,detail) VALUES(?,?,?,?)",
                     [(now_iso(), k, v, "") for k, v in results.items()])
    conn.commit()
    print("sync summary:", results)

    if args.export:
        export_json()
    conn.close()


if __name__ == "__main__":
    main()
