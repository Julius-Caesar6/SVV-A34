lst = [1,2,3,4]  #form: a x^3 + b x^2 + c x + d !!


#inip is initial power
#repin is repeat integration
def denval(inip,repin):
    den = 1
    for rep in range(repin): #Returns denominator for integration
        den = (inip + rep + 1) * den
    return den

#polylist is ONE list of spline polynomial values
#ni is number of times integrated
#startv is value for integration start
#endv is value for integration end
def integrate(polylist,ni,startv,endv):  #Returns a number of integrals over specified length
    a = polylist[0]/denval(3,ni)
    b = polylist[1]/denval(2,ni)
    c = polylist[2]/denval(1,ni)
    d = polylist[3]/denval(0,ni)
    return a*((endv)**(3+ni) - (startv)**(3+ni)) + b*((endv)**(2+ni) - (startv)**(2+ni)) + c*((endv)**(1+ni) - (startv)**(1+ni)) + d*((endv)**(0+ni) - (startv)**(0+ni))



print(integrate(lst,1,2,4))