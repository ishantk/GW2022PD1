# TUPLES
# Tuples are IMMUTABLE

prices = (100, 200, 300, 50, 80)
print(prices, hex(id(prices)))

my_prices = prices
print(my_prices, hex(id(my_prices)))

all_prices = (100, 200, 300, 50, 80)
print(all_prices, hex(id(all_prices)))

print(type(prices), type(my_prices), type(all_prices))

print(my_prices[0])
# prices[0] = 122 # error
# del prices[0]   # error
del prices