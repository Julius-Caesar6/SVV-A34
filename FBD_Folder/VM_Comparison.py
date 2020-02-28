import numpy as np
# from Equations import *
from main import *
# import matplotlib as plt


vyVM = y

topval = 100
x = np.linspace(0.01,la,topval)
sel = []
for i in range(len(x)):
    if int(i%(5/(100/topval))) == 0:
        print(int(100*i/topval),'%')
    sel.append(Mz(x[i]))

plt.plot(x,y)