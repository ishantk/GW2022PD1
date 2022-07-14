# PEP: for clean code: https://peps.python.org/pep-0008/
# Operators
# Arithmetic +, -, *, **, /, //, %
product_price = 125.50
taxes = 0.18

product_price = product_price + (taxes * product_price)
print("product_price:", product_price)

number = 10
# result = number/3
# result = number//3
result = number % 3
print("result:", result)

base = 2
result = base ** 3
print("result now is:", result)

# Assignment Operators
# =, +=, -=, *=, **=, /=, //=, %=
age = 20
# age = age + 10
age += 10 # 30
age -= 5 # 25
age %= 3 # 1
print("Age is:", age) # 1

# No Increment/Decrement i.e. ++ and --
idx = 0
idx += 1
idx -= 1

number = 37
bucket_size = 13
hash_code = number % bucket_size
print("hash_code is:", hash_code)
