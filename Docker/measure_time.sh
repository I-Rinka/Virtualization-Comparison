#!/bin/bash
start_time=$(date +%s%N)
end_time=$(sudo docker run ubuntu:bionic /bin/date "+%s%N")
echo $(($end_time - $start_time)) ns