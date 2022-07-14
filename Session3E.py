"""
idx = 1
while idx <= 10:
    print(idx)
    idx += 1
"""

# for idx in range(1, 11):
"""
for idx in range(1, 11, 2):
    print(idx)
"""

"""
for row in range(1, 9):
    print("\u2B1C", end=" ")

print()

for row in range(1, 9):
    print("\u2B1C", end=" ")
"""

for row in range(1, 9):
    # Nested Loop
    for column in range(1, 9):
        print("\u2B1C", end=" ")
    print()