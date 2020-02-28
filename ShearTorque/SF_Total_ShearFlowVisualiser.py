from ShearTorque.ShearForce_3 import *

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

#left curve
zcl = np.concatenate((z6,z1))
ycl = np.concatenate((y6,y1))
qbl = np.concatenate((q6_total,q1_total))

#right closed section
zcr = np.concatenate((z2,z3,z4,z5))
ycr = np.concatenate((y2,y3,y4,y5))
qbr = np.concatenate((q2_total,q3_total,q4_total,q5_total))

plt.close() #removes previous

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_aspect('equal')

#ax.plot_surface(zcl,ycl,[qbl,qbl*0]) #with shear
#ax.plot_surface(zcr,ycr,[qbr,qbr*0]) #with shear


#below is a bad way of trying to draw the surface but i couldnt figure it out with plot_surface
for i in range(len(zcl)):
    ax.plot([zcl[i],zcl[i]],[ycl[i],ycl[i]],[qbl[i],0],color='tab:cyan')

for i in range(len(zcr)):
    ax.plot([zcr[i],zcr[i]],[ycr[i],ycr[i]],[qbr[i],0],color='tab:cyan')


ax.plot(zcl,ycl,0,color='r')   #wing profile
ax.plot(zcl,ycl,qbl,color='b') #with shear
ax.plot(zcr,ycr,0,color='r')  #wing profile
ax.plot(zcr,ycr,qbr,color='b') #with shear
plt.show()