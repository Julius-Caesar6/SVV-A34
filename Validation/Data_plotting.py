import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from Validation.Data_processor import *

Bending_s_r1 = Element_to_coordinates(Bending_stress_R1)
print(Bending_s_r1)

fig = plt.figure()
ax = plt.axes(projection='3d')
# ax.set_aspect('equal')
ax.scatter(Bending_s_r1['intpointx'], Bending_s_r1['intpointy'], Bending_s_r1['intpointz'])
plt.show()