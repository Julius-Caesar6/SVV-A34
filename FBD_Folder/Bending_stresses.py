



def sigmaxx(y,z, My, Mz, Iyy, Izz):
    return (My*z/Iyy) - (Mz*y/Izz) # FIXME check if two terms should be added or subtracted