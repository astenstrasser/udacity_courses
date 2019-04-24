from binary_search_tree import Node
from binary_search_tree import BinarySearchTree
import pytest

class TestBinarySearchTree:
    
    @pytest.fixture
    def tree(self):
        tree = BinarySearchTree(4)
        return tree

    def test_insert(self, tree):
        tree.insert(2)
        tree.insert(1)
        tree.insert(3)
        tree.insert(5)
        assert tree.get_values() == '42135'
        
            