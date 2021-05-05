#!/bin/bash
for i in {1..3}
do
echo $i
sudo python3 ./get_fc_start_time.py
sleep 120
# sudo ps -aux | grep docker | awk '{print $2}' | sudo xargs kill
done