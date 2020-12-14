class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie




class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0   # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        #return self.length == 0
        return self.head is None

    def count(self):   # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(N)
        if self.head:   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):          # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node

    def remove_tail(self):   # klasy O(N)
        if self.is_empty():
            raise ValueError("pusta lista")

        removed = self.tail
        current = self.head
        if(current == removed):
            self.head = self.tail = None
        else:
            while current.next is not self.tail:
                current = current.next
            current.next = None
            self.tail = current
            self.length -= 1
        return removed

    def merge(self,other):
        if self == other:
            raise ValueError("error")
        
        if self.is_empty():
            self.head = other.head
            self.tail = other.tail
            self.length = other.length
        else: 
            self.tail.next = other.head
            self.tail = other.tail
            self.length += other.length
            other.head = None
            other.tail = None

            
          

    def display(self):
        if self.is_empty():
            return "[ ]"

        current = self.head
        lista = []

        while current:
            lista.append(str(current))
            current = current.next

        print(lista)







def main():
    list = SingleList()
    list2 = SingleList()
    list.insert_tail(Node(1))
    list.insert_tail(Node(2))
    list2.insert_tail(Node(3))
    list2.insert_tail(Node(4))
    list.merge(list2)
    list.display()
    

if __name__ == '__main__':
    main()
