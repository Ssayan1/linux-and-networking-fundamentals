# 🧪 Lab 2 — Docker Healthchecks

This lab teaches how Docker healthchecks detect failing apps and how containers transition between `starting → healthy → unhealthy`.

---

# 🎯 Objectives
- Add a healthcheck to a service
- Observe unhealthy containers
- Debug healthcheck logs
- Fix the application

---

# 📁 Step 1 — Open compose file

```yaml
healthcheck:
  test: ["CMD-SHELL", "wget -qO- http://localhost:5001/health || exit 1"]
  interval: 5s
  timeout: 2s
  retries: 3
```

---

# 🧪 Step 2 — Start stack

```sh
docker compose up -d --build
```

---

# 🔍 Step 3 — Check container health

```sh
docker compose ps
```
You may see:

```scss
(health: starting)
(healthy)
(unhealthy)
```

---

# 🧾 Step 4 — Inspect health logs

```sh
docker inspect loadbalanced-api-api-1 | jq '.[0].State.Health'
```
Look for:

```json
"ExitCode": 1
"Output": "Connection refused"
```

---

# 🛠 Step 5 — Fix app health endpoint

Open app.py:

```python
@app.route("/health")
def health():
    return "OK", 200
```
Rebuild:

```sh
docker compose up -d --build
```
Verify:

```sh
docker compose ps
```
Now all should be:

```scss
(healthy)
```
