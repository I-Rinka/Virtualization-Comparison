import numpy as np
import matplotlib.pyplot as plt

qemu_tp=[919,1120,840,765,1370,1310,1090,1060,608,1080,972,858]

fc_tp=[8560,10100,9890,10800,10700,10600,10800,10800,10600,10800,10500,10700]

docker_tp=[66300,69300,67800,69600,68600,66000,67400,65300,64400,66900,67000,64700]

host_tp=[71800,72300,73600,73900,74900,74900,74800,74600,74000,73300,75900,74800]



qemu_tp=np.array(qemu_tp)
fc_tp=np.array(fc_tp)
docker_tp=np.array(docker_tp)
host_tp=np.array(host_tp)


lables=['Qemu','Firecracker','Docker','Host']

plt.figure(figsize=(7,5))

plt.bar(lables,[qemu_tp.mean(),fc_tp.mean(),docker_tp.mean(),host_tp.mean()],color='#0089A7',width=0.5)

plt.axhline(fc_tp.mean(), ls='--', color='#AB3B3A',linewidth=2.0)

plt.title('Network Throughput',fontsize=15)

plt.ylabel('Mega Bytes/second',fontsize=15)
plt.savefig('NetworkThroughput')