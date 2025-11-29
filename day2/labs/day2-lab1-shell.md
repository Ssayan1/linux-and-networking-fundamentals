## Command: Executing a shell script

### Script Content:
--------------------------------------------------------------------
```bash
#!/bin/bash
echo "SRE Script Running..."
echo "Current date: $(date)"
echo "Uptime: $(uptime)"
echo "Logged in users:"
who
```
--------------------------------------------------------------------

### Output:
--------------------------------------------------------------------
```bash
SRE Script Running...
Current date: Fri Nov 28 06:04:03 UTC 2025
Uptime:  06:04:03 up  5:21,  1 user,  load average: 0.00, 0.01, 0.02
Logged in users:
sayans   pts/1        2025-11-27 14:34
```
--------------------------------------------------------------------

## Learning:
- The script runs with `#!/bin/bash`, meaning it's executed using the Bash shell.
- `echo` prints messages, useful for logging steps in automation scripts.
- `date` prints the current system date and time.
- `uptime` shows system load, running time, and user count — important for SRE monitoring.
- `who` lists logged-in users, useful during troubleshooting sessions.
- This script demonstrates basic Bash scripting used in automation, health checks, and SRE workflows.


## Command:
```bash
 ./script1-basic.sh
```
Output:
--------------------------------------------------------------------
```bash
SRE Script Running...
Current date: Fri Nov 28 06:20:59 UTC 2025
Uptime:  06:20:59 up  5:37,  1 user,  load average: 0.00, 0.00, 0.00
Logged in users:
sayans   pts/1        2025-11-27 14:34
```
--------------------------------------------------------------------

## Learning:
- Running a script with `./script1-basic.sh` executes the file in the current directory.
- This only works because you previously added execute permission with `chmod +x script1-basic.sh`.
- The script prints dynamic system information including date, uptime, load average, and logged-in users.
- This pattern is common in SRE automation for generating health checks, logs, and maintenance scripts.
----------------------------------------------->

## Command: 
```bash
./script2-monitor.sh
```
Output:
--------------------------------------------------------------------
CPU Usage:
%Cpu(s):  0.0 us,  2.2 sy,  0.0 ni, 97.8 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st

Memory Usage:
               total        used        free      shared  buff/cache   available
Mem:            3789         563        3074           4         244        3225
Swap:           1024           0        1024

Disk Usage:
/dev/sdd       1007G  5.6G  951G   1% /
--------------------------------------------------------------------

## Learning:
- The script successfully reports **CPU**, **memory**, and **disk** usage, which are essential system health metrics.
- CPU is mostly idle (`97.8 id`), meaning the system is under very low load.
- Memory usage shows more than **3GB free**, indicating no memory pressure.
- Disk usage is only **1%**, meaning there's plenty of storage available.
- This type of script is useful for quick system checks, automation, and SRE runbooks.
- SREs often extend this with thresholds, alerts, or continuous monitoring tools.

----------------------------------------------->

## Command: Running system-monitor script (script2-monitor.sh)

### Script Content:
--------------------------------------------------------------------
```
#!/bin/bash

echo "CPU Usage:"
top -bn1 | grep "Cpu(s)"

echo
echo "Memory Usage:"
free -m

echo
echo "Disk Usage:"
df -h | grep '^/dev/'
```
--------------------------------------------------------------------

### Output:
--------------------------------------------------------------------
```bash
CPU Usage:
%Cpu(s):  0.0 us,  9.5 sy,  0.0 ni, 90.5 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st

Memory Usage:
               total        used        free      shared  buff/cache   available
Mem:            3789         557        3091           5         234        3231
Swap:           1024           0        1024

Disk Usage:
/dev/sdd       1007G  5.6G  951G   1% /
```
--------------------------------------------------------------------

## Learning:
- This script prints three essential system metrics: CPU, RAM, and disk usage.
- CPU shows ~90% idle, meaning the system is under almost no load.
- Memory statistics show most RAM is free or available, indicating no memory pressure.
- Disk usage is minimal (1%), showing plenty of free space.
- This script mimics basic monitoring commands used by SREs when diagnosing system health manually.
- Can be enhanced with thresholds, alerts, logging, and automation for real SRE workflows.

## Command: Running system-monitor script (script2-monitor.sh)

### Script Content:
--------------------------------------------------------------------
```bash
#!/bin/bash

echo "CPU Usage:"
top -bn1 | grep "Cpu(s)"

echo
echo "Memory Usage:"
free -m

echo
echo "Disk Usage:"
df -h | grep '^/dev/'
```
--------------------------------------------------------------------

### Output:
--------------------------------------------------------------------
```bash
CPU Usage:
%Cpu(s):  0.0 us,  9.5 sy,  0.0 ni, 90.5 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st

Memory Usage:
               total        used        free      shared  buff/cache   available
Mem:            3789         557        3091           5         234        3231
Swap:           1024           0        1024

Disk Usage:
/dev/sdd       1007G  5.6G  951G   1% /
```
--------------------------------------------------------------------

## Learning:
- This script prints three essential system metrics: CPU, RAM, and disk usage.
- CPU shows ~90% idle, meaning the system is under almost no load.
- Memory statistics show most RAM is free or available, indicating no memory pressure.
- Disk usage is minimal (1%), showing plenty of free space.
- This script mimics basic monitoring commands used by SREs when diagnosing system health manually.
- Can be enhanced with thresholds, alerts, logging, and automation for real SRE workflows.

----------------------------------------------->

## Command:
```bash
 chmod +x script2-monitor.sh
```
Output:
--------------------------------------------------------------------
(No output — chmod runs silently unless there is an error)
--------------------------------------------------------------------

## Learning:
- `chmod +x` adds **execute permission** to a script, allowing it to be run directly.
- After this, you can execute the script with `./script2-monitor.sh`.
- This is required for any Bash script you want to run from your current directory.
- Common step in SRE workflows when preparing automation scripts, cron tasks, or CI/CD utilities.


## Command:
```bash
 ./script2-monitor.sh
```
Output:
--------------------------------------------------------------------
```bash
CPU Usage:
%Cpu(s):  0.0 us,  2.2 sy,  0.0 ni, 97.8 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st

Memory Usage:
               total        used        free      shared  buff/cache   available
Mem:            3789         563        3074           4         244        3225
Swap:           1024           0        1024

Disk Usage:
/dev/sdd       1007G  5.6G  951G   1% /
```
--------------------------------------------------------------------

## Learning:
- The script outputs **CPU, memory, and disk** usage—three critical system health indicators.
- The CPU is mostly idle (`97.8 id`), showing almost no load on the system.
- Memory shows over **3GB free**, meaning no RAM pressure.
- Disk usage is extremely low (1%), leaving plenty of free storage.
- Such monitoring scripts are commonly used in SRE workflows for quick diagnostics and pre-checks before deployments or troubleshooting sessions.

==================================================
## Script 3: Backup Script (script3-backup.sh)
==================================================
```bash
#!/bin/bash

SOURCE=$1
DEST=$2

if [ -z "$SOURCE" ] || [ -z "$DEST" ]; then
    echo "Usage: $0 <source_directory> <destination_directory>"
    exit 1
fi

if [ ! -d "$SOURCE" ]; then
    echo "Error: Source directory '$SOURCE' does not exist."
    exit 1
fi

if [ ! -d "$DEST" ]; then
    echo "Destination '$DEST' not found. Creating it..."
    mkdir -p "$DEST"
fi

DATE=$(date +%F-%H-%M-%S)
BACKUP="$DEST/backup-$DATE.tar.gz"

tar -czf "$BACKUP" "$SOURCE"

echo "Backup completed: $BACKUP"
```
----------------------------------------------------

### Example Run:
----------------------------------------------------
```bash
./script3-backup.sh test-folder backups
```
----------------------------------------------------

### Example Output:
----------------------------------------------------
```bash
Backup completed: backups/backup-2025-11-29-03-35-40.tar.gz
```
----------------------------------------------------

### Learning:
- Automates folder backups with timestamp.
- Checks for required arguments.
- Creates destination folder if missing.
- Used for config backups, log backups, and system snapshots in SRE tasks.
