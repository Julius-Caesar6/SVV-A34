from Validation.Outputs_reader import *
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from Validation.Inputs_reader import Elements
from Validation.Inputs_reader import inputs

def select_elements(stress_df, Elements):
    TF_df = Elements['Element'].isin(stress_df['Element'])
    return Elements.loc[TF_df]

def coords_from_nodes (nodes_df, inputs):
    TF_df = inputs['Node'].isin(nodes_df)
    return inputs.loc[TF_df]




# Stressese
s1 = Bending_stress_R1
elements = s1['Element'] # All elements covered in output
# Max = 6634, len = 5778

R = Elements['Element'].isin(elements)
U = Elements.loc[R]
print(U)




