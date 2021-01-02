
#10.2
class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementów na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full() :
            raise ValueError("Stack is full!")
        else:
            self.items[self.n] = data
            self.n += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty!")
        else:
            self.n -= 1
            data = self.items[self.n]
            self.items[self.n] = None    # usuwam referencję
        
        return data


import unittest

class Test(unittest.TestCase):
    
     def test_is_empty(self):
        self.assertTrue(Stack(55).is_empty())
        self.assertTrue(Stack(2).is_empty())
        s = Stack(10)
        s.push(7)
        self.assertFalse(s.is_empty())

     def test_is_full(self):
        s = Stack(1)
        self.assertFalse(s.is_full())
        s.push(1)
        self.assertTrue(s.is_full())


     def test_push(self):
         s = Stack(2)
         s.push(1)
         s.push(2)
         with self.assertRaises(ValueError):
             s.push(3)

     def test_pop(self):
         s = Stack(3)
         s.push(1)
         s.push(2)
         s.push(3)
         self.assertEqual(s.pop(),3)
         self.assertEqual(s.n, 2)
         self.assertEqual(s.pop(),2)
         self.assertEqual(s.pop(),1)
         with self.assertRaises(ValueError):
             s.pop()

     


if __name__ == '__main__':
    unittest.main()


