# Networking in Docker Compose

Each project gets its own network:
myproject_default

Services communicate over:
- Internal IPs
- DNS names
- Virtual Ethernet pairs

# Networking in Docker Compose

Every Compose stack automatically creates:

### ✔ A dedicated bridge network  
### ✔ DNS-based service discovery  
### ✔ Virtual Ethernet (veth) pairs  
### ✔ NAT routing for outbound traffic

---

## 🧠 How Networking Works

When Compose starts:

```yaml
 docker compose up
```

Docker creates:

Network: myapp_default

Every service attaches to this bridge and receives:

- Its own virtual NIC (`eth0`)
- A private IP (e.g., `172.19.0.2`)
- A DNS entry (`api`, `frontend`, `db`)

---

## 🧪 Inspecting the Network

```bash
docker network inspect myapp_default
```

shows:

- IP ranges  
- Connected containers  
- MAC addresses  
- DNS names  

---

## 💬 Container-to-container Communication

Containers communicate using **service names**, never IPs.

Example:

```
curl http://api:5001
```


---

## 🧱 Ports vs Internal Networking

Internal communication **does not** need port publication.

| Port Mapping | Purpose |
|--------------|---------|
| `5001:5001` | Accessible from laptop |
| Internal `api:5001` | Accessible only inside the Compose network |

---

## 🗺 Traffic Flow Diagram

Host Laptop -> nginx (reverse proxy)
-> api:5001
-> frontend:80

---


