import unittest
from FBD_Folder.Macaulay import Macaulay

class Macaulaytests(unittest.TestCase):

    def testxsmallera(self):
        # test if it returns 0 if x is smaller than a
        mac = Macaulay(5,1,1)
        self.assertEqual(mac.result(2),0)

    def testmacactive(self):
        # test if it returns x-a if x is bigger than a.
        mac = Macaulay(2,1,1)
        self.assertEqual(mac.result(5),3)

    def testpower(self):
        #test if result is to the correct power
        mac = Macaulay(2,1,2)
        self.assertEqual(mac.result(5),9)
        self.assertEqual(mac.result(2),0)

    def test0power(self):
        mac = Macaulay(2,1,0)
        self.assertEqual(mac.result(1), 0)
        self.assertEqual(mac.result(5), 1)
        self.assertEqual(mac.result(2), 1)

    def testintegrate(self):
        #test if integration works
        mac = Macaulay(2,1,2)
        mac.integrate()
        self.assertEqual(mac.power, 3)
        self.assertEqual(mac.b,1/3)


if __name__ == '__main__':
    unittest.main()



