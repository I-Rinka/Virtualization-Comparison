#%%
import numpy as np
#%%
docker_nc=open('docker_nocache.txt')
lines=docker_nc.readlines()
docker_nc=[]
for line in lines:
    docker_nc.append(float(line))
docker_nc=np.array(docker_nc)
print(docker_nc)
print(docker_nc.dtype)
# %%
docker_cosc=open('docker_consecu.txt')
lines=docker_cosc.readlines()
docker_cosc=[]
for line in lines:
    docker_cosc.append(float(line))
docker_cosc=np.array(docker_cosc)
print(docker_cosc)
print(docker_cosc.dtype)
# %%
fc=open('fc.txt')
lines=fc.readlines()
fc=[]
for line in lines:
    fc.append(float(line))
fc=np.array(fc)
print(fc)
print(fc.dtype)
# %%
qemu=open('qemu.txt')
lines=qemu.readlines()
qemu=[]
for line in lines:
    qemu.append(float(line))
qemu=np.array(qemu)
print(qemu)
print(qemu.dtype)
# %%
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rc('figure', figsize=(5, 2)) # adjust scale

column=['Qemu','Firecracker','Docker\nno cache','Docker start\nconsecutively']

data=[qemu,fc,docker_nc,docker_cosc]

# standard deviation

table_text=[]
data_bar=[]
for cell in data:
    table_text.append(['%.4f'%cell.mean(),'%.4f'%cell.std()])
    data_bar.append(cell.mean())
table_text=np.array(table_text)
table_text=np.swapaxes(table_text,0,1)

plt.figure(dpi=600)

table=plt.table(cellText=table_text,rowLabels=['Average (second)','Standard Deviation'],colLabels=column,loc='bottom',cellLoc='center',rowLoc='center')

table.auto_set_font_size(False)

table.set_fontsize(8)

plt.bar([1,2,3,4], data_bar,width=0.8,color='#0089A7')
plt.xticks([])

plt.ylabel('Startup time')

plt.yscale('linear')

plt.axhline(fc.mean(), ls='--', color='#AB3B3A',linewidth=1.0)

plt.subplots_adjust(left=0.2, bottom=-0.4)
plt.show()
# %%
