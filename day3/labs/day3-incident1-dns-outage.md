# 🛑 Incident 1: DNS Outage

## 📌 Incident Summary
Users were unable to access external websites using domain names.
Direct IP connectivity remained functional, indicating a DNS-related failure.

---

## 🔍 Symptoms
- `ping google.com` → ❌ failed  
- `curl https://google.com` → ❌ failed  
- `ping 8.8.8.8` → ✅ succeeded  
- Browser error: `DNS_PROBE_FINISHED_BAD_CONFIG`

These symptoms indicate that network connectivity was available, but DNS name resolution was failing.

---

## 🧠 Root Cause
The incident was caused by a **DNS resolver misconfiguration or failure** on the client/system.

Likely contributing factors:
- Incorrect DNS server configured in `/etc/resolv.conf`
- Local DNS resolver (`systemd-resolved`) stopped or unhealthy
- DNS traffic blocked on UDP/TCP port 53
- VPN or DHCP overriding DNS settings with invalid resolvers

Since connectivity to a public IP address worked, routing and general network connectivity were ruled out.

---

## 🔎 Detection & Diagnosis

### Step 1: Confirm network connectivity
```bash
ping 8.8.8.8
```
✅ Successful response confirmed basic network connectivity.

### Step 2: Validate DNS resolution failure
```bash
ping google.com
```
❌ Failed, indicating name resolution issues.

### Step 3: Direct DNS query
```bash
dig google.com
```
❌ No valid response, confirming DNS resolution failure.

### Step 4: Inspect DNS configuration
```bash
cat /etc/resolve.conf
```
Possible issues observed:
- Invalid or unreachable DNS servers
- Empty resolver configuration

### Step 5: Check DNS resolver service
```bash
systemctl status systemd-resolved
```
Service found stopped or unhealthy in affected cases.

---

## 🛠️ Resolution / Fix
### ✅ Immediate Mitigation
Restore a known working DNS resolver:
```bash
sudo resolvectl dns eth0 8.8.8.8 1.1.1.1
```
OR temporary manual override:
```bash
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
```

## ✅ Permanent Fix
- Restart DNS resolver service:
```bash
sudo systemctl restart systemd-resolved
```
- Correct DNS settings from DHCP or VPN
- Ensure firewall allows UDP/TCP traffic on port 53
- Prevent DNS override from misconfigured network profiles

## ✅ Verification
```bash
dig google.com
curl https://google.com
```
✅ DNS resolution and HTTPS connectivity restored.

## 📊 Impact on SLI / SLO

### Impacted SLIs
- Availability SLI ❌ — Users could not reach services
- Success Rate SLI ❌ — Requests relying on DNS failed
- Latency SLI ❌ — Requests failed before reaching backend services

### SLO Impact
- Near 100% error rate for DNS-dependent requests
- User-facing outage despite healthy application and network layers
- Demonstrates DNS as a critical shared dependency

## Key Learnings
- DNS outages can fully impact availability even when infrastructure is healthy
- Always isolate DNS vs Network vs Application early in incident response
- Monitoring DNS resolution is critical for reliability

## Preventive Actions

- Add DNS resolution checks to monitoring
- Configure fallback DNS resolvers
- Alert on resolver service failure
- Avoid unsafe DNS overrides from VPN or DHCP


