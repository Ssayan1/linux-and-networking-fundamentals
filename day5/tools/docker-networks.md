# Docker Networks — Quick Reference

This guide explains all Docker network types and essential commands.

---

## 🔹 1. List All Networks

```bash
docker network ls
```
Output includes:

- bridge(default)
- host
- none
- Your custom networks (example: sre-net)

---

## 🔹 2. Inspect Any Network

```bash
docker network inspect <network-name>
```
Important feilds:

- Subnet
- Gateway
- Containers
- MAC addresses
- EndpointIDs

---

## 🔹 3. Create a Custom Network

```bash
docker network create sre-net
```
Benefits:
- Container DNS
- Better isolation
- Service discovery

---

## 🔹 4. Run Containers on This Network

```bash
docker run -d --name web --network sre-net nginx
```

---

## 🔹 5. Connectivity Test

```bash
docker exec -it web ping -c 2 google.com
```
For internal DNS:
```bash
docker exec web ping web2
```

---

## Summary

Use custom networks for real production microservices.
