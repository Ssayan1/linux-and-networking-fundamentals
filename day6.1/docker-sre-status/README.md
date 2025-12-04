# SRE Status Service (Docker)

A minimal SRE-style status service packaged in a Docker container.

## Features

- HTTP endpoints:
  - `/` – basic status with hostname and timestamp
  - `/health` – liveness probe
  - `/ready` – readiness probe
- Non-root container user
- Resource limits support (`--cpus`, `--memory`)
- Clean, production-friendly Dockerfile

## Build

```bash
docker build -t sre-status-service:v1 .
```

## Run

```bash
docker run --rm -p 8000:8000 sre-status-service:v1
```
### Then:
 
```bash
curl http://localhost:8000/
curl http://localhost:8000/health
curl http://localhost:8000/ready

```

