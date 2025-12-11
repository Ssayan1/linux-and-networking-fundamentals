# 🚀 Day 8 — Scaling, Load Balancing & High Availability (Docker Compose + NGINX)

This module takes you beyond single-container apps and teaches real microservices scalability using Docker Compose, NGINX load balancing, healthchecks, and high availability patterns used by SRE teams in production.

By the end of Day 8, you will be able to build fault-tolerant, load-balanced backend systems that scale horizontally and recover automatically from failures.

---

## 📚 Topics Covered

- Horizontal scaling with docker compose up --scale
- Service discovery between replicas
- NGINX upstream load balancing (round robin)
- Healthchecks (starting → healthy → unhealthy logic)
- Simulating failures and self-healing
- Testing distribution under load
- Building production-style microservice stacks

---

## 📁 Repository Structure

```kotlin
day8/
 ├── README.md
 ├── docs/
 │   ├── scaling-concepts.md
 │   ├── docker-service-discovery.md
 │   ├── nginx-loadbalancing.md
 │   ├── healthchecks-deepdive.md
 │   ├── ha-patterns.md
 │   └── troubleshooting-guide.md
 ├── examples/
 │   └── loadbalanced-api/
 │       ├── app.py
 │       ├── Dockerfile
 │       ├── docker-compose.yml
 │       └── nginx.conf
 ├── labs/
 │   ├── lab1-scaling-basics.md
 │   ├── lab2-healthchecks.md
 │   ├── lab3-nginx-loadbalancer.md
 │   ├── lab4-scale-loadbalance-test.md
 │   └── lab5-high-availability-break-fix.md
 └── tools/
     ├── scaling-cheatsheet.md
     ├── docker-health.md
     ├── nginx-upstreams.md
     ├── load-testing.md
     └── debugging-replicas.md


```

---

## 🎯 Learning Objectives

✔ Scaling Fundamentals

- Replicas, service instances, container identity
- How Docker assigns IPs and DNS names (serviceName-1, serviceName-2, …)

✔ Load Balancing

- NGINX upstream blocks
- Round-robin distribution
- Testing traffic spread using loops & sorting

✔ Healthchecks

- Detecting failing containers
- Understanding starting, healthy, unhealthy
- How Docker restarts containers

✔ High Availability (HA)

- Self-healing architectures
- Removing and replacing dead nodes
- Scaling out & scaling in without downtime

---

## 📘 Documentation Included

Each doc in day8/docs/ is a complete chapter:

| File                            | Description                                         |
| ------------------------------- | --------------------------------------------------- |
| **scaling-concepts.md**         | Horizontal vs vertical scaling, service replication |
| **docker-service-discovery.md** | How services automatically resolve using DNS        |
| **nginx-loadbalancing.md**      | Configure upstreams, round robin, proxy rules       |
| **healthchecks-deepdive.md**    | How healthchecks work internally                    |
| **ha-patterns.md**              | Self-healing, redundancy, failover                  |
| **troubleshooting-guide.md**    | Fix unhealthy containers, LB issues                 |

---

## 🧪 Hands-On Labs Included

| Lab                                     | Description                                     |
| --------------------------------------- | ----------------------------------------------- |
| **lab1-scaling-basics.md**              | Scale replicas, inspect IPs, verify uniqueness  |
| **lab2-healthchecks.md**                | Add healthchecks, debug unhealthy containers    |
| **lab3-nginx-loadbalancer.md**          | Build a round-robin NGINX LB for 3 replicas     |
| **lab4-scale-loadbalance-test.md**      | Scale to 5 replicas + traffic distribution test |
| **lab5-high-availability-break-fix.md** | Kill replicas, watch LB adapt & recover         |

Every lab includes commands, expected output, diagrams, and SRE-style explanations.

---

## 🛠 Tools Included

| Tool File                 | Purpose                                          |
| ------------------------- | ------------------------------------------------ |
| **scaling-cheatsheet.md** | All scaling commands in one place                |
| **docker-health.md**      | Debugging healthchecks: logs, exit codes, states |
| **nginx-upstreams.md**    | Reference for upstream parameters                |
| **load-testing.md**       | Simple load-generation loops for traffic testing |
| **debugging-replicas.md** | Fixing inconsistent replicas, DNS issues         |

---

## 🧱 Example Project: Load-Balanced API

Your core example lives in:

```bash
day8/examples/loadbalanced-api/
```

Components:

- Multiple backend API replicas (api-1, api-2, api-3)
- NGINX Load Balancer that routes requests
- Healthcheck endpoint (/health)
- Round robin request distribution

Core files:

- app.py — Flask app returning container hostname
- Dockerfile — lightweight Python container
- docker-compose.yml — scaling + healthchecks
- nginx.conf — LB upstream definition

---

## 🔥 What You Built in This Module

✔ A horizontally scalable backend

Using:

```sh
docker compose up -d --scale api=5
```

✔ A real load balancer

That rotates traffic:
```csharp
Hello from container: 1a2b3c
Hello from container: 9fbc44
Hello from container: 0aef33
...
```

✔ A healthchecked, self-healing microservice

Docker automatically restarts unhealthy replicas.

✔ A break-fix simulation (SRE style)

You literally killed backend nodes and watched the system:

- remove them from rotation
- restart them
- reintegrate them automatically

---

## 🚀 End of Day 8 — You Now Understand:

🔹 Scaling
🔹 Load Balancing
🔹 High Availability
🔹 Healthchecks & Self-Healing
🔹 Real Microservice Patterns
