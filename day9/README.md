# 🚀 Day 9 — Advanced Docker Networking, Service Discovery & Distributed Tracing

Day 9 focuses on multi-network microservices architecture, service discovery, sidecar containers, and distributed tracing using Jaeger.
It teaches how real-world production systems route traffic, observe service behavior, and enforce network boundaries.

---

## 📚 Topics Covered

- Multi-network Docker Compose architecture
- Service discovery & internal DNS
- Sidecar pattern for logging
- Distributed tracing using Jaeger
- Network isolation & segmentation
- Debugging cross-service communication
- End-to-end microservices flow analysis


---

## 📁 Repository Structure

```pgsql

day9/
.
├── README.md
├── docs
│   ├── jaeger-tracing.md
│   ├── multi-network-basics.md
│   ├── network-debugging.md
│   ├── service-discovery.md
│   └── sidecar-pattern.md
├── examples
│   ├── multi-network-app
│   │   ├── api
│   │   │   ├── Dockerfile
│   │   │   └── app.py
│   │   ├── docker-compose.yml
│   │   ├── frontend
│   │   │   ├── Dockerfile
│   │   │   └── index.html
│   │   ├── jaeger
│   │   │   └── jaeger-config.yml
│   │   ├── logger-sidecar
│   │   │   ├── Dockerfile
│   │   │   └── logger.py
│   │   └── network-diagram.png
│   └── service-discovery-tests
│       ├── test1-ping.md
│       ├── test2-curl.md
│       └── test3-dns-lookup.md
├── labs
│   ├── lab1-multi-network.md
│   ├── lab2-service-discovery.md
│   ├── lab3-sidecar-logging.md
│   ├── lab4-tracing-jaeger.md
│   └── lab5-full-flow-debugging.md
└── tools
    ├── connectivity-checklist.md
    ├── dns-debugging.md
    ├── jaeger.debug.md
    ├── multi-network-inspect.md
    └── sidecar-tools.md

```

---

## 🎯 Learning Objectives

✔ Understand Multi-Network Architectures

How containers join multiple networks for limited-scope communication.

✔ Learn Docker’s Internal DNS

How services discover each other (api, logger, jaeger, frontend).

✔ Implement & Debug a Sidecar Pattern

A real logging sidecar that forwards requests and generates structured logs.

✔ Visualize System Behavior with Jaeger

Trace requests across multiple services:

```nginx
frontend → api → logger → jaeger
```

✔ Diagnose Network Segmentation

Ensure certain services intentionally cannot access others.

✔ Perform End-to-End Microservices Debugging

Network, ports, DNS, logs, tracing, connectivity all combined.

---

## 🧪 Hands-on Labs Included

| Lab                              | Description                                               |
| -------------------------------- | --------------------------------------------------------- |
| **lab1-multi-network-basics.md** | Learn how containers communicate across multiple networks |
| **lab2-service-discovery.md**    | DNS, service names, resolution, network isolation         |
| **lab3-sidecar-logging.md**      | Implement & debug a real sidecar logger                   |
| **lab4-tracing-jaeger.md**       | Visualize distributed traces in Jaeger                    |
| **lab5-full-flow-debugging.md**  | Diagnose full microservices flow end-to-end               |

Each lab includes:
- Commands
- Expected output
- Debugging steps
- Explanations

---

## 🛠 Tools Provided

| File                          | Purpose                                    |
| ----------------------------- | ------------------------------------------ |
| **multi-network-inspect.md**  | Network inspection, container membership   |
| **dns-debugging.md**          | DNS lookup, ping, curl, resolver debugging |
| **sidecar-tools.md**          | Sidecar logs, request forwarding tests     |
| **jaeger-debug.md**           | Jaeger logs, port checks, client behavior  |
| **connectivity-checklist.md** | Full microservices connectivity checklist  |

These tools make debugging faster, repeatable, and production-ready.

---

## 🗺 Network Diagram

Include or reference your diagram located at:

```bash
day9/examples/multi-network-app/network-diagram.png
```

This visual explains:

- network segmentation
- container connectivity
- routing flow
- tracing path

---
## 🌐 Example System: Multi-Network App 

Components

| Service            | Purpose                                  |
| ------------------ | ---------------------------------------- |
| **frontend**       | User-facing interface                    |
| **api**            | Business logic (joins multiple networks) |
| **logger-sidecar** | Observability/logging sidecar            |
| **jaeger**         | Distributed tracing backend              |

Networks

| Network          | Purpose                      |
| ---------------- | ---------------------------- |
| **frontend_net** | Frontend → API communication |
| **backend_net**  | API → Logger communication   |
| **tracing_net**  | API → Jaeger tracing export  |

Why multi-network?

Because real microservices environments isolate components for security:

- Frontend cannot talk to logger
- Logger cannot talk to frontend
- API can talk to both
- All systems export traces to Jaeger

---

## 🚦 Run the Entire Multi-Network System

```bash
cd day9/examples/multi-network-app
docker compose up -d --build
```

Check running services:

```bash
docker compose ps
```

Test API directly:

```bash
curl localhost:8000/api
```

View Jaeger UI:

```bash
http://localhost:16686
```

---

## 🏁 Summary

- How modern microservice communication works
- Multi-network routing and isolation
- Sidecar design (used in Kubernetes Service Meshes)
- Distributed tracing (Jaeger)
- Debugging connectivity 
