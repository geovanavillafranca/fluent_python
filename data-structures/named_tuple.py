from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')

"""
Required a class name and a list of field names
Can access the fields by name or position
"""

tokyo = City('Tokyo', 'JP', 36.933, (35.897779, 138.927733))
print(tokyo)
# City(name='Tokyo', country='JP', population=36.933, coordinates=(35.897779, 138.927733))

print(tokyo.population)
# 36.933

print(tokyo.country)
# JP

print(tokyo[0])
# Tokyo


print(City._fields)
# ('name', 'country', 'population', 'coordinates')


###################################################

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City(*delhi_data)
print(delhi)
# City(name='Delhi NCR', country='IN', population=21.935, coordinates=LatLong(lat=28.613889, long=77.208889))

print(delhi._asdict()) # this return a dict format so now we can do a for 
# {'name': 'Delhi NCR', 'country': 'IN', 'population': 21.935, 'coordinates': LatLong(lat=28.613889, long=77.208889)}

for key, value in delhi._asdict().items():
    print(key, ':', value)
"""
name : Delhi NCR
country : IN
population : 21.935
coordinates : LatLong(lat=28.613889, long=77.208889)
"""
