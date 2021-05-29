#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mlt

qemu_tp=409

fc_tp=980

docker_tp=2650
docker_NAT_tp=2100

host_tp=2640




lables=['Qemu','Firecracker','Docker-host','Docker-NAT','Host']

plt.figure(figsize=(7,5))

plt.bar(lables,[qemu_tp,fc_tp,docker_tp,docker_NAT_tp,host_tp],color='#0089A7',width=0.5)
plt.gca().yaxis.set_major_formatter(
    mlt.FuncFormatter(lambda x, p: format(int(x), ',')))
plt.axhline(fc_tp, ls='--', color='#AB3B3A',linewidth=2.0)

plt.title('Network Throughput',fontsize=15)

plt.ylabel('Mega Bytes/second',fontsize=15)
plt.savefig('NetworkThroughput')
# %%
