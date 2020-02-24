import unittest
from Numint import simpson, trapezoid,  comp_num_int
import numpy as np

class int_test(unittest.TestCase):
    def testpolythree(self):
        #testing if 3rd degree polynomial givens exact answer
        x0 = 1
        fun0 = x0**3 +x0**2 + x0 +1
        x2 = 5
        fun2 = x2**3 +x2**2 + x2 +1
        x1=(x2+x0)/2
        fun1 = x1**3 +x1**2 + x1 +1
        area = (1/4*x2**4 + 1/3*x2**3 + 1/2*x2**2+ x2) - (1/4*x0**4 + 1/3*x0**3 + 1/2*x0**2+ x0)
        self.assertEqual(simpson(fun0,fun1,fun2,x0,x2),area)

    def test_trap(self):
        #testing the trapezoid rule with a linear case
        x0=1
        fun0=2*x0+3
        x1=3
        fun1=2*x1+3
        area = (x1**2 +3*x1) - (x0**2 +3*x0)
        self.assertEqual(trapezoid(fun0,fun1,x0,x1),area)

class comp_test(unittest.TestCase):

    def test_comp_lin_even(self):
        #testing the com num int function with even linear function
        x_lst=np.linspace(1,10,10)
        f_lst = []
        for i in x_lst:
            f_lst.append(3*i+4)
        area = (3/2*x_lst[-1]**2 + 4*x_lst[-1]) - (3/2*x_lst[0]**2 + 4*x_lst[0])
        self.assertEqual(comp_num_int(x_lst,f_lst),area)

    def test_comp_lin_odd(self):
        #testing the com num int function with odd linear function
        x_lst=np.linspace(1,15,15)
        f_lst=[]
        for i in x_lst:
            f_lst.append(5*i+6)
        area = (5/2*x_lst[-1]**2 + 6*x_lst[-1]) - (5/2*x_lst[0]**2 + 6*x_lst[0])
        self.assertEqual(comp_num_int(x_lst,f_lst),area)

    def test_comp_polythree_even(self):
        #testing the com num int function with even amount of values on  polynomial to the power 3
        x_lst=np.linspace(1,10,100)
        f_lst=[]
        for i in x_lst:
            f_lst.append(3*i**3 + 4*i**2 + 5)
        area = (3/4*x_lst[-1]**4 + 4/3*x_lst[-1]**3 + 5*x_lst[-1])-(3/4*x_lst[0]**4 + 4/3*x_lst[0]**3 + 5*x_lst[0])
        self.assertAlmostEqual(comp_num_int(x_lst,f_lst),area, delta = 1)

    def test_comp_polythree_odd(self):
        #testing the com num int function with odd amount of values on  polynomial to the power 3
        x_lst=np.linspace(1,15,15)
        f_lst=[]
        for i in x_lst:
            f_lst.append(3*i**3 + 4*i**2 + 5)
        area = (3/4*x_lst[-1]**4 + 4/3*x_lst[-1]**3 + 5*x_lst[-1])-(3/4*x_lst[0]**4 + 4/3*x_lst[0]**3 + 5*x_lst[0])
        self.assertEqual(comp_num_int(x_lst,f_lst),area)

    def test_comp_cool_even(self):
        #testing the com num int function with even number of values but with a cool function!
        x_lst= np.linspace(1,10,300)
        f_lst= []
        for i in x_lst:
            f_lst.append(np.exp(i) + np.sin(i)+ i**5)
        area = (np.exp(x_lst[-1]) - np.cos(x_lst[-1]) + 1/6*x_lst[-1]**6) - (np.exp(x_lst[0]) - np.cos(x_lst[0]) + 1/6*x_lst[0]**6)
        self.assertAlmostEqual(comp_num_int(x_lst, f_lst), area, delta=1)

    def test_comp_cool_odd(self):
        #testing the com num int function with even (poly 3 more or less exact) number of point and odd (linear parts exact, )
        x_lst = np.linspace(1,15,800)
        f_lst= []
        for i in x_lst:
            f_lst.append(2*np.exp(i) + 4*i*np.cos(i)+ i**5)
        area = (2*np.exp(x_lst[-1]) + np.cos(x_lst[-1]) + 4*x_lst[-1]*np.sin(x_lst[-1]) + 1/6*x_lst[-1]**6) - (2*np.exp(x_lst[0]) + np.cos(x_lst[0]) + 4*x_lst[0]*np.sin(x_lst[0]) + 1/6*x_lst[0]**6)
        self.assertAlmostEqual(comp_num_int(x_lst, f_lst), area, delta= 1)


if __name__ == '__main__':
    unittest.main()
