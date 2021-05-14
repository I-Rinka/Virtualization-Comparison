import matplotlib.pyplot as plt
import numpy as np


labels = ['Qemu', 'Firecracker', 'Docker', 'Host']
fc_rd = np.array([2453.75, 2404.47, 2481.40])
host_rd = np.array([2420.49, 2496.83, 2464.06])
qemu_rd = np.array([2436.83, 2360.91, 2449.43])
docker_rd = np.array([971.20, 958.11, 949.94])

docker_sq = np.array([6687.47, 6572.97, 6312.05])
host_sq = np.array([6650.78, 6556.42, 6663.15])
fc_sq = np.array([6316.11, 6264.62, 6264.87])
qemu_sq = np.array([6261.64, 6286.27, 6205.02])


rnd = [qemu_rd.mean(), fc_rd.mean(), docker_rd.mean(), host_rd.mean()]
seq = [qemu_sq.mean(), fc_sq.mean(), docker_sq.mean(), host_sq.mean()]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, rnd, width, label='Random Access')
rects2 = ax.bar(x + width/2, seq, width, label='Sequential Access')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Mega Bytes/sec')
ax.set_title('Memory Test')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(loc='best',bbox_to_anchor=(1.0,1.0),fancybox=True,shadow=False)

fig.tight_layout()

plt.savefig('Memory')
plt.show()
