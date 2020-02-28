import numpy as np
from Equations import *

import matplotlib.pyplot as plt


vyVM = [ 9.01395737e-03,  5.35657838e-03,  2.00271919e-03 ,-6.64826056e-05,  8.85791145e-05 , 2.36863993e-03  ,6.29421672e-03 , 1.13583630e-02,  1.70485001e-02,  2.28884173e-02]
vzVM = [-4.45994920e-03, -2.60135970e-03, -9.21502315e-04 , 2.16149089e-05, -1.66191916e-04 ,-1.32989636e-03 ,-3.23564114e-03 ,-5.65026051e-03, -8.34281965e-03 ,-1.11017892e-02]
thetaVM = [-0.0015772, -0.00152025 ,-0.00121949, -0.00194817 ,-0.00292653, -0.00313099, -0.00334759 ,-0.00353636,-0.00369854, -0.00372817]

topval = 10
x = np.linspace(0.0,la,topval)
sel = []
sel2 = []
sel3 = []
for i in range(len(x)):
    if int(i%(5/(100/topval))) == 0:
        print(int(100*i/topval),'%')
    sel.append(vz(x[i]))
    sel2.append(vy(x[i]))
    sel3.append(theta(x[i]))

xVM = np.linspace(0,la,10)

a = plt.figure(1)
plt.plot(xVM,vzVM,'r+',label='Verification Model z displacement')
plt.plot(x,sel,label='Numerical Model z displacement')
plt.legend()
a.show()

b = plt.figure(2)
plt.plot(xVM,vyVM,'r+',label='Verification Model y displacement')
plt.plot(x,sel2,label='Numerical Model y displacement')
plt.legend()
b.show()

c = plt.figure(3)
plt.plot(xVM,thetaVM,'r+',label='Verification Model Twist')
plt.plot(x,sel3,label='Numerical Model Twist')
plt.legend()
c.show()

MSEvy = 0
MSEvz = 0
MSEtheta = 0

for p in range(10):
    MSEvy = MSEvy + ((vyVM[p]-vy(xVM[p]))**2)
    MSEvz = MSEvz + ((vzVM[p] - vz(xVM[p])) ** 2)
    MSEtheta = MSEtheta + ((thetaVM[p] - theta(xVM[p])) ** 2)

print(MSEvy*10,MSEvz*10,MSEtheta*10)  #*10 because *100/10 for % and n=10