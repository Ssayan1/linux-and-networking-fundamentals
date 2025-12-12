# ✅ Connectivity Checklist

### Container-to-container tests

```bash
docker exec -it frontend sh
curl http://api:5001
```

Test logger → API

```bash
docker exec -it logger sh
curl http://api:5001
```

Test tracing

```bash
curl localhost:8000/log
```

Verify networks

```bash
docker network inspect <network>
```
