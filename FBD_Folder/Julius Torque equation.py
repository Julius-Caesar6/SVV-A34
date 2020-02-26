from FBD_Folder.Macaulay import Macaulay
from FBD_Folder.Constants import *
from FBD_Folder.FBDvalues import *
import numpy as np

def Tx(x):
    return Macaulay(x1, Ry1*-zhat, 0).result(x) + Macaulay(x2, Ry2*-zhat, 0).result(x) + Macaulay(x3,Ry3*-zhat,0).result(x) + Macaulay(x2-(xa/2), Rj*((ha/2)-zhat)*np.sin(beta),0).result(x) + Macaulay(x2-(xa/2), -Rj*np.cos(beta)*(ha/2),0).result(x) + Macaulay(x2+(xa/2), -1*P*np.cos(beta)*(ha/2), 0).result(x) + Macaulay(x2+(xa/2), P*np.sin(beta)*((ha/2)-zhat), 0).result(x)

