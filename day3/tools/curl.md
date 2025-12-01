### Command
curl -v https://google.com

### Purpose
Debug HTTPS connectivity and inspect TLS and HTTP request/response flow.

### SRE Insight
`curl -v` is useful for diagnosing TLS failures, redirects, or header issues,
but verbose output should never be shared publicly.

--- ## Key Observations

### ✔ DNS resolution  
IPv4 + IPv6 both resolved.

### ✔ TCP handshake  
Connection established to 172.217.26.14.

### ✔ TLS handshake  
TLS 1.3  
AES-256-GCM  
X25519  
Certificate valid  
Issuer: Google Trust Services

### ✔ ALPN Negotiation  
Server accepts HTTP/2.

### ✔ HTTP Response  
`HTTP/2 301` → redirect to https://www.google.com

---

### Key Takeways

- Used in debugging API failures  
- Helps validate TLS certificates  
- Identifies redirects, loops, misconfigurations  
- Shows protocol negotiation (h2 vs h1.1)  
