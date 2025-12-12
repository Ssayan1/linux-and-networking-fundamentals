# 🔎 Docker Service Discovery — How Containers Find Each Other

Docker Compose has a built-in DNS resolver that maps service names → container IP addresses.

---

## 🧠 How It Works

Every container in a Compose network receives:

- Its own hostname  
- A `/etc/hosts` entry  
- DNS record resolving service name → IP

Example:

```bash
ping api
PING api (172.20.0.3) 56(84) bytes of data.
```

---

## 🏷 Service Name = DNS Name

Compose automatically creates DNS entries:

| Service | Resolves To |
|---------|-------------|
| api | 172.x.x.x |
| frontend | 172.x.x.x |
| logger | 172.x.x.x |
| jaeger | 172.x.x.x |

Inside containers:

```bash
curl http://api:5001
works without knowing the IP.
```

---

## 🚧 Multi-Network Special Note
A service is discoverable only to other services on the same network.

Example:

- frontend ↔ api : YES (both in frontend_net)
- logger ↔ api : YES (both in backend_net)
- frontend ↔ logger : ❌ NO (not on same network)
- frontend ↔ jaeger : ❌ NO

This isolation is intentional and improves security.

