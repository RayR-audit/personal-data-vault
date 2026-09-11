#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Personal Data Vault daily cron: sync + insight, output as report text."""
import subprocess, sys, datetime
ROOT = r"D:/HermesData/projects/personal-data-vault"
r1 = subprocess.run([sys.executable, ROOT + r"\aggregate.py", "--days", "2"],
                    capture_output=True, text=True, cwd=ROOT, timeout=300)
r2 = subprocess.run([sys.executable, ROOT + r"\insight.py", "--days", "1"],
                    capture_output=True, text=True, cwd=ROOT, timeout=120)
print(f"# PDV Daily · {datetime.datetime.now():%m-%d %H:%M} (CST)")
print(r2.stdout.strip() or "(empty report)")
if r1.returncode:
    print("[sync stderr]", r1.stderr[-200:])
# dogfood 打卡（本地日志留痕）
import pathlib, datetime as _dt
log = pathlib.Path(ROOT) / "data" / "dogfood_log.txt"
with open(log, "a", encoding="utf-8") as f:
    f.write(f"{_dt.datetime.now():%Y-%m-%d %H:%M} | sync={r1.returncode==0} | insight_len={len(r2.stdout)}\n")
