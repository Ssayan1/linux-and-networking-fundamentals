# Inspecting Docker Networks

This lab teaches you how to list networks, inspect them, understand their subnets, gateways, and connected containers.

---

## 🎯 Objectives

- Understand Docker default networks
- Inspect the default `bridge` network
- Explore your custom network (`sre-net`)
- Understand container IP allocation

---

## 🔧 Step 1 — List All Networks

```bash
docker network ls
```
Expected networks:
- bridge
- host
- none
- sre-net (user-created)

---

## 🔧 Step 2 — Inspect the Default Bridge

```bash
docker network inspect bridge
```
Focus on:
- Subnet: 172.17.0.0/16
- Gateway: 172.17.0.1
- Connected containers
- EndpointIDs
- MAC addresses

---

## 🔧 Step 3 — Inspect Your Custom Network

```bash
docker network inspect sre-net
```
User-defined networks provide:

✔ Container DNS
✔ Name-to-IP resolution
✔ Better isolation
✔ Clean multi-service networking

---

## 🔧 Step 4 — Run Two Containers on sre-net

```bash
docker run -d --name web1 --network sre-net nginx
docker run -d --name web2 --network sre-net nginx
```
Now test DNS:
```bash
docker exec -it web1 ping -c 2 web2
```
✔ If it works → Docker DNS is functioning.

---

## 🧠 Summary

- Default bridge (docker0) is for basic standalone containers.
- User-defined bridges offer service discovery + isolation.
- Networks help you build production-like microservice topologies.
