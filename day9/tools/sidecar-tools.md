# 🛠 Sidecar Debugging Tools

### Show logger output

```bash
docker compose logs logger --tail=100
```

Test API reachability from logger

```bash
docker exec -it logger sh
curl http://api:5001
```

Trigger sidecar manually

```bash
curl localhost:8000/log
```

---
