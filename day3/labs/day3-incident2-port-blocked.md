# 🛑 Incident 2: Port Blocked / Service Not Listening

## 📌 Incident Summary
An application failed to connect to its database despite basic network connectivity being available.  
The issue was isolated to the database service not listening on the expected TCP port.

---

## 🔍 Symptoms
- Application cannot connect to database
- `ping db-server` → ✅ works
- `curl db-server:5432` → ❌ fails
- `ss -tulnp` → ❌ no service listening on port `5432`

---

## 🧠 How This Happens (Root Cause Explanation)

This scenario occurs when **network connectivity exists**, but the **application-level service is unavailable**.

Key observations:
- ICMP (`ping`) succeeds → network & routing are OK
- TCP connection to port `5432` fails → service or port issue
- No process listening on the port → database service is down OR blocked

Common causes:
- Database service (e.g., PostgreSQL) is stopped or crashed
- Database configured to listen only on `localhost`
- Firewall rules blocking TCP port `5432`
- Container or system restart without service recovery
- Configuration change removing port binding

✅ This is **not a DNS issue**  
✅ This is **not a network routing issue**  
✅ This is an **application / TCP-layer failure**

---

## 🔎 Failed TCP State (Important)

### ❌ TCP Connection State
- **No `LISTEN` state on port 5432**

Expected state if DB were healthy:
```text
LISTEN 0 128 *:5432
```
Actual situation:
- Connection attempts result in connection refused or timeout
- Kernel rejects connection because no process is bound to the port

### Interpretation:
The TCP three-way handshake cannot begin because there is no listening socket on the destination port.

---

## 🛠️ Diagnosis Steps
### Step 1: Confirm network connectivity
```bash
ping db-server
```
✅ Confirms L3 connectivity.

### Step 2: Test application port
```bash
curl db-server:5432
```
❌ Fails → points to TCP/service issue.

### Step 3: Check listening services
```bash
ss -tulnp | grep 5432
```
❌ No output → service not listening.

---

## 🛠️ Resolution / Fix
### ✅ Fix Option 1: Start or Restart Database Service
```bash
sudo systemctl start postgresql
```
or 
```bash
sudo systemctl restart postgresql
```
Verify:
```bash
ss -tulnp | grep 5432
```

### ✅ Fix Option 2: Open Firewall Port
If the service is listening but still unreachable:
```bash
sudo ufw allow 5432/tcp
```
or update cloud security / firewall rules.

### Verification
```bash
ss -tulnp | grep 5432
curl db-server:5432
```
✅ Port is listening
✅ Application can connect to database

---

## 📊 Impact & Reliability Notes
### Impacted Layer
- Application connectivity
- Database dependency
- TCP Layer (Layer 4)
### SRE Insight
Successful ping does not guarantee service availability.
Always verify that the application is listening on the expected port.

---

## 🧠 Key Learnings
- ICMP success ≠ TCP success
- LISTEN state is mandatory for incoming connections
- Always distinguish between:
 - Network issues
 - Firewall issues
 - Application/service failures

---

## ✅ Preventive Actions
- Add monitoring for listening ports
- Alert if database service stops
- Ensure DB service auto-starts on reboot
- Validate firewall rules during deployment

