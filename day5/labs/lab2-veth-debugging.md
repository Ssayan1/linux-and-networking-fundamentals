#  veth Pair Debugging

This lab teaches how veth pairs connect containers to the host Linux network stack.

---

## 🎯 Objectives

- Discover veth interfaces inside Docker Desktop VM
- Map container eth0 ↔ host veth
- Understand EndpointIDs

---

## 🔧 Step 1 — Enter Docker Desktop Linux VM

```bash
wsl -d docker-desktop
```

---

## 🔧 Step 2 — List All Network Interfaces
```bash
ip link
```
You will now see many interfaces:
- docker0
- vethXXXXX
- eth0 (VM NIC)

---

## 🔧 Step 3 — Get Container EndpointID

On Windows terminal (outside VM):
```bash
docker inspect demo-nginx --format '{{.NetworkSettings.Networks.bridge.EndpointID}}'
```
Take the first 12 characters (prefix).

---

## 🔧 Step 4 — Match veth on Host

Inside Docker VM:
```bash
ip link | grep <first-12-chars>
```
This reveals the actual veth interface.

---

## Step 5 — Validate the Peer Link

```bash
ethtool -S <veth-name>
```
Confirm packet RX/TX counts change when pinging.

---

## Summary

- veth pairs = virtual cables
- one end in container
- one end in host namespace
- essential for Kubernetes CNI
