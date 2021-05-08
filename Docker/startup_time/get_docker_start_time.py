import socket
import os
import time
import threading

start_time=10000
end_time=9999

def block_socket(port):
    # create a socket object
    serversocket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM) 
                  
    host = '0.0.0.0'

    port = port                                           

    # bind to the port
    serversocket.bind((host, port))                                  

    # queue up to 5 requests
    serversocket.listen(1)                                           

    start_time=time.time()
    threading._start_new_thread(start_docker,())

    # establish a connection
    clientsocket,addr = serversocket.accept()      

    print("Got a connection from %s" % str(addr))

    msg = 'Thank you for connecting'+ "\r\n"

    clientsocket.send(msg.encode('ascii'))
    end_time=time.time()


    clientsocket.close()

    return end_time-start_time

def get_start_time():

    
    time_consume=block_socket(28888)

    return time_consume

def start_docker():
    os.system('sudo docker run --cpus="2" ubuntu18_msg "/usr/bin/python3" "/root/send_msg.py"')

if __name__ == "__main__":
        time_get=get_start_time()
        print("start time is:")
        print(time_get)

        file_obj=open("./start_time.txt","a")
        file_obj.write(time_get.__str__())
        file_obj.write('\n')
        file_obj.close()
