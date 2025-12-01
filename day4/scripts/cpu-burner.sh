#!/bin/bash
# cpu-burner.sh
# Purpose: Create predictable CPU load for performance debugging labs.

echo "[+] Starting CPU burner..."
echo "[+] This will continuously run 'yes' in the background."

yes > /dev/null &
BURN_PID=$!

echo "[+] CPU burner started with PID: $BURN_PID"
echo "[+] To stop: kill $BURN_PID  or  pkill yes"
