from Equations import *
import numpy as np
from Constants import *
import matplotlib.pyplot as plt


xshow = True  #show x1,x2, etc

topval = 20
x = np.linspace(0.01,la,topval)
Txa = []
Mya = []
Mza = []
vya = []
vza = []
Sya = []
Sza = []
thetaa = []
vydera = []
vzdera = []
for i in range(len(x)):
    if int(i%(10/(100/topval))) == 0:
        print(int(100*i/topval),'%')
    Txa.append(Tx(x[i]))
    Mya.append(My(x[i]))
    Mza.append(Mz(x[i]))
    vya.append(vy(x[i]))
    vza.append(vz(x[i]))
    Sza.append(Sz(x[i]))
    Sya.append(Sy(x[i]))
    thetaa.append(theta(x[i]))
    vydera.append(vyder(x[i]))
    vzdera.append(vzder(x[i]))
#
# print(Tx(0.1))
#
# y2 = []
# for i in range(len(x)):
#     y2.append(vy_(x[i]))


fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, vza, 'tab:cyan')
axs[0, 0].set_title('vz')
axs[1, 0].plot(x, Mya, 'tab:cyan')
axs[1, 0].set_title('My')
axs[0, 1].plot(x, vzdera, 'tab:cyan')
axs[0, 1].set_title("""vz slope """)
axs[1, 1].plot(x, Sza, 'tab:cyan')
axs[1, 1].set_title('Sz')

fig, axs2 = plt.subplots(2, 2)
axs2[0, 0].plot(x, vya, 'tab:cyan')
axs2[0, 0].set_title('vy')
axs2[1, 0].plot(x, Mza, 'tab:cyan')
axs2[1, 0].set_title('Mz')
axs2[0, 1].plot(x, vydera, 'tab:cyan')
axs2[0, 1].set_title("""vy slope """)
axs2[1, 1].plot(x, Sya, 'tab:cyan')
axs2[1, 1].set_title('Sy')


fig, axs3 = plt.subplots(2, 2)
axs3[0, 0].plot(x, thetaa, 'tab:cyan')
axs3[0, 0].set_title('twist')
#axs3[1, 0].plot(x, Mya, 'tab:cyan')
#axs3[1, 0].set_title('My')
axs3[0, 1].plot(x, Txa, 'tab:cyan')
axs3[0, 1].set_title("""Torque""")


if xshow == True:
    for ax in axs.flat:
        ax.set(xlabel='x-label', ylabel='y-label')
        ax.axvline(x1, label='x1', color='r', linestyle='--',linewidth=0.5)
        ax.axvline(x2, label='x2', color='r', linestyle='--',linewidth=0.5)
        ax.axvline(x3, label='x3', color='r', linestyle='--',linewidth=0.5)
        ax.axvline(x2 - 0.5 * xa, label='x_j', color='g', linestyle='--',linewidth=0.5)
        ax.axvline(x2 + 0.5 * xa, label='x_P', color='g', linestyle='--',linewidth=0.5)

    for ax in axs2.flat:
        ax.set(xlabel='x-label', ylabel='y-label')
        ax.axvline(x1, label='x1', color='r', linestyle='--',linewidth=0.5)
        ax.axvline(x2, label='x2', color='r', linestyle='--',linewidth=0.5)
        ax.axvline(x3, label='x3', color='r', linestyle='--',linewidth=0.5)
        ax.axvline(x2 - 0.5 * xa, label='x_j', color='g', linestyle='--',linewidth=0.5)
        ax.axvline(x2 + 0.5 * xa, label='x_P', color='g', linestyle='--',linewidth=0.5)

    for ax in axs3.flat:
        ax.set(xlabel='x-label', ylabel='y-label')
        ax.axvline(x1, label='x1', color='r', linestyle='--',linewidth=0.5)
        ax.axvline(x2, label='x2', color='r', linestyle='--',linewidth=0.5)
        ax.axvline(x3, label='x3', color='r', linestyle='--',linewidth=0.5)
        ax.axvline(x2 - 0.5 * xa, label='x_j', color='g', linestyle='--',linewidth=0.5)
        ax.axvline(x2 + 0.5 * xa, label='x_P', color='g', linestyle='--',linewidth=0.5)

    # Hide x labels and tick labels for top plots and y ticks for right plots.
    for ax in axs.flat:
        ax.label_outer()

    for ax in axs2.flat:
        ax.label_outer()

    for ax in axs3.flat:
        ax.label_outer()