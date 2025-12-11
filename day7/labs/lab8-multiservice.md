# Lab 8 — Frontend + Backend Compose App


## 🎯 Objective

Understand container-to-container networking using service names.

## 🧱 Structure

```bash
multi-service/
 ├── backend/
 ├── frontend/
 └── docker-compose.yml
```

🧪 Steps

1️⃣ Build & Run

```bash
docker compose up -d --build
```

2️⃣ Test Backend

```bash
curl http://localhost:5002
```

3️⃣ Test Frontend

```bash
curl http://localhost:8081
```

Expected Output

```bash
Backend from Multi-Service Example
```

