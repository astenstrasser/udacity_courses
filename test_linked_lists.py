from linked_lists import Element
from linked_lists import LinkedList
import pytest


class TestLinkedLists:

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
    def linkedlist(self, e1, e2, e3):
        linkedlist = LinkedList(e1)
        linkedlist.append(e2)
        linkedlist.append(e3)
        return linkedlist

    def test_linked_lists(self, linkedlist):
        assert linkedlist.head.next.next.value == 3

    def test_get_position(self,linkedlist):
        assert linkedlist.get_position(3).value == 3

    def test_insert(self, linkedlist, e4):
        linkedlist.insert(e4,3)
        assert linkedlist.get_position(3).value == 4

    def test_delete(self, linkedlist):
        value_to_be_deleted = 1
        linkedlist.delete(value_to_be_deleted)
        assert linkedlist.get_position(1).value == 2