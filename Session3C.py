# Bitwise Operators
# &, |, ^

num1 = 10
num2 = 8

print(bin(num1))         # 1 0 1 0
print(bin(num2))         # 1 0 0 0

result1 = num1 & num2    # 1 0 0 0 -> 8
result2 = num1 | num2    # 1 0 1 0 -> 10
result3 = num1 ^ num2    # 0 0 1 0 -> 2
print(result1, result2, result3)

# Assignment: Find a use case in the world of security, may be some algo where bitwise operators are used

# Shift Operators
# >> <<
num3 = 8    # 0 0 0 0  1 0 0 0
num4 = 2

result4 = num3 >> num4
#        >> 2 |  0 0 0 0  1 0 0 0 | _ _ 0 0  0 0 1 0  | -> 0 0 0 0  0 0 1 0
print(result4) # 2
#               0 0 0 0  0 0 1 0
#               0 0 0 0  1 0 _ _
#               0 0 0 0  1 0 0 0
result5 = result4 << num4 # 8

num5 = -11
result = num5 >> 3
print("result is:", result)

"""
    11:  0 0 0 0  1 0 1 1
         1 1 1 1  0 1 0 0
                        1
         1 1 1 1  0 1 0 1 -> -11
         >> 3
         _ _ _ 1  1 1 1 0
         1 1 1 1  1 1 1 0
         0 0 0 0  0 0 0 1
                        1
         0 0 0 0  0 0 1 0 -> -2
"""
result = -14 >> 3
print(result) # ?


