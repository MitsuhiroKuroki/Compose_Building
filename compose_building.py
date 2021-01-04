import csv
import numpy as np

#Program Starts

csv_file = open('79_09B303AK26.csv', mode = "r")
l_reader = csv.reader(csv_file)

dicnode = dict()
dicbeam = dict()

for row in l_reader:
    rmcol = [col for col in row]
    title = rmcol[0]
    
    if title == 'node':
        n = []
        n.append(float(rmcol[2]))
        n.append(float(rmcol[3]))
        n.append(float(rmcol[4]))
        dicnode[int(rmcol[1])] = n
        
    if title == 'beam':
        b = []
        b.append(int(rmcol[2]))
        b.append(int(rmcol[3]))
        dicbeam[int(rmcol[1])] = b

x = []
y = []
z = []

for key in dicbeam.keys():
    nod1 = dicbeam[key][0]
    nod2 = dicbeam[key][1]    
    
    x.append(dicnode[nod1][0])
    x.append(dicnode[nod2][0])
    x.append(np.nan)
    
    y.append(dicnode[nod1][1])
    y.append(dicnode[nod2][1])
    y.append(np.nan)
    
    z.append(dicnode[nod1][2])
    z.append(dicnode[nod2][2])
    z.append(np.nan)
    
X = x
Y = y
Z = z

xmax = max(X)
ymax = max(Y)
zmax = max(Z)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

%matplotlib notebook

fig = plt.figure(figsize = (4, 8))
ax = Axes3D(fig)

ax.set_xlim(0, int(xmax) + 1)
ax.set_ylim(0, int(ymax))
ax.set_zlim(0, int(zmax))

ax.view_init(elev = 25, azim = 40)
ax.set_axis_off()
ax.plot(X, Y, Z)

plt.show()
