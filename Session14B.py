john_followers = {"fionna", "jake", "dave", "mike", "leo", "jake"}
print(john_followers)

numbers = list(range(10, 101, 10))
numbers.append(20)
numbers.append(50)
numbers.append(70)
print(numbers)

set_numbers = set(numbers)
print(set_numbers)
set_numbers.add(101)
set_numbers.add(90)
print(set_numbers)

set_numbers.pop()
set_numbers.pop()
print(set_numbers)

# For-Each Loop
for number in set_numbers:
    print(number)

set_numbers.discard(30)
set_numbers.discard(50)
print(set_numbers)

john_followers = {"fionna", "jake", "dave", "mike", "leo", "jake"}
jake_followers = {"anna", "kim", "lee", "harry", "mike", "fionna"}
fionna_followers = {"jake", "dave"}

print(john_followers)
print(jake_followers)
print(fionna_followers)

followers = john_followers.intersection(jake_followers)
print(followers)

print(fionna_followers.issubset(john_followers))
print(john_followers.issuperset(fionna_followers))

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

C = A - B
print(C)

D = A & B
print(D)

E = A ^ B
print(E)

F = A | B
print(F)

A.clear()
print(A)