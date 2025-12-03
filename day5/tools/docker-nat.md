# Docker NAT / iptables Debugging

Understand how Docker performs SNAT & DNAT.

---

## 🔹 1. Check NAT Rules

Inside Docker VM:

```bash
wsl -d docker-desktop
sudo iptables -t nat -L -n -v
```
Look at:
- POSTROUTING → MASQUERADE
- DOCKER chain

----

## 🔹 2. View Raw NAT Rules

```bash
sudo iptables -t nat -S
```

---

##🔹 3. Observe SNAT in Action

Trigger traffic:
```bash
docker exec demo-nginx curl https://google.com
```
Return to VM:
```bash
sudo iptables -t nat -L -v
```
RX/TX counters increase.

---

## 🔹 4. DNAT for Published Ports

If you run:
```bash
docker run -p 8080:80 nginx
```
Check:
```bash
sudo iptables -t nat -L DOCKER
```
You’ll see DNAT:
```bash
host:8080 → container-IP:80
```

---

## Summary

Docker NAT provides internet access and port forwarding.

