from collections import namedtuple


Workshop = namedtuple('Workshop', 'name model price year km used')

onix = Workshop('Onix', 'LT', 79.000, 2022, 0, 'False')
print(onix)
print(onix.name)
print(onix.used)


kawazaki = Workshop('kawazaki Ninja', '400', 33.000, 2022, 34.980, 'True')
print(kawazaki)
print(kawazaki.name)
print(kawazaki.used)

