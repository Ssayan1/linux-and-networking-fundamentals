# Packet Capture with tcpdump

This lab teaches SRE-level network debugging using tcpdump to trace container traffic.

---

## 🎯 Objectives

- Capture container HTTP traffic
- Analyze SYN, ACK, GET, and response packets
- Understand packet flow through docker0

---

## 🔧 Step 1 — Install tcpdump

Inside Docker VM:

```bash
sudo apt update
sudo apt install -y tcpdump
```

---

## 🔧 Step 2 — Get Container IP
```bash
docker inspect -f '{{ .NetworkSettings.IPAddress }}' demo-nginx
```

---

## 🔧 Step 3 — Capture Traffic on docker0
```bash
sudo tcpdump -i docker0 -nn host <container-ip>
```
Leave this terminal running.

---

## 🔧 Step 4 — Trigger Traffic

From another terminal:
```bash
curl http://<container-ip>
```

---

## 🔧 Step 5 — Observe Packets

Expected flow:
- SYN → SYN/ACK → ACK (TCP handshake)
- HTTP GET /
- HTTP/1.1 200 OK

Save interesting output into:

---

## Summary

tcpdump helps debug:
- DNS failures
- NAT direction issues
- Connection resets
- Kubernetes CNI failures

