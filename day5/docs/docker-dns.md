# Docker DNS — How Containers Resolve Names

Docker provides internal DNS to containers for:

- Service discovery
- Name resolution
- Custom bridge networks

---

## 1. Where DNS Configuration Lives?

Inside container:

```bash
cat /etc/resolv.conf
```
Typically points to something like:
```bash
nameserver 192.168.65.7
```
This is a Docker-managed DNS server.

---

## 2. What Docker DNS Provides

✔ Container name → IP

Inside a custom bridge network:
```nginx
ping web
ping db
```
✔ Round-robin load balancing

Multiple containers with same name in Compose.

✔ Fallback to host DNS

If container name not found, queries go to host.

---

## 3. Why Default Bridge Lacks DNS?

docker0 does not provide container name resolution.

User-defined networks like sre-net DO.

---

## 4. Debug DNS

Install tools:
```bash
apt install -y dnsutils
nslookup google.com
dig web A
```

---

## 5. Summary

Docker provides built-in DNS capabilities to user-defined networks. This is the foundation of Kubernetes kube-dns/CoreDNS.

