# Docker veth Pair Debugging

This tool explains how containers connect to the host.

---

## 🔹 1. Find Container PID

```bash
docker inspect -f '{{ .State.Pid }}' demo-nginx
```

---

## 🔹 2. Enter Host Network Namespace (Linux only)

```bash
sudo nsenter -t <pid> -n
```
(WSL2 does not allow full namespace access.)

---

## 🔹 3. See Host veth Interfaces

Inside Docker Desktop VM:
```bash
wsl -d docker-desktop
ip link

```
Look for interfaces beginning with:
- vethXXXXX

---

## 🔹 4. Map veth ↔ Container

Get EndpointID:
```bash
docker inspect demo-nginx | grep EndpointID
```

Match prefix inside:
```bash
ip link | grep <first-12-chars>
```

---


## 🧠 Summary

- veth = virtual cable
- One end inside container

One end in host namespace
