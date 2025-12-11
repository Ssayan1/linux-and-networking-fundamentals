# 🧩 NGINX Upstreams — Configuring Backends for Load Balancing

NGINX uses an `upstream` block to define backend servers that receive traffic.

---

## 🧱 Basic Example

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

## ⚙ Advanced Options
🔹 Weighting servers

```nginx
upstream backend {
    server api-1:5001 weight=3;
    server api-2:5001 weight=1;
}
```

Meaning:
- api-1 receives more traffic (3x)

🔹 Least Connections

```nginx
upstream backend {
    least_conn;
    server api-1:5001;
    server api-2:5001;
}
```
🔹 IP Hash

```nginx
upstream backend {
    ip_hash;
    server api-1:5001;
    server api-2:5001;
}
```

Useful for:

- Session affinity
- Shopping carts
- User profiles

---

## 🧪 Health Checking (Open Source Limitations)

NGINX OSS supports:

- passive health checks (fail detection)
- max_fails and fail_timeout

Example:

```nginx
server api-1:5001 max_fails=3 fail_timeout=10s;
```

If 3 requests fail → temporarily removed.

---

## 📌 Recommended Settings for Docker Compose

```nginx
resolver 127.0.0.11 valid=5s;
proxy_http_version 1.1;
proxy_set_header Connection "";
proxy_set_header Host $host;
```
NGINX upstreams are the foundation of load balancing for microservices.


