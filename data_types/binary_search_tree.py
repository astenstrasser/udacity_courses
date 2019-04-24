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
        if position.value < value:
            if position.left == None:
                position.left = Node(value)
            else:
                insert(value, position.left)   
        if position.value > value:
            if position.right == None:
                position.right = Node(value)
            else:
                insert(value, position.right)

    def get_values(self, position = 'root', tree_values = ''):
        if position:
            if position == 'root':
                position = self.root
            tree_values += str(position.value)
            tree_values = get_values(self.left, tree_values)
            tree_values = get_values(self.right, tree_values)
        return tree_values
            
