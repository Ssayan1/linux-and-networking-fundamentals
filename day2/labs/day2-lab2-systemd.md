## File:
```bash
 sample-sre-demo-advanced.service (Systemd Unit)
```
### Service File Content:
--------------------------------------------------------------------
```bash
[Unit]
Description=Sample SRE Demo Service (safe demo)
After=network.target
StartLimitIntervalSec=60
StartLimitBurst=3

[Service]
Type=simple
ExecStart=/usr/local/bin/sample-sre-demo.sh
Restart=on-failure
RestartSec=5
User=nobody
RuntimeDirectory=sample-sre-demo
StandardOutput=journal
StandardError=journal
LimitNOFILE=4096

[Install]
WantedBy=multi-user.target
```
--------------------------------------------------------------------

### Learning:
- `StartLimitIntervalSec` + `StartLimitBurst` prevent restart loops (common SRE safety guard).
- `Type=simple` is used for long-running processes started directly by ExecStart.
- `ExecStart` points to a separate script (`/usr/local/bin/sample-sre-demo.sh`)—cleaner than inline loops.
- `Restart=on-failure` auto-restarts only on non-zero exit codes (safer than always).
- `RestartSec=5` adds a cooldown to avoid rapid restart storms.
- `User=nobody` drops privileges → recommended for safe, non-root background jobs.
- `RuntimeDirectory` creates `/run/sample-sre-demo/` automatically for PID files or sockets.
- `StandardOutput=journal` logs directly to journald (visible via `journalctl -u service`).
- `LimitNOFILE=4096` raises file descriptor limit—important for servers.
- This unit file reflects **real-world SRE production practices**: safety, logging, reduced privilege, and recoverability.

----------------------------------------------->
# Day 2 — Lab 2:
```bash
 systemd Service Demo
```
## Environment
- WSL Ubuntu (Version X.Y) — run `lsb_release -a`
- Date: 2025-11-29
- User: sayan (ran commands with sudo)

## Files created
- /etc/systemd/system/sample-sre-demo.service
- /usr/local/bin/sample-sre-demo.sh

## Unit file (production-style)

## Service script

## Commands executed
sudo systemctl daemon-reload
sudo systemctl enable sample-sre-demo
sudo systemctl start sample-sre-demo
sudo systemctl status sample-sre-demo --no-pager
sudo journalctl -u sample-sre-demo -n 50 --no-pager

## Output (paste real output)

## Observations & Learnings
- Explanation why we used `Restart=on-failure` vs `always`
- Why non-root user matters
- How `StartLimitBurst` prevents crash loops
- How to debug (journalctl, systemctl status, `ps`/`strace`)

## Next steps (what I'd do in production)
- Create a dedicated non-privileged user/group (e.g., `svc-demo`) and drop capabilities
- Add `ExecStartPre` for checks, `ExecStop` for graceful shutdown
- Add `WatchdogSec` and `NotifyAccess=all` for services that can signal liveness

## Troubleshooting Commands for systemd Service

### 1. Check service status (detailed output)
--------------------------------------------------------------------
sudo systemctl status sample-sre-demo -l
--------------------------------------------------------------------

### Learning:
- Shows service status, errors, exit codes, and recent logs.
- `-l` prints full lines (no truncation).
- First command to run when a service fails to start.


### 2. View logs from the current boot (last 200 lines)
--------------------------------------------------------------------
sudo journalctl -u sample-sre-demo -b --no-pager | tail -n 200
--------------------------------------------------------------------

### Learning:
- Fetches logs only for the current boot (`-b`).
- `--no-pager` prevents interactive scrolling.
- `tail -n 200` shows the most recent logs for fast debugging.
- Useful for detecting startup crashes, permission issues, missing files, etc.


### 3. Manually run the script as the service user
--------------------------------------------------------------------
sudo -u nobody /usr/local/bin/sample-sre-demo.sh
--------------------------------------------------------------------

### Learning:
- Runs the same script systemd uses, but outside of systemd.
- Helps identify permission issues, missing environment variables, or script syntax errors.
- If it fails here, the problem is in the script — not systemd.
- SRE best practice: **Always test service scripts manually as their target user.**

