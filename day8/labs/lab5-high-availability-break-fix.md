# 🧪 Lab 5 — High Availability Break & Fix Simulation

Learn how the system behaves when containers fail, and how load balancing + healthchecks provide self-healing.

---

# 🎯 Objectives
- Kill a backend replica
- Observe how the load balancer reacts
- Restore service automatically

---

# 🧨 Step 1 — Kill one container

```sh
docker kill loadbalanced-api-api-3
```

---

# 🔍 Step 2 — Test LB again

```sh
curl localhost:5001
```

Output will now skip the dead replica.


---

# 🔁 Step 3 — Docker restarts unhealthy container

Because of:

```yaml
restart: always
```
Check restart:

```sh
docker ps --filter name=api-3
```

You should see:

```scss
Restarting (1)
```

Then stable:

```nginx
healthy
```

---

# 🛠 Step 4 — Scale down

```sh
docker compose up -d --scale api=2
```
LB automatically adapts.

🎉 Lab Complete!

validated:

- healthchecks for recovery
- load balancer rerouting
- scaling down behavior

