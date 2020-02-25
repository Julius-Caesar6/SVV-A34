from Equations import *
from Equations_IntOff import *
import numpy as np
from Constants import *
import matplotlib.pyplot as plt



x = np.linspace(0.01,la,100)
Txa = []
Mya = []
Mza = []
vya = []
vza = []
thetaa = []
for i in range(len(x)):
    Txa.append(Tx(x[i]))
    Mya.append(-My(x[i]))
    Mza.append(Mz(x[i]))
    vya.append(vy(x[i]))
    vza.append(-vz(x[i]))
    thetaa.append(-theta(x[i]))
#
# print(Tx(0.1))
#
# y2 = []
# for i in range(len(x)):
#     y2.append(vy_(x[i]))


fig, axs = plt.subplots(2, 3)
axs[0, 0].plot(x, Txa)
axs[0, 0].set_title('Tx')
axs[0, 1].plot(x, Mya, 'tab:orange')
axs[0, 1].set_title('My')
axs[0, 2].plot(x, Mza, 'tab:blue')
axs[0, 2].set_title('Mz')
axs[1, 0].plot(x, vya, 'tab:green')
axs[1, 0].set_title('vy')
axs[1, 1].plot(x, vza, 'tab:red')
axs[1, 1].set_title('vz')
axs[1, 2].plot(x, thetaa, 'tab:cyan')
axs[1, 2].set_title('theta')


for ax in axs.flat:
    ax.set(xlabel='x-label', ylabel='y-label')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

