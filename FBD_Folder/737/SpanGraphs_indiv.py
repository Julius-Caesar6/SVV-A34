from Equations import *
import numpy as np
from Constants import *
import matplotlib.pyplot as plt


topval = 70
x = np.linspace(0.0,la,topval)
sel = []
for i in range(len(x)):
    if int(i%(5/(100/topval))) == 0:
        print(int(100*i/topval),'%')
    sel.append(Sy(x[i]))

#
# print(Tx(0.1))
#
# y2 = []
# for i in range(len(x)):
#     y2.append(vy_(x[i]))


plt.axvline(x1,label='x1',color='r',linestyle='--',linewidth=0.5)
plt.axvline(x2,label='x2',color='r',linestyle='--',linewidth=0.5)
plt.axvline(x3,label='x3',color='r',linestyle='--',linewidth=0.5)
plt.axvline(x2-0.5*xa,label='x_j',color='g',linestyle='--',linewidth=0.5)
plt.axvline(x2+0.5*xa,label='x_P',color='g',linestyle='--',linewidth=0.5)

plt.title('Shear Force in z')
plt.xlabel('x [m]')
plt.ylabel('S [N]')
plt.plot(x,sel)

#plt.legend()

plt.show()