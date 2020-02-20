import numpy as np
from MeshSpaceXZ import *
from Constants import *

loaddata = np.genfromtxt('aerodynamicloadcrj700.dat',delimiter=',')  #

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
def IntegratePoly(polylist,ni,startv,endv,zp2):  #Returns a number of integrals over specified length
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
        print('Possible Error in IntegrateMultiSpline in AeroInt. The lengths of lists do not match (+1)')#ADD TRUE TEST HERE!
    Integral = 0
    for i in range(len(ChordMesh)-1):
        print(lstlst[i])
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
    xnew = []
    for val in MeshSpaceXfunc(Nx,la):
        if val < x:
            xnew.append(val)
    zlst = []
    for idx in range(len(xnew)):
        zlst.append(IntegrateMultiSpline(MeshSpaceZfunc(Nz,Ca),NathanielFunc(loaddata[idx]),1,zp))  #integrating along z for all chordwise data lines until x position
    zlstpoly = NathanielFunc(zlst)
    return IntegrateMultiSpline(xnew,zlstpoly,n,0)




#VERIF (attempted)
def TempSpline1(num):
    return [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
def TempSpline2(num):
    return [[4,3,2,1],[5,3,2,1]]

def IntegrateXverif(x,n,zp):  #standard z once then x [n] times
    xnew = []

    for val in [1,2,4,6]:
        if val < x:
            xnew.append(val)
    zlst = []
    for idx in range(len(xnew)):
        zlst.append(IntegrateMultiSpline([1,3,5,8],TempSpline1(loaddataverif[idx]),1,zp))  #integrating along z for all chordwise data lines until x position
    zlstpoly = TempSpline2(zlst)
    return IntegrateMultiSpline(xnew,zlstpoly,n,0)


print(IntegrateXverif(5,1,))