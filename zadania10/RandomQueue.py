import random


#10.8
class RandomQueue:
    def __init__(self, size=5):
        self.n = size + 1  # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.head = 0  # pierwszy do pobrania
        self.tail = 0  # pierwsze wolne

    def insert(self, item):
        if self.is_full():
            raise ValueError("Kolejka jest przepelniona")
        else:
            self.items[self.tail] = item
            self.tail = (self.tail + 1) % self.n

    def remove(self):
        if self.is_empty():
            raise ValueError("Brak elementow w kolejce")
        #zabieramy losowy element i na miejsce usunietego elementu wstawiamy ostatni
        else:
            positionElement=random.randint(0, self.tail-1)
            data = self.items[positionElement]
            self.items[positionElement] = self.items[self.tail-1]  
            self.tail=self.tail-1 
            return data

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n - 1) % self.n == self.tail


import unittest

class Test(unittest.TestCase):
    def test_insert(self):
        q = RandomQueue(3)
        q.insert(1)
        q.insert(2)
        q.insert(3)
        self.assertTrue(q.is_full())
        with self.assertRaises(ValueError):
            q.insert(4)

    def test_remove(self):
        q = RandomQueue(5)
        q.insert(1)
        self.assertEqual(q.remove(),1)
        self.assertTrue(q.is_empty())
        with self.assertRaises(ValueError):
            q.remove()
       
    
    def test_is_full(self):
        q = RandomQueue(3)
        q.insert(1)
        q.insert(2)
        self.assertFalse(q.is_full())
        q.insert(3)
        self.assertTrue(q.is_full())
        q.remove()
        self.assertFalse(q.is_full())

    def test_is_empty(self):
        q = RandomQueue(3)
        self.assertTrue(q.is_empty())
        q.insert(1)
        self.assertFalse(q.is_empty())


        
    
     

     


if __name__ == '__main__':
    unittest.main()