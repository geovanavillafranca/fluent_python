colors = ['black', 'white']
sizes = ['S', 'M', 'L']

#  tshirts = [(color, size) for size in sizes for color in colors]

# print(tshirts)
# >>> [('black', 'S'), ('white', 'S'), ('black', 'M'), ('white', 'M'), ('black', 'L'), ('white', 'L')]

for tshirts in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirts)
    """
    black S
    black M
    black L
    white S
    white M
    white L
    """

