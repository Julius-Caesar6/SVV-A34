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

# Load Displacement DataFrames
Bending_disp = pd.read_csv('Displacement_plots/Bending_disp.csv')
Bending_disp_assembly =  pd.read_csv('Displacement_plots/Bending_disp_assembly.csv')
Jam_bent_disp = pd.read_csv('Displacement_plots/Jam_Bent_disp.csv')
Jam_bent_disp_assembly =  pd.read_csv('Displacement_plots/Jam_Bent_disp_assembly.csv')
Jam_straight_disp = pd.read_csv('Displacement_plots/Jam_straight_disp.csv')
Jam_straight_disp_assembly =  pd.read_csv('Displacement_plots/Jam_straight_disp_assembly.csv')

def plot_displacement_figure(disp_df, disp_df_assembly):
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    p = ax.scatter(disp_df['xnew'], disp_df['ynew'], disp_df['znew'])
    q = ax.scatter(disp_df_assembly['xnew'], disp_df_assembly['ynew'], disp_df_assembly['znew'])
    ax.set_xlabel('x [mm]')
    ax.set_ylabel('y [mm]')
    ax.set_zlabel('z [mm]')

    # ax.set_xlim3d(0, 2500)
    # ax.set_ylim3d(-1000,1000)
    # ax.set_zlim3d(-600,600)
    plt.show()
    plt.close()

def plot_spar_displacement_figure():



def plot_stress_figure(stress_dfr1, stress_dfr2, stress_type):
    if stress_type == 'Shear':
        type = 'S.S12.mean'
    elif stress_type == 'VMises':
        type = 'S.Mises.mean'

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    # ax.set_aspect('equal')
    p = ax.scatter(stress_dfr1['intpointx'], stress_dfr1['intpointy'], stress_dfr1['intpointz'],c=stress_dfr1[type], cmap='jet')
    q = ax.scatter(stress_dfr2['intpointx'], stress_dfr2['intpointy'], stress_dfr2['intpointz'], c = stress_dfr2[type], cmap='jet')
    clb = fig.colorbar(p)
    ax.set_xlabel('x [mm]')
    ax.set_ylabel('y [mm]')
    ax.set_zlabel('z [mm]')
    clb.set_label(stress_type)
    ax.set_xlim3d(600, 2000)
    ax.set_ylim3d(-200,200)
    ax.set_zlim3d(-600,600)
    plt.show()
    plt.close()



plot_displacement_figure(Bending_disp, Bending_disp_assembly)
plot_stress_figure(Bending_stress_R1, Bending_stress_R2, 'VMises')
plot_stress_figure(Jam_Bent_stress_R1, Jam_Bent_stress_R2, 'VMises')