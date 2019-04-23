
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
    # """Retorne Verdadeiro caso o valor 
    # estiver contido na árvore, caso contrário, 
    # retorne Falso."""
        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        """Imprima todos os nodes (nós) de árvore
        conforme são visitados em
        uma travessia preordenada."""
        return ""

    def preorder_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False

    def preorder_print(self, start, traversal):
        """Método auxiliar - utilize-o para criar uma 
        solução recursiva de impressão."""
        return traversal
