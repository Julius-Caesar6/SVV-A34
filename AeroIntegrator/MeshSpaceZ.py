import numpy as np

Nz = 81
Ca = 0.484

lstz = []

for i in range(Nz):
    thetai = (i-1)*np.pi/Nz
    thetai1 = (i) * np.pi / Nz
    lstz.append((-1/2)*((Ca/2)*(1-np.cos(thetai))+(Ca/2)*(1-np.cos(thetai1))))  #verification check, sum() = Nz and lst[-1] ~ Ca

