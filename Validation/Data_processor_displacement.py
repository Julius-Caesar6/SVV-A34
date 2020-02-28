from Validation.Outputs_reader import *
from Validation.Inputs_reader import inputs
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

Bending_disp = pd.read_csv('Displacement/Bending_disp.csv', delimiter='\s+')
Bending_disp_assembly =  pd.read_csv('Displacement/Bending_disp_assembly.csv', delimiter='\s+')
Jam_bent_disp = pd.read_csv('Displacement/Jam_Bent_disp.csv', delimiter='\s+')
Jam_bent_disp_assembly =  pd.read_csv('Displacement/Jam_Bent_disp_assembly.csv', delimiter='\s+')
Jam_straight_disp = pd.read_csv('Displacement/Jam_straight_disp.csv', delimiter='\s+')
Jam_straight_disp_assembly =  pd.read_csv('Displacement/Jam_straight_disp_assembly.csv', delimiter='\s+')

def coords_from_nodes (node, inputs):
    return inputs.loc[inputs['Node']==node]


def prepare_displacementdf_for_plotting(Disp_df):
    X = []
    Y = []
    Z = []

    for index, row in Disp_df.iterrows():
        X.append(float(coords_from_nodes(row['Node'], inputs)['x']))
        Y.append(float(coords_from_nodes(row['Node'], inputs)['y']))
        Z.append(float(coords_from_nodes(row['Node'], inputs)['z']))

    cords = pd.DataFrame(Disp_df['Node'])
    cords['xold'] = X
    cords['yold'] = Y
    cords['zold'] = Z

    cords['xnew'] = cords['xold'] + Disp_df['U.U1']
    cords['ynew'] = cords['yold'] + Disp_df['U.U2']
    cords['znew'] = cords['zold'] + Disp_df['U.U3']

    return cords[['Node','xnew','ynew','znew']]

def prepare_spar_displacement_for_plotting(Disp_df):
    sparnodes = pd.read_csv('spar_coordinates.csv')

    cords = pd.DataFrame(sparnodes['Node'])
    cords['xold'] = sparnodes['sparx']
    cords['yold'] = sparnodes['spary']
    cords['zold'] = sparnodes['sparz']

    xdelta = []
    ydelta = []
    zdelta = []
    for index, row in sparnodes.iterrows():
        xdelta.append(float(Disp_df.loc[Disp_df['Node']==row['Node']]['U.U1']))
        ydelta.append(float(Disp_df.loc[Disp_df['Node'] == row['Node']]['U.U2']))
        zdelta.append(float(Disp_df.loc[Disp_df['Node'] == row['Node']]['U.U3']))

    cords['xdelta'] = xdelta
    cords['ydelta'] = ydelta
    cords['zdelta'] = zdelta

    cords['xnew'] = cords['xold'] + cords['xdelta']
    cords['ynew'] = cords['yold'] + cords['ydelta']
    cords['znew'] = cords['zold'] + cords['zdelta']

    return cords[['Node', 'xnew', 'ynew', 'znew']]

prepare_spar_displacement_for_plotting(Bending_disp).to_csv('Bending_disp_spar.csv')
# prepare_spar_displacement_for_plotting(Bending_disp_assembly).to_csv('Bending_disp_assembly_spar.csv')

prepare_spar_displacement_for_plotting(Jam_bent_disp).to_csv('Jam_Bent_disp_spar.csv')
# prepare_spar_displacement_for_plotting(Jam_bent_disp_assembly).to_csv('Jam_Bent_disp_assembly_spar.csv')

prepare_spar_displacement_for_plotting(Jam_straight_disp).to_csv('Jam_straight_disp_spar.csv')
# prepare_spar_displacement_for_plotting(Jam_straight_disp_assembly).to_csv('Jam_straight_disp_assembly_spar.csv')




# Run plot preparation and save to csv files
#
# prepare_displacementdf_for_plotting(Bending_disp).to_csv('Bending_disp.csv')
# prepare_displacementdf_for_plotting(Bending_disp_assembly).to_csv('Bending_disp_assembly.csv')
#
# prepare_displacementdf_for_plotting(Jam_Bent_disp).to_csv('Jam_Bent_disp.csv')
# prepare_displacementdf_for_plotting(Jam_Bent_disp_assembly).to_csv('Jam_Bent_disp_assembly.csv')
#
# prepare_displacementdf_for_plotting(Jam_Straight_disp).to_csv('Jam_straight_disp.csv')
# prepare_displacementdf_for_plotting(Jam_Straight_disp_assembly).to_csv('Jam_straight_disp_assembly.csv')


