# ⚡ CPU Debugging Cheat Sheet 

## Find top CPU processes

```shell
ps aux --sort=-%cpu | head
```

## Real-time CPU load

uptime
## Live CPU analysis

```shell
pidstat -u -p <PID> 1 5
```

## System-wide monitoring

```shell
top
htop
mpstat 1 5
vmstat 1 5
```

## Process inspection

```shell
ls -l /proc/<PID>
```

## Syscall analysis

```shell
sudo strace -c -p <PID> -e trace=all
```


---

# ✅ **7. `docs/ps-pidstat-examples.md`**

```markdown
# 📝 Example ps & pidstat Outputs (Sanitized)

## ps aux

```shell
USER PID %CPU %MEM COMMAND
user 1234 98.0 0.1 yes
```

## pidstat -u

```shell
13:10:10 UID PID %usr %sys %CPU Command
1000 1234 28.0 68.0 96.0 yes
```


