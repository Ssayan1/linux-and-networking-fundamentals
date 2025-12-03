# veth Pairs Explained — Docker Networking Internals

veth (virtual Ethernet) pairs are the backbone of Docker container networking.

---

## 1. What Is a veth Pair?

veth pairs behave like a virtual Ethernet cable:

- Whatever goes into one end comes out the other
- Useful for connecting network namespaces

---

## 2. veth Diagram

```bash
[ Container NetNS ] [ Host NetNS ]
┌───────────────┐ ┌───────────────┐
│ eth0 │◀────────────▶│ vethXXXX │
└───────────────┘ └───────────────┘
```

---

## 3. Why Docker Uses veth?

✔ Allows container to have its own network stack  
✔ Clean isolation between containers  
✔ Packets still reach host via docker0 bridge  
✔ Necessary for NAT and routing

---

## 4. Finding veth for a Container

1. Get the container PID:

```bash
docker inspect -f '{{.State.Pid}}' <container>
```
2. Enter the Docker Desktop VM:

```bash
wsl -d docker-desktop
```
3. Find veth pairs:

```bash
ip link
```
4. Match EndpointID from:
```bash
docker inspect <container> | grep EndpointID
```

---

## 5. Lifetime of veth

veth interface is deleted when:

- Container stops
- Network namespace is removed

---

## 6. Summary

veth pairs are the key abstraction that links container namespaces to host networking. Understanding them is essential for debugging Docker and Kubernetes networking issues.

---

