#!/bin/bash
for i in {1..6}
do
echo $i
sudo service docker start
sudo python3 ./get_docker_start_time.py
sudo docker container prune -f
# sleep 100
sudo ps -aux | grep docker | awk '{print $2}' | sudo xargs kill
if [ i == 3 ]
    then
        exit 0
    fi
sleep 600
done