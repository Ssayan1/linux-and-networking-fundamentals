# ❤️ Docker Healthchecks — Ensuring Containers Stay Healthy

Healthchecks allow Docker to know if a container is working correctly.

A container can be:
- **healthy**
- **starting**
- **unhealthy**

Only **healthy** containers should receive production traffic.

---

## 🧪 Why Use Healthchecks?

Without a healthcheck, Docker assumes the app is always fine — even if it’s failing.

### Healthchecks fix this by validating:

- API responses
- Database readiness
- App crash loops
- Dependency failures

---

## 📝 Example Healthcheck (Flask App)

```yaml
healthcheck:
  test: ["CMD-SHELL", "curl -f http://localhost:5001/health || exit 1"]
  interval: 5s
  timeout: 2s
  retries: 3
```

Logic:

- Every 5 seconds → run health endpoint
- If it fails 3 times → mark container as unhealthy

--- 

## 🔍 View Health Status

```bash
docker ps
```

Output example:

```bash
STATUS: Up 10 minutes (healthy)
```

Inspect logs:

```bash
docker inspect <container> | jq '.[0].State.Health'
```

---

## 💡 Best Practices

- Always implement /health endpoint
- Avoid expensive healthchecks (DB queries)
- Keep timeout small (1–2 seconds)
- For production, prefer:
  - readiness checks
  - liveness checks

---

## 🚑 What Happens if Container Becomes Unhealthy?

If restart policy is set:

restart: always


Docker will auto-restart the failed container, giving self-healing behavior.

Healthchecks are required for any load balanced or scaled architecture.
