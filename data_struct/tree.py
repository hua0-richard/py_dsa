class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def insert(self, v, n):
        if n == None:
            return Node(v)
        elif n.value < v:
            n.right = self.insert(v, n.right)
        elif n.value > v:
            n.left = self.insert(v, n.left)
        return n
    
    def printTree(self, n):
        if (n == None):
            return
        self.printTree(n.left)
        print(n.value)
        self.printTree(n.right);

b = BinaryTree(0)
b.insert(1, b.root)
b.insert(2, b.root)
b.insert(-1, b.root)
b.insert(3, b.root)
b.insert(45, b.root)

b.printTree(b.root)
                

            