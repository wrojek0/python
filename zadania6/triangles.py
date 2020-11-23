
from points import Point
import math
class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):          # "[(x1, y1), (x2, y2), (x3, y3)]"
        return "[{0}, {1}, {2}]".format(str(self.pt1),str(self.pt2),str(self.pt3))

    def __repr__(self):        # "Triangle(x1, y1, x2, y2, x3, y3)"
        return "Triangle({0}, {1}, {2}, {3}, {4}, {5})".format(self.pt1.x,self.pt1.y,self.pt2.x,self.pt2.y,self.pt3.x,self.pt3.y)

    def __eq__(self, other):    # obsługa tr1 == tr2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2 and self.pt3 == other.pt3

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def center(self):           # zwraca środek trójkąta
        return Point((self.pt1.x+self.pt2.x+self.pt3.x)/3,(self.pt1.y+self.pt2.y+self.pt3.y)/3)

    def area(self):             # pole powierzchni
        area = (1/2)*abs((self.pt2.x-self.pt1.x)*(self.pt3.y-self.pt1.y)-(self.pt2.y-self.pt1.y)*(self.pt3.x-self.pt1.x))

        return area



    def move(self, x, y):       # przesunięcie o (x, y)
        self.pt1.x+=x
        self.pt1.y+=y

        self.pt2.x+=x
        self.pt2.y+=y

        self.pt3.x+=x
        self.pt3.y+=y

# Kod testujący moduł.

import unittest

class TestTriangle(unittest.TestCase):
    def test_str(self):
        tr = Triangle(0,1,1,1,-1,0)
        self.assertEqual(str(tr),"[(0, 1), (1, 1), (-1, 0)]")

    def test_repr(self):
        tr = Triangle(0,1,1,1,-1,0)
        self.assertEqual(repr(tr), "Triangle(0, 1, 1, 1, -1, 0)")

    def test_eq(self):
        tr = Triangle(0,1,1,1,-1,0)
        tr1 = Triangle(0,1,1,1,-1,0)
        tr2 = Triangle(1,2,3,2,5,6)
        self.assertTrue(tr == tr1)
        self.assertFalse(tr == tr2)

    def test_center(self):
        tr = Triangle(0,1,1,1,-1,0)
        print("Srodek trojkata o wspolrzednych ",repr(tr),tr.center())

    def test_area(self):
        tr = Triangle(-2,0,2,0,0,3)
        self.assertEqual(tr.area(),6)

    def test_move(self):
        tr = Triangle(-2,0,2,0,0,3)
        tr.move(1,1)
        self.assertEqual(tr,Triangle(-1,1,3,1,1,4))




if __name__ == '__main__':
    unittest.main()
