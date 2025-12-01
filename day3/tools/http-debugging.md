# HTTP Debugging Toolkit

Includes:

### ✔ curl -v  
Full TLS + HTTP debugging.

### ✔ curl -I  
Header-only requests.

### ✔ curl --resolve  
Force IP without DNS.

### ✔ curl -H "Host: ..."  
Virtual host testing.

### ✔ curl -k  
Skip TLS verification (used in labs, not production).

### ✔ curl -o /dev/null -w "%{time_total}\n"  
Latency measurement.

These tools are essential during outages involving:
- Load balancers
- Microservices routing
- TLS certificate issues
- DNS failures
- API 500 / 503 / timeout scenarios  
