"""we are going to make a pretty file to do numerical intergation v1"""
import numpy as np

def simpson(f0, f1, f2, x1, x2):
    h=(x2-x1)/2
    return h/3 * (f0+4*f1+f2)

def comp_num_int(a, b, f, n=3):
    step = (b-a)/n
    xlst = np.linspace(a, b, n)
    function_value = 0
    for i in range(n):



        function_value += simpson(fo, f1, f2, xlst[i], xlst[i+1])


