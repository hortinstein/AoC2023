#!/bin/bash

# sudo apt install bc

# Function to convert KB to GB
convert_kb_to_gb() {
    echo "scale=2; $1 / 1024 / 1024" | bc
}

# Check if a PID was provided
if [ -z "$1" ]; then
    echo "Usage: $0 <PID>"
    exit 1
fi

PID=$1

# Check if the given PID exists
if ! ps -p $PID > /dev/null; then
    echo "PID $PID not found."
    exit 1
fi

# Get RAM and Swap usage in KB for the given PID
RAM_USAGE_KB=$(ps -o rss= -p $PID)
SWAP_USAGE_KB=$(grep VmSwap /proc/$PID/status | awk '{print $2}')

# Convert KB to GB
RAM_USAGE_GB=$(convert_kb_to_gb $RAM_USAGE_KB)
SWAP_USAGE_GB=$(convert_kb_to_gb ${SWAP_USAGE_KB:-0})

echo "RAM Usage for PID $PID: $RAM_USAGE_GB GB"
echo "Swap Usage for PID $PID: $SWAP_USAGE_GB GB"
