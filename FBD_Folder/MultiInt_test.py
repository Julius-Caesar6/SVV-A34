hangfrom AeroInt import IntegrateMultiSpline

lst1 = [[1,2,3,4],[5,6,7,8],[5,4,6,3]]  #Nathaniel spline maker
lst2 = [[1,2,2,1],[4,3,2,1],[2,5,5,6]]
lst3 = [[3,2,3,4],[7,6,5,4],[2,3,1,3]]

lstx = [1,3,8,9]  #MeshSpaceXfunc
lstz = [1,3,5,9]  #MeshSpaceZfunc


zvals = [IntegrateMultiSpline(lst1,lstx,1),IntegrateMultiSpline(lst2,lstx,1),IntegrateMultiSpline(lst3,lstx,1)]

Int5 = IntegrateMultiSpline(zvals,lstz,4)
