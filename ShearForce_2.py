#Shear force analysis
from MOI import *
import numpy as np

z = np.dot(z,-1)

Sz = 0
Sy = 1
z_sc = 1
G = 1

#qb1--------------------------------------------------------------------------------------------------------------------
#positive z values and positive y values
range1 = np.linspace(0,np.pi/2,100)
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

#moment around point 0 -------------------------------------------------------------------------------------------------
integral1 = 1 #integral of qb1*(h/2)**2*dTheta from 0 to pi/2
integral2 =1 #integral of qb3*cos(alpha)*h/2*ds from 0 to straight

#0 = Sy*z_sc + 2*integral1 + 2*integral2 + 2*Am_cell1*qso1 + 2*Am_cell2*qso2 #equation1

#rate of twist----------------------------------------------------------------------------------------------------------
#cell 1
integral3= 1 #integral of qb1*h/2*dtheta from 0 to pi/2
integral4 = 1 #integral of qb2*-dy from h/2 to 0
integral5 = 1 #integral of qb5*-dy from 0 to -h/2
integral6 = 1#integral of qb6*h/2*dtheta from -pi/2 to 0

#G*dtheta = 1/(2*Am_cell1) *((integral3+qso1)/t + (integral4+qso1-qso2)/tspar + (integral5+qso1-qso2)/tspar + (integral6+qso1)/t)  #equation2

#cell2
integral7 = 1 #integral of qb2*dy from 0 to h/2
integral8 =1 #integral of qb3*ds from 0 to straight
integral9 =1 #integral of qb4*ds from 0 to straight
integral10=1 #integral of qb5*dy from -h/2 to straight

#G*dtheta = 1/(2*Am_cell2)*((integral7+qso2-qso1)/tspar + (integral8+qso2)/t + (integral9+qso2)/t + (integral10+qso2-qso1)/tspar) #equation3

#solving matrix of 3 equations
a = np.array( [[2*Am_cell1,2*Am_cell2,0], [1/(2*Am_cell1)*(1/t + 1/tspar + 1/tspar +1/t), 1/(2*Am_cell1)*(-1/tspar - 1/tspar), -G],[1/(2*Am_cell2)*(-1/tspar -1/tspar), 1/(2*Am_cell2)*(1/tspar+ 1/t + 1/t + 1/tspar), -G]])
b = np.array([-Sy*z_sc - 2*integral1 - 2*integral2, -1/(2*Am_cell1)*(integral3/t + integral4/tspar + integral5/tspar + integral6/tspar), -1/(2*Am_cell2)*(integral7/tspar + integral8/t + integral9/t +integral10/tspar)])
matrix_force = np.linalg.solve(a,b) #0th entry qso1, 1th entry qso2, 2nd entry, dtheta/dx

#Torque analysis
T = 1
#T = 2*Am_cell1*qso1_t + 2*Am_cell2*qso2_t #equation1
#G*dtheta/dx = 1/(2*Am_cell1)*((qso1_t *np.pi*(h/2)/t + (qso1_t-qso2_t)*h/tspar)) #equation2
#G*dtheta/dx = 1/(2*Am_cell2)*((qso2_2*straight/t + (qso2_t-qso1_t)*h/tspar)) #equation3

c = np.array([[2*Am_cell1,2*Am_cell2,0], [ 1/(2*Am_cell1)*(np.pi*(h/2)/t), 1/(2*Am_cell1)*-h/tspar, -G ] , [1/(2*Am_cell2)*(-h/tspar), 1/(2*Am_cell2)*(h/tspar + 2*straight/t), -G]])
d = np.array([-T,0,0])

matrix_torque = np.linalg.solve(c,d) #0th entry is qso1_t, 1 entry is qso2_t , second entry is dtheta/dx

#total shear flow distributions
qb1_total= qb1 + matrix_force[0] - matrix_torque[0]
qb2_total= qb2 - matrix_force[0] + matrix_force[1] - matrix_torque[0] + matrix_torque[1]
qb3_total = qb3 + matrix_force[1] - matrix_torque[1]
qb4_total = qb4 + matrix_force[1] - matrix_torque[1]
qb5_total = qb5 - matrix_force[0] + matrix_force[1] + matrix_torque[0] - matrix_torque[1]
qb6_total = qb6 + matrix_force[0] - matrix_torque[0]

#z-y-q values
qb1_zvalues = np.linspace(h/2,0,100)
qb1_yvalues = c2y = np.sqrt((h/2)**2-qb1_zvalues**2)
qb2_zvalues =  np.zeros(100)
qb2_yvalues =np.linspace(0,h/2,100)
qb3_zvalues = np.linspace(0,ca-h/2,100)
qb3_yvalues = h/2 - (h/2)/straight*qb3_zvalues
plt.plot(qb3_zvalues,qb3_yvalues)