# Lab 12 — Simulate Production Failure & Recovery


## 🚨 Scenario

Frontend suddenly shows 502 Bad Gateway.

🧪 Troubleshooting Steps

1️⃣ Check proxy logs

```bash
docker compose logs -f proxy
```

2️⃣ Check API health

```bash
curl http://localhost:5001
docker compose logs -f api
```

3️⃣ Restart API

```bash
docker compose restart api
```

4️⃣ Validate

```bash
curl http://localhost/api
```

Expected:

Backend API is working!
