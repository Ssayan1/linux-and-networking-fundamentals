# 🧪 Lab 4 — Scaling + Load Balancing Stress Test

This lab verifies how load balancing behaves when scaling replicas dynamically.

---

# 🎯 Objectives
- Scale replicas to 5
- Test distribution
- Confirm round-robin behavior

---

# 🚀 Step 1 — Scale replicas

```sh
docker compose up -d --scale api=5
```
Check containers:

```sh
docker compose ps
```
Expected:

```
api-1 … healthy
api-2 … healthy
api-3 … healthy
api-4 … healthy
api-5 … healthy
```

---

# 🧪 Step 2 — Send multiple requests

```sh
for i in {1..15}; do curl -s localhost:5001; echo; done
```

Expected rotating outputs:

```csharp
Hello from container: 1a2b3c
Hello from container: 9cd88f
Hello from container: 7abd12
Hello from container: 5dc221
Hello from container: 0afee1
(repeat…)
```

---

# 📊 Step 3 — Verify distribution by counting responses

```sh
for i in {1..50}; do curl -s localhost:5001; echo; done | sort | uniq -c
```
Expected:

```csharp
10 Hello from container: <ID1>
10 Hello from container: <ID2>
10 Hello from container: <ID3>
10 Hello from container: <ID4>
10 Hello from container: <ID5>
```

---

# 🎉 Lab Complete!
Validated real load balancing across replicas.
