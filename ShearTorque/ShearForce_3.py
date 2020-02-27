
from MOI import *
from NumericalIntegrator import *
import numpy as np

z = np.dot(z,-1)
#print(z)
Sz =
Sy =
z_sc = np.abs(0.8*10**(-2)) #m
G = 28*10^9
T =

#Shear force analysis

#qb1_Sy ----------------------------------------------------------------------------------------------------------------
range1 = np.linspace(0,np.pi/2,100)
qb1_Sy =  - Sy/Izz_total *(t*h**2/4*(-np.cos(range1)+1)+ A_stringer/2*y[0])

for i in range(len(qb1_Sy)):
    #print(i)
    if range1[i] > np.arccos(z[1]*2/h): #OK
        #print('added A1',z[1])
        qb1_Sy[i] = qb1_Sy[i]  - Sy/Izz_total *( A_stringer*y[1])

#qb1_Sz----------------------------------------------------------------------------------------------------------------
qb1_Sz = -Sz/Iyy_total * (t*h**2/4 *(np.sin(range1))+t*h/2*z_sc*range1 + A_stringer/2*(z[0]+z_sc))
for i in range(len(qb1_Sz)):
    #print(i)
    if range1[i] > np.arccos(z[1]*2/h): #OK
        #print('added A1',z[1])
        qb1_Sz[i] = qb1_Sz[i] -Sz/Iyy_total * (A_stringer*(z[1]+z_sc))
#qb1_total
qb1 = qb1_Sy + qb1_Sz

#qb2_Sy ----------------------------------------------------------------------------------------------------------------
range2 = np.linspace(0,h/2,100)
qb2_Sy = -Sy/Izz_total * tspar * (range2**2/2 -0)

#qb_Sz------------------------------------------------------------------------------------------------------------------
qb2_Sz = -Sz/Iyy_total*tspar*z_sc*range2

#qb2_total -------------------------------------------------------------------------------------------------------------
qb2 =qb2_Sy + qb2_Sz

#qb3_Sy ---------------------------------------------------------------------------------------------------------------
range3 = np.linspace(0,straight,100)
#qb3_const = qb1_Sy[-1] + qb2_Sy[-1]
qb3_Sy = - Sy/Izz_total*( t*(h/2)*range3 - (t*(h/2))/straight*range3**2/2  )

for i in range(len(range3)):
    #print(i)
    for p in range(2,len(z)):
        if range3[i] > z[p]*straight/(-ca + h/2): #OK
            #print('Added A',p,z[p])
            qb3_Sy[i] = qb3_Sy[i] - Sy/Izz_total*( A_stringer*(y[p]))

#qb3_Sz ---------------------------------------------------------------------------------------------------------------
qb3_Sz = - Sz/Iyy_total *( t* (-ca+h/2)/straight*(range3**2/2) + t*z_sc*range3 )

for i in range(len(range3)):
    #print(i)
    for p in range(2,len(z)):
        if range3[i] > z[p]*straight/(-ca + h/2): #OK
            #print('Added A',p,z[p])
            qb3_Sz[i] = qb3_Sz[i] - Sz/Iyy_total *(A_stringer*(z[p] + z_sc))

#qb3_total ------------------------------------------------------------------------------------------------------------
qb3 = qb1[-1] + qb2[-1] + qb3_Sy + qb3_Sz

#qb4_Sy-----------------------------------------------------------------------------------------------------------------
range4 = range3
qb4_Sy = -Sy/Izz_total*(t*(-h/2)/straight*range4**2/2)
for i in range(len(range4)):
    #print(i)
    for p4 in range(6):
        #print (p4)
        if range4[i] > (z[6-p4] + ca -h/2)/((ca-h/2)/straight):
            #print('Added A',6-p4,z[6-p4])
            qb4_Sy[i] = qb4_Sy[i] - Sy/Izz_total*(A_stringer*(-y[6-p4]))

#qb4_Sz ----------------------------------------------------------------------------------------------------------------
qb4_Sz = -Sz/Iyy_total*(t*(ca-h/2)/straight*range4**2/2 + t*(-ca+h/2)*range4 + t*z_sc*range4)
for i in range(len(range4)):
    #print(i)
    for p4 in range(6):
        #print (p4)
        if range4[i] > (z[6-p4] + ca -h/2)/((ca-h/2)/straight):
            #print('Added A',6-p4,z[6-p4])
            qb4_Sz[i] = qb4_Sz[i] - Sz/Iyy_total*(A_stringer*(z[6-p4] + z_sc))
#qb4_total ---------------------------------------------------------------------------------------------------------------
qb4 = qb4_Sy + qb4_Sz+ qb3[-1]

#qb5_Sy -----------------------------------------------------------------------------------------------------------------
range5 = np.linspace(-h/2,0,100)
qb5_Sy = -Sy/Izz_total*(tspar*range5**2/2 - tspar*(-h/2)**2/2)
#range5 = np.linspace(0,-h/2,100)
#qb5_Sy = Sy/Izz_total*(tspar*range5**2/2)

#qb5_Sz-----------------------------------------------------------------------------------
qb5_Sz = -Sz/Iyy_total*tspar*z_sc*range5

#qb5_total-----------------------------------------------------------------------------------
qb5 = qb5_Sy + qb5_Sz - (qb5_Sy[-1]+ qb5_Sz[-1])

#qb6_Sy --------------------------------------------------------------------------------------------------------
range6 = np.linspace(-np.pi/2,0,100)
qb6_Sy = -Sy/Izz_total*t*h**2/4*(-np.cos(range6))

for i in range(len(qb6_Sy)):
    #print(i)
    if range6[i] > np.arcsin(z[1]*2/h) -np.pi/2 : #OK
        #print('added A1',z[1])
        qb6_Sy[i] = qb6_Sy[i]  - Sy/Izz_total *( A_stringer*(-y[1]))

#qb6_Sz ------------------------------------------------------------------------------------------------------------------
qb6_Sz = -Sz/Iyy_total*(t*h**2/4*(np.sin(range6)+1) +t*h/2*z_sc*(range6+np.pi/2))
for i in range(len(qb6_Sz)):
    #print(i)
    if range6[i] > np.arcsin(z[1]*2/h) -np.pi/2 : #OK
        #print('added A1',z[1])
        qb6_Sz[i] = qb6_Sz[i]  - Sz/Iyy_total *(A_stringer*(z[1]+z_sc))

qb6_Sz[-1] += -Sz/Iyy_total*A_stringer/2*(z[0]+z_sc)

#qb6_total --------------------------------------------------------------------------------------------------------------
qb6 = qb6_Sy + qb6_Sz +qb4[-1] - qb5[0]

# # --------PREVIOUS ----------------PREVIOUS ---------------------------------------------------------------------------
#
# #qb1--------------------------------------------------------------------------------------------------------------------
# #positive z values and positive y values
# range1 = np.linspace(0,np.pi/2,100)
# qb1_Sz = -Sz/Iyy_total * (t*h**2/4 *(np.sin(range1)-0) + A_stringer/2*z[0] )
# qb1_Sy =  - Sy/Izz_total *(t*h**2/4*(-np.cos(range1)+1) + A_stringer/2*y[0])
# #qb1 = -Sz/Iyy_total * (t*h**2/4 *(np.sin(range1)-0) + A_stringer/2*z[0] ) - Sy/Izz_total *(t*h**2/4*(-np.cos(range1)+1) + A_stringer/2*y[0])
# qb1 = qb1_Sz + qb1_Sy
#
# for i in range(len(qb1)):
#     #print(i)
#     if range1[i] > np.arccos(z[1]*2/h):
#         #print('added A1',z[1])
#         qb1[i] = qb1[i] -Sz/Iyy_total * (A_stringer*z[1]) - Sy/Izz_total *( A_stringer*y[1])
#
#
#
# #qb2 -------------------------------------------------------------------------------------------------------------------
# #positive y, zero z
# range2 = np.linspace(0,h/2,100)
# qb2 = -Sy/Izz_total * tspar * (range2**2/2 -0)
#
# #qb3-------------------------------------------------------------------------------------------------------------------
# # positive y values, negative z values
# range3 = np.linspace(0,straight,100)
# #qb3 = qb1[-1] + qb2[-1] - Sz/Iyy_total *( t* (-ca+h/2)/straight*(range3**2/2) ) - Sy/Izz_total*( t*(h/2)*range3 - (t*(h/2))/straight*range3**2/2  )
# qb3_const = qb1[-1] + qb2[-1]
# qb3_Sz = - Sz/Iyy_total *( t* (-ca+h/2)/straight*(range3**2/2) )
# qb3_Sy = - Sy/Izz_total*( t*(h/2)*range3 - (t*(h/2))/straight*range3**2/2  )
# qb3 = qb3_const + qb3_Sz + qb3_Sy
#
# for i in range(len(range3)):
#     #print(i)
#     for p in range(2,len(z)):
#         if range3[i] > z[p]*straight/(-ca + h/2):
#             #print('Added A',p,z[p])
#             qb3[i] = qb3[i] - Sz/Iyy_total *( A_stringer*(z[p])) - Sy/Izz_total*( A_stringer*(y[p]))
#
#
# #qb4 -------------------------------------------------------------------------------------------------------------------
# #negative values of z, negative values of y
# range4 = np.linspace(0,straight,100)
# qb4 = qb3[::-1]
#
# #qb5 -------------------------------------------------------------------------------------------------------------------
# #negative y, zero z
# #range5 = np.linspace(0,h/2,100)
# range5 = np.linspace(-h/2,0,100)
# #qb5 = qb4[-1] - Sy/Izz_total*(tspar*(-h/2*range5 + range5**2/2))
# qb5 = qb2[::-1]
#
# #qb6 -------------------------------------------------------------------------------------------------------------------
# range6 = np.linspace(-np.pi/2,0,100)
# qb6 = qb1[::-1]


#moment around point 0 -------------------------------------------------------------------------------------------------
integral1_1 = comp_num_int(np.linspace(0,np.pi/2,100),qb1*(h/2)**2) #integral of qb1*(h/2)**2*dTheta from 0 to pi/2
integral1_2 = comp_num_int(np.linspace(-np.pi/2,0,100),qb6*(h/2)**2) #integral of qb6*(h/2)**2*dtetha from -pi/2 to 0
integral1 = integral1_1 + integral1_2
integral2_1 =comp_num_int(np.linspace(0,straight,100),qb3*np.cos(alpha)*h/2) #integral of qb3*np.cos(alpha)*h/2*ds from 0 to straight
integral2_2 = comp_num_int(np.linspace(0,straight,100),qb4*np.cos(alpha)*h/2) #integral of qb4*np.cos(alpha)*h/2*ds from 0 to straight
integral2 = integral2_1 + integral2_2
#0 = Sy*z_sc + integral1 + integral2 + 2*Am_cell1*qso1 + 2*Am_cell2*qso2 #equation1 #######!!!!!!!!!!!!!!!REMEMBER TO CHANGE

#rate of twist----------------------------------------------------------------------------------------------------------
#cell 1
integral3= comp_num_int(np.linspace(0,np.pi/2,100),qb1*(h/2)) #integral of qb1*h/2*dtheta from 0 to pi/2
integral4 = comp_num_int(np.linspace(h/2,0,100),-qb2)  #integral of qb2*-dy from h/2 to 0
integral5 = comp_num_int(np.linspace(0,-h/2,100),-qb5) #integral of qb5*-dy from 0 to -h/2
integral6 = comp_num_int(np.linspace(-np.pi/2,0,100),qb6*h/2) #integral of qb6*h/2*dtheta from -pi/2 to 0

#G*dtheta = 1/(2*Am_cell1) *((integral3+qso1)/t + (integral4+qso1-qso2)/tspar + (integral5+qso1-qso2)/tspar + (integral6+qso1)/t)  #equation2

#cell2
integral7 = comp_num_int(np.linspace(0,h/2,100),qb2) #integral of qb2*dy from 0 to h/2
integral8 = comp_num_int(np.linspace(0,straight,100),qb3) #integral of qb3*ds from 0 to straight
integral9 = comp_num_int(np.linspace(0,straight,100),qb4) #integral of qb4*ds from 0 to straight
integral10= comp_num_int(np.linspace(-h/2,0,100),qb5) #integral of qb5*dy from -h/2 to 0

#G*dtheta = 1/(2*Am_cell2)*((integral7+qso2-qso1)/tspar + (integral8+qso2)/t + (integral9+qso2)/t + (integral10+qso2-qso1)/tspar) #equation3

#solving matrix of 3 equations
a = np.array( [[2*Am_cell1,2*Am_cell2,0], [1/(2*Am_cell1)*(np.pi*h/4/t + (h/2)/tspar + (h/2)/tspar +(np.pi*h/4)/t), 1/(2*Am_cell1)*(-(h/2)/tspar - (h/2)/tspar), -G],[1/(2*Am_cell2)*((-h/2)/tspar -(h/2)/tspar), 1/(2*Am_cell2)*((h/2)/tspar+ straight/t + straight/t + (h/2)/tspar), -G]])
b = np.array([-Sy*z_sc - integral1 - integral2, -1/(2*Am_cell1)*(integral3/t + integral4/tspar + integral5/tspar + integral6/tspar), -1/(2*Am_cell2)*(integral7/tspar + integral8/t + integral9/t +integral10/tspar)])
matrix_force = np.linalg.solve(a,b) #0th entry qso1, 1th entry qso2, 2nd entry, dtheta/dx

#Torque analysis
#T = 1
#T = 2*Am_cell1*qso1_t + 2*Am_cell2*qso2_t #equation1
#G*dtheta/dx = 1/(2*Am_cell1)*((qso1_t *np.pi*(h/2)/t + (qso1_t-qso2_t)*h/tspar)) #equation2
#G*dtheta/dx = 1/(2*Am_cell2)*((qso2_2*straight/t + (qso2_t-qso1_t)*h/tspar)) #equation3

c = np.array([[2*Am_cell1,2*Am_cell2,0], [ 1/(2*Am_cell1)*((np.pi*(h/2)/t) +h/tspar) , 1/(2*Am_cell1)*(-h/tspar), -G ] , [1/(2*Am_cell2)*(-h/tspar), 1/(2*Am_cell2)*(h/tspar + 2*straight/t), -G]])
d = np.array([T,0,0])

matrix_torque = np.linalg.solve(c,d) #0th entry is qso1_t, 1 entry is qso2_t , second entry is dtheta/dx

#total shear flow distributions
q1_total= qb1 + matrix_force[0] - matrix_torque[0]
q2_total= qb2 - matrix_force[0] + matrix_force[1] + matrix_torque[0] - matrix_torque[1]
q3_total = qb3 + matrix_force[1] - matrix_torque[1]
q4_total = qb4 + matrix_force[1] - matrix_torque[1]
q5_total = qb5 - matrix_force[0] + matrix_force[1] + matrix_torque[0] - matrix_torque[1]
q6_total = qb6 + matrix_force[0] - matrix_torque[0]

#z-y-q values
q1_zvalues = np.linspace(h/2,0,100)
q1_yvalues =  np.sqrt((h/2)**2-q1_zvalues**2)
q2_zvalues =  np.zeros(100)
q2_yvalues =np.linspace(0,h/2,100)
q3_zvalues = -np.linspace(0,ca-h/2,100)
q3_yvalues = graph_straight1
q4_zvalues = -np.linspace(ca-h/2,0,100)
q4_yvalues = graph_straight1 -h/2*np.ones(100)
q5_zvalues = np.zeros(100)
q5_yvalues = np.linspace(-h/2,0,100)
q6_zvalues = -np.linspace(0,-h/2,100)
q6_yvalues = -np.sqrt((h/2)**2-q6_zvalues**2)

q_zvalues = [] #list if all z values following the shear flow direction as in sketch
q_zvalues.extend(q1_zvalues)
q_zvalues.extend(q2_zvalues)
q_zvalues.extend(q3_zvalues)
q_zvalues.extend(q4_zvalues)
q_zvalues.extend(q5_zvalues)
q_zvalues.extend(q6_zvalues)

q_yvalues = [] #list of all y values following the shear flow direction as in sketch
q_yvalues.extend(q1_yvalues)
q_yvalues.extend(q2_yvalues)
q_yvalues.extend(q3_yvalues)
q_yvalues.extend(q4_yvalues)
q_yvalues.extend(q5_yvalues)
q_yvalues.extend(q6_yvalues)

q_qvalues = [] #list of all q values following the shear flow direction as in sketch
q_qvalues.extend(q1_total)
q_qvalues.extend(q2_total)
q_qvalues.extend(q3_total)
q_qvalues.extend(q4_total)
q_qvalues.extend(q5_total)
q_qvalues.extend(q6_total)


#maximum stress
# tau= qmax/tmin
tau_values = [] #list of all tau values following the shear flow direction as in sketch
tau_values.extend(q1_total/t)
tau_values.extend(q2_total/tspar)
tau_values.extend(q3_total/t)
tau_values.extend(q4_total/t)
tau_values.extend(q5_total/tspar)
tau_values.extend(q6_total/t)

#maximum shear stress in the figure
tau_max = np.max(tau_values)

#polar moment of inertia
J = T/(G*matrix_torque[2])

