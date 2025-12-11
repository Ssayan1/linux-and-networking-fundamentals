# 🧪 Lab 3 — Build a Load Balancer with NGINX Upstreams

Learn how NGINX distributes traffic across backend replicas.

---

# 🎯 Objectives
- Configure upstream block
- Forward traffic to container replicas
- Understand round-robin load balancing

---

# 📁 Step 1 — Open `nginx.conf`

```nginx
events {}
http {
    upstream backend {
        server loadbalanced-api-api-1:5001;
        server loadbalanced-api-api-2:5001;
        server loadbalanced-api-api-3:5001;
    }

    server {
        listen 80;

        location / {
            proxy_pass http://backend;
        }
    }
}

```

---

# 🚀 Step 2 — Start the load balancer

```sh
docker compose up -d
```

---

# 🧪 Step 3 — Curl via NGINX

```sh
curl localhost:5001
```
Expected sequence (round robin):

```csharp
Hello from container: abc123
Hello from container: dfe233
Hello from container: 99ac77
Hello from container: abc123
```

---

# 🛠 Step 4 — Debug LB

View logs:

```sh
docker compose logs lb
```

Common errors:

- Missing }
- Wrong container names
- Port mismatch

🎉 Lab Complete!
 created a functioning load balancer.

yaml
Copy code
