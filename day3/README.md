# Day 3 — SRE Networking & HTTP Deep Dive

This day focuses on **real-world debugging**, the exact skills used by SREs during on-call and production incidents.

---

# 🔥 Topics Covered

### ✅ DNS
- dig A / AAAA / NS / +trace
- Root → TLD → Authoritative flow
- DNS override debugging (`curl --resolve`)

### ✅ HTTP & TLS
- curl verbose debugging
- TLS handshake breakdown
- HTTP/2, ALPN, cert validation
- HTTPS redirect analysis

### ✅ Linux Networking Tools
- ss (ports)
- ip r (routing table)
- traceroute (path analysis)

---

# 📁 Folder Structure

```
day3/
├── networking/
├── tools/
└── labs/
└── scripts/
```

Each folder contains production-grade SRE notes and real outputs captured from WSL.

---

# 🎯 Learning Outcome


- Diagnose DNS issues end-to-end  
- Follow traffic across root, TLD, and authoritative servers  
- Debug TLS certificate problems  
- Trace network paths across ISP → Google  
- Use curl for HTTP, HTTPS, SNI, ALPN, and cert inspection  

---
