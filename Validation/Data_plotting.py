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


fig = plt.figure()
ax = plt.axes(projection='3d')
# ax.set_aspect('equal')
ax.scatter(Bending_s_r1['intpointx'], Bending_s_r1['intpointy'], Bending_s_r1['intpointz'])
plt.show()