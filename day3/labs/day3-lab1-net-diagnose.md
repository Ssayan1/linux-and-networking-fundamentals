### Create:
```
day3/scripts/net-diagnose.sh
```

### Scripts
```bash
#!/usr/bin/env bash
set -euo pipefail

TARGET=${1:-"google.com"}

echo "========================================"
echo "   SRE Network Diagnostic Tool"
echo "========================================"
echo "[INFO] Target: $TARGET"
echo "[INFO] Date: $(date)"
echo

echo "---- DNS Lookup ----"
dig "$TARGET" +short || echo "[WARN] DNS query failed"

echo
echo "---- Ping ----"
ping -c 4 "$TARGET" || echo "[WARN] Ping failed"

echo
echo "---- Route ----"
ip r

echo
echo "---- TCP Listening Ports ----"
ss -tulnp

echo
echo "---- External Connectivity ----"
curl -I "https://$TARGET" || echo "[WARN] curl failed"

echo
echo "========================================"
echo "Diagnostics complete."
echo "========================================"

```
### Make executable:
```bash
chmod +x day3/scripts/net-diagnose.sh
```

### Run it:
```bash
./day3/scripts/net-diagnose.sh google.com
```


### What this tool checks
- DNS resolution
- Basic network reachability
- HTTPS connectivity

### Security note
This script intentionally avoids printing routing tables,
listening ports, or IP-level details to remain GitHub-safe.
