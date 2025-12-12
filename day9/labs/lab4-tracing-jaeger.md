# 🧪 Lab 4 — Distributed Tracing with Jaeger

## 🎯 Objective
View API + Logger traces inside Jaeger and understand cross-service request flow.

---

## 📝 Step 1 — Open Jaeger UI

Visit:

```yaml
http://localhost:16686
```

---

## 📝 Step 2 — Generate Load

```bash
for i in {1..20}; do curl localhost:8000/log; done
```

This sends:

```nginx
Frontend → API → Logger → Jaeger
```

---

## 📝 Step 3 — View Traces in Jaeger UI

In the UI:

- Select service: api
- Select service: logger
- View the timeline

Expected:

- You should see spans for API + Logger
- Logger span should appear slightly later


---

## 📝 Step 4 — View Dependency Graph

Click System Architecture / Dependencies

See a flow similar to:

```nginx
frontend → api → logger → jaeger
```

---

## 🎉 Lab Complete
Now visually understand distributed tracing across multiple services.

