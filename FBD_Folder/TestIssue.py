import numpy as np
from MeshSpaceXZ import *
from Constants import *
from interpolator import *
from Macaulay import *
from AeroInt import *
from pandas import *

import matplotlib.pyplot as plt

# x = np.linspace(0.01,la,100)
# y = []
#
# for i in range(len(x)):
#     y.append(IntegrateX(x[i],0,0))
#
# plt.plot(x,y)
# plt.show()

print(Macaulay(x2-(xa/2), -np.cos(beta)*P/(6*E*Iyy),3).result(x2))

