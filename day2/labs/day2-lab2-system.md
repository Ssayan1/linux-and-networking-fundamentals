## File:
```bash
 sample-sre-demo.service (Systemd Unit)
```
### Service File Content:
--------------------------------------------------------------------
```bash
[Unit]
Description=Sample SRE Demo Service
After=network.target

[Service]
ExecStart=/bin/bash -c "while true; do echo 'Service running'; sleep 5; done"
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```
--------------------------------------------------------------------

### Learning:
- Systemd unit files are used to run services in the background (daemons).
- `ExecStart` defines the command that systemd will run—here, an infinite loop printing "Service running".
- `Restart=always` ensures the service auto-recovers if it crashes (important for reliability).
- `After=network.target` ensures the service starts only after the system has networking available.
- `WantedBy=multi-user.target` makes this service start automatically at boot.
- SREs use systemd to manage processes, ensure stability, auto-restart services, and improve system reliability.

----------------------------------------------->
## Command: 
```bash
sudo cp day2/systemd/sample-service.service /etc/systemd/system/
```
Output:
--------------------------------------------------------------------
(No output — `cp` runs silently unless there is an error)
--------------------------------------------------------------------

## Learning:
- This command copies your custom systemd unit file into `/etc/systemd/system/`, which is where user-defined services are stored on Linux.
- `sudo` is required because `/etc/systemd/system/` is a protected system directory.
- After copying a service file, you **must reload systemd** so it recognizes the new unit.
- This is the standard workflow SREs use when installing or updating system service definitions.

----------------------------------------------->
## Commands:
```bash
sudo systemctl daemon-reload
sudo systemctl enable sample-service
sudo systemctl start sample-service
```
Output:
--------------------------------------------------------------------
(No output — these systemctl commands run silently unless there is an error)
--------------------------------------------------------------------

## Learning:
- `systemctl daemon-reload` refreshes systemd so it recognizes new or updated service files.
- `systemctl enable sample-service` enables the service to start automatically at system boot.
- `systemctl start sample-service` starts the service immediately without needing a reboot.
- These three steps are required **every time** you add, modify, or install a systemd service.
- This workflow is essential for SREs when deploying automation, background services, or agents.
----------------------------------------------->

## Command:
```bash
 systemctl status sample-service
```
Output:
--------------------------------------------------------------------
```bah
● sample-service.service - Sample SRE Demo Service
     Loaded: loaded (/etc/systemd/system/sample-service.service; enabled)
     Active: active (running) since Sat 2025-11-29
   Main PID: 6266 (bash)
      Tasks: 2 (limit: 4535)
     Memory: 720.0K (peak: 1.0M)
        CPU: 9ms
     CGroup: /system.slice/sample-service.service
             ├─6266 /bin/bash -c "while true; do echo 'Service running'; sleep 5; done"
             └─6269 sleep 5

Nov 29 04:43:57 sayan systemd[1]: Started Sample SRE Demo Service.
Nov 29 04:43:57 sayan bash[6266]: Service running
Nov 29 04:44:02 sayan bash[6266]: Service running
Nov 29 04:44:07 sayan bash[6266]: Service running
```
--------------------------------------------------------------------

## Learning:
- The service is **active (running)**, meaning systemd successfully started it.
- `Loaded: loaded` confirms the service file is correctly installed under `/etc/systemd/system/`.
- `Main PID: 6266` shows the actual process started by systemd.
- `CGroup` details show the bash loop continuously printing “Service running”.
- Repeated log lines confirm the service executes the loop every 5 seconds.
- This verifies that your systemd service works reliably and restarts on boot as expected—core SRE knowledge.



## Command:
```bash
 journalctl -u sample-service -f
```
Output:
--------------------------------------------------------------------
```bash
Nov 29 04:52:39 sayan bash[6266]: Service running
Nov 29 04:52:44 sayan bash[6266]: Service running
Nov 29 04:52:49 sayan bash[6266]: Service running
Nov 29 04:52:54 sayan bash[6266]: Service running
Nov 29 04:52:59 sayan bash[6266]: Service running
Nov 29 04:53:05 sayan bash[6266]: Service running
Nov 29 04:53:10 sayan bash[6266]: Service running
Nov 29 04:53:15 sayan bash[6266]: Service running
Nov 29 04:53:20 sayan bash[6266]: Service running
Nov 29 04:53:25 sayan bash[6266]: Service running
```
--------------------------------------------------------------------

## Learning:
- `journalctl -u <service> -f` shows **real-time logs** for a systemd-managed service.
- The repeating "Service running" lines confirm that the loop inside your systemd service executes every 5 seconds.
- This command is equivalent to `tail -f` but for systemd’s centralized logging system.
- SREs use real-time journal logs during debugging, incident response, and service verification.
- Continuous logging confirms the service is healthy, active, and not crashing.

