from FBD_Folder.Macaulay import Macaulay
import numpy as np
from FBD_Folder.Constants import *

#Solving reaction forces using Ax = b
# A = equations
# x = unknowns
# b = boundary conditions


# Unknowns = np.array([[
# Rz1,
# Ry1,
# Rz2,
# Ry2,
# Rz3,
# Ry3,
# Rj,
# C1,
# C2,
# C3,
# C4,
# C5,
# ]])

def reaction_solver(zhat, c, B, ha, d1, d2, d3, x1, x2, x3, xa, la, beta, P, E, Izz, Iyy, G, J): #TODO : ADJUST FOR UNITS!!
    beta = np.radians(beta)
    equations = np.zeros((12,12))
    resultants = np.zeros((12,1))
    # First equation My:
 #   equations[0] = [Macaulay(x1,1,1).result(c), 0, Macaulay(x2,1,1).result(c)]
 #   [Rz1, Ry1, Rz2, Ry2, Rz3, Ry3, Rj, C1, C2, C3, C4, C5]
    row1 = [Macaulay(x1,1,1).result(la), 0,  Macaulay(x2,1,1).result(la), 0, Macaulay(x3,1,1).result(la), 0, Macaulay(x2-(xa/2), np.cos(beta), 1).result(la), 0, 0, 0, 0, 0]
    #b:
    brow1 = [Macaulay(x2+(xa/2),-P,1).result(la)]

   # Second equation Mz:
    row2 = [0, Macaulay(x1, -1, 1).result(la), 0, Macaulay(x2, -1 ,1).result(la), 0, Macaulay(x3,-1,1).result(la), Macaulay(x2-(xa/2), -np.sin(beta), 1).result(la), 0, 0, 0, 0, 0]
    #b:
    brow2 = [Macaulay(x2+(xa/2),P*np.sin(beta), 1).result(la) + """integral"""] #TODO add integral

    # Third equation Tx:
    row3 = [0, Macaulay(x1,zhat,0).result(la), 0, Macaulay(x2, zhat, 0).result(la), 0, Macaulay(x3, zhat, 0).result(la), Macaulay(x2-(xa/2), zhat*np.sin(beta), 0).result(la), 0, 0, 0, 0, 0]
    #b:
    brow3 = [Macaulay(x2+(xa/2), P*ha*np.sin(beta)/2, 0).result(la) - Macaulay(x2+(xa/2), P*np.sin(beta)*(zhat+(ha/2)), 0).result(la) - """Integral"""] #TODO add integral

    # Fourth equation Sy:
    row4 = [0, Macaulay(x1, -1, 0).result(la), 0, Macaulay(x2, -1,0).result(la), 0, Macaulay(x3, -1, 0).result(la), Macaulay(x2-(xa/2), -np.sin(beta),0).result(la), 0 ,0, 0, 0, 0]
    #b:
    brow4 = [Macaulay(x2+(xa/2), P*np.sin(beta),0).result(la)  - """Integral"""] #TODO add loads

    # Fifth equation Sz:
    row5 = [Macaulay(x1, 1,0).result(la), 0, Macaulay(x2, 1, 0).result(la), 0, Macaulay(x3,1,0).result(la), 0, Macaulay(x2-(xa/2), np.cos(beta),0).result(la), 0, 0, 0, 0, 0]
    #b:
    brow5 = [Macaulay(x2+(xa/2), -P, 0).result(la)] #TODO add loads

    # Sixth equation Vy(x1) - theta(x1)zhat
    row6 = [0,0,0,0,0,0,0, x1, 1, 0, 0, -zhat]
    #b:
    brow6 = ["integral1" + "integral2" + d1*np.cos(beta)] #TODO add loads

    #   [Rz1, Ry1, Rz2, Ry2, Rz3, Ry3, Rj, C1, C2, C3, C4, C5]

    # Seventh equation Vy(x2..)
    row7 = [0, (Macaulay(x1, 1/(6*E*Izz), 3).result(x2)) - (Macaulay(x1, (zhat**2)/(G*J), 1).result(x2)), 0, 0, 0, 0, (Macaulay(x2-(xa/2), np.sin(beta)/(6*E*Izz), 3).result(x2)) - (Macaulay(x2-(xa/2), (zhat**2)*np.sin(beta)/(G*J), 1).result(x2)), x2, 1, 0, 0, -zhat]
    #b:
    brow7 = ["integral1" +"integral2"] #TODO add loads

    # Eight equation Vy(x3..)
    row8 = [0, (Macaulay(x1, 1/(6*E*Izz), 3).result(x3))-(Macaulay(x1, (zhat**2)/(G*J), 1).result(x3)), 0, (Macaulay(x2, 1/(6*E*Izz), 3).result(x3))-(Macaulay(x2, (zhat**2)/(G*J), 1).result(x3)), 0, 0, (Macaulay(x2-(xa/2), np.sin(beta)/(6*E*Izz), 3).result(x3)) - (Macaulay(x2-(xa/2), (zhat**2)*np.sin(beta)/(G*J), 1).result(x3)), x3, 1, 0, 0, -zhat]
    #b:
    brow8 = [P*(Macaulay(x2+(xa/2), np.sin(beta)/(-6*E*Izz),3).result(x3) + Macaulay(x2+(xa/2), (zhat*np.sin(beta)*(zhat+(ha/2)))/(G*J),1).result(x3) + Macaulay(x2+(xa/2), (zhat*np.cos(beta)*(ha/2))/(-G*J), 1).result(x3)) + "integral" + "integral"  + d3*np.cos(beta)] #TODO add loads

    #Ninth equation Vz(x3):
    row9 = [Macaulay(x1, -1/(6*E*Iyy), 3).result(x3), 0, Macaulay(x2, -1/(6*E*Iyy), 3).result(x3), 0, 0, Macaulay(x2-(xa/2), (-np.cos(beta))/(6*E*Iyy), 3).result(x3), 0, 0, x3, 1, 0]
    #b:
    brow9 = [d3*np.sin(beta) + Macaulay(x2-(xa/2), P/(6*E*Iyy), 3).result(x3)] #TODO add loads

    #Tenth equation Vz(x2):
    row10 = [Macaulay(x1, -1/(6*E*Iyy), 3).result(x2), 0 ,0 ,0 , 0, 0, Macaulay(x2-(xa/2), (-np.cos(beta))/(6*E*Iyy), 3).result(x2), 0, 0, x2, 1, 0]
    #b:
    brow10 = [Macaulay(x2-(xa/2), P/(6*E*Iyy),3).result(x2)] #TODO add loads

    #Eleventh equation Vz(x1):
    row11 = [0,0,0,0,0,0,0,0,0,x1, 1,0]
    #b:
    brow11 = [d1*np.sin(beta)]

    #Twelfth equation weird theta one:
    row12 = [Macaulay(x1, (np.cos(beta))/(-E*Iyy*2), 3).result(x2-(xa/2)), Macaulay(x1, np.sin(beta)/(6*E*Izz), 3).result(x2-(xa/2)) + Macaulay(x1, (-ha*np.cos(beta)*zhat)/(2*G*J), 1).result(x2-(xa/2)) + Macaulay(x1, ((zhat**2)*np.sin(beta))/(G*J), 1).result(x2-(xa/2)), 0,0,0,0,0, np.sin(beta)*(x2-(xa/2)), np.sin(beta), np.cos(beta)*(x2-(xa/2)), np.cos(beta), (zhat*np.sin(beta)) - ((ha/2)*np.cos(beta))]
    #b:
    brow12 = ["loads of integrals"]

    equations[0] = row1
    equations[1] = row2
    equations[2] = row3
    equations[3] = row4
    equations[4] = row5
    equations[5] = row6
    equations[6] = row7
    equations[7] = row8
    equations[8] = row9
    equations[9] = row10
    equations[10] = row11
    equations[11] = row12



