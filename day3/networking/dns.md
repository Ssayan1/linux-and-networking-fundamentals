## DNS Resolution Test

### Command
```bash
dig google.com
```
### Result
- DNS resolution succeeded
- A records returned
- TTL approximately 300 seconds

### SRE Insight
If this command fails, DNS resolution is the issue, not application networking.

### Command
```bash
dig +trace google.com
```
### What it does
Performs iterative DNS resolution by querying root servers,
then TLD servers, and finally authoritative name servers.

### Observation
- Root → TLD → authoritative flow confirmed
- Final A records returned from authoritative servers

### SRE Insight
Useful for debugging DNS failures when recursive resolvers
hide where resolution breaks.

### Command
```bash
dig google.com A
```
### Observation
- Successfully returned IPv4 A records
- Confirms DNS resolution for google.com

### SRE Insight
Used to verify DNS resolution when connectivity issues are suspected.

### Command
```bash
dig google.com AAAA
```
### Observation
- IPv6 AAAA records returned
- Confirms IPv6 DNS support

### SRE Insight
If IPv4 works but IPv6 fails, dual-stack networking issues may exist.

### Command
```bash
dig google.com NS
```
### Observation
- Multiple authoritative name servers returned
- Ensures DNS high availability and redundancy

### SRE Insight
NS records define which servers are authoritative.
Misconfigured NS records can cause global outages.

### Command
```bash
dig gmail.com MX
```
### Observation
- Multiple MX records returned
- Each record has a priority value
- Lower priority number = higher preference

### SRE Insight
MX records define how email is routed.
Incorrect MX configuration can cause email delivery failures.

- NS records = Define authoritative DNS servers for a domain
- A record   = Maps hostname to IPv4 address
- AAAA record= Maps hostname to IPv6 address
- MX record  = Defines mail servers and routing priority
- DNS trace  = Shows step-by-step DNS resolution path (root → TLD → authoritative)
