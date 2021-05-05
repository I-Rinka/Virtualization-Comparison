import socket
import os
import time
import threading

start_time=10000
end_time=9999

def power_on():
    os.system("bash ./start_firecracker.sh")

def block_socket(port):
    # create a socket object
    serversocket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM) 

    # get local machine name
    # host = socket.gethostname()                           
    host = '0.0.0.0'

    port = port                                           

    # bind to the port
    serversocket.bind((host, port))                                  

    # queue up to 5 requests
    serversocket.listen(1)                                           


    # establish a connection
    clientsocket,addr = serversocket.accept()      

    print("Got a connection from %s" % str(addr))

    msg = 'Thank you for connecting'+ "\r\n"

    clientsocket.send(msg.encode('ascii'))


    clientsocket.close()

def get_start_time():

    power_on()
    start_time=time.time()
    block_socket(29999)
    end_time=time.time()

    time_consume=end_time-start_time

    os.system("sleep 2")

    # power off
    os.system('''curl --unix-socket /tmp/firecracker.socket -i \\
    -X PUT "http://localhost/actions" \\
    -H  "accept: application/json" \\
    -H  "Content-Type: application/json" \\
    -d "{
            \\"action_type\\": \\"SendCtrlAltDel\\"
    }"''')

    return time_consume

if __name__ == "__main__":
        n=os.fork()
        if n>0:
            os.system("sleep 1")
            time_get=get_start_time()

            os.wait()

            print("start time is:")
            print(time_get)

            file_obj=open("./start_time.txt","a")
            file_obj.write(time_get.__str__())
            file_obj.write('\n')
            file_obj.close()

        else:
            os.execl("./1_start_vm.sh","./1_start_vm.sh")