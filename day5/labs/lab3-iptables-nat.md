#  NAT & iptables Debugging

This lab shows how Docker uses NAT (SNAT + DNAT) to give containers internet access.

---

## 🎯 Objectives

- Inspect NAT table
- Understand MASQUERADE rules
- Validate SNAT translation
- See Docker-managed chains

---

## 🔧 Step 1 — Enter Docker Desktop VM

```bash
wsl -d docker-desktop
```

---

## 🔧 Step 2 — List NAT Rules
```bash
sudo iptables -t nat -L -n -v
```
Look at chains:
- DOCKER
- POSTROUTING
- MASQUERADE

---

## 🔧 Step 3 — See How a Container Is NATed

Run curl from container:
```bash
docker exec -it demo-nginx bash
curl -I https://google.com
```
Then check NAT table again.

RX/TX counters increase on POSTROUTING MASQUERADE.

---

## 🔧 Step 4 — Print SNAT Rule

Search for MASQUERADE:
```bash
sudo iptables -t nat -S | grep MASQUERADE
```
This shows Docker rewriting:
```bash
172.17.x.x → host_IP
```

---

## Summary

- Docker uses MASQUERADE to reach internet
- POSTROUTING = outbound SNAT
- Docker injects chains dynamically
- Everything applies equally to Kubernetes nodes
