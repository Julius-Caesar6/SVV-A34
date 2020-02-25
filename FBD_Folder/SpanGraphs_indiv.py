from Equations import *
from Equations_IntOff import *
import numpy as np
from Constants import *
import matplotlib.pyplot as plt


topval = 300
x = np.linspace(0.01,la,topval)
sel = []
for i in range(len(x)):
    if int(i%(5/(100/topval))) == 0:
        print(int(100*i/topval),'%')
    sel.append(Tx(x[i]))

#
# print(Tx(0.1))
#
# y2 = []
# for i in range(len(x)):
#     y2.append(vy_(x[i]))

plt.plot(x,sel)
plt.show()