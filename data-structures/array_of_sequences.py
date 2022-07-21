'''
# Without map
prices = [10, 1000, 1020]

def add_taxes(price):
    return price * 1.1

price_with_taxes = []

for p in prices:
    price_with_taxes.append(add_taxes(p))

print(price_with_taxes)
# [11.0, 1100.0, 1122.0]

# With map()
price_with_taxes = map(add_taxes, prices)
print(price_with_taxes)
# <map object at 0x0000011372BD8FA0>

price_with_taxes = list(map(add_taxes, prices))
print(price_with_taxes)
# [11.0, 1100.0, 1122.0]
'''









