import unittest
from frac import *

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([1,7],[2,9]), [23,63])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([2,4],[1,4]),[1,4])
        self.assertEqual(sub_frac([18,20],[1,3]),[17,30])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([2,4],[1,4]),[1,8])
        self.assertEqual(mul_frac([2,6],[3,4]),[1,4])

    def test_div_frac(self):
        self.assertEqual(div_frac([3,4],[2,3]),[9,8])
        self.assertEqual(div_frac([2,6],[3,4]),[4,9])

    def test_is_positive(self):
        self.assertEqual(is_positive([-1,2]),False)
        self.assertEqual(is_positive([2,3]),True)
        self.assertEqual(is_positive([-2,-3]),True)

    def test_is_zero(self):
        self.assertEqual(is_zero([-1,2]),False)
        self.assertEqual(is_zero([0,3]),True)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1,3],[1,2]),-1)
        self.assertEqual(cmp_frac([1,5],[1,5]),0)


    def test_frac2float(self):
        self.assertEqual(frac2float([1,2]),0.5)


    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
