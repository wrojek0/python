import math

class Point:
    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):         # zwraca string "(x, y)"
        return "({0}, {1})".format(self.x,self.y)

    def __repr__(self):         # zwraca string "Point(x, y)"
        return "Point({0}, {1})".format(self.x,self.y)


    def __eq__(self, other):    # obsługa point1 == point2
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):   # v1 + v2
        return Point(self.x+other.x,self.y+other.y)

    def __sub__(self, other):  # v1 - v2
        return Point(self.x-other.x,self.y-other.y)

    def __mul__(self, other):   # v1 * v2, iloczyn skalarny
        return self.x*other.x+self.y*other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def length(self):           # długość wektora
        return math.sqrt(self.x**2+self.y**2)

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase):
    def test_str(self):
        point = Point(1,2)
        self.assertEqual(str(point),"(1, 2)")

    def  test_repr(self):
        point = Point(1,2)
        self.assertEqual(repr(point),"Point(1, 2)")

    def test_eq(self):
        point = Point(1,2)
        point1 = Point(1,2)
        point2 = Point(1,3)
        self.assertTrue(point==point1)
        self.assertFalse(point==point2)

    def test_add(self):
        point = Point(1,2)
        point1 = Point(2,3)
        point3 = Point(3,5)
        self.assertEqual(point+point1,point3)

    def test_sub(self):
        point = Point(1,2)
        point1 = Point(2,3)
        point3 = Point(-1,-1)
        self.assertEqual(point-point1,point3)

    def  test_mul(self):
        point = Point(1,2)
        point1 = Point(2,3)
        res = 8
        self.assertEqual(point*point1,res)

    def test_len(self):
        point = Point(2,3)
        self.assertEqual(Point.length(point),math.sqrt(13))







if __name__ == '__main__':
    unittest.main()
