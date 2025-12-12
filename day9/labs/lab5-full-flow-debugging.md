# 🧪 Lab 5 — Full Flow Debugging (End-to-End)

## 🎯 Objective
Debug the entire multi-network microservices pipeline.

---

# 📝 Step 1 — Check Network Routes

```bash
docker network inspect multi-network-app_backend_net
```
Verify all expected containers exist.


---

# 📝 Step 2 — Test All Service Connections

| Source            | Destination | Expected |
| ----------------- | ----------- | -------- |
| frontend → api    | OK          |          |
| api → logger      | OK          |          |
| logger → jaeger   | OK          |          |
| frontend → logger | FAIL        |          |
| frontend → jaeger | FAIL        |          |

Run:

```bash
docker exec -it <container> sh
curl <target>
```

---

# 📝 Step 3 — Check Logs for Each Service

```bash
docker compose logs api --tail=50
docker compose logs logger --tail=50
docker compose logs jaeger --tail=20
docker compose logs frontend --tail=20
```

---

# 📝 Step 4 — Enable Debug Mode (optional)

```bash
docker exec -it api-1 sh
env | grep JAEGER
```

---

# 📝 Step 5 — Validate End-to-End Functionality

```bash
curl localhost:8000/log
```
Expected:

- Logger logs request
- API prints request receipt
- Jaeger captures traces


---

# 🎉 Lab Complete

Networking + service discovery + telemetry + logging across a real microservices ecosystem.
