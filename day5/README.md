# Day 5 — Docker Networking Internals 
This module teaches you **exactly how Docker networking works internally**:

- bridge networks  
- custom networks  
- veth pairs  
- NAT & iptables  
- DNS inside containers  
- debugging with tcpdump  
- entering namespaces  

You’ll learn real SRE-level debugging: *“Why can’t a container reach the internet?”*  
**Every concept has labs, diagrams, and tools.**

---

# 🚀 Topics Covered

```bash
| Topic | Description |
|-------|------------|
| Docker Network Types | bridge, host, none, user-defined |
| Container Interfaces | eth0 inside container, veth on host |
| docker0 Bridge | how traffic flows |
| NAT | MASQUERADE, DNAT, SNAT |
| DNS | internal Docker DNS |
| tcpdump | packet capture from docker0 |
| iptables | NAT debugging |
| Network Namespace | entering via nsenter |
```
---

# 🧩 Architecture Overview

```bash
+---------------------+
|   Host Network      |
|                     |
|  +--------------+   |
Internet <--->| docker0
|---+--- vethXXXX (host)
| +--------------+ |
+---------|-----------+
|
| veth pair
|
+---------------------+
| Container (eth0) |
| 172.17.0.X/16 |
| |
| nginx / app |
+---------------------+
```

Traffic path:

1. Container sends packets → eth0  
2. eth0 → vethXXXX → docker0  
3. docker0 → iptables → NAT → internet  

---

# 🛠 Key Commands (Cheat Sheet)

### 🔹 List networks
```bash
docker network ls
```

### 🔹 Inspect a network

```bash
docker network inspect bridge
```

### 🔹 Create custom network

```bash
docker network create sre-net
```

### 🔹 Run containers in it

```bash
docker run -d --name web --network sre-net nginx
```

### 🔹 Exec into container

```bash
docker exec -it web bash
```

### 🔹 Check IP inside container

```bash
ip a
hostname -i
```

### 🔹 Capture packets (VM)

```bash
tcpdump -i docker0 -nn
```

---

## 🔍 Network Debugging Scenarios

### Scenario 1 — Container has no internet

Checklist:

1. Is DNS working?
   → cat /etc/resolv.conf

2. Is NAT working?
   → iptables -t nat -L -n -v

3. Can the host reach the internet?
   → curl https://google.com

4. Does container's veth exist?
   → ip link | grep veth

---

### Scenario 2 — Two containers cannot talk

Checklist:

1. Are they in the same network?
   → docker inspect <container> | grep Network

2. Use container-to-container DNS
   → docker exec web1 ping web2

3. Verify firewall / iptables (if custom)

---

### Scenario 3 — Port not accessible on host

Checklist:

1. Did you expose port?
   → docker run -p 8080:80 nginx

2. Check DNAT rules
   → iptables -t nat -L DOCKER

3. Is container listening?
   → docker exec web ss -tlnp

4. Host port conflict?
   → ss -tlnp | grep 8080

---

## 🧪 Labs Included

Your labs are located in:

```bash
day5/labs/
```
They include:

- Lab 1 — Bridge Network Deep Dive
- Lab 2 — Custom Networks + Container DNS
- Lab 3 — NAT & Packet Flow (tcpdump)
- Lab 4 — Debugging Broken Networking
- Lab 5 — Namespace Exploration

Each lab is SRE-style: “You are on-call. Fix the issue.”

---

## 🧰 Tools Included

Located under:

```bash
day5/tools/
```

Tools:

- docker-networks.md
- docker-veth.md
- docker-nat.md
- docker-tcpdump.md
- docker-dns.md

These are copy-paste ready references you can use in production.

---

## 📦 Scripts Included

Located under:
```bash
day5/scripts/
```

Scripts:

- container-net-debug.sh
- capture-docker0.sh
- nsenter-container.sh

## 🎯 Today's Learning

✔ How containers get IP addresses
✔ What docker0 bridge actually does
✔ How NAT makes internet work inside containers
✔ How to trace packets leaving containers
✔ How to debug DNS issues inside containers
✔ How to enter network namespaces (real Linux only)
✔ How to inspect veth pairs and link them to containers
