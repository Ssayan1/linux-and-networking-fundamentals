# 🧪 Lab 1 — Multi-Network Basics (Docker Compose)

## 🎯 Objective
Understand how multi-network communication works in Docker Compose by inspecting networks, validating container membership, and testing connectivity.

---

## 📝 Step 1 — List All Networks

```bash
docker network ls
```
Identify:

  - frontend_net
  - backend_net
  - tracing_net

---

## 📝 Step 2 — Inspect Each Network

```bash
docker network inspect multi-network-app_frontend_net
docker network inspect multi-network-app_backend_net
docker network inspect multi-network-app_tracing_net
```

Record:

- Containers joined
- IP ranges
- Gateways

---

## 📝 Step 3 — Check API Network Membership

```bash
docker inspect -f "{{json .NetworkSettings.Networks}}" multi-network-app-api-1 | jq
```

Expected:
- Should appear in all 3 networks

---

## 📝 Step 4 — Validate Frontend → API Connectivity

```bash
docker exec -it multi-network-app-frontend-1 sh
curl http://api:5001
```

Expected:

```csharp
Hello from API!
```

---

## 📝 Step 5 — Validate API Isolation

Try accessing logger from frontend (should fail):

```bash
curl http://logger:6000
```
Expected:

```yaml
Could not resolve host: logger
```
✅ Lab Complete

Understanding network isolation, routing, and segmentation.
