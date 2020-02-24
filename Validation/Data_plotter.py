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
def Element_to_coordinates(stress_df):
    Elem = select_elements(stress_df, Elements)
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
    cordsx['mean'] = cordsx[['LTx', 'RTx', 'LBx', 'RBx']].mean(axis=1)

    cordsy = pd.DataFrame(Elem['Element'])
    cordsy['LTy'] = LTy
    cordsy['RTy'] = RTy
    cordsy['LBy'] = LBy
    cordsy['RBy'] = RBy
    cordsy['mean'] = cordsy[['LTy', 'RTy', 'LBy', 'RBy']].mean(axis=1)

    cordsz = pd.DataFrame(Elem['Element'])
    cordsz['LTz'] = LTz
    cordsz['RTz'] = RTz
    cordsz['LBz'] = LBz
    cordsz['RBz'] = RBz
    cordsz['mean'] = cordsz[['LTz', 'RTz', 'LBz', 'RBz']].mean(axis=1)

    stress_df['intpointx'] = cordsx['mean']
    stress_df['intpointy'] = cordsy['mean']
    stress_df['intpointz'] = cordsz['mean']

    return stress_df

test1 = Element_to_coordinates(Bending_stress_R1)

print(test1)


