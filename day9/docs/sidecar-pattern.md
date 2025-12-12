# 🧩 Sidecar Pattern — Explained with Docker

The “sidecar” pattern is a design where a helper container is placed next to the main app container to extend functionality.

In Day 9, the sidecar performs:

- Logging of API requests  
- Forwarding requests to the API  
- Sending tracing info to Jaeger  

---

## 🧱 Why Use a Sidecar?

| Feature | Provided by Sidecar |
|---------|----------------------|
| Centralized logging | Yes |
| Request tracing | Yes |
| Security isolation | Yes |
| Modular architecture | Yes |

Sidecars allow teams to add features without modifying the main app.

---

## 🧩 How It Works in Our Setup

```python
Frontend → API → Logger → Jaeger
```

Logger container:

```python
@app.route("/log")
def log_request():
    response = requests.get("http://api:5001")
    print(f"[LOGGER] Forwarded request to API: {response.text}")
    return "Logged"
```

---

## 📡 Benefits in Production
Traffic visibility

- Runtime behavior monitoring
- No need to change main application
- Works with any language or framework

