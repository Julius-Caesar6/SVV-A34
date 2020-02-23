from Validation.Outputs_reader import *
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from Validation.Inputs_reader import Elements
from Validation.Inputs_reader import inputs


# Stressese
s1 = Bending_stress_R1
elements = s1['Element']


data  = inputs.loc[inputs['Node'].isin(nodes)]
print(inputs['Node'].max(), inputs['Node'].shape)