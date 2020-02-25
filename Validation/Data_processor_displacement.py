from Validation.Outputs_reader import *
from Validation.Inputs_reader import inputs
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


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


prepare_displacementdf_for_plotting(Bending_disp).to_csv('Bending_disp.csv')
prepare_displacementdf_for_plotting(Bending_disp_assembly).to_csv('Bending_disp_assembly.csv')

prepare_displacementdf_for_plotting(Jam_Bent_disp).to_csv('Jam_Bent_disp.csv')
prepare_displacementdf_for_plotting(Jam_Bent_disp_assembly).to_csv('Jam_Bent_disp_assembly.csv')

prepare_displacementdf_for_plotting(Jam_Straight_disp).to_csv('Jam_straight_disp.csv')
prepare_displacementdf_for_plotting(Jam_Straight_disp_assembly).to_csv('Jam_straight_disp_assembly.csv')


