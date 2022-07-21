# Unpacking tuple

lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates
print(latitude)
print(longitude)
"""
33.9425
-118.408056
"""


traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

# % formatting operator understands tuples and treats each item as a separate field
for passport in sorted(traveler_ids):
    print( '%s/%s' % passport)

"""
BRA/CE342567
ESP/XDA205856
USA/31195855
"""

# Retrieve the items of a tuple separately (unpacking). Not interested in the secound item, so it's assigned to _ a dummy variable
for country, _ in traveler_ids:
    print(country)

"""
USA
BRA
ESP
"""


# Defining function parameters with *args to grab arbitrary excess arguments
a, b, *rest = range(5)
print(a, b, rest)
#     0  1  [2, 3, 4]
a, b, *rest = range(3)

a, b, *rest = range(2)
print(a, b, rest)
#     0  1  []

# It can appear in any position
a, *body, c, d = range(5)
print(a, body, c, d)
#     0 [1, 2] 3  4

*head, b, c, d = range(5)
print(head, b, c, d)
#    [0, 1] 2  3  4
