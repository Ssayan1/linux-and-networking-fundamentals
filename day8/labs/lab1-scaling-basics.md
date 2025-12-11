# 🧪 Lab 1 — Scaling Basics with Docker Compose

This lab teaches how to scale container replicas, how Compose creates multiple containers, and how service discovery works.

---

# 🎯 Objectives
- Understand horizontal scaling
- Scale a service to 3–5 replicas
- Inspect replica IPs
- Verify load distribution manually

---

# 📦 Step 1 — Clone or enter the Day 8 example

```sh
cd day8/examples/loadbalanced-api
```

---

# 📁 Step 2 — View docker-compose.yml

```yaml
services:
  api:
    build: .
    deploy:
      replicas: 3
```

📌 The deploy.replicas field tells Compose to create 3 replicas.

---

# 🚀 Step 3 — Start the stack

```sh
docker compose up -d --build
```

Check running containers:

```sh
docker compose ps
```

Expected:

```
api-1
api-2
api-3
```

---

# 🔍 Step 4 — View container IPs

```bash
docker inspect -f "{{ .Name }} => {{ .NetworkSettings.IPAddress }}" $(docker compose ps -q)
```

Expected output:

```ini
api-1 => 172.20.0.3
api-2 => 172.20.0.4
api-3 => 172.20.0.5
```

---

# 👀 Step 5 — Call each container manually

```sh
docker exec -it loadbalanced-api-api-1 curl localhost:5001
docker exec -it loadbalanced-api-api-2 curl localhost:5001
docker exec -it loadbalanced-api-api-3 curl localhost:5001
```

Each returns:

```css
Hello from container: <hostname>
```
