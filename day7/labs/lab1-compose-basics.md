# Lab 1 — Build & Run Your First Docker Compose App

## 🎯 Objective

Learn how to use docker-compose to run a multi-container application (web + API).

## 🧱 App Structure
```bash
simple-web/
 ├── Dockerfile
 └── index.html
```

## 🧪 Steps

1️⃣ Build the image

```bash
docker compose build
```

2️⃣ Run containers

```bash
docker compose up -d
```

3️⃣ Test the app

```bash
curl http://localhost:8080
```

Expected output:

```
<h1>Simple Web App</h1>
```

4️⃣ Stop containers

```bash
docker compose down
```
