from FBD_Folder.Equations import *
import numpy as np
from FBD_Folder.Constants import *
import matplotlib.pyplot as plt


def sigmaxx(y,z, x, Iyy, Izz):
    return (My(x)*z/Iyy) - (Mz(x)*y/Izz) # FIXME check if two terms should be added or subtracted



xrange = np.linspace(0, la, 50)



def setup_aileron_profile():
    straight = np.sqrt((ha / 2) ** 2 + (Ca - ha / 2) ** 2)  # length of straight section
    range1 = np.linspace(0,np.pi/2,100)
    range2 = np.linspace(0,ha/2,100)
    range3 = np.linspace(0,straight,100)
    range4 = range3
    range5 = np.linspace(-ha/2,0,100)
    range6 = np.linspace(-np.pi/2,0,100)


    z1 = (ha/2)*np.cos(range1)
    y1 = (ha/2)*np.sin(range1)

    z2 = range2*0
    y2 = range2

    z3 = (-Ca + ha/2)*range3/straight
    y3 = (ha/2 -ha*range3/(2*straight))

    z4 = z3[::-1]
    y4 = -y3[::-1]

    z5 = z2[::-1]
    y5 = -y2[::-1]

    z6 = z1[::-1]
    y6 = -y1[::-1]

    #left curve
    zcl = np.concatenate((z6,z1))
    ycl = np.concatenate((y6,y1))

    #right closed section
    zcr = np.concatenate((z2,z3,z4,z5))
    ycr = np.concatenate((y2,y3,y4,y5))

    z = np.concatenate((zcl, zcr))
    y = np.concatenate((ycl,ycr))
    return y,z







fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot(z,y,0,color='r')   #wing profile
plt.show()