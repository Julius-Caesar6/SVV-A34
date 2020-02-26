import unittest
from interpolator import interpolate
import numpy as np
import matplotlib.pyplot as plt
''' THIS WONT WORK AS WE ARE DOING A NATURAL CUBIC SPLINE SO IT WILL NOT BE EXACT
def cubic_funct(a, b, c, d, x):
    return a*x**3 + b*x**2 + c*x + d

class test_interpolate(unittest.TestCase):

    def test_cubic_function(self):
        x0 = 3
        x1 = 4
        x2 = 5
        a,b,c,d = 2,5,3,2
        xlst = [x0,x1,x2]
        flst = [cubic_funct(a,b,c,d,x0),cubic_funct(a,b,c,d,x1),cubic_funct(a,b,c,d,x2)]
        abcd = interpolate(flst,xlst).abcd
        self.assertEqual(abcd[0],a)
        self.assertEqual(abcd[1],b)
        self.assertEqual(abcd[2],c)
        self.assertEqual(abcd[3],d)
'''
        
#Example 4.2 from the ANA reader
#data = [0,0.2624,0.6419,1.0296]
#pos = [0,0.1,0.3,0.6]
#print(interpolate(data,pos).abcd)


if __name__ == '__main__':
    unittest.main()
