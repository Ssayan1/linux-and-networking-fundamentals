# Lab 3: Networking Basics

## Commands Used
```bash
ip a
ip r
dig google.com
ping -c 4 google.com
ss -tulnp
curl -I https://example.com
```

## Command: ip a

Output:
--------------------------------------------------------------------
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet 10.255.255.254/32 brd 10.255.255.254 scope global lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever

2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:15:5d:00:a4:c5 brd ff:ff:ff:ff:ff:ff
    inet 172.29.171.134/20 brd 172.29.175.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::215:5dff:fe00:a4c5/64 scope link
       valid_lft forever preferred_lft forever
--------------------------------------------------------------------

## Learning:
- `lo` (loopback) is used for internal communication inside the system (127.0.0.1).
- `eth0` is the main WSL network interface with IP `172.29.x.x`.
- Shows IPv4/IPv6 addresses, MTU, interface flags, and state (UP/DOWN).
- Used to confirm IP assignment, check active interfaces, and debug networking issues.
- Common SRE usage: verifying connectivity paths, discovering routing issues, and validating interface health.

## Command: ip r

Output:
--------------------------------------------------------------------
default via 172.29.160.1 dev eth0 proto kernel
172.29.160.0/20 dev eth0 proto kernel scope link src 172.29.171.134
--------------------------------------------------------------------

## Learning:
- Shows the current routing table (how your system decides where to send packets).
- `default via 172.29.160.1` means all traffic outside your local network goes to the gateway (router) at 172.29.160.1.
- `172.29.160.0/20 dev eth0` means traffic to this subnet stays inside the same network (`eth0` interface).
- Useful for debugging connectivity issues, especially when pinging outside networks fails.
- As an SRE, you use this to confirm if default gateway, routes, or subnets are configured correctly.

## Command: dig google.com

Output:
--------------------------------------------------------------------
; <<>> DiG 9.18.39-0ubuntu0.24.04.2-Ubuntu <<>> google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 57083
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1280
;; QUESTION SECTION:
;google.com.                    IN      A

;; ANSWER SECTION:
google.com.             241     IN      A       142.250.183.78

;; Query time: 30 msec
;; SERVER: 10.255.255.254#53(10.255.255.254) (UDP)
;; WHEN: Fri Nov 28 03:20:26 UTC 2025
;; MSG SIZE  rcvd: 55
--------------------------------------------------------------------

## Learning:
- `dig` performs a DNS lookup and shows how a domain name resolves to an IP.
- `google.com IN A 142.250.183.78` means the DNS A-record returned Google’s IPv4 address.
- `status: NOERROR` means DNS resolution succeeded without issues.
- `SERVER: 10.255.255.254` shows the DNS server your WSL system is using.
- `Query time: 30 msec` helps measure DNS performance.
- SREs use `dig` to debug DNS issues (slow resolution, wrong DNS server, incorrect DNS records).

## Command: ping -c 4 google.com

Output:
--------------------------------------------------------------------
PING google.com (142.250.183.78) 56(84) bytes of data.
64 bytes from bom12s12-in-f14.1e100.net (142.250.183.78): icmp_seq=1 ttl=110 time=40.3 ms
64 bytes from bom12s12-in-f14.1e100.net (142.250.183.78): icmp_seq=2 ttl=110 time=80.7 ms
64 bytes from bom12s12-in-f14.1e100.net (142.250.183.78): icmp_seq=3 ttl=110 time=47.2 ms
64 bytes from bom12s12-in-f14.1e100.net (142.250.183.78): icmp_seq=4 ttl=110 time=60.4 ms

--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3285ms
rtt min/avg/max/mdev = 40.280/57.138/80.681/15.393 ms
--------------------------------------------------------------------

## Learning:
- `ping` tests network connectivity and measures latency to a host using ICMP packets.
- All 4 packets were received → the host is reachable with **0% packet loss** (healthy network path).
- `time=40–80 ms` shows the round-trip latency; `avg=57.138 ms` indicates typical delay to Google.
- `ttl=110` reveals how many hops remain; lower TTL means farther distance or more routers.
- SREs use `ping` to diagnose reachability, packet loss, jitter, and general network health.

## Command: ss -tulnp

Output:
--------------------------------------------------------------------
Netid State  Recv-Q Send-Q  Local Address:Port        Peer Address:Port      Process
udp   UNCONN 0      0          127.0.0.54:53              0.0.0.0:*
udp   UNCONN 0      0       127.0.0.53%lo:53              0.0.0.0:*
udp   UNCONN 0      0      10.255.255.254:53              0.0.0.0:*
udp   UNCONN 0      0           127.0.0.1:323             0.0.0.0:*
udp   UNCONN 0      0               [::1]:323                [::]:*

tcp   LISTEN 0      1000   10.255.255.254:53              0.0.0.0:*
tcp   LISTEN 0      4096    127.0.0.53%lo:53              0.0.0.0:*
tcp   LISTEN 0      128           0.0.0.0:44323           0.0.0.0:*
tcp   LISTEN 0      128           0.0.0.0:44322           0.0.0.0:*
tcp   LISTEN 0      5             0.0.0.0:44321           0.0.0.0:*
tcp   LISTEN 0      4096       127.0.0.54:53              0.0.0.0:*
tcp   LISTEN 0      511           0.0.0.0:80              0.0.0.0:*
tcp   LISTEN 0      5           127.0.0.1:61209           0.0.0.0:*
tcp   LISTEN 0      5             0.0.0.0:4330            0.0.0.0:*
tcp   LISTEN 0      511                 *:8080                 *:*
tcp   LISTEN 0      128              [::]:44323              [::]:*
tcp   LISTEN 0      128              [::]:44322              [::]:*
tcp   LISTEN 0      5                [::]:44321              [::]:*
tcp   LISTEN 0      511              [::]:80                 [::]:*
tcp   LISTEN 0      5                [::]:4330               [::]:*
--------------------------------------------------------------------

## Learning:
- `ss -tulnp` shows all active listening ports and the protocols (TCP/UDP) in use.
- Ports like `53` indicate DNS listeners, `80` indicates an HTTP service, and `8080` is a common app port.
- IPs like `127.0.0.1:*` mean the service is only listening locally; `0.0.0.0:*` means it’s open on all interfaces.
- Helps identify which services are running and whether something unexpected is listening (very important for security).
- As an SRE, this command is crucial for debugging network issues, service binding, port conflicts, and verifying app deployments.

## Command: curl -I https://example.com

Output:
--------------------------------------------------------------------
HTTP/2 200
content-type: text/html
etag: "bc2473a18e003bdb249eba5ce893033f:1760028122.592274"
last-modified: Thu, 09 Oct 2025 16:42:02 GMT
cache-control: max-age=86000
date: Fri, 28 Nov 2025 03:24:44 GMT
alt-svc: h3=":443"; ma=93600
--------------------------------------------------------------------

## Learning:
- `curl -I` fetches only the HTTP headers, allowing you to inspect the server response without downloading content.
- `HTTP/2 200` means the server successfully responded over HTTP/2 (status 200 OK).
- `content-type: text/html` shows the MIME type returned by the server.
- `etag` and `last-modified` help with caching; they let clients know if a page has changed.
- `cache-control: max-age=86000` tells browsers how long to cache the response.
- `alt-

## What I Learned
```bash
- DNS lookup
- Routing table basics
- Checking open ports
- HTTP headers and response codes
```

