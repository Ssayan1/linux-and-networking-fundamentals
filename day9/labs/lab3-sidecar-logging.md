# 🧪 Lab 3 — Sidecar Logging Pipeline

## 🎯 Objective
Understand how a sidecar container intercepts API requests and forwards them while logging activity.

---

## 📝 Step 1 — Trigger a Sidecar Request

```bash
curl localhost:8000/log
```
Expected:

```vbnet
Sidecar: forwarded request to API
```

---

## 📝 Step 2 — Check Sidecar Logs

```bash
docker compose logs logger --tail=50
```
Look for:

```css
[LOGGER] Forwarded request to API...
```

---

##📝 Step 3 — Verify Logger → API Communication

Inside logger:

```bash
docker exec -it multi-network-app-logger-1 sh
curl http://api:5001
```

---

## 📝 Step 4 — Break the API Intentionally (optional test)

Stop API:

```bash
docker compose stop api
```
Retry the log route:

```bash
curl localhost:8000/log
```
Expected:

```vbnet
LOGGER ERROR: API unreachable
```

---

## 📝 Step 5 — Restart API

```bash
docker compose up -d api
```

---

🎉 Lab Complete

Learning sidecar → API dependency chain, logging, and failure behavior.

yaml
Copy code
