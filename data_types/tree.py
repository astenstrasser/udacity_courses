
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        tree = self.preorder_print(self.root, '')[:-1]
        return tree

    def preorder_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False

    def preorder_print(self, node, tree_track):
        if node:
            tree_track += str(node.value)+'-'
            tree_track = self.preorder_print(node.left, tree_track)
            tree_track = self.preorder_print(node.right, tree_track)
        return tree_track
