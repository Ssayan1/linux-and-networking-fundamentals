# Docker Compose Basics

Docker Compose allows you to define and run multi-container applications using a single YAML file.  
Instead of manually running individual `docker run` commands, Compose handles:

- Network creation
- Service dependency ordering
- Volume management
- Image building
- Environment variables
- Healthchecks
- Scaling

---

## 🧱 Core Concepts

### **1. Services**
Each container is defined as a “service”. Example:

```yaml
services:
  api:
    build: ./api
  frontend:
    image: nginx
```

### **2. Networks

Compose auto-creates a network named:
<folder>_default

Every service automatically joins this network.

### **3. Volumes

Persistent storage across container restarts.

### **4. Build Context

Images can be built automatically via:
```yaml
build:
```
## 🐳 Compose Lifecycle
Command	Meaning
docker compose up	Create + start all services
docker compose up -d	Run in background
docker compose down	Stop & delete all resources
docker compose logs	View logs
docker compose ps	List running services

---

## 📌 Important Notes

- Services communicate using DNS names equal to service names
  Example: the API service can be reached as http://api:5001

- All services share the same network unless defined otherwise

- Ports are published only for external access (from host)
