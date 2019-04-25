from binary_search_tree import Node
from binary_search_tree import BinarySearchTree
import pytest

class TestBinarySearchTree:
    
    @pytest.fixture
    def tree(self):
        tree = BinarySearchTree(4)
        tree.insert(2)
        tree.insert(1)
        tree.insert(3)
        tree.insert(5)
        return tree

    def test_insert(self, tree):
        assert tree.get_values() == '42135'
    
    test_input = [(1, True),
                  (0, False),
                  (3, True),
                  (6, False)]
        
    @pytest.mark.parametrize('search_input, expected', test_input)
    def test_search(self, tree, search_input, expected):
        assert tree.search(search_input) == expected
        
            