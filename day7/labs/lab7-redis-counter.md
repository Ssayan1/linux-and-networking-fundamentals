# Lab 7 — Redis Counter with Docker Compose

## 🎯 Objective

Run two containers that talk to each other:

- Python API
- Redis database

🧪 Steps

1️⃣ Start the environment


```bash
docker compose up -d --build
```

2️⃣ Call the API

```bash
curl http://localhost:5000
```

Expected:

Counter: 1


Run again:

Counter: 2

3️⃣ Check logs

```bash
docker compose logs -f api
docker compose logs -f redis
```

4️⃣ Clean up


```bsh
docker compose down
```
