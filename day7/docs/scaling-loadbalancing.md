# Scaling & Load Balancing

To scale any service:

```bash
docker compose up -d --scale api=5
```

If using Nginx reverse proxy:

- Nginx sees 5 upstream backends
- Distributes traffic automatically

