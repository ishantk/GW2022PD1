# This is session1 on Storage Containers i.e. MODEL
"""
    Authored By
    Ishant Kumar
    @Auribises
"""

# Textual Storage Container -> String
# Decimal Values -> Floating Point
# Integer
# '', "", """"""

# Creating Storage Containers
dish_name = 'Poori Thali'
dish_ratings = 4.5
dish_price = 149

# Read Storage Containers
print("dish_name is:", dish_name, id(dish_name), oct(id(dish_name)))
print("dish_ratings is:", dish_ratings, id(dish_ratings), bin(id(dish_name)))
print("dish_price is:", dish_price, id(dish_price), hex(id(dish_price)))

# Copy Operation + Create Operation
mojito_price = dish_price
print("mojito_price is:", mojito_price, id(mojito_price), hex(id(mojito_price)))

age_of_tree = 149
print("age_of_tree is:", age_of_tree, id(age_of_tree), hex(id(age_of_tree)))

print("Class of dish_name is:", type(dish_name))
print("Class of dish_ratings is:", type(dish_ratings))
print("Class of dish_price is:", type(dish_price))


