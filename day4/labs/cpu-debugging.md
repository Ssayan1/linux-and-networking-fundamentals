## 📘 DAY 4 — CPU & Performance Debugging

An extremely comprehensive hands-on lab designed to teach FAANG-level Linux performance debugging using real tools SREs use during incidents.

---

## Overview 
In this lab, you will learn how to:
- Generate controlled CPU load
- Identify high-CPU processes
- Analyze CPU usage with top, htop, ps, pidstat
- Inspect running processes via /proc
- Use strace to capture syscall profiles
- Understand user-space vs kernel-space CPU usage
- Analyze syscall overhead & kernel behavior
- Perform an SRE-style CPU incident investigation

---

## 🧪 Lab Part 1 — Generate a Controlled CPU Spike

We will use the yes utility, which prints a character repeatedly, causing predictable CPU saturation.

### Run in a separate terminal:
```bash
yes > /dev/null
```
This produces:
- 1 thread
- near 100% CPU usage on one core
- continuous stream of write() syscalls

Keep it running

---

## 🧪 Lab Part 2 — Identify the High-CPU Process

```bash
ps aux --sort=-%cpu | head
```
📌 Expected (generic) output:
```bash
USER     PID  %CPU  %MEM   VSZ   RSS TTY   STAT START TIME COMMAND
user   12345  98.5   0.1  3124  1664 pts/2  R+   ...  0:12 yes
```
✔ The yes command should appear at the top consuming ±100% CPU.

---

## 🧪 Lab Part 3 — Measure CPU Usage Over Time (pidstat)

```bash
pidstat -u -p <PID> 1 5
```
📌 Expected interpretation:
- %usr ≈ 25–35% (user-space work)
- %sys ≈ 60–75% (kernel handling write() syscalls)
- %wait ≈ 0% (no I/O waiting)
- %CPU ≈ 95–100%
This is typical of tight loops making frequent syscalls.

---

## 🧪 Lab Part 4 — Inspect Process Metadata (the /proc filesystem)

### List process metadata:
```bash
ls -l /proc/<PID>
```
Explore specific files:

### Command line:
```bash
cat /proc/<PID>/cmdline
```

### Threads:
```bash
ls /proc/<PID>/task | wc -l
```
Expected: 1 thread

### Open file descriptors:
```bash
ls -l /proc/<PID>/fd
```
Expected:
- stdin → pts/X
- stdout → /dev/null
- stderr → pts/X

### CPU Affinity:
```bash
taskset -pc <PID>
```
Expect: "0-3" (means kernel can schedule on any CPU)

## 🧪 Lab Part 5 — Memory Stats of the Process
```bash
cat /proc/<PID>/status | grep -E "Vm|Threads"
```
output:
```
VmSize:  3 MB
VmRSS:   1.6 MB
Threads: 1
```
✔ yes is extremely lightweight.

---

## 🧪 Lab Part 6 — Syscall Profiling (strace summary mode)
This is the most important part of the lab.
### Run:
```bash
sudo strace -c -p <PID> -e trace=all
```
Press Ctrl + C after 2–3 seconds.

📌 Expected generic output:
```
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
100.00     1.23           20      60000           write

```
✔ 100% write() → exactly what a CPU burner should produce
✔ This proves the process is syscall-limited, not compute-limited.

---

## Interpretation of This Syscall Profile

#### Why only write()?

Because yes does:
```bash
printf("y\n") inside infinite loop
```

#### Why does CPU go high?

Because syscalls are expensive:

- context switch
- kernel boundary crossing
- buffer checks
- scheduler updates

Even though /dev/null discards data instantly, reaching that point still consumes CPU cycles.

#### Why is %system > %user?

Because kernel work dominates: file descriptor handling + write syscalls.

---

## 🧪 Lab Part 7 — Visual Diagram: Syscall Hot Loop


---

## Key Takeaways

1. A “CPU spike” is not always a compute problem
→ It can be a syscall flood.
2. pidstat reveals user-space vs kernel-space ratio
→ Critical in real incidents.
3. /proc/<PID> is your single best debugging tool for live processes.
4. strace -c shows exactly where CPU cycles are being spent.
5. If a production service spikes CPU:
   - inspect syscalls
   - inspect IO
   - inspect threads
   - inspect affinity
   - inspect contention (futex, poll, epoll)
6. This lab builds for the foundation for:
   - perf
   - eBPF
   - flamegraphs
   - distributed tracing
   - kernel profiling

---

## 🧪 Lab Part 8 — Cleanup

kill the CPU load:
```bash
pkill yes
```
Verify:
```bash
pgrep yes
```
Expected: no output

---

## Conclusion

- Linux performance debugging
- CPU incident analysis
- Syscall profiling
- Kernel vs user space behavior
- /proc filesystem deep inspection
- Real incident-style root cause analysis
