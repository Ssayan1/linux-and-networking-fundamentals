# Docker Networking Basics — Day 5

This document explains how Docker creates isolated network environments using namespaces, virtual Ethernet devices, and bridges.

---

## 1. What Happens When Docker Starts a Container?

When you run:

```bash
docker run -d nginx
```
Docker automatically sets up the following:
1. A network namespace for the container
2. A new interface (eth0) inside that namespace
3. A veth pair (virtual Ethernet cable)
4. The host side of the veth is attached to docker0 bridge
5. The container receives an IP (e.g., 172.17.x.x)
6. iptables rules are added for NAT / MASQUERADE
7. Docker DNS is configured inside /etc/resolv.conf

## 2. Architecture Diagram (Bridge Mode)

```bash
Container Namespace
 └── eth0 ──┐
            │ (veth pair)
Host NS     │
 └── vethXYZ ── docker0 bridge ── iptables NAT ── Internet

```

## 3. Default docker0 Network

- Subnet: 172.17.0.0/16
- Gateway: 172.17.0.1
- Driver: bridge
- NAT enabled
- All containers connect here by default

## 4 Custom User-Defined Bridge

You created:
```bash
docker network create sre-net
```
User-defined bridges support:

- Container DNS
- Hostname resolution
- Better isolation
- Better for microservices

## 5. Packet Flow Summary

1. Container sends packet via eth0
2. Packet goes through veth into docker0
3. NAT translates 172.17.x.x → host IP
4. Response is de-NATed and delivered back to container

## 6. Why Docker Uses Network Namespaces?

Namespaces allow:

- Isolation of routing tables
- Isolation of interfaces
- Separate ARP tables
- Separate iptables
Each container behaves like a tiny isolated Linux node.

## 7. Why Docker Uses veth Pairs?

veth devices behave like a network cable:

- One end in the container
- One end in the host

Both ends mirror traffic

## 8. Why Docker Uses Bridge Networking?

- Easy to configure
- NAT allows private IP range
- All containers can talk through docker0
- Host can reach containers

## 9. Summary

Docker networking consists of:

- Network namespaces
- veth pair
- docker0 bridge
- IPAM
- NAT via iptables
- Optional user-defined networks
