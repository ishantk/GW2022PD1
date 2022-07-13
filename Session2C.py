# Create Operation - Single Value Container
fries_price = 50
# Create + Copy Operation
coke_price = fries_price
# Update Operation
coke_price = 70

print("fries_price:", fries_price, hex(id(fries_price)))
print("coke_price:", coke_price, hex(id(coke_price)))

# Create Operation - Multi Value Container (List)
dish_prices = [10, 20, 30, 40, 50]
# Create + Copy Operation ---> REFERENCE COPY
johns_cafe_dish_prices = dish_prices

print("dish_prices:", dish_prices, hex(id(dish_prices)))
print("johns_cafe_dish_prices:", johns_cafe_dish_prices, hex(id(johns_cafe_dish_prices)))

# Update Operation
johns_cafe_dish_prices[2] = 375
johns_cafe_dish_prices[3] = 400

# Delete Element
del johns_cafe_dish_prices[1]
del johns_cafe_dish_prices

print("dish_prices:", dish_prices, hex(id(dish_prices)))
# print("johns_cafe_dish_prices:", johns_cafe_dish_prices, hex(id(johns_cafe_dish_prices)))


