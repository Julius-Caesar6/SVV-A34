
def Von_mises_stress(Sxx, Syy, Szz, Txy, Tyz, Tzx):
    return (0.5*(((Sxx-Syy)**2) + ((Syy-Szz)**2) +((Szz-Sxx)**2)) + 3*((Txy**2) + (Tyz**2) + (Tzx**2)))**0.5

