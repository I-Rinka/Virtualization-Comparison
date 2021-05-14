#!/bin/bash
qemu-system-x86_64 -enable-kvm ./ubuntu-18.04-server-cloudimg-amd64.img  -nographic \
-cpu host -smp 2 \
-m 1024 \
-net nic -net tap
#  -net tap,ifname=tap1,script=no,downscript=no
