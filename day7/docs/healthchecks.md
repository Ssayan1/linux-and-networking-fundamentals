# Healthchecks in Docker Compose

Healthchecks ensure a service is ready before others rely on it.

---

## 🩺 Example Healthcheck

```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:5001"]
  interval: 5s
  timeout: 2s
  retries: 5
```

## 📊 Health States

| State       | Meaning                   |
| ----------- | ------------------------- |
| `starting`  | Running tests until ready |
| `healthy`   | Ready                     |
| `unhealthy` | Failed multiple tests     |


---

## 🔍 Debugging Healthchecks

```bash
docker inspect api | jq '.[0].State.Health'
```

Check logs:

```bash
docker logs api
```

---

## 🚨 Failure Scenarios

- Wrong port exposed
- Service takes too long to start
- Proxy misconfigured
- Missing dependencies
