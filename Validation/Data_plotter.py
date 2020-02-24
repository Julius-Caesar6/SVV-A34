from Validation.Outputs_reader import *
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from Validation.Inputs_reader import Elements
from Validation.Inputs_reader import inputs

def select_elements(stress_df, Elements):
    TF_df = Elements['Element'].isin(stress_df['Element'])
    return Elements.loc[TF_df]

def coords_from_nodes (node, inputs):
    return inputs.loc[inputs['Node']==node]

# def coords_from_nodes (node_df, inputs):
#     TF_df = inputs['Node'].isin(node_df)
#     return inputs.loc[TF_df]


# Stresses
Elem = select_elements(Bending_stress_R1, Elements)
LTx = []
RTx = []
LBx = []
RBx = []

LTy = []
RTy = []
LBy = []
RBy = []

LTz = []
RTz = []
LBz = []
RBz = []

for index, row in Elem.iterrows():
    LTx.append(float(coords_from_nodes(row['NodeLT'], inputs)['x']))
    RTx.append(float(coords_from_nodes(row['NodeRT'], inputs)['x']))
    LBx.append(float(coords_from_nodes(row['NodeLB'], inputs)['x']))
    RBx.append(float(coords_from_nodes(row['NodeRB'], inputs)['x']))

    LTy.append(float(coords_from_nodes(row['NodeLT'], inputs)['y']))
    RTy.append(float(coords_from_nodes(row['NodeRT'], inputs)['y']))
    LBy.append(float(coords_from_nodes(row['NodeLB'], inputs)['y']))
    RBy.append(float(coords_from_nodes(row['NodeRB'], inputs)['y']))

    LTz.append(float(coords_from_nodes(row['NodeLT'], inputs)['z']))
    RTz.append(float(coords_from_nodes(row['NodeRT'], inputs)['z']))
    LBz.append(float(coords_from_nodes(row['NodeLB'], inputs)['z']))
    RBz.append(float(coords_from_nodes(row['NodeRB'], inputs)['z']))

cordsx = pd.DataFrame(Elem['Element'])
cordsx['LTx'] = LTx
cordsx['RTx'] = RTx
cordsx['LBx'] = LBx
cordsx['RBx'] = RBx
print(cordsx)

cordsy = pd.DataFrame(Elem['Element'])
cordsy['LTy'] = LTy
cordsy['RTy'] = RTy
cordsy['LBy'] = LBy
cordsy['RBy'] = RBy
print(cordsy)

cordsz = pd.DataFrame(Elem['Element'])
cordsz['LTz'] = LTz
cordsz['RTz'] = RTz
cordsz['LBz'] = LBz
cordsz['RBz'] = RBz
print(cordsz)




# Elem['LTX'] = Elem['NodeLT'].apply(coords_from_nodes, , axis=1)


# node1 = coords_from_nodes(Elem['NodeLT'], inputs)
# node2 = coords_from_nodes(Elem['NodeRT'], inputs)
# node3 = coords_from_nodes(Elem['NodeLB'], inputs)
# node4 = coords_from_nodes(Elem['NodeRB'], inputs)
# xaxis = 1
# yaxis = pd.DataFrame([node1['y'], node2['y'], node3['y'], node4['y']])
# zaxis = pd.DataFrame([node1['z'], node2['z'], node3['z'], node4['z']])

# xaxis['mean'] = xaxis.mean(axis=1)


# Element_means = pd.DataFrame([xaxis.mean(axis=1), yaxis.mean(axis=1), zaxis.mean(axis=1)])



# s1 = Bending_stress_R1
# elements = s1['Element'] # All elements covered in output
# # Max = 6634, len = 5778
#
# R = Elements['Element'].isin(elements)
# U = Elements.loc[R]
# print(U)




