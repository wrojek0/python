import math

def area(a,b,c):
    if( a+b < c or a+c<b or b+c<a or a<0 or b<0 or c<0 ):
        raise ValueError("This is not a triangle!")
    p = (a+b+c)/2
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return area


import unittest

class test(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(3,4,5),6)
        with self.assertRaises(ValueError):
            area(0,3,5)



if __name__ == '__main__':
    unittest.main()
