import numpy as np
from Equations import *

import matplotlib.pyplot as plt



vyVM = [ 9.01395737e-03,  5.35657838e-03,  2.00271919e-03 ,-6.64826056e-05,  8.85791145e-05 , 2.36863993e-03  ,6.29421672e-03 , 1.13583630e-02,  1.70485001e-02,  2.28884173e-02]
vzVM = [-4.45994920e-03, -2.60135970e-03, -9.21502315e-04 , 2.16149089e-05, -1.66191916e-04 ,-1.32989636e-03 ,-3.23564114e-03 ,-5.65026051e-03, -8.34281965e-03 ,-1.11017892e-02]
thetaVM = [-0.0015772, -0.00152025 ,-0.00121949, -0.00194817 ,-0.00292653, -0.00313099, -0.00334759 ,-0.00353636,-0.00369854, -0.00372817]
MyVM = [  3117.07108789,  11044.30898622  ,66185.48164779, 109115.2695308,  87015.14389607 , 67560.21113792  ,45892.95564786,  24833.12508346,   4055.89375751   ,1468.29299167]
MzVM = [  -762.06219586 , -2500.4018320, -14947.74006796, -28588.19235043, -25603.57968357, -19927.92311162 ,-13702.11051313 , -7483.42950983,  -1219.5937162,    -393.56680923]
SyVM = [150432.77647098, -68249.78794854, -74140.77702434 ,-30504.93622459,  33336.24080637 , 32852.09486299 , 30503.85222933  ,33817.83431824,  32892.85641165 ,-78817.43044869]
SzVM = [-623934.04441872 , 294380.29319201 , 306681.00005747 ,  16956.95826382, -128932.67407148, -115858.70474572 ,-101588.4597311 , -114328.71345911, -110835.49598617,  288687.75342454]
TxVM = [  -56.46707975  , 306.0471938   , 137.12751349 ,-1786.89314286,  -459.73837304 , -315.18711077  ,-221.304646   , -214.71755027,  -185.80247279 ,  -28.96213835]
vyderVM = [-0.01947292, -0.0193589, -0.01544687, -0.00551364 , 0.00690175 , 0.01695979,  0.02436324,  0.0290815,   0.03102965,  0.03108505]
vzderVM = [ 0.00989669,  0.009827,    0.00752015 , 0.00207079, -0.00382895, -0.00837484, -0.0116956 , -0.01379851, -0.01466109, -0.01468568]


topval = 60
x = np.linspace(0.0,la,topval)
sel = []

# for i in range(len(x)):
#     if int(i%(5/(100/topval))) == 0:
#         print(int(100*i/topval),'%')
#     sel.append(Sz(x[i]))  #HERE
#
# plt.axvline(x1,color='r',linestyle='--',linewidth=0.5)
# plt.axvline(x2,color='r',linestyle='--',linewidth=0.5)
# plt.axvline(x3,color='r',linestyle='--',linewidth=0.5)
# plt.axvline(x2-0.5*xa,color='g',linestyle='--',linewidth=0.5)
# plt.axvline(x2+0.5*xa,color='g',linestyle='--',linewidth=0.5)
#
# plt.title('Shear Force in z') #HERE
# plt.xlabel('x [m]')
# plt.ylabel('S [N]')  #HERE
#
xVM = np.linspace(0,la,10)
#
#
#
# plt.plot(x,sel,label='Numerical Model z displacement')
# plt.plot(xVM,SzVM,'r+',label='Verification Model z displacement') #HERE
#
# plt.show()

MSEvy = 0

lst = []


for p in range(0,10):
    MSEvy = MSEvy + ((MyVM[p]-My(xVM[p]))**2)
    lst.append(100*np.abs((vyVM[p]-vy(xVM[p])))/vyVM[p])


print(MSEvy*10)  #*10 because *100/10 for % and n=10

print(lst)
print(max(lst))