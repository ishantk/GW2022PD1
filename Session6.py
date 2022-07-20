def add(num1, num2):
    result = num1 + num2
    print("result from add is:", result)


print("add is:", add) # HashCode

# Reference Copy
addition = add      # addition and add they both refer to the same function

# del add

print("addition is:", addition) # HashCode which is same as of add
addition(10, 20)

# defining addition function
def addition(num1, num2, num3):
    result = num1+num2+num3
    print("Result from addition is:", result)

# ReDefining the Function: Update the definition of the function
# Now, old definition does not exists and new one will work
def addition(amount):
    return amount * 0.18


print("add now is:", add)               # HashCode
print("addition now is:", addition)     # HashCode which is same as of add

del addition

# addition(10, 20, 30) -> error
print(addition(1200))
add(10, 20)