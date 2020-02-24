import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits import mplot3d

# Load Stress DataFrames
Bending_stress_R1 = pd.read_csv('Stress_plots/Bending_sr1.csv')
Bending_stress_R2 = pd.read_csv('Stress_plots/Bending_sr2.csv')
Jam_Bent_stress_R1 = pd.read_csv('Stress_plots/Jam_Bent_sr1.csv')
Jam_Bent_stress_R2 = pd.read_csv('Stress_plots/Jam_Bent_sr2.csv')
Jam_Straight_stress_R1 = pd.read_csv('Stress_plots/Jam_straight_sr1.csv')
Jam_Straight_stress_R2 = pd.read_csv('Stress_plots/Jam_straight_sr2.csv')

from matplotlib import cm
fig = plt.figure()
ax = plt.axes(projection='3d')
# ax.set_aspect('equal')
ax.scatter(Jam_Bent_stress_R1['intpointx'], Jam_Bent_stress_R1['intpointy'], Jam_Bent_stress_R1['intpointz'], color = cm.brg(Jam_Bent_stress_R1['S.Mises.mean']))
ax.scatter(Jam_Bent_stress_R2['intpointx'], Jam_Bent_stress_R2['intpointy'], Jam_Bent_stress_R2['intpointz'], color = cm.brg(Jam_Bent_stress_R2['S.Mises.mean']))
ax.legend()

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')

plt.show()