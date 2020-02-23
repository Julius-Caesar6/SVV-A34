import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from ShearForce_3 import *

z1 = (h/2)*np.cos(range1)
y1 = (h/2)*np.sin(range1)

z2 = range2*0
y2 = range2

z3 = (-ca + h/2)*range3/straight
y3 = (h/2 -h*range3/(2*straight))

z4 = z3[::-1]
y4 = -y3[::-1]

z5 = z2[::-1]
y5 = -y2[::-1]

z6 = z1[::-1]
y6 = -y1[::-1]
print(z6)
#left curve
zcl = np.concatenate((z6,z1))
ycl = np.concatenate((y6,y1))
qbl = np.concatenate((qb6,qb1))

#right closed section
zcr = np.concatenate((z2,z3,z4,z5))
ycr = np.concatenate((y2,y3,y4,y5))
qbr = np.concatenate((qb2,qb3,qb4,qb5))

plt.close() #removes previous

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_aspect('equal')

ax.plot_surface(zcl,ycl,[qbl,qbl*0]) #with shear
ax.plot_surface(zcr,ycr,[qbr,qbr*0]) #with shear


ix = np.linspace(-h/2, h/2)
iy = func(ix)
verts = [(a, 0), *zip(ix, iy), (b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)

ax.plot(zcl,ycl,0,color='b')   #wing profile
ax.plot(zcl,ycl,qbl,color='r') #with shear
ax.plot(zcr,ycr,0,color='b')  #wing profile
ax.plot(zcr,ycr,qbr,color='r') #with shear
plt.show()