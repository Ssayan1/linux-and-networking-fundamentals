#!/bin/bash
# cpu-stress.sh
# Purpose: Create CPU load using multiple concurrent workers.

WORKERS=${1:-4}

echo "[+] Starting CPU stress with $WORKERS workers..."

for i in $(seq 1 $WORKERS); do
    yes > /dev/null &
done

echo "[+] CPU stress started."
echo "[+] To stop: pkill yes"
