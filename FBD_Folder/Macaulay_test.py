import unittest
from FBD_Folder.Macaulay import macaulay

class Macaulaytests(unittest.TestCase):

    def testxsmallera(self):
        # test if it returns 0 if x is smaller than a
        self.assertEqual(macaulay(2,5),0)

    def testmacactive(self):
        # test if it returns x-a if x is bigger than a.
        self.assertEqual(macaulay(5,2),3)


if __name__ == '__main__':
    unittest.main()



