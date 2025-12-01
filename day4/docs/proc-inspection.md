# 📂 Inspecting Processes Using /proc/<PID>

The `/proc` filesystem gives real-time information about any running process.

## Key files

### Command line

```shell
cat /proc/<PID>/cmdline
```

### Threads

```shell
ls /proc/<pid>/task | wc -l
```

### Memory stats 

```shell
grep -E "Vm|Threads" /proc/<PID>/status
```

### File descriptors

```shell
ls -l /proc/<PID>/fd
```

### CPU affinity

```shell
taskset -pc <PID>
```

###

