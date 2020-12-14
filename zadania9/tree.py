class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def insert(self, node):
        if node.data < self.data:   # mniejsze na lewo
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
        else:   # większe lub równe na prawo
            if self.right:
                self.right.insert(node)
            else:
                self.right = node

    def count(self):
        counter = 1
        if self.left:
            counter += self.left.count()
        if self.right:
            counter += self.right.count()
        return counter

    def search(self, data):
        if self.data == data:
            return self
        if data < self.data:
            if self.left:
                return self.left.search(data)
        else:
            if self.right:
                return self.right.search(data)
        return None

    def remove(self, data):  # self na pewno istnieje
        # Są lepsze sposoby na usuwanie.
        if data < self.data:
            if self.left:
                self.left = self.left.remove(data)
        elif self.data < data:
            if self.right:
                self.right = self.right.remove(data)
        else:                # self.data == data
            if self.left is None:   # przeskakuje self
                return self.right
            else:     # self.left na pewno niepuste
                # Szukamy największego w lewym poddrzewie.
                node = self.left
                while node.right:   # schodzimy w dół
                    node = node.right
                node.right = self.right   # przyczepiamy
                return self.left
        return self




class BinarySearchTree:
    """Klasa reprezentująca binarne drzewo poszukiwań."""

    def __init__(self):
        self.root = None

    def insert(self, node):
        if self.root:
            self.root.insert(node)
        else:
            self.root = node

    def count(self):
        if self.root:
            return self.root.count()
        else:
            return 0

    def search(self, data):   # zwraca node lub None
        if self.root:
            return self.root.search(data)
        else:
            return None

    def remove(self, data):
        if self.root:
            self.root = self.root.remove(data)



def bst_max(top): #wersja iteracyjna
        if top == None:
            raise ValueError("top is None!!!")
    
        current = top
        while current.right != None:
            current = current.right

        return current

def bst_max_r(top): #wersja rekurencyjna
    if(top.right == None):
        return top
    
    return bst_max_r(top.right)

def bst_min(top): #wersja interacyjna
        if top == None:
            raise ValueError("top is None!!!")
    
        current = top
        while current.left != None:
            current = current.left

        return current

def bst_min_r(top): #wersja rekurencyjna
    if(top.left == None):
        return top
    
    return bst_max_r(top.left)
        
    
def main():
    tree = BinarySearchTree()
    tree.insert(Node(5))
    tree.insert(Node(99))
    tree.insert(Node(55))
    tree.insert(Node(1))
    print(bst_max(tree.root))
    print(bst_max_r(tree.root))
    print(bst_min(tree.root))
    print(bst_min_r(tree.root))



if __name__ == "__main__":
    main()

