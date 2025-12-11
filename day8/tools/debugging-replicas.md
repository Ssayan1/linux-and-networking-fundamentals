# 🛠 Debugging Replica Issues (Day 8)

This guide helps diagnose problems when running multiple replicas in a load-balanced setup.

---

# 🔹 Check Replica Health

```bash
docker compose ps
```

Look for:
- `(healthy)`
- `(starting)`
- `(unhealthy)`

---

# 🔹 Inspect Health Details

```bash
docker inspect <container> | grep -A10 Health
```

---

# 🔹 Check If API Is Actually Running

```bash
docker exec -it <container> curl http://localhost:5001
docker exec -it <container> curl http://localhost:5001/health
```

---

# 🔹 Verify DNS Resolution

From load balancer:

```bash
docker exec lb getent hosts api
docker exec lb ping api-1
```
If DNS fails → service won't load balance.

---

# 🔹 Debug Traffic Through LB

```bash
docker logs lb
```
Look for:
- NGINX config errors  
- upstream failures  
- connection timeouts  

---

# 🔹 View Replica Container Logs

```bash
docker compose logs api --tail 50
```

---

# 🔹 Check Network & IP Assignments

```bash
docker network inspect loadbalanced-api_default
```

---

# 🔹 Fix Common Issues

| Issue | Fix |
|-------|-----|
| healthcheck failing | verify path, port, timing |
| NGINX 502 errors | replica not reachable |
| uneven traffic | check weights or LB config |
| DNS not resolving | container restart / recreate network |
| LB not loading | NGINX config syntax error |

---

# 🔹 Restart Only the Load Balancer

```bash
docker compose restart lb
```

---

# 🔹 Recreate All Replicas Cleanly

```bash
docker compose down
docker compose up -d --scale api=3
```
---

# 🔹 Summary

This tool helps you quickly fix issues with:
- scaling  
- healthchecks  
- DNS discovery  
- NGINX load balancing  
- container failures 
