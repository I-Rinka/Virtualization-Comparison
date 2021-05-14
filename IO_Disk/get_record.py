import os
io_command = 'iozone -r 1 -r 2 -r 3 -r 4 -r 5 -r 6 -r 7 -r 8 -r 9 -r 10 -r 16 -r 32 -r 64 -r 128 -r 256 -r 512 -i 0 -i 1 -i 2 -s 1G -I'

for i in range(1,3):
    file_path = f"host_io_{i}.txt"
    # os.system(f"{io_command} > {file_path}")
    # file_path = f"docker_io_{i}.txt"

    # qemu
    file_path = f"qemu_io_{i}.txt"
    ssh_command = "ssh root@172.19.0.2"
    os.system(f"{ssh_command} \"{io_command}\" > {file_path}")
    