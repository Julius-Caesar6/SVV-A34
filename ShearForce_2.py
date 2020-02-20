#Shear force analysis
from MOI import z,y,Iyy_total,Izz_total,A_stringer,h,t
import numpy as np


Sz = 1
Sy = 1

#qb1--------------------------------------------------------------------------------------------------------------------
#positive z values and positive y values
range1 = np.linspace(0,np.pi,100)
qb1 = -Sz/Iyy_total * (t*h**2/4 *(np.sin(range1)-0) + A_stringer/2*z[0] + A_stringer*z[1]) - Sy/Izz_total *(t*h**2/4*(-np.cos(range1)+1) + A_stringer/2*y[0] + A_stringer*y[1])

