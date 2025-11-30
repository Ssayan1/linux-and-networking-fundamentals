# 🛑 Incident 3: Routing Issue

## 📌 Incident Summary
Users were able to reach some external websites, but connections to specific destinations failed.
Basic network connectivity was available, but traffic to certain IP ranges could not be routed successfully.

---

## 🔍 Symptoms
- Some websites work, others do not
- `ping 8.8.8.8` → ✅ works
- `ping 142.250.193.206` (Google) → ❌ fails
- `traceroute` stops at hop 2
- Partial connectivity observed

---

## 🧠 Likely Router Problem (Root Cause)

This incident indicates a **routing issue beyond the local network**, typically involving an upstream router.

Key reasoning:
- Successful ping to `8.8.8.8` confirms:
  - Local network is up
  - Default gateway works
- Failure to reach a different public IP indicates:
  - Selective routing failure
  - Not a DNS issue
  - Not a full network outage

Most likely problems:
- Missing or incorrect route on upstream router
- BGP route withdrawal or misconfiguration
- ISP or transit provider routing failure
- Packet drops due to ACLs or routing loops
- Blackholed prefix for specific IP ranges

✅ Traffic is exiting the local system  
❌ But cannot reach certain external networks  

---

## 🔎 Troubleshooting Steps (SRE Workflow)

### Step 1: Confirm general connectivity
```bash
ping 8.8.8.8
```
✅ Confirms local routing and gateway are functional.

### Step 2: Test failing destination
```bash
ping 142.250.193.206
```
❌ Failure confirms destination-specific routing issue.

### Step 3: Trace network path
```bash
traceroute 142.250.193.206
```
Observed behavior:
- Traceroute progresses until hop 2
- No response beyond that point

Interpretation:
- Routing breaks after the second hop
- Failure is outside the local host
- Strong indicator of upstream router or ISP issue

### Step 4: Compare with a working destination
```bash
traceroute 8.8.8.8
```
✅ Completes successfully → routes differ after early hops

---

## 🧾 How This Is Detected from Logs
### 📍 Application Logs
- Connection timeouts
- No TCP handshake completion
- Requests stuck in retry state
Example indicators:
- Increased request latency
- Spike in timeout errors
- Partial success patterns based on destination
---

## 📍 Network / Infrastructure Logs
- Firewall logs showing no denies (rules unchanged)
- No local kernel drops
- No service crashes

---
## 📍 Monitoring Signals
- Synthetic probes failing only for specific external IPs
- Regional or destination-based alerts
- Asymmetric connectivity patterns
✅ Logs indicate no local fault, confirming routing beyond host boundary.

---

## 📊 Error Budget Impact
###Impacted SLIs
- Availability SLI ❌ — Some requests fail
- Latency SLI ❌ — Requests stall or timeout
- Success Rate SLI ❌ — Partial failure scenario

---

## Error Budget Consumption
- Partial outage → slow but steady error budget burn
- Harder to detect than full outage
- Often causes prolonged customer frustration
📉 Severity is medium to high, depending on:
- Traffic percentage affected
- Importance of unreachable destinations

---

## 🛠️ Mitigation & Fix
### Immediate Mitigation
- Reroute traffic if multi-homed
- Shift traffic regionally if possible
- Escalate to ISP or upstream provider

---
## Permanent Fix
- Correct routing tables or BGP configuration
- Restore missing prefixes
- Add routing health checks to detect partial outages
- Implement multi-path routing where possible

---
## 🧠 Key Learnings
- Ping success to one IP does not imply full Internet connectivity
- Routing failures often appear as partial outages
- Traceroute is essential to locate where packets stop
- Not all incidents originate within the application or host
