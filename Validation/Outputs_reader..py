import pandas as pd


Bending_stress_R1 = pd.read_csv('Bending_stresses_reg_1.csv',  delimiter ="\s+" )
print(Bending_stress_R1.max())