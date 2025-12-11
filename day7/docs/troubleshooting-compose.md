# Troubleshooting Docker Compose

A set of common SRE-level debugging steps for microservices.

---

## ❗ Port Already in Use

```bash
sudo ss -tulnp | grep :8080
```

Stop offender:

```bash
sudo systemctl stop apache2
```


---

## ❗ Reverse Proxy 301/404 Errors

Check:

- Trailing slash in `proxy_pass`
- Upstream services up and healthy
- Correct port mapping

---

## ❗ API Unhealthy

```bash
docker logs api
curl localhost:5001
```

## ❗ DNS Resolution Failures

```bash
docker exec api getent hosts frontend
```

If failed → services on different networks.

---

## ❗ Containers Restarting

```bash
docker compose ps
docker compose logs <service>
```

---

## ❗ Verify Route in Proxy

```bash
docker exec proxy nginx -T | grep api
```

---
