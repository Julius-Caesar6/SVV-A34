from MOI import Izz_total, Am_cell1 , Am_cell2, A_stringer, y, z , h, straight, t , tspar
import numpy as np

#integral1
input1 = np.linspace(0,np.pi,100) #list of inputs
function1 = t*h**2*np.sin(input1) #list of outputs

#qb1 = 0 + -1/Izz_total * (integral1 + A_stringer * y[1] + A_stringer * y[2])

#integral2
input2 = np.linspace(0,h/2,100) #list of inputs
function2 = tsp*y #list of outputs 

#qb2 = 0 + -1/Izz_total * (integral 2 )
