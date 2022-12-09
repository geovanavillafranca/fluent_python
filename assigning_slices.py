l = list(range(10))
print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

l[2:5] = [20, 30]
print(l)
# [0, 1, 20, 30, 5, 6, 7, 8, 9]

del l[5:7]
print(l)
# [0, 1, 20, 30, 5, 8, 9]

l[3::2] = [11, 22]
print(l)
# [0, 1, 20, 11, 5, 22, 9]

"""
l[2:5] = 100
print(l)
# TypeError: can only assign an iterable
"""

l[2:5] = [100]
print(l)
# [0, 1, 100, 22, 9]


t = (1, 2, [30, 40])
# t[2] += [50, 60]
print(t)
"""
Traceback (most recent call last):
  File "d:\workspace\fluent-python\assigning_slices.py", line 29, in <module>
    t[2] += [50, 60]
TypeError: 'tuple' object does not support item assignment

(1, 2, [30, 40, 50, 60])
"""

#  works without error
t[2].extend([50, 60])
print(t)
# (1, 2, [30, 40, 50, 60])


fruits = ['grape', 'raspberry', 'apple', 'banana']

print(sorted(fruits))
# ['apple', 'banana', 'grape', 'raspberry']

print(fruits)
# ['grape', 'raspberry', 'apple', 'banana']

print(sorted(fruits, reverse=True))
# ['raspberry', 'grape', 'banana', 'apple']

print(sorted(fruits, key=len))
# ['grape', 'apple', 'banana', 'raspberry']

print(sorted(fruits, key=len, reverse=True))
# ['raspberry', 'banana', 'grape', 'apple']

fruits.sort()
print(fruits)
# ['apple', 'banana', 'grape', 'raspberry']

