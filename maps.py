# maps exercise - python practice

locations = {'América do Norte': {'Estados Unidos': ['Mountain View']}}
locations['América do Norte']['Estados Unidos'].append('Atlanta')

locations['Ásia'] = {'Índia': ['Bangalore']}
locations['Ásia']['China'] = ['Xangai']

locations['África'] = {'Egito': ['Cairo']}

cities_of_asia = []
for countries, cities in locations['Ásia'].items():
    city_country = cities[0] + " - " + countries
    cities_of_asia.append(city_country)


print(sorted(locations['América do Norte']['Estados Unidos']))
print(sorted(cities_of_asia))
