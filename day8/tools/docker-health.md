# ❤️ Docker Healthchecks — SRE Debugging Guide

Healthchecks allow Docker to detect when a service is **healthy**, **starting**, or **unhealthy**.

Used heavily in Day 8 for load-balanced microservices.

---

# 🔹 Understand Health States

### ✔ `starting`
Container launched, healthcheck still warming up.

### ✔ `healthy`
Healthcheck returned exit code 0.

### ✔ `unhealthy`
Healthcheck failed multiple times.

Docker may **restart the container** based on restart policy.

---

# 🔹 Inspect a Container’s Health

```bash
docker inspect --format '{{json .State.Health}}' <container> | jq
```

---

# 🔹 Run the Healthcheck Command Manually

```bash
docker exec api-1 wget -qO- http://localhost:5001/health
```

---

# 🔹 Most Common Failures

### ❌ Wrong PORT in healthcheck
Healthcheck uses container-internal port, NOT host port.

### ❌ Service not ready before first check  
Fix by increasing interval:
interval: 10s
retries: 5

### ❌ DNS failure  
Replica not reachable inside the network.

---

# 🔹 Making a Strong Healthcheck

```yaml
healthcheck:
test: ["CMD-SHELL", "wget -qO- http://localhost:5001/health || exit 1"]
interval: 5s
timeout: 2s
retries: 3
```

---

# 🔹 Summary

| Issue | Fix |
|------|-----|
| Containers stuck at “starting” | Increase interval/timeouts |
| Unhealthy due to wrong path | Verify `/health` endpoint |
| LB routing to dead node | Healthchecks remove it from pool |
| DNS error | Test with `getent hosts api` |




