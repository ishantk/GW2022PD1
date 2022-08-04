"""
    Sequences
        Tuple
        List
        Set
        Dictionary
        String

    Properties:
        1. Indexing
        2. Negative Indexing
        3. Slicing
        4. Concatenation
        5. Multiplicity
        6. Membership Testing

"""

my_data = (10, 20, 30)
print(my_data, hex(id(my_data)), type(my_data), len(my_data))

numbers = [
    [10, 20, 30],
    [40, 50, 60, 70, 80],
    [99, 77]
]

# Indexing
print(my_data[1])
print(my_data[2])
print(my_data[len(my_data)-1])

print()

# Negative Indexing
print(my_data[-1])
print(my_data[-2])
print(my_data[-3])

print(numbers[-2][-1])

# Slicing
data = list(range(10, 101, 10))
print("data:", data)
print(data[5:])
print(data[5:8])
print(data[:4])

print(data[:-5])
print(data[-5:-2])
# print(data[-2:-5]) # Invalid Slice

# Concatenation
data1 = [10, 20, 30]
data2 = [40, 50, 60]
data3 = data1 + data2
print(data1)
print(data2)
print(data3)

#Multiplicity
data4 = data1 * 2
print(data4)

# Membership Testing
print(10 in data1)
print(100 in data1)
print(1000 not in data1)

student = {
    "roll": 101,
    "name": "John",
    "age": 20,
    "email": "john@example.com"
}

print(student["roll"])
print("roll" in student)
print(101 in student)