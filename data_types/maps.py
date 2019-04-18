# maps exercise - python practice

locations = {'América do Norte': {'Estados Unidos': ['Mountain View']}}
locations['América do Norte']['Estados Unidos'].append('Atlanta')

locations['Ásia'] = {'Índia': ['Bangalore']}
locations['Ásia']['China'] = ['Xangai']

locations['África'] = {'Egito': ['Cairo']}


def cities_of_asia(locations):
    cities_of_asia = []
    for countries, cities in locations['Ásia'].items():
        city_country = cities[0] + " - " + countries
        cities_of_asia.append(city_country)
    return cities_of_asia


def cities_of_usa(locations):
    cities_of_usa = sorted(locations['América do Norte']['Estados Unidos'])
    return cities_of_usa


print(cities_of_usa(locations))
print(cities_of_asia(locations))
