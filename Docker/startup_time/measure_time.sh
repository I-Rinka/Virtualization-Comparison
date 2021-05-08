#!/bin/bash
start_time=$(date +%s%N)
end_time=$(sudo docker run ubuntu18 /bin/date "+%s%N")
echo $(($end_time - $start_time)) ns

# sudo docker run ubuntu18_msg /bin/python3 /root/send_msg.py