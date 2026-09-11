#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Personal Data Vault daily cron: sync + insight, output as report text (for Feishu/local push).'''
import subprocess, sys, datetime, pathlib
ROOT = pathlib.Path(__file__).resolve().parent
# 1) sync (both sources, last 2 days rolling)
r1 = subprocess.run([sys.executable, str(ROOT/"aggregate.py"), "--days", "2"],
                    capture_output=True, text=True, cwd=ROOT, timeout=300)
# 2) insight report (last 1 day)
r2 = subprocess.run([sys.executable, str(ROOT/"insight.py"), "--days", "1"],
                    capture_output=True, text=True, cwd=ROOT, timeout=120)
print(f"# PDV Daily · {datetime.datetime.now():%m-%d %H:%M} (CST)")
print(r2.stdout.strip() or "(empty report)")
if r1.returncode:
    print("[sync stderr]", r1.stderr[-200:])
