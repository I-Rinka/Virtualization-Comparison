#!/usr/bin/env python3
import socket
import os
import time
import threading

def power_on():
    os.system("sudo bash ./start_vm.sh")


if __name__ == "__main__":
        n=os.fork()
        if n>0:
            os.system("sleep 2")
            os.system("sudo ip addr add 172.19.0.1/24 dev tap1")
            os.system("sudo ip link set tap1 up")

            os.wait()


        else:
            # os.execl("./1_start_vm.sh","./1_start_vm.sh")
            power_on()

            
