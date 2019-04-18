from tree import Node
from tree import BinaryTree
import pytest

class TestBinaryTree:

    @pytest.fixture
    def binary_tree(self):
        binary_tree = BinaryTree(1)
        return binary_tree

    def test_search(self):
        pass