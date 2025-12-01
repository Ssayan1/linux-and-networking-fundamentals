# Network Path Analysis — `traceroute google.com`

## Command
```
traceroute google.com
```

## Summary (Your Actual Output)

### ✔ Hop 1 — WSL NAT gateway  
`172.29.160.1`

### ✔ Hop 2 — Home Router  
`192.168.29.1`

### ✔ Hops 3–7 — ISP internal backbone  
Private IPs:
- 10.x.x.x
- 172.16.x.x
- 192.168.x.x

### ✔ Hop 8–14 — ISP → Peering → silent backbone routers  
No ICMP replies → normal.

### ✔ Hop 15–17 — Google Global Network  
`172.253.67.86`  
`142.251.76.192`  
`bom07s29-in-f14.1e100.net` (final)

Google’s Mumbai data center.

---
### Key Takeways
- Confirms ISPs use private IP backbone routing  
- Shows Google Anycast + regional load balancing  
- Packet loss in traceroute ≠ real packet loss  
- Helps diagnose routing loops, asymmetric paths, peering issues
