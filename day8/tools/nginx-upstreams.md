# 🌐 NGINX Upstreams Guide for Load Balancing (Day 8)

This file explains how NGINX load balancing works for multiple backend replicas.

---

# 🔹 Basic Upstream Block

```bash

upstream backend {
server api-1:5001;
server api-2:5001;
server api-3:5001;
}
```

NGINX will automatically perform **round-robin** balancing.

---

# 🔹 Proxy Pass Configuration

```nginx
server {
     listen 80;
     location / {
     proxy_pass http://backend;
            }
}
```

---

# 🔹 Useful Upstream Options

### ✔ Control Weights

```shell
server api-1:5001 weight=3;
server api-2:5001 weight=1;
```

### ✔ Slow Start (production)

```shell
server api-1:5001 slow_start=30s;
```

### ✔ Fail Timeout

```shell
server api-1:5001 max_fails=3 fail_timeout=10s;
```

---

# 🔹 How NGINX Detects Replica Failure

NGINX marks a server as DOWN if:
- it fails connections repeatedly  
- healthchecks (if configured) fail  
- the container is not reachable  

---

# 🔹 Testing Load Balancing

```csharp
for i in {1..20}; do curl -s localhost:5001; echo; done
```
sort by frequency:

```csharp
for i in {1..50}; do curl -s localhost:5001; done | sort | uniq -c
```

---

# 🔹 Recommended Settings

```yaml
proxy_http_version 1.1;
proxy_set_header Connection "";
proxy_read_timeout 120s;
proxy_connect_timeout 5s;
```

---

# 🔹 Summary

| Feature | Purpose |
|---------|---------|
| `upstream {}` | pool of backend nodes |
| round robin | default load balancing method |
| `max_fails` | remove unhealthy nodes |
| `weight` | control traffic distribution |
| `slow_start` | avoid spike after replica restart |

