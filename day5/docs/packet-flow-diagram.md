# Packet Flow Diagram — How Traffic Moves Inside Docker

This diagram shows full packet flow from container → internet.

---

## 1. High-Level Diagram
```bash
Container
│
├── eth0
│
├── vethXYZ (container end)
│
Host Network Namespace
│
├── vethXYZ@if123 (host end)
│
├── docker0 bridge
│
iptables NAT
│
├── MASQUERADE (SNAT)
│
Host External Interface (eth0)
│
Internet
```

---

## 2. Step-by-Step Flow

1. Container sends packet to Google (e.g., `142.x.x.x`)
2. Packet enters eth0
3. Goes through veth pair
4. Enters docker0 bridge
5. Routed to host interface
6. iptables performs SNAT
7. Packet leaves host to internet
8. Reply comes back
9. DNAT restores container IP
10. Packet delivered back to container

---

## 3. Tools to Debug This

- `tcpdump`
- `iptables -t nat -L -n -v`
- `ip link`
- `ip netns`
- `docker inspect`

---

## 4. Summary

Understanding packet flow is essential for troubleshooting:

- Container cannot reach internet
- Port publishing issues
- NAT problems
- Kubernetes pod networking

