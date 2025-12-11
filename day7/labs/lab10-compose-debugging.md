## Lab 10 — Debugging Containers in Docker Compose


## 🧪 Steps

1️⃣ Inspect the compose network

```bash
docker network inspect microservices-stack_default
```

2️⃣ View container logs

```bash
docker compose logs -f proxy
docker compose logs -f api
```

3️⃣ Run a shell inside a container

```bash
docker compose exec api sh
```

4️⃣ Check DNS resolution

From inside container:

```bash
ping api
ping frontend
```
