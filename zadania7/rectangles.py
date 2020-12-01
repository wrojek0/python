from points import Point
import math
class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
    # Chcemy, aby x1 < x2, y1 < y2.
        if x1<x2 and y1<y2:
            self.pt1 = Point(x1, y1)
            self.pt2 = Point(x2, y2)
        else:
            raise ValueError("bad points!")


    def __str__(self):          # "[(x1, y1), (x2, y2)]"
        return "[{0}, {1}]".format(str(self.pt1),str(self.pt2))

    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle({0}, {1})".format(str(self.pt1),str(self.pt2))

    def __eq__(self, other):    # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):           # zwraca środek prostokąta
        temp = self.pt2 - self.pt1
        temp.x = float(temp.x/2)
        temp.y = float(temp.y/2)
        return temp+self.pt1

    def area(self):           # pole powierzchni
        temp = self.pt2 - self.pt1
        area = temp.x*temp.y
        return abs(area)

    def move(self, x, y):       # przesunięcie o (x, y)
        if((isinstance(x,int) or isinstance(x,float)) and (isinstance(y,int) or isinstance(y,float))):
            #sprawdz czy int/float
            return Rectangle(self.pt1.x+x,self.pt1.y+y,self.pt2.x+x,self.pt2.y+y)
        else:
            raise ValueError("Error")


    def intersection(self, other):  # część wspólna prostokątów
        if(isinstance(other,Rectangle) == False):
            raise ValueError("Invalid argument")

        def max(x1,x2):
            if(x1>x2):
                return x1
            else:
                return x2

        def min(x1,x2):
            if(x1>x2):
                return x2
            else:
                return x1


        wpX=max(self.pt1.x,other.pt1.x)
        wkX=min(self.pt2.x,other.pt2.x)
        czwX=wkX-wpX
        wpY=max(self.pt1.y,other.pt1.y)
        wkY=min(self.pt2.y,other.pt2.y)
        czwY=wkY-wpY
        if((czwX<=0) or (czwY<=0)):
            return 0
        else:
            tmpx1=max(self.pt1.x, other.pt1.x)
            tmpy1=max(self.pt1.y, other.pt1.y)
            tmpx2=min(self.pt2.x, other.pt2.x)
            tmpy2=min(self.pt2.y, other.pt2.y)
            return Rectangle(tmpx1,tmpy1,tmpx2,tmpy2)






    def cover(self, other):     # prostąkąt nakrywający oba
        if(isinstance(other,Rectangle) == False):
            raise ValueError("Invalid argument")

        def max(x1,x2):
            if(x1>x2):
                return x1
            else:
                return x2

        def min(x1,x2):
            if(x1>x2):
                return x2
            else:
                return x1

        tmpx1 = min(self.pt1.x,other.pt1.x)
        tmpy1 = min(self.pt1.y,other.pt1.y)
        tmpx2 = max(self.pt2.x,other.pt2.x)
        tmpy2 = max(self.pt2.y,other.pt2.y)
        return Rectangle(tmpx1,tmpy1,tmpx2,tmpy2)



    def make4(self):            # zwraca krotkę czterech mniejszych
        mid=self.center()
        return  Rectangle(self.pt1.x, self.pt1.y, mid.x, mid.y),Rectangle(mid.x, mid.y, self.pt2.x, self.pt2.y),Rectangle(self.pt1.x,mid.y, mid.x,self.pt2.y),Rectangle(mid.x,self.pt1.y,self.pt2.x,mid.y);
# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):
    def test_str(self):
        rec = Rectangle(0,0,2,2)
        self.assertEqual(str(rec),"[(0, 0), (2, 2)]")

    def test_repr(self):
        rec = Rectangle(0,0,2,2)
        self.assertEqual(repr(rec),"Rectangle((0, 0), (2, 2))")

    def test_eq(self):
        rec = Rectangle(0,0,2,2)
        self.assertTrue( rec == Rectangle(0,0,2,2))
        self.assertFalse( rec == Rectangle(1,2,3,4))

    def test_center(self):
        rec = Rectangle(1,2,4,4)
        self.assertEqual(rec.center(),Point(2.5,3))

    def test_area(self):
        rec  = Rectangle(1,2,4,4)
        self.assertEqual(rec.area(),6)

    def test_move(self):
        rec  = Rectangle(1,2,4,4)
        rec.move(1,1)
        self.assertFalse( rec == Rectangle(2,3,5,5))

    def test_intersection(self):
        rec = Rectangle(3,2,9,6)
        rec2 = Rectangle(1,2,7,5)
        rec3 = Rectangle(7,5,10,10)
        self.assertEqual(rec.intersection(rec2),Rectangle(3,2,7,5))
        self.assertEqual(rec.intersection(rec3),Rectangle(7,5,9,6))

    def test_cover(self):
        rec = Rectangle(3,2,9,6)
        rec2 = Rectangle(1,2,7,5)
        rec3 = Rectangle(7,5,10,10)
        self.assertEqual(rec.cover(rec2),Rectangle(1,2,9,6))
        self.assertEqual(rec.cover(rec3),Rectangle(3,2,10,10))

    def test_make4(self):
        rec2 = Rectangle(3,2,9,6)
        print(rec2.make4())




if __name__ == '__main__':
    unittest.main()
