"""we are going to make a pretty file to do numerical intergation v1"""
import numpy as np

def simpson(f0, f1, f2, x0, x2):
    h=(x2-x0)/2
    return h/3 * (f0+4*f1+f2)

def comp_num_int(x_lst,f_lst):
    """input coordinates and the function values at those coordinate as two lists of the same length. Include a point at the beginning and end"""
    
    function_sum  = 0

    #Check length of array for compatibility with simpson
    if len(x_lst) == len(f_lst):
        if len(x_lst)%3 == 0:
            #no weird bits needed
            n = len(x_lst)/3 
            for i in range(int(n)):
                function_sum += simpson(f_lst[i*3], f_lst[i*3+1], f_lst[i*3+2], x_lst[i*3], x_lst[i*3+2])
        
        elif len(x_lst)%3 == 1:
            #Do something
            n = len(x_lst)/3 - 1
            for i in range(int(n)):
                function_sum += simpson(f_lst[i*3], f_lst[i*3+1], f_lst[i*3+2], x_lst[i*3], x_lst[i*3+2])

        elif len(x_lst)%3 == 2:
            #Do final thing
            n = len(x_lst)/3 - 1
            for i in range(int(n)):
                function_sum += simpson(f_lst[i*3], f_lst[i*3+1], f_lst[i*3+2], x_lst[i*3], x_lst[i*3+2])

        else
            #throw a shit fit as this is impossible

    return function_sum

print(comp_num_int([0,1,2],[1,1,1]))