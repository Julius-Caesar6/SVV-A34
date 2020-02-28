import numpy as np
import math as m
import matplotlib.pyplot as plt
import scipy.interpolate as scp
from pandas import *

x=2.661
la=2.661
x1=0.172
x2=1.221
x3=2.591
xa=0.272
ha=0.205
tsk=0.0011
tsp=0.0028
tst=0.0012
hst=0.016
wst=0.019
nst=15
d1=0.01154
d2=0
d3=0.0184
theta=np.radians(28) #degrees (please leave)
P=97400
E = 73.1*10**9       # E-modulus (Pa)
G = 28*10**9       # G-modulus (Pa)
Nz = 81
Nx = 41
xI = x2-xa/2
xII = x2 + xa/2
Izz = 6.046530925746499e-06
Iyy = 4.536899107316306e-05
J = 8.62997e-06
zsc = -0.0053 - ha/2





#Order of the results matrix
#R=[R1y 0
#	R1z 1
#	RI  2
#	R2y 3
#	R2z 4
#	R3y 5
#	R3z 6
#	C1  7
#	C2  8
#	C3  9
#	C4  10
#	C5] 11


## Line 1: Sum of forces in y-direction
line1 = np.array([1,0,-np.sin(theta),1,0,1,0,0,0,0,0,0])				            

## Line 2: Sum of forces in the z-direction
line2 = np.array([0,1,-np.cos(theta),0,1,0,1,0,0,0,0,0])

## Line 3: Moments around y
line3 = np.array([0,(x-x1),-np.cos(theta)*(x-(xI)),0,(x-x2),0,(x-x3),0,0,0,0,0])

## Line 4: Moments around z
line4 = np.array([x-x1,0,-np.sin(theta)*(x-(xI)),x-x2,0,x-x3,0,0,0,0,0,0])

## Line 5: Torque
line5 = np.array([-(np.abs(zsc)-ha/2),0,np.sin(theta)*(np.abs(zsc)) - np.cos(theta)*ha/2,-(np.abs(zsc)-ha/2),0,-(np.abs(zsc)-ha/2),0,0,0,0,0,0])

## Line 6: Boundary condition 1  vy(x1) + theta(x1)*(zsc+ha/2)=d1*cos(theta0)
line6 = np.array([-(1/(6*E*Izz))*(x1-x1)**3 - (1/(G*J))*(zsc + ha/2)*(x1-x1)*(np.abs(zsc) - ha/2),0,0,0,0,0,0,0,0,x1,1,(zsc + ha/2)])

## Line 7: Boundary condition 2  vy(x2) + theta(x2)*(zsc+ha/2)=0
line7 = np.array([-(1/(6*E*Izz))*(x2-x1)**3 - (1/(G*J))*(zsc + ha/2)*(x2-x1)*(np.abs(zsc) - ha/2),0,-(1/(6*E*Izz))*-np.sin(theta)*(x2-(xI))**3 + (1/(G*J))*(np.sin(theta)*np.abs(zsc)*(x2-(xI)) - np.cos(theta)*ha/2*(x2-(xI)))*(zsc + ha/2),-(1/(6*E*Izz))*(x2-x2)**3 - (1/(G*J))*(np.abs(zsc) - ha/2)*(x2-x2)*(zsc + ha/2),0,0,0,0,0,x2,1,(zsc + ha/2)])

## Line 8: Boundary condition 3  vy(x3) + theta(x3)*(zsc+ha/2)=d3*cos(theta0)
line8 = np.array([-(1/(6*E*Izz))*(x3-x1)**3 - (1/(G*J))*(zsc + ha/2)*(x3-x1)*(np.abs(zsc) - ha/2),0,-(1/(6*E*Izz))*-np.sin(theta)*(x3-(xI))**3 + (1/(G*J))*(np.sin(theta)*np.abs(zsc)*(x3-(xI)) - np.cos(theta)*ha/2*(x3-(xI)))*(zsc + ha/2),-(1/(6*E*Izz))*(x3-x2)**3 - (1/(G*J))*(np.abs(zsc) - ha/2)*(x3-x2)*(zsc + ha/2),0,-(1/(6*E*Izz))*(x3-x3)**3 - (1/(G*J))*(zsc + ha/2)*(x3-x3)*(np.abs(zsc) - ha/2),0,0,0,x3,1,(zsc + ha/2)])

## Line 9: Boundary condition 4  vz(x1) = -d1*sin(theta0)
line9 = np.array([0,-(1/(6*E*Iyy))*(x1-x1)**3,0,0,0,0,0,x1,1,0,0,0])

## Line 10: Boundary condition 5 vz(x2) = 0
line10 = np.array([0,-(1/(6*E*Iyy))*(x2-x1)**3,(1/(6*E*Iyy))*np.cos(theta)*(x2-(xI))**3,0,-(1/(6*E*Iyy))*(x2-x2)**3,0,0,x2,1,0,0,0])

## Line 11: Boundary condition 6 vz(x3) = -d3*sin(theta0)
line11 = np.array([0,-(1/(6*E*Iyy))*(x3-x1)**3,(1/(6*E*Iyy))*np.cos(theta)*(x3-(xI))**3,0,-(1/(6*E*Iyy))*(x3-x2)**3,0,-(1/(6*E*Iyy))*(x3-x3)**3,x3,1,0,0,0])

## Line 12: Boundary condition 7 vz(xI)*cos(theta) + vy(xI)*sin(theta) - theta(xI)*abs(zsc)*sin(theta) = 0
line12 = np.array([-(1/(6*E*Izz))*np.sin(theta)*(xI-x1)**3 + (1/(G*J))*np.sin(theta)*np.abs(zsc)*(np.abs(zsc)-ha/2),-(1/(6*E*Iyy))*np.cos(theta)*(xI-x1)**3,-(1/(6*E*Iyy))*np.cos(theta)*np.cos(theta)*(xI-xI)**3 - (1/(6*E*Izz))*np.sin(theta)*np.sin(theta)*(xI-xI)**3 + (1/(G*J))*np.abs(zsc)*np.sin(theta)*np.sin(theta)*np.abs(zsc)*(xI-xI),0,0,0,0,xI*np.cos(theta),np.cos(theta),xI*np.sin(theta),np.sin(theta),-np.abs(zsc)*np.sin(theta)])


BadBoi = np.matrix([line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12])



B = np.matrix([[-P*np.sin(theta)], # Add Aero
			   [-P*np.cos(theta)],
			   [-P*np.cos(theta)*(x-(xII))],
			   [-P*np.sin(theta)*(x-(xII))], #-q Add Aero afterwards
			   [-P*(np.cos(theta)*ha/2 - np.abs(zsc)*np.sin(theta))],#-q Add Aero,
			   [d1*np.cos(theta)],#+(1/(E*Izz))*q -(1/(G*J))*q Add Aero
			   [0], #[(1/(E*Izz))*q - (1/(G*J))*q] Add Aero
			   [d3*np.cos(theta) - (1/(6*E*Izz))*-P*np.sin(theta)*(x3-(xII))**3 - (1/(G*J))*P*(zsc + ha/2)*(x3-(xII))*(np.abs(zsc)*np.sin(theta)-ha/2*np.cos(theta)) ], # + (1/(E*Izz))*q  - (1/(G*J))*q Add Aero
			   [-d1*np.sin(theta)],
			   [0],
			   [-d3*np.sin(theta) - (1/(6*E*Iyy))*-P*np.cos(theta)*(x3-(xII))**3],
			   [0]]) #-(1/(G*J))*q Add Aero

df1x = DataFrame(BadBoi)
df2x = DataFrame(B)

R = np.dot(np.linalg.inv(BadBoi),B)
R1 = np.linalg.solve(BadBoi,B)



print(R1)

R = R1


def positivo(x,power):
	if power>0 and x>=0:
		return x**power
	elif power==0 and x>=0:
		return 1
	else:
		return 0

def Sy(x):
	return  R[0]*positivo(x-x1,0) - R[2]*np.sin(theta)*positivo(x-(xI),0) + R[3]*positivo(x-x2,0) + P*np.sin(theta)*positivo(x-(xII),0) + R[5]*positivo(x-x3,0)
	
def Sz(x):
	return  R[1]*positivo(x-x1,0) - R[2]*np.cos(theta)*positivo(x-(xI),0) + R[4]*positivo(x-x2,0) + P*np.cos(theta)*positivo(x-(xII),0) + R[6]*positivo(x-x3,0)

def My(x):
	return  R[1]*positivo(x-x1,1) - R[2]*np.cos(theta)*positivo(x-(xI),1) + R[4]*positivo(x-x2,1) + P*np.cos(theta)*positivo(x-(xII),1) + R[6]*positivo(x-x3,1)

def Mz(x):
	return  R[0]*positivo(x-x1,1) - R[2]*np.sin(theta)*positivo(x-(xI),1) + R[3]*positivo(x-x2,1) + P*np.sin(theta)*positivo(x-(xII),1) + R[5]*positivo(x-x3,1)

def T(x):
	return -R[0]*(np.abs(zsc) - ha/2)*positivo(x-x1,0) + R[2]*(np.sin(theta)*np.abs(zsc) - np.cos(theta)*ha/2)*positivo(x-(xI),0) - R[3]*(np.abs(zsc) - ha/2)*positivo(x-x2,0) - P*(np.sin(theta)*np.abs(zsc) - np.cos(theta)*ha/2)*positivo(x-(xII),0) - R[5]*(np.abs(zsc) - ha/2)*positivo(x-x3,0)

def Vy(x):
	return -(1/(6*E*Izz))*(R[0]*positivo(x-x1,3) - R[2]*np.sin(theta)*positivo(x-(xI),3) + R[3]*positivo(x-x2,3) + P*np.sin(theta)*positivo(x-(xII),3) + R[5]*positivo(x-x3,3)) + R[9]*x + R[10]

def Vz(x):
	return -(1/(6*E*Iyy))*(R[1]*positivo(x-x1,3) - R[2]*np.cos(theta)*positivo(x-(xI),3) + R[4]*positivo(x-x2,3) + P*np.cos(theta)*positivo(x-(xII),3) + R[6]*positivo(x-x3,3)) + R[7]*x + R[8]
print(Vy(1))
def Theta(x):
	return  (1/(G*J))*(-R[0]*(np.abs(zsc) - ha/2)*positivo(x-x1,1) + R[2]*(np.sin(theta)*np.abs(zsc) - np.cos(theta)*ha/2)*positivo(x-(xI),1) - R[3]*(np.abs(zsc) - ha/2)*positivo(x-x2,1) - P*(np.sin(theta)*np.abs(zsc) - np.cos(theta)*ha/2)*positivo(x-(xII),1) - R[5]*(np.abs(zsc) - ha/2)*positivo(x-x3,1)) - R[11]

xcheck = np.linspace(0,x,100)

Shearplot = np.array([])
for i in range(len(xcheck)):
	Syplot = Vy(xcheck[i])
	Shearplot = np.append(Shearplot,Syplot)
	
plt.plot(xcheck,Shearplot)

## Check list
# Torque is good, the rest not so much, why???
# Check the Twist equation, take constant out and multiply by 2 and you get a close result