from FBD_Folder.Macaulay import Macaulay
from FBD_Folder.Constants import *
from AeroInt import *
from FBDvalues import *

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

def My(x):
    return Macaulay(x1,Rz1,1).result(x) + Macaulay(x2,Rz2,1).result(x) + Macaulay(x3,Rz3,1).result(x) + Macaulay(x2-0.5*xa,Rj,1).result(x) + Macaulay(x2+0.5*xa,P,1).result(x)

def Mz(x):
    return Macaulay(x1,-Ry1,1).result(x) + Macaulay(x2,-Ry2,1).result(x) + Macaulay(x3,-Ry3,1).result(x) + Macaulay(x2-0.5*xa,-Rj,1).result(x) + Macaulay(x2+0.5*xa,-P*np.sin(beta),1).result(x) - IntegrateX(x,2,0)

def Tx(x):
    return Macaulay(x1,Ry1*zhat,0).result(x) + Macaulay(x2,Ry2*zhat,0).result(x) + Macaulay(x3,Ry3*zhat,0).result(x) + Macaulay(x2-0.5*xa,Rj*np.sin(beta)*zhat,0).result(x) + Macaulay(x2-0.5*xa,-Rj*np.cos(beta)*ha/2,0).result(x) + Macaulay(x2+0.5*xa,-P*np.cos(beta)*ha/2,0).result(x) + Macaulay(x2-0.5*xa,P*np.sin(beta)*(zhat+ ha/2),0).result(x)+IntegrateX(x,1,1)-zhat*IntegrateX(x,1,0)

def Sy(x):
    return Macaulay(x1,-Ry1,0).result(x) + Macaulay(x2,-Ry2,0).result(x) + Macaulay(x3,-Ry3,0).result(x) + Macaulay(x2-0.5*xa,-Rj,0).result(x) + Macaulay(x2+0.5*xa,-P*np.sin(beta),0).result(x) - IntegrateX(x,1,0)

def Sz(x):
    return Macaulay(x1,Rz1,0).result(x) + Macaulay(x2,Rz2,0).result(x) + Macaulay(x3,Rz3,0).result(x) + Macaulay(x2-0.5*xa,Rj,0).result(x) + Macaulay(x2+0.5*xa,P,0).result(x)

def vy(x):
    return (-1/(E*Izz))*(-IntegrateX(x,4,0) + Macaulay(x1,-Ry1/6,3).result(x)+ Macaulay(x2,-Ry2/6,3).result(x) +  Macaulay(x3,-Ry3/6,3).result(x)  + Macaulay(x2+0.5*xa,-P*np.sin(beta)/6,3).result(x)  + Macaulay(x2-0.5*xa,-Rj*np.sin(beta)/6,3).result(x)  ) + C1*x + C2

def vz(x):
    return (-1/(E*Iyy)) * ( Macaulay(x1,Rz1/6,3).result(x) + Macaulay(x2,Rz2/6,3).result(x) + Macaulay(x3,Rz3/6,3).result(x) +  Macaulay(x2-0.5*xa,Rj*np.cos(beta)/6,3).result(x) +  Macaulay(x2+0.5*xa,P/6,3)   )  + C3*x + C4

def theta(x):
    return (1/(G*J))*(IntegrateX(x,2,1) -zhat*IntegrateX(x,2,0) + Macaulay(x1,Ry1*zhat,1).result(x) + Macaulay(x2,Ry2*zhat,1).result(x) + Macaulay(x3,Ry3*zhat,1).result(x)  + Macaulay(x2-0.5*xa,Rj*np.sin(beta)*zhat,1).result(x) + Macaulay(x2+0.5*xa,P*np.sin(beta)*(zhat+ ha/2),1).result(x) + Macaulay(x2+0.5*xa,-P*np.cos(beta)*ha/2,1).result(x))+C5


