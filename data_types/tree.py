
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
        found = False
        return found

    def print_tree(self):
        """Imprima todos os nodes (nós) de árvore
        conforme são visitados em
        uma travessia preordenada."""
        return ""

    def preorder_search(self, start, find_val):
        """Método auxiliar - utilize-o para criar uma 
        solução recursiva de pesquisa."""
        return False

    def preorder_print(self, start, traversal):
        """Método auxiliar - utilize-o para criar uma 
        solução recursiva de impressão."""
        return traversal
