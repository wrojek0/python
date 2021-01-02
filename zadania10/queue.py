


#10.4
class Queue:

    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None] 
        self.head = 0           # pierwszy do pobrania 
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, data):
        if self.is_full():
            raise ValueError("Queue is full!")
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if self.is_empty():
            raise ValueError("Queue is empty!")
        data = self.items[self.head]
        self.items[self.head] = None      # usuwam referencję
        self.head = (self.head + 1) % self.n
        return data


import unittest

class Test(unittest.TestCase):
    
     def test_is_empty(self): 
        q = Queue(10)
        self.assertTrue(q.is_empty())
        q.put(1)
        self.assertFalse(q.is_empty())        

     def test_is_full(self):
         q = Queue(3)
         self.assertFalse(q.is_full())
         q.put(1)
         q.put(2)
         q.put(3)
         self.assertTrue(q.is_full())

     def test_put(self):
         q = Queue(3)
         q.put(1)
         q.put(2)
         q.put(3)
         with self.assertRaises(ValueError):
             q.put(4)

     def test_get(self):
         q = Queue(3)
         q.put(1)
         q.put(2)
         q.put(3)
         self.assertEquals(q.get(),1)
         self.assertEquals(q.get(),2)
         self.assertEquals(q.get(),3)
         with self.assertRaises(ValueError):
            q.get()

     


if __name__ == '__main__':
    unittest.main()