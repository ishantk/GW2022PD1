# Unicode Table: https://unicode-table.com/en/blocks/
# Print Your Name in Native Language of Your Choice

message = """
    Welcome to Zomato
    Apply Promo Code
    
    -------
    TRYNEW
    -------
    Get 30% OFF up to ₹75
    Valid on total value of items worth ₹149 or more.
    
    -------
    ZOMATO
    -------
    FLAT 100 OFF
     Valid on total value of items worth ₹249 or more.
"""
print(message)

amount = int(input("Enter Order Amount: "))
promo_code = input("Enter Promo Code: ")

print("Amount: \u20b9", amount)
print("Prom Code:", promo_code)

# Regular or Basic if/else
"""
if amount >= 149:
    print("You can Apply Promo Code")
    print("You can get some discounts :)")
else:
    print("Sorry, Promo Code Not Available")
    print("Add items worth", (149-amount), "more")
"""

"""
if promo_code == "TRYNEW" and amount >= 149:
    discount = 0.30 * amount
    print("Dicount is: \u20b9", discount)
    amount -= discount
    print("Please Pay: \u20b9", amount)
else:
    print("Either Promo Code or Amount is Invalid")
"""

# Nested if/else
"""
if promo_code == "TRYNEW":
    if amount >= 149:
        discount = 0.30 * amount
        print("Discount is: \u20b9", discount)
        amount -= discount
        print("Please Pay: \u20b9", amount)
    else:
        print("Add items worth", (149-amount), "more")
else:
    print("Promo Code is Invalid")
    print("Please Pay: \u20b9", amount)
"""

"""
if promo_code == "TRYNEW":
    if amount >= 149:
        discount = 0.30 * amount

        if discount > 75:
            discount = 75

        print("Discount is: \u20b9", discount)
        amount -= discount
        print("Please Pay: \u20b9", amount)
    else:
        print("Add items worth", (149-amount), "more")
else:
    print("Promo Code is Invalid")
    print("Please Pay: \u20b9", amount)
"""

if promo_code == "TRYNEW":
    if amount >= 149:
        discount = 0.30 * amount

        if discount > 75:
            discount = 75

        print("Discount is: \u20b9", discount)
        amount -= discount
        print("Please Pay: \u20b9", amount)
    else:
        print("Add items worth", (149-amount), "more")

elif promo_code == "ZOMATO":
    if amount >= 249:
        print("ZOMATO Applied Successfully")
        print("Please Pay: \u20b9", amount-100)
    else:
        print("Please Pay: \u20b9", amount)
else:
    print("Promo Code is Invalid")
    print("Please Pay: \u20b9", amount)

# Assignment: Suggest the correct promo code to the user :)
#             which saves money :)

