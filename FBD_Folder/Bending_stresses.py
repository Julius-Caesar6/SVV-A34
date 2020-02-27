from FBD_Folder.Equations import *
import numpy as np
from FBD_Folder.Constants import *

def sigmaxx(y,z, x, Iyy, Izz):
    return (My(x)*z/Iyy) - (Mz(x)*y/Izz) # FIXME check if two terms should be added or subtracted



xrange = np.linspace(0, la, 50)

