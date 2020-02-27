from FBD_Folder.Macaulay import Macaulay
from FBD_Folder.Constants import *
from AeroInt import *
from FBDvalues import *   #make sure not V

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

#Integration on/off   - on = 1, off = 0
Iswitch = 1

#sign convention
scv = 1  #Th
scf = 1  #T

beta = np.radians(beta)

def My(x):
    return Macaulay(x1,Rz1,1).result(x) + Macaulay(x2,Rz2,1).result(x) + Macaulay(x3,Rz3,1).result(x) + Macaulay(x2-0.5*xa,Rj*np.cos(beta),1).result(x) + Macaulay(x2+0.5*xa,P*np.cos(beta),1).result(x)

def Mz(x):
    return Macaulay(x1,-Ry1,1).result(x) + Macaulay(x2,-Ry2,1).result(x) + Macaulay(x3,-Ry3,1).result(x) + Macaulay(x2-0.5*xa,-Rj*np.sin(beta),1).result(x) + Macaulay(x2+0.5*xa,-P*np.sin(beta),1).result(x) - Iswitch*IntegrateX(x,2,0)

def Tx(x):
    return Macaulay(x1, Ry1*-zhat, 0).result(x) + Macaulay(x2, Ry2*-zhat, 0).result(x) + Macaulay(x3,Ry3*-zhat,0).result(x) + -1*(Macaulay(x2-(xa/2), Rj*((ha/2)-zhat)*np.sin(beta),0).result(x) + Macaulay(x2-(xa/2),-1*Rj*np.cos(beta)*(ha/2),0).result(x) + Macaulay(x2+(xa/2), -1*P*np.cos(beta)*(ha/2), 0).result(x) + Macaulay(x2+(xa/2), P*np.sin(beta)*((ha/2)-zhat), 0).result(x)) +Iswitch*IntegrateX(x,1,1)-zhat*Iswitch*IntegrateX(x,1,0)

def Sy(x): #check
    return Macaulay(x1,-Ry1,0).result(x) + Macaulay(x2,-Ry2,0).result(x) + Macaulay(x3,-Ry3,0).result(x) + Macaulay(x2-0.5*xa,-Rj*np.sin(beta),0).result(x) + Macaulay(x2+0.5*xa,-P*np.sin(beta),0).result(x) - Iswitch*IntegrateX(x,1,0)

def Sz(x): #check
    return Macaulay(x1,Rz1,0).result(x) + Macaulay(x2,Rz2,0).result(x) + Macaulay(x3,Rz3,0).result(x) + Macaulay(x2-0.5*xa,Rj*np.cos(beta),0).result(x) + Macaulay(x2+0.5*xa,P*np.cos(beta),0).result(x)

def vy(x):
    return (-1/(E*Izz))*(-Iswitch*IntegrateX(x,4,0) + Macaulay(x1,-Ry1/6,3).result(x)+ Macaulay(x2,-Ry2/6,3).result(x) +  Macaulay(x3,-Ry3/6,3).result(x)  + Macaulay(x2+0.5*xa,-P*np.sin(beta)/6,3).result(x)  + Macaulay(x2-0.5*xa,-Rj*np.sin(beta)/6,3).result(x)  ) + C1*x + C2

def vz(x):
    return (-1/(E*Iyy)) * ( Macaulay(x1,Rz1/6,3).result(x) + Macaulay(x2,Rz2/6,3).result(x) + Macaulay(x3,Rz3/6,3).result(x) +  Macaulay(x2-0.5*xa,Rj*np.cos(beta)/6,3).result(x) +  Macaulay(x2+0.5*xa,P*np.cos(beta)/6,3).result(x)   )  + C3*x + C4

def theta(x):
    return (1/(G*J))*(  Macaulay(x1, Ry1*-zhat, 1).result(x) + Macaulay(x2, Ry2*-zhat, 1).result(x) + Macaulay(x3,Ry3*-zhat,1).result(x) + -1*(Macaulay(x2-(xa/2), Rj*((ha/2)-zhat)*np.sin(beta),1).result(x) + Macaulay(x2-(xa/2),-1*Rj*np.cos(beta)*(ha/2),1).result(x) + Macaulay(x2+(xa/2), -1*P*np.cos(beta)*(ha/2), 1).result(x) + Macaulay(x2+(xa/2), P*np.sin(beta)*((ha/2)-zhat), 1).result(x)) +Iswitch*IntegrateX(x,2,1)-zhat*Iswitch*IntegrateX(x,2,0))

def vyder(x): #CHECK
    return (-1/(E*Izz))*(-Iswitch*IntegrateX(x,3,0) + Macaulay(x1,-Ry1/2,2).result(x)+ Macaulay(x2,-Ry2/2,2).result(x) +  Macaulay(x3,-Ry3/2,2).result(x)  + Macaulay(x2+0.5*xa,-P*np.sin(beta)/2,2).result(x)  + Macaulay(x2-0.5*xa,-Rj*np.sin(beta)/2,2).result(x)  ) + C1

def vzder(x):  #CHECK
    return (-1/(E*Iyy)) * ( Macaulay(x1,Rz1/2,2).result(x) + Macaulay(x2,Rz2/2,2).result(x) + Macaulay(x3,Rz3/2,2).result(x) +  Macaulay(x2-0.5*xa,Rj*np.cos(beta)/2,2).result(x) +  Macaulay(x2+0.5*xa,P*np.cos(beta)/2,2).result(x)   )  + C3


print(vz(x3))