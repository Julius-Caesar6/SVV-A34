from MeshSpaceXZ import MeshSpaceZfunc      #not necessarily needed until using the 'real' data


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
def IntegratePoly(polylist,ni,startv,endv):  #Returns a number of integrals over specified length
    a = polylist[0]/denval(3,ni)
    b = polylist[1]/denval(2,ni)
    c = polylist[2]/denval(1,ni)
    d = polylist[3]/denval(0,ni)
    return a*((endv)**(3+ni) - (startv)**(3+ni)) + b*((endv)**(2+ni) - (startv)**(2+ni)) + c*((endv)**(1+ni) - (startv)**(1+ni)) + d*((endv)**(0+ni) - (startv)**(0+ni))


#ChordMesh is Chord with Points at Nodes
#lstlst is the list of polynomial coefficients
# MUST SATISFY: len(ChordMesh) = len(lstlst) + 1
#nint is number of times integrated
def IntegrateMultiSpline(ChordMesh,lstlst,nint):
    #ADD TRUE TEST HERE!
    Integral = 0
    for i in range(len(ChordMesh)-1):
        Integral = Integral + IntegratePoly(lstlst[i],nint,ChordMesh[i],ChordMesh[i+1])
    return Integral

#VERIFICATION. By hand, 4 nodes, 3 sets of splines. First on even grid, then varying grid all at one time integration. Then multiple integrations on varying grid. Answers consistent.

#Below: Example test verification
#print(IntegrateMultiSpline([1,2,3,6],[[1,2,3,4],[5,6,7,8],[9,10,11,12]],2))
#print(271/20 + 1529/12 + 98217/20)