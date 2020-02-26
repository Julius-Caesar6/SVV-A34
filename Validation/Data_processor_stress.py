from Validation.Outputs_reader import *
from Validation.Inputs_reader import Elements
from Validation.Inputs_reader import inputs

def select_elements(stress_df, Elements):
    TF_df = Elements['Element'].isin(stress_df['Element'])
    return Elements.loc[TF_df]

def coords_from_nodes (node, inputs):
    return inputs.loc[inputs['Node']==node]

def get_hingeline_Coordinates():
    reg_2_elements = select_elements(Bending_stress_R2, Elements)
    nodeslst = []

    for index, row in reg_2_elements.iterrows():
        nodeslst.append(row['NodeLT'])

    for index, row in reg_2_elements.iterrows():
        nodeslst.append(row['NodeRT'])

    for index, row in reg_2_elements.iterrows():
        nodeslst.append(row['NodeRB'])

    for index, row in reg_2_elements.iterrows():
        nodeslst.append(row['NodeLB'])

    spar_nodes_coords = pd.DataFrame(columns=['sparx', 'spary', 'sparz'])
    sparx = []
    spary = []
    sparz = []
    for node in nodeslst:
        sparx.append(float(coords_from_nodes(node, inputs)['x']))
        spary.append(float(coords_from_nodes(node, inputs)['y']))
        sparz.append(float(coords_from_nodes(node, inputs)['z']))

    spar_nodes_coords['sparx'] = sparx
    spar_nodes_coords['spary'] = spary
    spar_nodes_coords['sparz'] = sparz


    return spar_nodes_coords

hinge_coords = get_hingeline_Coordinates()
hinge_coords.to_csv('hinge_coordinates.csv')


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

    stress_df['intpointx'] = list(cordsx['mean'])
    stress_df['intpointy'] = list(cordsy['mean'])
    stress_df['intpointz'] = list(cordsz['mean'])
    return stress_df



# Running functions and saving DataFrames to csv files
# Bending_s_r1 = Element_to_coordinates(Bending_stress_R1)
# Bending_s_r2 = Element_to_coordinates(Bending_stress_R2)
# Jam_Bent_s_r1 = Element_to_coordinates(Jam_Bent_stress_R1)
# Jam_Bent_s_r2 = Element_to_coordinates(Jam_Bent_stress_R2)
# Jam_Straight_s_r1 = Element_to_coordinates(Jam_Straight_stress_R1)
# Jam_Straight_s_r2 = Element_to_coordinates(Jam_Straight_stress_R2)
#
# Bending_s_r1.to_csv('Bending_sr1.csv')
# Bending_s_r2.to_csv('Bending_sr2.csv')
# Jam_Bent_s_r1.to_csv('Jam_Bent_sr1.csv')
# Jam_Bent_s_r2.to_csv('Jam_Bent_sr2.csv')
# Jam_Straight_s_r1.to_csv('Jam_straight_sr1.csv')
# Jam_Straight_s_r2.to_csv('Jam_straight_sr2.csv')
#


