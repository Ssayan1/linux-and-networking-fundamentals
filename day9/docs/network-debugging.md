# 🛠 Network Debugging for Multi-Network Microservices

This guide covers how to debug connectivity between containers across isolated networks.

---

# 🔍 1. Check Networks

List networks:

```bash
docker network ls
```
Inspect a specific one:

```bash
docker network inspect multi-network-app_backend_net
```

---

# 🔍 2. Test Service Discovery (DNS)

Inside any container:

```bash
docker exec -it <container> sh
ping api
```

Expected:

```java
PING api (172.x.x.x)
```

---

## 🔍 3. Test HTTP Connectivity

Frontend → API:

```bash
docker exec -it multi-network-app-frontend-1 sh
curl http://api:5001
```

Logger → API:

```bash
docker exec -it multi-network-app-logger-1 sh
curl http://api:5001
```

---

## 🔍 4. Check Container IPs

```bash
docker inspect -f "{{ .NetworkSettings.Networks }}" multi-network-app-api-1
```

---

## 🔍 5. Debug With tcpdump (optional)

If installed:

```bash
docker exec -it api-1 tcpdump -i eth0 port 5001
```

---

## 🔍 6. Check Logs

API logs:

```bash
docker compose logs api
```

Logger logs:

```bash
docker compose logs logger
```

Jaeger logs:

```bash
docker compose logs jaeger
```

---

## 🔍 7. Restart Individual Services

```bash
docker compose restart api
```
