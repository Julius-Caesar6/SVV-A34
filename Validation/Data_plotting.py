import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits import mplot3d
import matplotlib.style as style
style.use('seaborn-talk') #sets the size of the charts
style.use('ggplot')

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

# Load Spar displacement DataFrames
Bending_disp_spar = pd.read_csv('Spar_displacement_plots/Bending_disp_spar.csv')
Jam_bent_disp_spar = pd.read_csv('Spar_displacement_plots/Jam_Bent_disp_spar.csv')
Jam_straight_disp__spar = pd.read_csv('Spar_displacement_plots/Jam_straight_disp_spar.csv')

Own_model_hingeline_disp_Jam_straight = pd.read_csv('737hingelinedeflectionsJam_straight.csv')
Own_model_hingeline_disp_Jam_Bent = pd.read_csv('737hingelinedeflectionsJam_bent.csv')
Own_model_hingeline_disp_Bending = pd.read_csv('737hingelinedeflectionsBending.csv')

def plot_displacement_figure_2D(disp_df, disp_df_assembly, title, xmin, xmax, ymin, ymax):
    fig = plt.figure()
    ax = plt.axes()
    
    p = ax.plot(disp_df['xnew'], disp_df['ynew'],'b.', label='Validation data')
    q = ax.plot(disp_df_assembly['xvalues']*1000, disp_df_assembly['vydisp']*1000, 'r.', label='Our data')
    ax.set_title(title)
    ax.set_xlabel('x [mm]')
    ax.set_ylabel('y [mm]')
    ax.legend()
    # ax.set_zlabel('z [mm]')

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin,ymax)
    # ax.set_zlim3d(-600,600)
    plt.show()
    plt.close()


plot_displacement_figure_2D(Bending_disp_spar, Own_model_hingeline_disp_Bending, 'Bending hingeline deflection', 0, 2700, -0.5,20)
plot_displacement_figure_2D(Bending_disp_spar, 0, 'Bending hingeline deflection', 0,2700, 0,20)
plot_displacement_figure_2D(Jam_bent_disp_spar,0, 'Jammed-bent hingeline deflection', 0,2700,-5,20)

def plot_stress_figure(stress_dfr1, stress_dfr2, stress_type):
    if stress_type == 'Shear':
        type = 'S.S12.mean'
    elif stress_type == 'VMises':
        type = 'S.Mises.mean'

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    p = ax.scatter(stress_dfr1['intpointx'], stress_dfr1['intpointy'], stress_dfr1['intpointz'],c=stress_dfr1[type], cmap='jet')
    q = ax.scatter(stress_dfr2['intpointx'], stress_dfr2['intpointy'], stress_dfr2['intpointz'], c = stress_dfr2[type], cmap='jet')
    clb = fig.colorbar(p)
    ax.set_xlabel('x [mm]')
    ax.set_ylabel('y [mm]')
    ax.set_zlabel('z [mm]')
    clb.set_label(stress_type+" N/m2")
    ax.set_xlim3d(600, 2000)
    ax.set_ylim3d(-200,200)
    ax.set_zlim3d(-600,600)
    plt.show()
    plt.close()
