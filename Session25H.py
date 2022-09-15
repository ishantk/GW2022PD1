from functools import reduce

product_prices = [2000, 2500, 1500, 6000, 7000, 8000, 11000, 12000]

# def calculate_discount(amount, discount=0.50):
#     return amount - (amount*discount)

discount_lambda = lambda amount, discount=0.50 : amount - (amount*discount)


print("Original Prices:")
print(product_prices)

"""
for idx in range(len(product_prices)):
    product_prices[idx] = discount_lambda(product_prices[idx])

print("Discounted Prices:")
print(product_prices)
"""

# map(discount_lambda, product_prices)

discounted_prices = list(map(discount_lambda, product_prices))
print("Discounted Prices:")
print(discounted_prices)


filtered_products = list(filter(lambda price: price > 5000 and price < 10000, product_prices))
print("Filtered Products:")
print(filtered_products)

shopping_cart = [1200, 3000, 2000]
print(sum(shopping_cart))

amount_to_pay = reduce(lambda x, y: x+y, shopping_cart)
print(amount_to_pay)

