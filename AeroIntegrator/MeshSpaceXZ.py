import numpy as np

#Nz is number of Nodes (Nz = 81)
#Ca is length of chord (Ca = 0.484 [m])
def MeshSpaceZfunc(Nz,Ca):  #Creates a list of nodes on chord   NOTE NEGATIVE RESULTS!!
    lstz = []
    for i in range(Nz):
        thetai = (i-1)*np.pi/Nz
        thetai1 = (i) * np.pi / Nz
        lstz.append((-1/2)*((Ca/2)*(1-np.cos(thetai))+(Ca/2)*(1-np.cos(thetai1))))  #verification check, sum() = Nz and lst[-1] ~ Ca
    return lstz

#Nx is number of Nodes (Nx = 41)
#la is length of aileron span (la = 1.691 [m])
def MeshSpaceXfunc(Nx,la):  #Creates a list of nodes on span
    lstx = []
    for i in range(Nz):
        thetai = (i-1)*np.pi/Nz
        thetai1 = (i) * np.pi / Nz
        lstx.append((1/2)*((la/2)*(1-np.cos(thetai))+(la/2)*(1-np.cos(thetai1))))  #verification check, sum() = Nz and lst[-1] ~ Ca
    return lstx
