# Reverse Proxy in Docker Compose (NGINX)

A reverse proxy sits in front of the application and routes requests to the correct service.

---

## 📌 Purpose of a Reverse Proxy

- Simplify URLs ( `/api` → backend )
- Serve static content
- Provide TLS termination (HTTPS)
- Load balance multiple API instances
- Hide internal IPs
- Add caching and rate limiting

---

## 🧱 Example Architecture

Client → NGINX → API
→ Frontend


---

## 🛠 Sample Proxy Config

```nginx
server {
    listen 80;

    location /api/ {
        proxy_pass http://api:5001/;
        proxy_set_header Host $host;
        proxy_http_version 1.1;
    }

    location / {
        proxy_pass http://frontend:80/;
    }
}
```

---

## 🚨 Common Mistake: Missing Trailing Slash

Bad:

```bash
proxy_pass http://api:5001;
```

Good:

```bash
proxy_pass http://api:5001/;
```

Without the slash, paths break and become:

```bash
/apiusers instead of /api/users
```

---

## 🔧 Debugging the Proxy

Check logs:

```bash
docker compose logs proxy
```

Test upstreams:

```bash
docker exec proxy curl api:5001
```
