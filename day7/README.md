# 🚀 Day 7 — Docker Compose Deep Dive  
### Multi-Service Networking • Reverse Proxy • Service Discovery

This module teaches how real production microservices communicate using Docker Compose.  
You will understand multi-container networking, DNS-based service discovery, load balancing, healthchecks, reverse proxies, and debugging tools.

---

# 📚 Topics Covered

### ✔ Multi-container architecture  
### ✔ Docker Compose networking  
### ✔ Service discovery (DNS inside Docker)  
### ✔ Reverse proxy routing (NGINX → API → Frontend)  
### ✔ Healthchecks & container lifecycle  
### ✔ Debugging HTTP, DNS, Ports, and API failures  
### ✔ Running full microservices locally

---

# 📁 Folder Structure

```bash
day7/
├── README.md
├── docs
│   ├── docker-compose-basics.md
│   ├── healthchecks.md
│   ├── networking-in-compose.md
│   ├── reverse-proxy-deep-dive.md
│   ├── scaling-loadbalancing.md
│   ├── service-communication.md
│   ├── troubleshooting-compose.md
│   └── volumes-bind-mounts.md
├── examples
│   ├── microservices-stack
│   │   ├── api
│   │   │   ├── Dockerfile
│   │   │   └── app.py
│   │   ├── docker-compose.yml
│   │   ├── frontend
│   │   │   ├── Dockerfile
│   │   │   └── index.html
│   │   └── reverse-proxy.conf
│   ├── multi-service
│   │   ├── backend
│   │   │   ├── Dockerfile
│   │   │   └── app.py
│   │   ├── docker-compose.yml
│   │   └── frontend
│   │       ├── Dockerfile
│   │       └── index.html
│   ├── redis-counter
│   │   ├── Dockerfile
│   │   ├── app.py
│   │   ├── docker-compose.yml
│   │   └── requirements.txt
│   └── simple-web
│       ├── app.py
│       └── docker-compose.yml
├── labs
│   ├── lab1-compose-basics.md
│   ├── lab10-compose-debugging.md
│   ├── lab11-build-optimization.md
│   ├── lab12-production-simulation.md
│   ├── lab2-network-debugging.md
│   ├── lab3-volumes-storage.md
│   ├── lab4-healthchecks.md
│   ├── lab5-scaling-loadbalancing.md
│   ├── lab6-production-microservices.md
│   ├── lab7-redis-counter.md
│   ├── lab8-multiservice.md
│   └── lab9-reverse-proxy.md
└── tools
    ├── compose-commands.md
    ├── compose-logs.md
    ├── compose-networking.md
    ├── compose-volumes.md
    └── troubleshooting.md

```


---

# 🏗 Architecture Overview

```
            ┌────────────┐
Client ---> │ NGINX      │ (reverse proxy)
            └─────┬──────┘
                  │ /api → API service
                  │ / → Frontend
        ┌─────────┴───────────┐
        │                     │
  ┌──────────────┐ ┌──────────────┐
  │ Frontend     │ │    API       │
  │ (nginx html) │ │ (Flask/Node) │
  └──────────────┘ └──────────────┘
```

---

# 🔥 Key Learning Objectives

### 1️⃣ Understand how Compose creates networks  
Every `docker compose up` creates:

- One bridge network  
- DNS entries for each service  
- Virtual Ethernet interfaces (veth pairs)  

### 2️⃣ Learn how services communicate  
- `api` resolves `frontend` using DNS inside Docker  
- Reverse proxy routes HTTP to upstream services  
- Ports are published only on proxy

### 3️⃣ Debug containers l  
You learn:  
- traceroute between containers  
- curl to internal services  
- dig inside networks  
- healthcheck debugging  
- reading logs, inspecting IPs  

### 4️⃣ Build real microservices  
A full working stack using:

- Flask API  
- NGINX frontend  
- NGINX reverse proxy  
- Docker Compose networking  

---

# 🧪 Hands-On Labs Included

### **Lab 1 — Run the multi-service Compose stack**  
Build + start + validate architecture.

### **Lab 2 — Networking Observability**  
Inspect networks, bridges, veth pairs, DNS, and routing.

### **Lab 3 — Reverse Proxy Debugging**  
Fix broken NGINX routes (`/api` vs `/api/` issues).

### **Lab 4 — Healthchecks**  
Understand unhealthy → healthy transitions for microservices.

### **Lab 5 — Production Incident Simulation**  
A full troubleshooting scenario involving:  
- port conflicts  
- healthcheck failures  
- wrong upstream routing  
- DNS resolution issues  

---

# 🛠 Tools Used in This Module

- `docker compose`
- `docker network inspect`
- `docker exec`
- `ss -tulnp`
- `curl`, `wget`, `nc`, `dig`
- NGINX reverse proxy  
- Flask / Node.js lightweight API

---

# 🌐 Example Services Included

### ✔ Simple Web App  
Hello World container + Compose

### ✔ Redis Counter  
Flask API + Redis backend + shared network

### ✔ Microservices Stack (Main Project)  
- `/api` → backend API  
- `/` → frontend  
- reverse proxy in front  

The same architecture is used in real production microservice deployments.

---

# 🧠 Troubleshooting Cheatsheet

### ❗ API not responding  

```shell
docker logs microservices-stack-api-1
docker exec api curl localhost:5001
```

### ❗ `/api` returns 301 or 404  
Fix NGINX route:

```shell
location /api/ {
proxy_pass http://api:5001/
;
}
```
### ❗ Port conflict  
Check who is using the port:

```bash
sudo ss -tulnp | grep:8080
```


### ❗ Healthcheck unhealthy  
Inspect:

```bash
docker inspect api | jq '.[0].State.Health'
```


---

# 🎯 Final Outcome



- Build multi-service applications  
- Use Compose to orchestrate microservices  
- Debug networking, routing, and DNS issues  
- Configure NGINX reverse proxies  
- Analyze container health and logs  
- Solve real-world SRE container incidents  



---


