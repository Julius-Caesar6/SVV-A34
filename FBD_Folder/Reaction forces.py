from FBD_Folder.Macaulay import Macaulay
import numpy as np
from AeroInt import *
from FBD_Folder.Constants import *
from pandas import *

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

def reaction_solver(zhat, c, ha, d1, d2, d3, x1, x2, x3, xa, la, beta, P, E, Izz, Iyy, G, J): #TODO : ADJUST FOR UNITS!! (if needed?)
    beta = np.radians(beta)
    # First equation My:
 #   equations[0] = [Macaulay(x1,1,1).result(c), 0, Macaulay(x2,1,1).result(c)]
 #   [Rz1, Ry1, Rz2, Ry2, Rz3, Ry3, Rj, C1, C2, C3, C4, C5]
    row1 = [Macaulay(x1,1,1).result(la), 0,  Macaulay(x2,1,1).result(la), 0, Macaulay(x3,1,1).result(la), 0, Macaulay(x2-(xa/2), np.cos(beta), 1).result(la), 0, 0, 0, 0, 0]
    #b:
    brow1 = Macaulay(x2+(xa/2),-np.cos(beta)*P,1).result(la)

   # Second equation Mz:
    row2 = [0, Macaulay(x1, -1, 1).result(la), 0, Macaulay(x2, -1 ,1).result(la), 0, Macaulay(x3,-1,1).result(la), Macaulay(x2-(xa/2), -np.sin(beta), 1).result(la), 0, 0, 0, 0, 0]
    #b:
    brow2 = Macaulay(x2+(xa/2),P*np.sin(beta), 1).result(la) + IntegrateX(la,2,0)

    # Third equation Tx:
    row3 = [0, Macaulay(x1,zhat,0).result(la), 0, Macaulay(x2, zhat, 0).result(la), 0, Macaulay(x3, zhat, 0).result(la), Macaulay(x2-(xa/2), zhat*np.sin(beta), 0).result(la), 0, 0, 0, 0, 0]
    #b:
    brow3 = Macaulay(x2+(xa/2), P*ha*np.cos(beta)/2, 0).result(la) - Macaulay(x2+(xa/2), P*np.sin(beta)*(zhat+(ha/2)), 0).result(la) - IntegrateX(la,1,1) + zhat*IntegrateX(la,1,0)

    # Fourth equation Sy:
    row4 = [0, Macaulay(x1, -1, 0).result(la), 0, Macaulay(x2, -1,0).result(la), 0, Macaulay(x3, -1, 0).result(la), Macaulay(x2-(xa/2), -np.sin(beta),0).result(la), 0 ,0, 0, 0, 0]
    #b:
    brow4 = Macaulay(x2+(xa/2), P*np.sin(beta),0).result(la)  - IntegrateX(la,1,0)

    # Fifth equation Sz:
    row5 = [Macaulay(x1, 1,0).result(la), 0, Macaulay(x2, 1, 0).result(la), 0, Macaulay(x3,1,0).result(la), 0, Macaulay(x2-(xa/2), np.cos(beta),0).result(la), 0, 0, 0, 0, 0]
    #b:
    brow5 = Macaulay(x2+(xa/2), -P, 0).result(la)

    # Sixth equation Vy(x1) - theta(x1)zhat
    row6 = [0,0,0,0,0,0,0, x1, 1, 0, 0, -zhat]
    #b:
    brow6 = (-1/(E*Izz))*IntegrateX(x1,4,0) + (zhat/(G*J))*IntegrateX(x1,2,1) - (zhat**2/(G*J))*IntegrateX(x1,2,0) + d1*np.cos(beta)

    #   [Rz1, Ry1, Rz2, Ry2, Rz3, Ry3, Rj, C1, C2, C3, C4, C5]

    # Seventh equation Vy(x2..)
    row7 = [0, (Macaulay(x1, 1/(6*E*Izz), 3).result(x2)) - (Macaulay(x1, (zhat**2)/(G*J), 1).result(x2)), 0, 0, 0, 0, (Macaulay(x2-(xa/2), np.sin(beta)/(6*E*Izz), 3).result(x2)) - (Macaulay(x2-(xa/2), (zhat**2)*np.sin(beta)/(G*J), 1).result(x2)), x2, 1, 0, 0, -zhat]
    #b:
    brow7 = (-1/(E*Izz))*IntegrateX(x2,4,0) +(zhat/(G*J))*IntegrateX(x2,2,1) - (zhat**2/(G*J))*IntegrateX(x2,2,0)

    # Eight equation Vy(x3..)
    row8 = [0, (Macaulay(x1, 1/(6*E*Izz), 3).result(x3))-(Macaulay(x1, (zhat**2)/(G*J), 1).result(x3)), 0, (Macaulay(x2, 1/(6*E*Izz), 3).result(x3))-(Macaulay(x2, (zhat**2)/(G*J), 1).result(x3)), 0, 0, (Macaulay(x2-(xa/2), np.sin(beta)/(6*E*Izz), 3).result(x3)) - (Macaulay(x2-(xa/2), (zhat**2)*np.sin(beta)/(G*J), 1).result(x3)), x3, 1, 0, 0, -zhat]
    #b:
    brow8 = P*(Macaulay(x2+(xa/2), np.sin(beta)/(-6*E*Izz),3).result(x3) + Macaulay(x2+(xa/2), (zhat*np.sin(beta)*(zhat+(ha/2)))/(G*J),1).result(x3) - Macaulay(x2+(xa/2), (zhat*np.cos(beta)*(ha/2))/(G*J), 1).result(x3)) + (-1/(E*Izz))*IntegrateX(x3,4,0)  + (zhat/(G*J))*IntegrateX(x3,2,1) - (zhat**2/(G*J))*IntegrateX(x3,2,0)  + d3*np.cos(beta)

    #Ninth equation Vz(x3):
    row9 = [Macaulay(x1, -1/(6*E*Iyy), 3).result(x3), 0, Macaulay(x2, -1/(6*E*Iyy), 3).result(x3), 0, 0, 0, Macaulay(x2-(xa/2), (-np.cos(beta))/(6*E*Iyy), 3).result(x3), 0, 0, x3, 1, 0]
    #b:
    brow9 = d3*np.sin(beta) + Macaulay(x2-(xa/2), np.cos(beta)*P/(6*E*Iyy), 3).result(x3)

    #Tenth equation Vz(x2):
    row10 = [Macaulay(x1, -1/(6*E*Iyy), 3).result(x2), 0 ,0 ,0 , 0, 0, Macaulay(x2-(xa/2), (-np.cos(beta))/(6*E*Iyy), 3).result(x2), 0, 0, x2, 1, 0]
    #b:
    brow10 = Macaulay(x2-(xa/2), np.cos(beta)*P/(6*E*Iyy),3).result(x2)

    #Eleventh equation Vz(x1):
    row11 = [0,0,0,0,0,0,0,0,0,x1, 1,0]
    #b:
    brow11 = d1*np.sin(beta)

    #Twelfth equation weird theta one:
    row12 = [Macaulay(x1, (np.cos(beta))/(-E*Iyy*6), 3).result(x2-(xa/2)), Macaulay(x1, np.sin(beta)/(6*E*Izz), 3).result(x2-(xa/2)) + Macaulay(x1, (-ha*np.cos(beta)*zhat)/(2*G*J), 1).result(x2-(xa/2)) + Macaulay(x1, ((zhat**2)*np.sin(beta))/(G*J), 1).result(x2-(xa/2)), 0,0,0,0,0, np.sin(beta)*(x2-(xa/2)), np.sin(beta), np.cos(beta)*(x2-(xa/2)), np.cos(beta), (zhat*np.sin(beta)) - ((ha/2)*np.cos(beta))]
    #b:
    brow12 = (-np.sin(beta)/(E*Izz))*IntegrateX(x2-0.5*xa,4,0) - (zhat*np.sin(beta)/(G*J))*IntegrateX(x2-0.5*xa,2,1) + (np.sin(beta)*zhat**2/(G*J))*IntegrateX(x2-0.5*xa,2,0) + (ha*np.cos(beta)/(2*G*J))*IntegrateX(x2-0.5*xa,2,1) - (ha*np.cos(beta)*zhat/(2*G*J))*IntegrateX(x2-0.5*xa,2,0)

    equations = np.array([row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11, row12])
    resultants = np.array([brow1, brow2, brow3, brow4, brow5, brow6, brow7, brow8, brow9, brow10, brow11, brow12])

    df = DataFrame(equations)
  #  xvalues = np.linalg.solve(equations,resultants)
    return df



print(reaction_solver(0.1, Ca, ha, d1, d2, d3, x1, x2, x3, xa, la, beta, P, E, 1.0280189203385745e+05, 8.651211860639685e+05 , G, 0.00022293131689593327e+05))