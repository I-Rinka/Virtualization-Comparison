# %%
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mlt
# import os

# %%

io_command = 'iozone -r 1 -r 2 -r 3 -r 4 -r 5 -r 6 -r 7 -r 8 -r 9 -r 10 -r 16 -r 32 -r 64 -r 128 -r 256 -r 512 -i 0 -i 1 -i 2 -s 1G -I'


def get_x_wt_rd_rwt_rrd(files):
    x = []
    dwrite = []
    dread = []
    random_write = []
    random_read = []
    file_count=0

    for file in files:
        file_count=file_count+1
        i = 0
        lines = file.readlines()
        for line in lines:
            i = i+1
            offset=42
            if i > offset and i < len(lines)-2:
                data = line.split()

                if file_count==1:
                    x.append(int(data[1]))
                    dwrite.append(int(data[2]))
                    dread.append(int(data[4]))
                    random_read.append(int(data[6]))
                    random_write.append(int(data[7]))

                else:
                    dwrite[i-offset-1]+=int(data[2])
                    dread[i-offset-1]+=int(data[4])
                    random_read[i-offset-1]+=int(data[6])
                    random_write[i-offset-1]+=int(data[7])

    
    dwrite=np.array(dwrite)
    dread=np.array(dread)
    random_read=np.array(random_read)
    random_write=np.array(random_write)

    dwrite=(dwrite/len(files)).astype(np.int64)
    dread=(dread/len(files)).astype(np.int64)
    random_read=(random_read/len(files)).astype(np.int64)
    random_write=(random_write/len(files)).astype(np.int64)

    return x, dwrite, dread, random_write, random_read

# %%


def get_host_io():
    file_path = "host_io.txt"

    files=[]
    for i in range(3):
        file = open(f"host_io_{i}.txt")    
        files.append(file)

    return files

# %%


def get_docker_io():
    file_path = "docker_io.txt"

    files=[]
    for i in range(3):
        file = open(f"docker_io_{i}.txt")    
        files.append(file)

    return files

# %%


def get_qemu_io():
    ssh_command = "ssh root@172.19.0.2"
    file_path = "qemu_io.txt"
   
    files=[]
    for i in range(3):
        file = open(f"qemu_io_{i}.txt")    
        files.append(file)

    return files
# %%


def get_fc_io():
    ssh_command = "ssh root@172.16.0.2"
    files=[]
    for i in range(3):
        file = open(f"fc_io_{i}.txt")    
        files.append(file)

    return files

# %%

# 0:x 1:write 2:read 3:random write 4:random read
docker_data = get_x_wt_rd_rwt_rrd(get_docker_io())
host_data = get_x_wt_rd_rwt_rrd(get_host_io())
fc_data = get_x_wt_rd_rwt_rrd(get_fc_io())
qemu_data=get_x_wt_rd_rwt_rrd(get_qemu_io())

i=0
for tag in ['Write','Read','Random Write','Random Read']:
    i+=1
    plt.figure(figsize=(6,5))

    plt.rc('font',family='Times New Roman')

    plt.plot(host_data[0], host_data[i]/1024, '-o', label="Host %s"%tag)
    plt.plot(docker_data[0], docker_data[i]/1024,':^',label="Docker %s"%tag)
    plt.plot(qemu_data[0], qemu_data[i]/1024,'-->',label="QEMU %s"%tag)
    plt.plot(fc_data[0], fc_data[i]/1024,':^',label="Firecracker %s"%tag)
    plt.legend(fontsize=13)
    plt.ylabel('Mega Bytes/sec',fontsize=18)
    plt.title('Disk '+tag,fontsize=18)
    plt.ticklabel_format(style='plain')
    plt.gca().yaxis.set_major_formatter(
    mlt.FuncFormatter(lambda x, p: format(int(x), ',')))
    plt.savefig(tag, dpi=600)
    # plt.show()
    # plt.clf()

# %%
