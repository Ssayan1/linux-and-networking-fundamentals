# 🌐 Multi-Network Docker Compose — Deep Dive

Microservices often require multiple networks for isolation, security, and controlled communication.  
In this module, we explore how multi-network architecture works using Docker Compose.

---

## 🔥 Why Use Multiple Networks?

| Network | Purpose |
|--------|---------|
| **frontend_net** | Serves public traffic (browser → frontend) |
| **backend_net** | Internal communication (frontend → API → logger) |
| **tracing_net** | Sends telemetry to Jaeger (API + logger → Jaeger) |

Using separate networks improves:

- Security (hide API from the internet)
- Observability (send traces to Jaeger only)
- Maintainability (clear boundaries)
- Performance (limit broadcast domains)

---

## 🧱 Architecture Diagram

        ┌────────────┐
        │  Frontend   │
        └─────┬──────┘
              │  frontend_net
        ┌─────▼──────┐
        │    API      │──────────┐ backend_net
        └─────┬──────┘          │
              │ tracing_net      │
        ┌─────▼────────┐        │
        │ Logger Sidecar│────────┘
        └─────┬────────┘
              │ tracing_net
        ┌─────▼────────┐
        │    Jaeger     │
        └───────────────┘

---

## 🌍 Multi Network in docker-compose.yml

```yaml
networks:
  frontend_net:
  backend_net:
  tracing_net:
```

Each service joins only the networks it needs:

```yaml
api:
  networks:
    - frontend_net
    - backend_net
    - tracing_net
```
This ensures the API:

- Receives requests from frontend
- Logs to sidecar
- Sends traces to Jaeger
