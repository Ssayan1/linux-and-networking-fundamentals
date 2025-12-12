# 🛠 Jaeger Debugging Toolkit

### Check Jaeger container

```bash
docker compose ps jaeger
```

Check Jaeger port exposure

```bash
ss -tulnp | grep 16686
```

View Jaeger logs

```bash
docker compose logs jaeger
```

Test UDP ingestion

```bash
nc -u localhost 6831
```
