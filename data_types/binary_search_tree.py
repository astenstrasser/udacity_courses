class Node:

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:

    def __init__(self, value):
        self.root = Node(value)

    def insert(self, value, position = 'root'):
        if position == 'root':
            position = self.root
        if position.value > value:
            if position.left == None:
                position.left = Node(value)
            else:
                self.insert(value, position.left)   
        if position.value < value:
            if position.right == None:
                position.right = Node(value)
            else:
                self.insert(value, position.right)

    def get_values(self, position = 'root', tree_values = ''):
        if position:
            if position == 'root':
                position = self.root
            tree_values += str(position.value)
            tree_values = self.get_values(position.left, tree_values)
            tree_values = self.get_values(position.right, tree_values)
        return tree_values
    
    def search(self, value, position = 'root'):
        if position:
            if position == 'root':
                position = self.root
            if position.value == value:
                return True
            else:
                if self.search(value, position.left) or self.search(value, position.right):
                    return True
            return False
            
