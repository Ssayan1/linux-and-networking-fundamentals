## Command:
```bash
 htop
```
Output:
--------------------------------------------------------------------
Uptime output:
 05:21:34 up 10:05,  1 user,  load average: 0.00, 0.00, 0.00

Interpretation:
- Load averages 1/5/15 min all zero => idle system.
- MiB Mem shows 3133MB free, 539MB used, so memory pressure is low.

--------------------------------------------------------------------

## Learning:
- `htop` is an advanced, interactive process viewer used to monitor CPU, memory, processes, and load.
- It shows real-time information with color bars and an easy-to-read interface.
- Allows sorting processes by CPU, memory, PID, user, etc.
- Provides details like threads, process tree, and system load averages.
- SREs use `htop` for live performance analysis and troubleshooting high CPU/memory issues.

### Understanding Load Average (Simple Explanation)
- Load average shows how many processes are either **running** or **waiting for CPU**.
- It is displayed as three numbers: **1-minute, 5-minute, 15-minute** averages.
- For a 4-core system:
  - Load 4.00 = fully busy  
  - Load < 4.00 = healthy  
  - Load > 4.00 = CPU saturation  
- Example: `0.00, 0.00, 0.00` means the system is idle with no CPU pressure.

### Understanding Memory Numbers (free -m)
- **total**: total physical RAM available to the system.
- **used**: memory actively used by applications and the kernel.
- **free**: RAM not used at all (this number is usually small in Linux).
- **buff/cache**: memory Linux uses to cache files and accelerate I/O (this is good).
- **available**: the *real* amount of memory that applications can still use safely.
- **swap**: disk-based memory used when RAM is full — if swap usage grows, the system is under memory pressure.

### Quick SRE Interpretation
- High **load average** + high **CPU usage** = CPU bottleneck.
- Low **available memory** + non-zero **swap used** = memory pressure.
- High **buff/cache** is normal — Linux caches aggressively.
- `available` is the key metric: if it's large, your system is healthy.

----------------------------------------------------->
## Command:
```bash
 iostat -xz 1
```
Output:
--------------------------------------------------------------------
Linux 6.6.87.2-microsoft-standard-WSL2 (sayan) 11/29/25  _x86_64_  (4 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.18    0.00    0.43    0.04    0.00   99.34

Device            r/s     rkB/s   rrqm/s  %rrqm r_await rareq-sz     w/s     wkB/s   wrqm/s  %wrqm w_await wareq-sz     d/s     dkB/s   drqm/s  %drqm d_await dareq-sz     f/s f_await  aqu-sz  %util
sda              0.07      4.01     0.01  15.53    0.51    60.90    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
sdb              0.01      0.41     0.00  28.51    0.60    41.29    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   9.49
sdc              0.00      0.09     0.00   0.00    0.08    22.44    0.00      0.00     0.00   0.00    2.00     2.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    2.00    0.00   0.00
sdd              2.78     97.74     1.05  27.40    0.88    35.11    1.20     35.58     0.95   44.19   13.27    29.68    0.04     30.22     0.00   3.78    0.37   688.86    0.23    3.78    0.02   0.58

(Note: iostat continues printing new samples every 1 second...)
--------------------------------------------------------------------

## Learning:
- `iostat -xz 1` provides **extended disk statistics** updated every 1 second.
- `avg-cpu` section shows system-level CPU usage including I/O wait (`%iowait`).
- `r/s`, `w/s` = read/write operations per second.
- `rkB/s`, `wkB/s` = read/write throughput (KB per second).
- `%util` shows how busy each disk is; near **100% means bottleneck**.
- `await` = average request latency in milliseconds (important metric).
- `aqu-sz` = average queue size; higher values indicate I/O backlog.
- Device `sdd` is the busiest disk in your system — shows highest throughput and activity.
- Low `%util` and low `await` mean **no disk bottleneck** on your system during measurement.

## Practical SRE Use:
- Diagnose slow application performance due to disk I/O.
- Detect high latency (`await`) or queue build-up (`aqu-sz`).
- Identify which disk is a bottleneck using `%util`.
- Evaluate usage patterns during incidents or load testing.
- Understand read/write characteristics for capacity planning.

----------------------------------------------------->

## Command:
```bash
 vmstat 1 5
```
Output:
--------------------------------------------------------------------
procs -----------memory---------- ---swap-- -----io---- -system-- -------cpu-------
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st gu
 1  0      0 3253812   1152 155796    0    0   101    37  215    0  0  0 99  0  0  0
 0  0      0 3253812   1160 155796    0    0     0    20  108   98  0  0 99  0  0  0
 0  0      0 3253812   1160 155864    0    0     0     0   60   59  0  0 100  0  0  0
 0  0      0 3253448   1160 155864    0    0     0     0   86   85  0  0 100  0  0  0
 0  0      0 3253448   1160 155864    0    0     0     0   55   50  0  0 100  0  0  0
--------------------------------------------------------------------

## Learning:
- `vmstat` provides real-time insight into CPU, memory, processes, I/O, and system interrupts.
- `r` = number of runnable (ready) processes. A value near 0 means low CPU load.
- `b` = processes blocked on I/O. Always 0 → no I/O wait congestion.
- `free`, `buff`, `cache` show memory distribution; free memory is very high here → system is under light load.
- `si`/`so` = swap in/out; both 0 → no swapping (good).
- `bi`/`bo` = blocks read/written. Very small numbers → low disk I/O usage.
- `in` (interrupts) and `cs` (context switches) remain low → system is idle.
- CPU columns: `us`, `sy`, `id`, `wa` → CPU is 99–100% idle across all samples.

## SRE Interpretation:
- The system is **almost completely idle**.
- No CPU pressure (`r` stays 0–1, `id` 99–100%).
- No I/O bottleneck (`wa` = 0, `b` = 0).
- No memory pressure (free memory > 3 GB, swap unused).
- No I/O spikes (bi/bo very low).

This is an example of a **healthy, low-load system**.

----------------------------------------------------->


## Command:
```bash
 uptime
```
Output:
--------------------------------------------------------------------
05:21:34 up 10:05,  1 user,  load average: 0.00, 0.00, 0.00
--------------------------------------------------------------------

## Learning:
- System has been running for **10 hours and 5 minutes**.
- Only **1 user** is logged in.
- Load average is **0.00 / 0.00 / 0.00** → system is completely idle with no CPU pressure.
- Load average indicates the runnable process queue over **1, 5, and 15 minutes**.
- For a 4-core system, load average below **4.0** means CPU is not saturated.
----------------------------------------------------->

## Command:
```bash
 top
```
Output:
--------------------------------------------------------------------
top - 05:23:17 up 10:06,  1 user,  load average: 0.00, 0.00, 0.00
Tasks:  57 total,   1 running,  56 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.0 us,  0.1 sy,  0.0 ni, 99.8 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :   3789.2 total,   3137.6 free,    540.2 used,    111.4 buff/cache
MiB Swap:   1024.0 total,   1024.0 free,      0.0 used.   

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
    426 pcp       20   0   15556   9216   8192 S   0.0  0.2   0:00.00 pcp
      1 root      20   0   22412  13044   9332 S   0.0  0.3   0:01.23 systemd
      2 root      20   0    3072   1920   1792 S   0.0  0.0   0:00.00 kthreadd
      7 root      20   0    3072   1792   1792 S   0.0  0.0   0:00.00 kworker
     43 root      19  -1   50424  17152  16256 S   0.0  0.4   0:00.00 systemd-journal
     88 root      20   0   25464   6656   4992 S   0.0  0.1   0:00.00 systemd-udevd
    103 root      20   0  152936   1540   1408 S   0.0  0.0   0:00.00 snapd
    104 root      20   0  152936   1284   1152 S   0.0  0.0   0:00.00 snapd
    105 root      20   0  227832   1540   1408 S   0.0  0.0   0:00.00 snapd
    108 root      20   0  228360   1796   1152 S   0.0  0.0   0:00.00 snapd
    121 root      20   0  227832   1540   1408 S   0.0  0.0   0:00.00 snapd
    167 systemd+  20   0   21456  12800  10624 S   0.0  0.3   0:00.00 systemd-timesync
    175 systemd+  20   0   91024   7680   6784 S   0.0  0.2   0:00.00 systemd-networkd
    191 root      20   0    4236   2560   2432 S   0.0  0.0   0:00.00 bash
    192 message+  20   0    9600   4864   4352 S   0.0  0.1   0:00.00 dbus-daemon
    196 root      20   0  269492  39416  12928 S   0.0  1.0   0:00.00 systemd-logind
    219 root      20   0 1923376  37760  24192 S   0.0  1.0   0:00.00 dockerd
    222 root      20   0   17964   8320   7424 S   0.0  0.2   0:00.00 cron
    248 root      20   0    3160   2048   1920 S   0.0  0.0   0:00.00 sh
    250 root      20   0   11156   1716    768 S   0.0  0.0   0:00.00 test
    256 www-data  20   0   12880   4276   3072 S   0.0  0.1   0:00.00 apache2
    257 www-data  20   0   12880   4276   3072 S   0.0  0.1   0:00.00 apache2
    258 www-data  20   0   12880   4276   3072 S   0.0  0.1   0:00.00 apache2
--------------------------------------------------------------------

## Learning:
- System load is **0.00**, meaning no CPU pressure.
- CPU is **99.8% idle**, extremely low system usage.
- Memory usage is light: **3137 MB free**, **540 MB used**.
- Swap is completely unused (1024 MB free).
- Most processes are sleeping (`S` state), only 1 running — typical for an idle system.
- Useful for identifying high CPU processes, runaway memory usage, and real-time performance debugging.
- SREs use `top` heavily during incidents to find offenders quickly.
----------------------------------------------------->

## Command:
```bash
 df -h
```
Output:
--------------------------------------------------------------------
Filesystem      Size  Used Avail Use% Mounted on
none            1.9G     0  1.9G   0% /usr/lib/modules/6.6.87.2-microsoft-standard-WSL2
none            1.9G  4.0K  1.9G   1% /mnt/wsl
drivers         148G  137G   12G  93% /usr/lib/wsl/drivers
/dev/sdd       1007G  5.9G  950G   1% /
none            1.9G  120K  1.9G   1% /mnt/wslg
none            1.9G     0  1.9G   0% /usr/lib/wsl/lib
rootfs          1.9G  2.7M  1.9G   1% /init
none            1.9G  840K  1.9G   1% /run
none            1.9G     0  1.9G   0% /run/lock
none            1.9G     0  1.9G   0% /run/shm
none            1.9G   76K  1.9G   1% /mnt/wslg/versions.txt
none            1.9G   76K  1.9G   1% /mnt/wslg/doc
C:\             148G  137G   12G  93% /mnt/c
D:\             329G  100G  229G  31% /mnt/d
snapfuse        331M  331M     0 100% /snap/code/215
snapfuse         64M   64M     0 100% /snap/core20/2682
snapfuse        331M  331M     0 100% /snap/code/214
snapfuse         67M   67M     0 100% /snap/core24/1225
snapfuse         51M   51M     0 100% /snap/snapd/25577
tmpfs           379M   20K  379M   1% /run/user/1000
--------------------------------------------------------------------

## Learning:
- `df -h` displays **filesystem usage** in human-readable format.
- `/dev/sdd` is your main Linux filesystem inside WSL → very healthy at **1% usage**.
- `/mnt/c` shows your Windows C: drive — **93% full**, close to the danger zone.
- Snap mounts (`snapfuse`) show as **100% full** — this is normal and safe for Snap packages.
- `tmpfs` and `none` entries are temporary filesystem mounts created by WSL.
- SREs check disk usage regularly because **full disks (100%) cause service crashes**, logging failures, and database corruption.

----------------------------------------------------->

## Command:
```bash
 free -m
```
Output:
--------------------------------------------------------------------
```bash
               total        used        free      shared  buff/cache   available
Mem:            3789         535        3137           4         198        3253
Swap:           1024           0        1024
```
--------------------------------------------------------------------

## Learning:
- Shows system memory usage in **megabytes (MB)**.
- `total = 3789 MB` → Your WSL VM has ~3.8 GB RAM allocated.
- `used = 535 MB` → Very low usage; system is idle.
- `free = 3137 MB` → Large amount of unused RAM.
- `buff/cache = 198 MB` → Memory used by kernel buffers + file cache to speed up I/O.
- `available = 3253 MB` → The **true amount of memory available** for new applications.
- `Swap = 0 used` → No swapping at all → system is not under memory pressure.

### SRE Interpretation:
- No memory issues.
- No swap usage → excellent for performance.
- Plenty of available RAM → no risk of out-of-memory (OOM) kill.

--------------------------------------------------------------------
## Commands: Install and Run Sample SRE Demo Service

### 1. Create the service script
--------------------------------------------------------------------

```bash
cat > /tmp/sample-sre-demo.sh <<'EOF'
#!/bin/bash
while true; do
  echo "$(date --iso-8601=seconds) - Service running"
  sleep 5
done
EOF
```
--------------------------------------------------------------------

### 2. Install script into /usr/local/bin with correct permissions
--------------------------------------------------------------------
```bash
sudo install -m 755 /tmp/sample-sre-demo.sh /usr/local/bin/sample-sre-demo.sh
```
--------------------------------------------------------------------

### Learning:
- `install -m 755` copies the script and ensures correct executable permissions.
- Scripts in `/usr/local/bin` follow Linux FHS best practices.


### 3. Create improved systemd unit file
--------------------------------------------------------------------
```bash
cat > /tmp/sample-sre-demo.service <<'EOF'
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
EOF
```
--------------------------------------------------------------------

### 4. Move the service into systemd directory
--------------------------------------------------------------------
```bash
sudo cp /tmp/sample-sre-demo.service /etc/systemd/system/sample-sre-demo.service
```
--------------------------------------------------------------------


### 5. Reload systemd, enable service, and start it immediately
--------------------------------------------------------------------
```bash
sudo systemctl daemon-reload
sudo systemctl enable --now sample-sre-demo
```
--------------------------------------------------------------------

### Learning:
- `daemon-reload` tells systemd to re-read new unit files.
- `enable --now` enables at boot **and** starts immediately.


### 6. Check service status
--------------------------------------------------------------------
```bash
sudo systemctl status sample-sre-demo --no-pager
```
--------------------------------------------------------------------


### 7. View last 50 log lines
--------------------------------------------------------------------
```bash
sudo journalctl -u sample-sre-demo -n 50 --no-pager
```
--------------------------------------------------------------------

## What This Workflow Demonstrates (SRE-Level Learning)
- Creating system services safely and reproducibly.
- Using systemd with automatic restarts and throttled restart limits.
- Running services as **non-root users** (`nobody`) for security.
- Logging through `journalctl` for observability.
- Packaging scripts in `/usr/local/bin` and units in `/etc/systemd/system`.
- Automating deployments using `cat <<EOF` patterns — widely used in SRE automation, Ansible, Terraform, and Kubernetes bootstrap scripts.

