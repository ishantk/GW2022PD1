mc_donalds_menu = {
    "burger": 100,
    "fries": 50,
    "coke": 40,
    "icecream": 70,
    "noodles": 150,
    "pizza": 200
}

# Shopping Cart
cart = []

choice = "yes"

while choice == "yes":
    dish_name = input("Enter Dish Name: ")
    cart.append(mc_donalds_menu[dish_name])

    choice = input("Do You wish to continue (yes/no): ")

print("CART")
print(cart)
print("Please Pay: \u20b9:", sum(cart))