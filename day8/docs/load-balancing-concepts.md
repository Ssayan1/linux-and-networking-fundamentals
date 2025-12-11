# ⚖ Load Balancing Concepts — Distributing Traffic Across Containers

Load balancing ensures fair distribution of traffic across multiple backend replicas.

In Day 8, we implement an NGINX reverse proxy as a load balancer.

---

## 🧱 Why Load Balancers Are Required

If you scale containers:

```
api-1
api-2
api-3
```
Clients must NOT directly call each container.

Instead:

```yaml
Client → Load Balancer → Backends
```

---

## 🌍 Types of Load Balancing

### 1️⃣ Round Robin (default)
Sends traffic to backends sequentially:

```yaml
1 → api-1
2 → api-2
3 → api-3
4 → back to api-1
```

### 2️⃣ Least Connections
Sends requests to the instance with the least active connections.

### 3️⃣ IP Hash
Same client → always same backend (session persistence).

---

## 📦 Load Balancing with NGINX

Example upstream config:

```nginx
upstream backend {
    server api-1:5001;
    server api-2:5001;
    server api-3:5001;
}

server {
    listen 80;
    location / {
        proxy_pass http://backend;
    }
}
```

---

## 🛠 How Load Balancers Detect Unhealthy Servers

NGINX does NOT automatically remove unhealthy backends unless you configure:
  - max_fails
  - fail_timeout
  - Active health checks (Premium only)

Hence Docker healthchecks + restart policy are required.

---

## 👀 Debugging Load Balancing

Tools:

- docker logs
- NGINX $upstream_addr log variable
- tcpdump
- Request counters inside the app

Load balancing is a core component of all modern distributed systems.

---
