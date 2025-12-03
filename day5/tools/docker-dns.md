# Docker DNS Troubleshooting Guide

---

## 🔹 1. View DNS Configuration

Inside container:

```bash
cat /etc/resolv.conf
```
Typical:
```nginx
nameserver 192.168.65.7
```
(Docker Desktop’s internal DNS)

---

## 🔹 2. Install DNS Tools

```bash
apt update && apt install -y dnsutils
```

---

## 🔹 3. Test Upstream DNS

```bash
dig google.com
```

---

## 🔹 4. Test Container DNS (user-defined networks)

```bash
docker exec web1 dig web2
```

---

## 🔹 5. Simulate DNS Failure

```bash
echo "nameserver 127.0.0.1" > /etc/resolv.conf
dig google.com
```
Expected: failure

---

## 🔹 6. Fix DNS

```bash
echo "nameserver 192.168.65.7" > /etc/resolv.conf
```

---

## Summary

Docker uses built-in DNS when using user-defined networks only.
