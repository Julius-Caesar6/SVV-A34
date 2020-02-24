from Validation.Outputs_reader import *
from Validation.Inputs_reader import inputs
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


def coords_from_nodes (node, inputs):
    return inputs.loc[inputs['Node']==node]

X = []
Y = []
Z = []

for index, row in Bending_disp.iterrows():
    X.append(float(coords_from_nodes(row['Node'], inputs)['x']))
    Y.append(float(coords_from_nodes(row['Node'], inputs)['y']))
    Z.append(float(coords_from_nodes(row['Node'], inputs)['z']))

cords = pd.DataFrame(Bending_disp['Node'])
cords['xold'] = X
cords['yold'] = Y
cords['zold'] = Z

cords['xnew'] = cords['xold'] + Bending_disp['U.U1']
cords['ynew'] = cords['yold'] + Bending_disp['U.U2']
cords['znew'] = cords['zold'] + Bending_disp['U.U3']

Bending_displacement = cords[['Node','xnew','ynew','znew']]

fig = plt.figure()
ax = plt.axes(projection='3d')
# ax.set_aspect('equal')
p = ax.scatter(Bending_displacement['xnew'], Bending_displacement['ynew'], Bending_displacement['znew'])
# ax.set_xlim3d(0,2500)
# ax.set_ylim3d(-1250,1250)
# ax.set_zlim3d(-1000,1000)
plt.show()