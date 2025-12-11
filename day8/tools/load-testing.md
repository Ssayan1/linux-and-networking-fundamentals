# 🔥 Load Testing Tools for Docker Scaling (Day 8)

These simple load-test loops help validate load balancing behavior.

---

# 🔹 Test Round Robin

```yaml
for i in {1..10}; do curl -s localhost:5001; echo; done
```

---

# 🔹 Test Distribution Among Replicas

```bash
for i in {1..50}; do curl -s localhost:5001; done | sort | uniq -c
```

Example output:

```yaml
12 Hello from container abc123
19 Hello from container 9fbc44
19 Hello from container ee7731
```

---

# 🔹 High Pressure Test

```yaml
seq 1 200 | xargs -I{} -P10 curl -s localhost:5001 > /dev/null
```

---

# 🔹 See Which Node Responds Most

```yaml
while true; do curl -s localhost:5001; sleep 0.2; done
```

---

# 🔹 Test When You Kill a Replica

```yaml
docker stop loadbalanced-api-api-1
```

Watch NGINX automatically reroute.

---

# 🔹 Break-Fix Load Test

```bash
docker rm -f $(docker ps -q --filter name=api)
docker compose up -d --scale api=5
```
---

# 🔹 Summary

| Test | Purpose |
|------|---------|
| Round robin | Verify LB rotation |
| 50-call test | Statistical distribution |
| Pressure test | Stability check |
| Failure simulation | High availability testing |
