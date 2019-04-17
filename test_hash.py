from hash import HashTable
import pytest

class TestHash:

    @pytest.fixture
    def hash_table(self):
        hash_table = HashTable()
        return hash_table

    def test_calculate_hash_value(self):
        pass