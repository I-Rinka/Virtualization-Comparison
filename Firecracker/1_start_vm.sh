#!/bin/bash
rm /tmp/firecracker.socket
./2_power_on.sh &
./firecracker --api-sock /tmp/firecracker.socket
