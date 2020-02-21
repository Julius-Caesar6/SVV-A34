import numpy as np
from MOI import Izz_total,A_stringer,y,straight,alpha,Am_cell1,Am_cell2

h = 17.3 #cm
ca = 48.4 #cm
stringers = 13
hst = 1.4 #cm
wst = 1.8 #cm
tst = 1.2/10 #cm
t = 1.1/10 #cm
tspar= 2.5/10 #cm

## constant eq1

q01_c1 = h*np.pi/(2*t) + h/tspar
q02_c1 = -h/tspar

c1 = 1/Izz_total * t*h**4/4
r1 = 1/Izz_total*(A_stringer*(y[1])  -  t*h**4/4)
R1 = h/t*(c1+r1*np.pi/2)

c2 = -tspar/Izz_total/2
R2 = 2/tspar*c2/3*(h/2)**3

## constant eq2
q01_c2 = -h/tspar
q02_c2 = 2*straight/t+h/tspar

E1 = 2/tspar*c2/3*(h/2)**3

qb1 = r1
qb2 = c2*(h/2)**2
r3 = qb1 + qb2 - 1/Izz_total * A_stringer* sum(y[2:])
c31 = -1/Izz_total*(t*h/2)
c32 = -1/Izz_total*(-t*h/straight/2)
E2 = 2/t*(straight*r3  +  c31*straight**2/2  +  c32*straight**3/3)

eq1 = [q01_c1,q02_c1,R1+R2]
eq2 = [q01_c2,q02_c2,E1+E2]

q02 =  (eq1[2]/eq1[0]-eq2[2]/eq2[0])/(-eq1[1]/eq1[0]+eq2[1]/eq2[0])
q01 = -(eq1[1]*q02+eq1[2])/eq1[0]

print("q01",q01,"q02",q02)

## calculating shear centre

F1 = h**2/4*(c1+r1*np.pi/2   )
F2 = np.cos(alpha)*h/2*(r3*straight+c31*straight**2/2+c32*straight**3/3)

print(F1,F2)
sc = 2*(F1+F2) + 2*q01*Am_cell1  +  2*q02*Am_cell2
print(sc)