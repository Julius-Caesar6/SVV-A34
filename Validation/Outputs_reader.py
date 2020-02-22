import pandas as pd

# Create dataframes for Stress data
Bending_stress_R1 = pd.read_csv('Stress/Bending_stresses_reg_1.csv',  delimiter ="\s+" )
Bending_stress_R2 = pd.read_csv('Stress/Bending_stresses_reg_2.csv',  delimiter ="\s+" )
Jam_Bent_stress_R1 = pd.read_csv('Stress/Jam_Bent_stresses_reg_1.csv',  delimiter ="\s+" )
Jam_Bent_stress_R2 = pd.read_csv('Stress/Jam_Bent_stresses_reg_2.csv',  delimiter ="\s+" )
Jam_Straight_stress_R1 = pd.read_csv('Stress/Jam_straight_stresses_reg_1.csv',  delimiter ="\s+" )
Jam_Straight_stress_R2 = pd.read_csv('Stress/Jam_straight_stresses_reg_2.csv',  delimiter ="\s+" )

# Create dataframes for displacement data
Bending_disp =  pd.read_csv('Displacement/Bending_disp.csv',  delimiter ="\s+" )
Bending_disp_assembly =  pd.read_csv('Displacement/Bending_disp_assembly.csv',  delimiter ="\s+" )
Jam_Bent_disp =  pd.read_csv('Displacement/Jam_Bent_disp.csv',  delimiter ="\s+" )
Jam_Bent_disp_assembly =  pd.read_csv('Displacement/Jam_Bent_disp_assembly.csv',  delimiter ="\s+" )
Jam_Straight_disp =  pd.read_csv('Displacement/Jam_Straight_disp.csv',  delimiter ="\s+" )
Jam_Straight_disp_assembly =  pd.read_csv('Displacement/Jam_Straight_disp_assembly.csv',  delimiter ="\s+" )

# Create dataframes for reaction forces
Bending_RF_assembly =  pd.read_csv('Reaction_Forces/Bending_RF_assembly.csv',  delimiter ="\s+" )
Jam_Bent_RF_assembly =  pd.read_csv('Reaction_Forces/Jam_Bent_RF_assembly.csv',  delimiter ="\s+" )
Jam_Straight_RF_assembly =  pd.read_csv('Reaction_Forces/Jam_Straight_RF_assembly.csv',  delimiter ="\s+" )


