### Command
```bash
ping -c 4 google.com
```

### Output:
```
PING google.com (142.250.xxx.xxx)
64 bytes from ... ttl=118 time=22.3 ms

```
### Observation
- ICMP packets sent successfully
- No packet loss observed
- Latency within normal range

### SRE Insight
Used to verify basic L3 connectivity before deeper debugging.

### Command
```bash
traceroute google.com
```
### Purpose
Identify the network path and hops taken to reach a remote host.

### Observation
- Multiple network hops involved
- Latency increases across upstream networks

### SRE Insight
Traceroute helps locate where packet loss or latency is introduced,
but raw output should not be shared publicly.

### Command
```bash
curl -v https://example.com
```
### Purpose
Test HTTPS connectivity and inspect TLS and HTTP request/response flow.

### Observation
- TLS handshake completed successfully
- Server returned HTTP 200 response

### SRE Insight
`curl -v` helps debug SSL/TLS issues, redirects, and headers, but verbose output
should not be shared publicly.

### Command
```
curl --resolve example.com:443:<IP> https://example.com
```
### Purpose
Force an HTTPS request to a specific IP while preserving the Host header.

### Use case
- Test load balancer routing
- Bypass DNS during debugging
- Validate TLS SNI configuration

### SRE Insight
Useful when DNS is suspected to be incorrect, but should be used carefully.

### Command
```bash
curl ifconfig.me
```
### Purpose
Fetch the machine’s public IP address from an external service.

### SRE Insight
Useful for debugging NAT, firewall, or outbound connectivity,
but public IPs should never be shared publicly.
