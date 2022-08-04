numbers = list(range(10, 101, 10))
print(numbers)

numbers.append(30)
numbers.append(77)
numbers.append(95)

# reversed_numbers = reversed(numbers)
reversed_numbers = list(reversed(numbers))

print(numbers)
print(reversed_numbers)

print(numbers.index(50))
print(numbers.count(30))

print()

data = [70, 30, 50, 90, 20]
print(data)
data.sort()
print(data)

data.reverse()
print(data)

data.remove(50)
print(data)

# data.pop()
data.pop(1)
print(data)

data.append(100)
data.insert(2, 350)
print(data)

data.clear()