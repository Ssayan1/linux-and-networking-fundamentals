#!/usr/bin/env bash
#
# script1-basic.sh
# Author: Sayan Sanki
# Purpose: Display basic system information for SRE diagnostics.
# This script demonstrates good Bash practices and proper formatting.
#

# Enable strict mode (safer scripts)
set -euo pipefail

# Variables
CURRENT_DATE=$(date)
UPTIME_OUTPUT=$(uptime)
LOGGED_USERS=$(who)

echo "==============================================="
echo "        SRE System Information Script"
echo "==============================================="
echo ""
echo "[INFO] Script executed at: $CURRENT_DATE"
echo "[INFO] Hostname: $(hostname)"
echo "[INFO] Current user: $USER"
echo ""
echo "-------------- System Uptime ------------------"
echo "$UPTIME_OUTPUT"
echo ""
echo "-------------- Logged-in Users ----------------"
echo "$LOGGED_USERS"
echo ""
echo "==============================================="
echo " Script completed successfully."
echo "==============================================="

exit 0
