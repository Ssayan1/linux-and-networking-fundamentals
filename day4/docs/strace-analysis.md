# 🔍 strace Analysis — Day 4 CPU Debugging

This document explains how to interpret `strace -c` output during CPU debugging.

## Example sanitized strace summary

% time seconds usecs/call calls errors syscall
100.00 1.23 20 60000 write


## Interpretation

- **100% CPU spent in write() syscall**
- Typical pattern of programs producing output in a tight loop
- Indicates a **syscall-bound workload**, not compute-bound

## What's look for

- High %sys → kernel overhead (network, disk, syscalls)
- High %usr → user-space compute loops
- Other syscalls of interest:
  - read()
  - futex()
  - nanosleep()
  - epoll_wait()
  - poll()
  - recv/send

This analysis is essential during CPU-related incidents.

