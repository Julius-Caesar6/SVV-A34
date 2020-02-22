from Validation.Outputs_reader import *
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

from Validation.Inputs_reader import inputs

# s1: 5778 nodes, highest node =6634
s1 = Bending_stress_R1
nodes = s1['Node'].tolist()
data  = inputs.loc[inputs['Node'].isin(nodes)]
print(inputs['Node'].max(), inputs['Node'].shape)