# Lab 9 — Build a Real Microservices Proxy System


## 🎯 Objective

Learn how NGINX reverse proxy routes traffic inside Docker networks.

## 🧱 System Architecture

```
client → proxy → (frontend, api)
```

🧪 Steps

1️⃣ Start the system

```bash
docker compose up -d --build
```

2️⃣ Test directly

```bash
curl http://localhost:5001     # API
curl http://localhost:8080     # Frontend
```

3️⃣ Test via proxy

```bash
curl http://localhost/api/
```

Expected output:

```bash
Backend API is working!
```


## 🐞 Troubleshooting

Fix 301 redirects

Use:

```nginx
location /api/ {
    proxy_pass http://api:5001/;
}
```

Use trailing slash in both:

```bash
/api/ → http://api:5001/
```
