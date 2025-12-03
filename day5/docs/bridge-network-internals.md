# Bridge Network Internals — How docker0 Really Works

This document explains the internals of the docker0 bridge and how containers communicate through it.

---

## 1. What Is docker0?

docker0 is a **Linux bridge** created automatically by Docker.

It behaves like a simple virtual switch:

- Forwards packets between veth interfaces
- Maintains a MAC address table (FDB)
- Handles broadcast and ARP
- Acts as subnet gateway

---

## 2. docker0 Diagram

```bash
  ┌──────────────┐
veth0──│ │
│ │
veth1──│ docker0 │── host network
│ (virtual SW) │
veth2──│ │
└──────────────┘
```

---

## 3. docker0 Functions

### ✔ L2 Switching  
Moves Ethernet frames between containers.

### ✔ Acts as Gateway  
Every packet goes through the bridge IP (e.g., `172.17.0.1`).

### ✔ Handles ARP  
Containers ARP for each other’s MAC.

### ✔ Enables NAT  
Without docker0, Docker cannot do NAT.

---

## 4. Inspecting docker0

```bash
ip addr show docker0
bridge link
bridge fdb show
```

## 5. How docker0 Connects Containers

When Docker creates a container:

1. Create veth pair
2. Attach one end to docker0
3. Put the other end inside container namespace
4. Assign IP via internal DHCP

## 6. docker0 Limitations

- Cannot span multiple hosts
- Not encrypted
- Not suitable for production multi-server clusters
- No service discovery by default

Kubernetes solves these limitations using CNI plugins like Calico, Flannel, Cilium.

## 7. Summary

docker0 is a simple, effective, local-only network switch used for container networking. Understanding docker0 helps you understand Kubernetes pod networking.
