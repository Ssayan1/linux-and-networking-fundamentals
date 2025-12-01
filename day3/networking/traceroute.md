### Command
traceroute google.com

### Purpose
Identify the network path and hops taken to reach a remote destination.

### Key Findings
- ✔ Hop 1: WSL2 NAT Gateway

WSL virtual router (172.X.X.X)
Confirms local virtualization networking is functioning.

- ✔ Hop 2: Home Router

192.XXX.XX.X — healthy.

- ✔ Hop 3–7: ISP internal routing

Private IPs: 10.x, 172.16.x, 192.168.x
ISP backbone nodes
Latency under 10 ms → stable connection.

- ✔ Hop 8–14: Upstream + silent backbone routers

Some backbone nodes do not respond to ICMP → normal.

- ✔ Hop 15–17: Google Global Network

Entered Google via Anycast
Reached Mumbai GGC/Edge → 1e100.net
Final IP: 142.250.182.238
 
- ✔ Latency Stabilized

~45 ms → excellent for India ↔ Google.


### SRE Insight
Traceroute helps locate where packets are dropped or delayed,
but raw hop-by-hop output should never be published publicly.
 
