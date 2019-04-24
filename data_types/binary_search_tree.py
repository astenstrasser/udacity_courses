

class Node:

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:

    def __init__(self, value):
        self.root = Node(value)

    def insert(self, value):
        pass

    def get_values(self, position = self.root, tree_values = ''):
        if position:
            tree_values += str(position.value)
            tree_values = get_values(self.left, tree_values)
            tree_values = get_values(self.right, tree_values)
        return tree_values
            
