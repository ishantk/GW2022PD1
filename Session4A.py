subway_menu = [
    {
        "name": "Paneer Tikka Sandwich",
        "ratings": 4.5,
        "price": 223.81,
        "description": "Your favourite cheese cubes marinated with tandoori sauce, spices and condiments, cooked in an oven to give a smoky taste. Served with a choice of nutritious veggies and a freshly baked bread."
    },

    {
        "name": "Aloo Patty Sandwich",
        "ratings": 3.0,
        "price": 209.57,
        "description": "Your favourite cheese cubes marinated with tandoori sauce, spices and condiments, cooked in an oven to give a smoky taste. Served with a choice of nutritious veggies and a freshly baked bread."
    },

    {
        "name": "Mexican Patty Sandwich",
        "ratings": 5.0,
        "price": 153.81,
        "description": "Your favourite cheese cubes marinated with tandoori sauce, spices and condiments, cooked in an oven to give a smoky taste. Served with a choice of nutritious veggies and a freshly baked bread."
    },
]

for idx in range(0, len(subway_menu)):
    if subway_menu[idx]["price"] <= 200:
        continue

    subway_menu[idx]["price"] -= 0.20*subway_menu[idx]["price"]

print(subway_menu)