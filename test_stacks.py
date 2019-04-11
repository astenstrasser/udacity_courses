from stacks import Stack
from stacks import Element
from stacks import LinkedList
import pytest


class TestStacks:

    @pytest.fixture
    def e1(self):
        e1 = Element(1)
        return e1

    @pytest.fixture
    def e2(self):
        e2 = Element(2)
        return e2

    @pytest.fixture
    def e3(self):
        e3 = Element(3)
        return e3

    @pytest.fixture
    def e4(self):
        e4 = Element(4)
        return e4

    @pytest.fixture
    def stack(self, e1, e2, e3):
        stack = Stack(e1)
        stack.append(e2)
        stack.append(e3)
        return stack

    def test_push(self, e1):
        pass