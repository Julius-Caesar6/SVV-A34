import numpy as np
from MeshSpaceXZ import *
from Constants import *
from interpolator import *

loaddata = np.genfromtxt('aerodynamicloadcrj700.dat',delimiter=',')  #
loaddata = np.matrix.transpose(loaddata) #CHEEEEEEEEEEEEEEEEEEEEEEEECK

loaddataverif = np.genfromtxt('verif.dat',delimiter=',')





#inip is initial power
#repin is repeat integration
def denval(inip,repin):
    den = 1
    for rep in range(repin): #Returns denominator for integration
        den = (inip + rep + 1) * den
    return den


#polylist is ONE list of spline polynomial values       #form: a x^3 + b x^2 + c x + d !!
#ni is number of times integrated
#startv is value for integration start
#endv is value for integration end
#zp2 is extra z power.
def IntegratePoly(polylist,ni,startvi,endvi,zp2):  #Returns a number of integrals over specified length          #
    endv = endvi - startvi  #done to account for xi spline issue
    startv = 0
    #print(polylist)  #Turn on for debuggin nans
    a = (polylist[0])/denval(3+zp2,ni)
    b = (polylist[1])/denval(2+zp2,ni)
    c = (polylist[2])/denval(1+zp2,ni)
    d = (polylist[3])/denval(0+zp2,ni)
    return a*((endv)**(3+ni+zp2) - (startv)**(3+ni+zp2)) + b*((endv)**(2+ni+zp2) - (startv)**(2+ni+zp2)) + c*((endv)**(1+ni+zp2) - (startv)**(1+ni+zp2)) + d*((endv)**(0+ni+zp2) - (startv)**(0+ni+zp2))


#ChordMesh is Chord with Points at Nodes
#lstlst is the list of polynomial coefficients
# MUST SATISFY: len(ChordMesh) = len(lstlst) + 1
#nint is number of times integrated
def IntegrateMultiSpline(ChordMesh,lstlst,nint,zp1):
    if len(ChordMesh) != len(lstlst) + 1:
        print('Error in IntegrateMultiSpline in AeroInt: The lengths of lists do not match (+1). chordmesh: ',len(ChordMesh),' polycoeff: ',len(lstlst))#ADD TRUE TEST HERE!
    Integral = 0
    for i in range(len(ChordMesh)-1):
        Integral = Integral + IntegratePoly(lstlst[i],nint,ChordMesh[i],ChordMesh[i+1],zp1)
    return Integral


#VERIFICATION. By hand, 4 nodes, 3 sets of splines. First on even grid, then varying grid all at one time integration. Then multiple integrations on varying grid. Answers consistent.

#Below: Example test verification
#print(IntegrateMultiSpline([1,2,3,6],[[1,2,3,4],[5,6,7,8],[9,10,11,12]],2,0))
#print(271/20 + 1529/12 + 98217/20)


#x is the point at which you are at spanwise on aileron
#n is the number of times integrated
#zp is the extra power for z (eg zp = 1 if inside integral is multiplied by z)
def IntegrateX(x,n,zp):  #standard z once then x [n] times
    MeshZ = MeshSpaceZfunc(Nz,Ca)
    MeshX = MeshSpaceXfunc(Nx,la)
    xnew = []
    for val in MeshX:
        if val < x:
            xnew.append(val)
    xlst = []
    for idx in range(len(xnew)):
        xlst.append(IntegrateMultiSpline(MeshZ,interpolate(list(loaddata[idx]),MeshZ).abcd,1,zp))  #integrating along z for all chordwise data lines until x position
    xlstpoly = interpolate(xlst,xnew).abcd
    return IntegrateMultiSpline(xnew,xlstpoly,n,0)













#VERIF BELOW

# def IntegrateXverif(x,n,zp):  #standard z once then x [n] times
#     MeshZ = [1,2,4]
#     MeshX =  [1,2,3,6,7,9]
#     xnew = []
#     for val in MeshX:
#         if val < x:
#             xnew.append(val)
#     xlst = []
#     for idx in range(len(xnew)):
#         xlst.append(IntegrateMultiSpline(MeshZ,interpolate(list(loaddataverif[idx]),MeshZ).abcd,1,zp))  #integrating along z for all chordwise data lines until x position
#     xlstpoly = interpolate(xlst,xnew).abcd
#     return IntegrateMultiSpline(xnew,xlstpoly,n,0)

#print(IntegrateXverif(2.3,1,1))


al = []
for i in range(41):
    al.append(sum(loaddata[i]))

print(sum(al)/(81*41))