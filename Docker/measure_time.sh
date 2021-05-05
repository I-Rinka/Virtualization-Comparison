#!/bin/bash
start_time=$(date +%s%N)
end_time=$(sudo docker run ubuntu18 /bin/date "+%s%N")
echo $(($end_time - $start_time)) ns