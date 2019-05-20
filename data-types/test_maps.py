import maps
import pytest


class TestMaps:

    @pytest.fixture
    def locations(self):
        locations = {'América do Norte': {'Estados Unidos': ['Mountain View']}}
        locations['América do Norte']['Estados Unidos'].append('Atlanta')
        locations['Ásia'] = {'Índia': ['Bangalore']}
        locations['Ásia']['China'] = ['Xangai']
        locations['África'] = {'Egito': ['Cairo']}
        return locations

    def test_cities_of_asia(self, locations):
        expected = ['Bangalore - Índia', 'Xangai - China']
        assert maps.cities_of_asia(locations) == expected

    def test_cities_of_usa(self, locations):
        expected = ['Atlanta', 'Mountain View']
        assert maps.cities_of_usa(locations) == expected
