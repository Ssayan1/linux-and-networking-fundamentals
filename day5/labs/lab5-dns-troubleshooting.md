# Docker DNS Troubleshooting

This lab teaches how to analyze DNS behavior inside Docker containers.

---

## 🎯 Objectives

- Inspect resolv.conf
- Test DNS resolution
- Verify Docker DNS server
- Perform troubleshooting

---

## 🔧 Step 1 — Enter Container

```bash
docker exec -it demo-nginx bash
```

---

## 🔧 Step 2 — Inspect resolv.conf

```bash
cat /etc/resolv.conf
```
Docker Desktop normally provides:
```nginx
nameserver 192.168.65.7
```

---

## 🔧 Step 3 — Install DNS Tools

```bash
apt update && apt install -y dnsutils
```

---

## 🔧 Step 4 — Test Internet DNS

```bash
dig google.com
```

---

## 🔧 Step 5 — Test Internal DNS (user-defined network)

If you have services attached to sre-net:
```bash
dig web2
ping web2
```

---

## 🔧 Step 6 — Simulate DNS Failure

Temporarily override nameserver:
```bash
echo "nameserver 127.0.0.1" > /etc/resolv.conf
dig google.com
```
Expect failure.

---

## 🔧 Step 7 — Restore DNS
```bash
echo "nameserver 192.168.65.7" > /etc/resolv.conf
```

---

## Summary

- Docker DNS = core mechanism for container name resolution
- Only works on user-defined networks
- Essential for Kubernetes CoreDNS behavior
