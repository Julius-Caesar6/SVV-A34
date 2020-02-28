from FBD_Folder.ShearForce_3 import q_qvalues, q_yvalues, q_zvalues, tau_values
import pandas as pd
import matplotlib.pyplot as plt
from FBD_Folder.Bending_stresses import *

bending_stress = pd.read_csv('Bending_stress_data.csv')


def prepare_Von_mises_plot():
    # Shear stress
    shearstress = pd.DataFrame(columns=['shearstress'])
    shearstress['shearstress'] = tau_values
    shearstress['y'] = q_yvalues
    shearstress['z'] = q_zvalues
    # Bending stress
    stress = bending_stress
    stress['shearstress'] = shearstress['shearstress']
    stress['shearflow'] = q_qvalues

    def Von_mises_stress(Sxx, Tyz):
        return (((Sxx**2)/2)+ 3*(Tyz**2))**0.5

    VMises = []
    for index, row in stress.iterrows():
        VMises.append(Von_mises_stress(row['sigma'], row['shearstress']))

    stress['V.Mises'] = VMises
    return stress


stress = prepare_Von_mises_plot()


fig2 = plt.figure()
ax2 = plt.axes()
p = ax2.scatter(stress['z'], stress['y'],c=stress['shearflow'], cmap='jet')   #wing profile
clb = fig2.colorbar(p)
ax2.set_title('Shear flow distribution')
ax2.set_ylabel('y [m]')
ax2.set_xlabel('z [m]')
ax2.set_xlim(-0.5,0.2)
ax2.invert_xaxis()
clb.set_label(' Shear flow [N/m]') #TODO add units
plt.show()

fig3 = plt.figure()
ax3 = plt.axes()
p = ax3.scatter(stress['z'], stress['y'],c=stress['sigma'], cmap='jet')   #wing profile
clb = fig3.colorbar(p)
ax3.set_title('Direct stress')
ax3.set_ylabel('y [m]')
ax3.set_xlabel('z [m]')
ax3.set_xlim(-0.5,0.2)
ax3.invert_xaxis()
clb.set_label(' Direct stress [Pa]')
plt.show()


fig = plt.figure()
ax = plt.axes()
p = ax.scatter(stress['z'], stress['y'],c=stress['V.Mises'], cmap='jet')   #wing profile
clb = fig.colorbar(p)
ax.set_title('Von Mises stress')
ax.set_ylabel('y [m]')
ax.set_xlabel('z [m]')
ax.set_xlim(-0.5,0.2)
ax.invert_xaxis()
clb.set_label(' Von Mises stress [Pa]')
plt.show()







