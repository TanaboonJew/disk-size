#!/bin/bash

echo "Storage Devices Info:"
echo "---------------------------------"

df -h | grep '^/dev/' | awk '{print $1, $2, $4}' | while read -r device size avail; do
    echo "Device Path: $device"
    echo "Total Capacity: $size"
    echo "Unused Capacity: $avail"
    echo "---------------------------------"
done
