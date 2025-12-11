# Service Discovery in Docker Compose

Docker includes a built-in DNS server that runs on every user-defined network.

---

## 📌 Rules for Service Discovery

### 1. Every service name becomes a DNS hostname

Example:
services:
api:
frontend:
redis:

Can be reached at:

```bash
http://api

http://frontend

http://redis
```


### 2. DNS is automatic — no config needed  
Docker manages DNS entries internally.

### 3. Containers resolve names via `/etc/resolv.conf`  
Typically pointing to Docker's internal DNS server (e.g. `127.0.0.11`)

---

## 🔍 Testing DNS Inside the Network

```bash
docker exec api getent hosts frontend
docker exec frontend getent hosts api
```


---

## 🌐 Multiple Networks

A service only resolves services on the **same network**.

---

