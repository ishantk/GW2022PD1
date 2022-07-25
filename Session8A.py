mc_donalds_menu = [
    {
        "name": "burger",
        "price": 100,
        "quantity": 0
    },
    {
        "name": "fries",
        "price": 70,
        "quantity": 0
    },
    {
        "name": "coke",
        "price": 50,
        "quantity": 0
    },
    {
        "name": "pizza",
        "price": 300,
        "quantity": 0
    },
    {
        "name": "noodles",
        "price": 200,
        "quantity": 0
    }
]

def shoppin_cart():

    # Shopping Cart
    cart = []

    total_amount = 0
    total_dishes = 0

    choice = "yes"
    while choice == "yes":
        dish_name = input("Enter Dish Name: ")

        for idx in range(len(mc_donalds_menu)):
            if mc_donalds_menu[idx]["name"] == dish_name:
                quantity = int(input("Enter the Quantity for "+dish_name+" :"))
                mc_donalds_menu[idx]["quantity"] = quantity
                total_dishes += quantity
                total_amount += quantity * mc_donalds_menu[idx]["price"]
                cart.append(mc_donalds_menu[idx])
                break

        choice = input("Do You wish to continue (yes/no): ")

    print("CART [", len(cart), "]")
    print(cart)
    print("Total Dishes:", total_dishes)
    print("Please Pay: \u20b9:", total_amount)

    return total_amount


result = shoppin_cart()




# Complete the journey of checkout by asking user to apply promo code :)