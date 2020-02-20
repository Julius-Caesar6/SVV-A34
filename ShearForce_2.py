#Shear force analysis
from MOI import *
import numpy as np


Sz = 1
Sy = 1

#qb1--------------------------------------------------------------------------------------------------------------------
#positive z values and positive y values
range1 = np.linspace(0,np.pi,100)
qb1 = -Sz/Iyy_total * (t*h**2/4 *(np.sin(range1)-0) + A_stringer/2*z[0] + A_stringer*z[1]) - Sy/Izz_total *(t*h**2/4*(-np.cos(range1)+1) + A_stringer/2*y[0] + A_stringer*y[1])

#qb2 -------------------------------------------------------------------------------------------------------------------
#positive y, zero z
range2 = np.linspace(0,h/2,100)
qb2 = -Sy/Izz_total * tspar * (range2**2/2 -0)

#qb3-------------------------------------------------------------------------------------------------------------------
# positive y values, negative z values
range3 = np.linspace(0,straight,100)
qb3 = qb1[-1] + qb2[-1] - Sz/Iyy_total *( t* (ca-h/2)/straight*(range3**2/2) - A_stringer*sum(z[2:])) - Sy/Izz_total*( t*(h/2*range3 - h/2/straight*range3**2/2)  + A_stringer*sum(y[2:]))

#qb4 -------------------------------------------------------------------------------------------------------------------
#negative values of z, negative values of y
range4 = np.linspace(0,straight,100)
qb4 = qb3[-1] - Sz/Iyy_total* (t*  (   (ca-h/2)/straight*range4**2/2 + (ca-h/2)*range1   ) - A_stringer*sum(z[2:])) - Sy/Izz_total*(-t*h/straight*(range4**2/2) - A_stringer*sum(y[2:]))

#qb5 -------------------------------------------------------------------------------------------------------------------
#negative y, zero z
range5 = np.linspace(-h/2,0,100)
qb5 = qb4[-1] - Sy/Izz_total*(tspar*range5**2/2)

#qb6 -------------------------------------------------------------------------------------------------------------------
range6 = np.linspace(-np.pi/2,0,100)
qb6 = qb4[-1] - qb5[-1] - Sz/Iyy_total*(t*h**2/4*np.sin(range6) + A_stringer/2*z[0] + A_stringer*z[1]) - Sy/Izz_total*(t*h**2/2*np.cos(range6) - A_stringer/2*y[0] - A_stringer*y[1])
