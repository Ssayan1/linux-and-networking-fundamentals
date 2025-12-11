# 📌 Docker Scaling Cheat Sheet (Day 8)

This guide summarizes all important scaling commands used for horizontal scaling in Docker Compose.

---

## 🔹 Scale a Service

```bash
docker compose up -d --scale api=3
```

Increase or decrease replicas:

```
docker compose up -d --scale api=5
docker compose up -d --scale api=1
```

---

## 🔹 Inspect Running Replicas

```bash
docker compose ps
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
```

---

## 🔹 View Container Hostnames (Replica Identity)

Example:

```bash
docker execapi-1 hostname
```

---

## 🔹 Remove and Re-Create Replicas

```bash
docker compose up -d --force-recreate --scale api=3
```

---

## 🔹 Stop All Replicas

```bash
docker compose down
```

---

## 🔹 Check Docker DNS Resolution

```bash
docker exec lb ping api
docker exec lb getent hosts api
```

Docker automatically resolves:
```
api → api-1, api-2, api-3
```

---

## 🔹 View Each Replica's IP

```bash
docker inspect -f '{{.Name}} - {{.NetworkSettings.Networks.loadbalanced-api_default.IPAddress}}' $(docker ps -q)
```

---

## 🔹 Summary

| Need | Command |
|------|---------|
| Scale replicas | `docker compose up -d --scale api=N` |
| Reset replicas | `--force-recreate` |
| View health | `docker inspect <container> | grep Health` |
| Identify node | `docker exec <container> hostname` |
| Test distribution | `curl localhost:5001` repeatedly |
