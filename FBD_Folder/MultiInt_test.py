
from MeshSpaceXZ import *

lst1 = [[1,2,3,4],[5,6,7,8],[5,4,6,3]]  #Nathaniel spline maker
lst2 = [[1,2,2,1],[4,3,2,1],[2,5,5,6]]
lst3 = [[3,2,3,4],[7,6,5,4],[2,3,1,3]]

lstx = [1,3,8,9]  #MeshSpaceXfunc
lstz = [1,3,5,9]  #MeshSpaceZfunc

print(MeshSpaceXfunc(41,1.691))

#zvals = [IntegrateMultiSpline(lstx,lst1,1),IntegrateMultiSpline(lstx,lst2,1),IntegrateMultiSpline(lstx,lst3,1)]

#zvals = zvals*(1) #into spline function!!

#Int5 = IntegrateMultiSpline(lstz,zvals,4)
