# 🛠 Multi-Network Inspection Tools

### Check all networks

```bash
docker network ls
```
Inspect one network

```bash
docker network inspect <network>
```
Show container ↔ networks

```bash
docker inspect -f "{{json .NetworkSettings.Networks}}" <container> | jq
```

---
