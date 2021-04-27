#!/bin/bash
rm /tmp/firecracker.socket

./firecracker --api-sock /tmp/firecracker.socket

# bash ./start_firecracker.sh