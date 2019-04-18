from hash import HashTable
import pytest

class TestHash:

    @pytest.fixture
    def hash_table(self):
        hash_table = HashTable()
        return hash_table

    def test_calculate_hash_value(self, hash_table):
        assert hash_table.calculate_hash_value('UDACITY') == 8568

    def test_edge_case(self, hash_table):
        assert hash_table.lookup('UDACITY') == -1

    def test_store(self, hash_table):
        hash_table.store('UDACITY')
        assert hash_table.lookup('UDACITY') == 8568