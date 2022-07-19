"""
for idx in range(1, 11, 1):
    print("idx is:", idx)
"""


def print_number(number):
    print("number is:", number)
    number += 1
    if number <= 10:
        print_number(number)


print_number(1)


