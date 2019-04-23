from tree import Node
from tree import BinaryTree
import pytest

class TestBinaryTree:

    @pytest.fixture
    def binary_tree(self):
        binary_tree = BinaryTree(1)
        binary_tree.root.left = Node(2)
        binary_tree.root.right = Node(3)
        binary_tree.root.left.left = Node(4)
        binary_tree.root.left.right = Node(5)
        return binary_tree

    search_test_input = [(3, True),
                         (0, False)] 
    @pytest.mark.parametrize('searched, expected', search_test_input)
    def test_search(self, binary_tree, searched, expected):
        assert binary_tree.search(searched) == expected

    def test_print(self, binary_tree):
        assert binary_tree.print_tree() == '1-2-4-5-3'
