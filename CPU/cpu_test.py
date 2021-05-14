import numpy as np
import matplotlib.pyplot as plt

qemu=[3043.47,2992.04,2960.03]

fc=[3122.49,2978.14,3031.28]

docker=[3114.42,2892.88,2943.60]

host=[2905.05,3059.79,3051.47]



qemu=np.array(qemu)
fc=np.array(fc)
docker=np.array(docker)
host=np.array(host)


lables=['Qemu','Firecracker','Docker','Host']

plt.bar(lables,[qemu.mean(),fc.mean(),docker.mean(),host.mean()])

plt.ylabel('events per second')
plt.savefig('CPU')
plt.show()