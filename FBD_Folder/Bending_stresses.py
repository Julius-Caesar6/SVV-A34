from FBD_Folder.Equations import *
import numpy as np
from FBD_Folder.Constants import *
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pandas as pd

def sigmaxx(y,z, x, Iyy, Izz):
    return (My(x)*z/Iyy) - (Mz(x)*y/Izz) # FIXME check if two terms should be added or subtracted


def setup_aileron_profile():
    straight = np.sqrt((ha / 2) ** 2 + (Ca - ha / 2) ** 2)  # length of straight section
    range1 = np.linspace(0,np.pi/2,100)
    range2 = np.linspace(0,ha/2,100)
    range3 = np.linspace(0,straight,100)

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


y,z = setup_aileron_profile()



def stress_at_span_coordinate(x,y,z):
    sigx = []
    for i in range(len(y)):
        sigx.append(sigmaxx(y[i], z[i], x, Iyy, Izz))


    df = pd.DataFrame(sigx, columns=['sigma'])
    df['y'] = y
    df['z'] = z
    return df



x01stress = stress_at_span_coordinate(0.1,y,z)


#
# fig = plt.figure()
#     ax = plt.axes(projection='3d')
#     p = ax.scat(stress_dfr1['intpointx'], stress_dfr1['intpointy'], stress_dfr1['intpointz'],c=stress_dfr1[type], cmap='jet')
#     q = ax.scatter(stress_dfr2['intpointx'], stress_dfr2['intpointy'], stress_dfr2['intpointz'], c = stress_dfr2[type], cmap='jet')
#     clb = fig.colorbar(p)
#     ax.set_xlabel('x [mm]')
#     ax.set_ylabel('y [mm]')
#     ax.set_zlabel('z [mm]')
#     clb.set_label(stress_type)
#     ax.set_xlim3d(600, 2000)
#     ax.set_ylim3d(-200,200)
#     ax.set_zlim3d(-600,600)
#     plt.show()
#     plt.close()


fig = plt.figure()
ax = plt.axes()
p = ax.scatter(x01stress['z'],x01stress['y'],c=x01stress['sigma'], cmap='jet')   #wing profile
clb = fig.colorbar(p)
ax.set_ylabel('y [mm]')
ax.set_xlabel('z [mm]')
ax.set_xlim(-0.5,0.2)
clb.set_label('$\sigma_x$ stress')
plt.show()
plt.close()