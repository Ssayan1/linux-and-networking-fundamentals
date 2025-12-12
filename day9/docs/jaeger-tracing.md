# 🔭 Distributed Tracing with Jaeger

Jaeger collects request traces across microservices.  
In Day 9, it receives traces from:

- API  
- Logger  

---

## 🧠 What Jaeger Shows

Jaeger UI (http://localhost:16686) displays:

- Latency per service
- Request call chain
- Dependency diagram
- Bottlenecks

Example trace:

```yaml
Frontend → API → Logger → API (forwarded)
```

---

## 🛠 Sending Traces

Containers use Jaeger's OTLP or UDP endpoint:

```yaml
JAFFER_AGENT_HOST=jaeger
JAFFER_AGENT_PORT=6831
```
In Compose:

```yaml
depends_on:
  - jaeger
```

---

## 📦 Jaeger Container

```yaml
jaeger:
  image: jaegertracing/all-in-one:latest
  ports:
    - "16686:16686"   # UI
    - "6831:6831/udp" # Tracing
```

--- 

## 🚀 Why Tracing Matters

- Helps debug slow requests
- Shows cross-service behavior
- Required for SRE-level production monitoring
