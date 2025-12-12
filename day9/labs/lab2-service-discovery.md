# 🧪 Lab 2 — Service Discovery & DNS in Docker Compose

## 🎯 Objective
Learn how Docker's internal DNS resolver maps service names to IPs and how containers discover each other.

---

## 📝 Step 1 — Enter Frontend Container

```bash
docker exec -it multi-network-app-frontend-1 sh
```
Ping API:

```bash
ping -c 3 api
```

Expected:

```java
PING api (172.x.x.x)
```

---

## 📝 Step 2 — Resolve DNS Using nslookup

If nslookup is not available:

```bash
apk add bind-tools
```
Then:

```bash
nslookup api
```

---

## 📝 Step 3 — Test HTTP Resolution

```bash
curl http://api:5001
```

LOG expected:

```csharp
Hello from API!
```

---

## 📝 Step 4 — Test Wrong Network Access

Try API → frontend_net access from logger:

```bash
docker exec -it multi-network-app-logger-1 sh
curl http://frontend
```

Expected:

```nginx
Could not resolve host
```

---

## 📝 Step 5 — Explore DNS Through /etc/hosts

```bash
cat /etc/hosts
```

Observe:

- Service names available inside this network only

🎉 Lab Complete

Understanding service name → DNS mapping → network accessibility.
