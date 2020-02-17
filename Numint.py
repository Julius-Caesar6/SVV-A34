"""we are going to make a pretty file to do numerical intergation v1"""

def simpson(f0,f1,f2,x1,x2):
    h=(x2-x1)/2
    return h/3 * (f0+4*f1+f2)

def comp_num_int(a,b,f,n=3):
    step=(b-a)/n
    for i in range(n):

