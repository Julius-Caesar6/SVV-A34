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
p = ax.scatter(Bending_stress_R1['intpointx'], Bending_stress_R1['intpointy'], Bending_stress_R1['intpointz'],c=Bending_stress_R1['S.Mises.mean'])
q = ax.scatter(Bending_stress_R2['intpointx'], Bending_stress_R2['intpointy'], Bending_stress_R2['intpointz'], c = Bending_stress_R2['S.Mises.mean'])
fig.colorbar(p)
ax.xlabel()
ax.set_xlim3d(0,2500)
ax.set_ylim3d(-1250,1250)
ax.set_zlim3d(-1000,1000)
plt.show()
