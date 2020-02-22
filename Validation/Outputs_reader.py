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

# Process Stress data
# Taking mean of Loc1 and Loc2 for shear and von mises stress.
Bending_stress_R1['S.Mises.mean'] = Bending_stress_R1[['S.Mises1','S.Mises2']].mean(axis=1)
Bending_stress_R1['S.S12.mean'] = Bending_stress_R1[['S.S121','S.S122']].mean(axis=1)
Bending_stress_R1 = Bending_stress_R1[['Node','S.Mises.mean', 'S.S12.mean']]  # Leaving other columns and keeping only relevant columns

Bending_stress_R2['S.Mises.mean'] = Bending_stress_R2[['S.Mises1','S.Mises2']].mean(axis=1)
Bending_stress_R2['S.S12.mean'] = Bending_stress_R2[['S.S121','S.S122']].mean(axis=1)
Bending_stress_R2 = Bending_stress_R2[['Node','S.Mises.mean', 'S.S12.mean']]  # Leaving other columns and keeping only relevant columns


Jam_Bent_stress_R1['S.Mises.mean'] = Jam_Bent_stress_R1[['S.Mises1','S.Mises2']].mean(axis=1)
Jam_Bent_stress_R1['S.S12.mean'] = Jam_Bent_stress_R1[['S.S121','S.S122']].mean(axis=1)
Jam_Bent_stress_R1 = Jam_Bent_stress_R1[['Node','S.Mises.mean', 'S.S12.mean']]  # Leaving other columns and keeping only relevant columns

Jam_Bent_stress_R2['S.Mises.mean'] = Jam_Bent_stress_R2[['S.Mises1','S.Mises2']].mean(axis=1)
Jam_Bent_stress_R2['S.S12.mean'] = Jam_Bent_stress_R2[['S.S121','S.S122']].mean(axis=1)
Jam_Bent_stress_R2 = Jam_Bent_stress_R2[['Node','S.Mises.mean', 'S.S12.mean']]  # Leaving other columns and keeping only relevant columns



Jam_Straight_stress_R1['S.Mises.mean'] = Jam_Straight_stress_R1[['S.Mises1','S.Mises2']].mean(axis=1)
Jam_Straight_stress_R1['S.S12.mean'] = Jam_Straight_stress_R1[['S.S121','S.S122']].mean(axis=1)
Jam_Straight_stress_R1 = Jam_Straight_stress_R1[['Node','S.Mises.mean', 'S.S12.mean']]  # Leaving other columns and keeping only relevant columns

Jam_Straight_stress_R2['S.Mises.mean'] = Jam_Straight_stress_R2[['S.Mises1','S.Mises2']].mean(axis=1)
Jam_Straight_stress_R2['S.S12.mean'] = Jam_Straight_stress_R2[['S.S121','S.S122']].mean(axis=1)
Jam_Straight_stress_R2 = Jam_Straight_stress_R2[['Node','S.Mises.mean', 'S.S12.mean']]  # Leaving other columns and keeping only relevant columns


