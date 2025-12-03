# tcpdump for Docker Containers

Use this for packet-level debugging.

---

## 🔹 1. Install tcpdump (inside Docker VM)

```bash
sudo apt update
sudo apt install -y tcpdump
```

---

## 🔹 2. Get Container IP

```bash
docker inspect demo-nginx -f '{{ .NetworkSettings.IPAddress }}'
```

---

## 🔹 3. Capture Traffic on docker0

```bash
sudo tcpdump -i docker0 -nn host <container-ip>
```

---

## 🔹 4. Trigger Traffic

```bash
curl http://<container-ip>
```
Expected packets:
- SYN
- SYN/ACK
- ACK
- GET /
- 200 OK

---

## Summary

tcpdump = best low-level tool for debugging container networking.

