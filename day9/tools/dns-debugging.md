# 🛠 DNS Debugging for Docker Compose

### Check service resolution

```bash
docker exec -it <container> ping api
```

Install DNS tools (Alpine)

```bash
apk add bind-tools
```

Test DNS lookup

```bash
nslookup logger
```

Test HTTP name resolution

```bash
curl http://api:5001

---
