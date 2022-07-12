"""
    MODEL
        Storage Container
            1. Single Value Container
                Holds 1 value
            2. Multi Value Container
                Holds multiple values
                2.1 Homogenous
                2.2. Hetrogeneous

"""
# Single Value Container
name = "John, Jennie, Jim, Jack, Joe"
print(name, hex(id(name)))

# Multi Value Container
# INDEXED         0         1       2       3      4
student_names = "john", "jennie", "jim", "jack", "joe"
marks = (90, 80, 70)
data = 10, 20, "Hello", "50", 2.5

print("student_names:", student_names, hex(id(student_names)), type(student_names))
print("marks:", marks, hex(id(marks)), type(marks))
print("data:", data, hex(id(data)), type(data))

print(student_names[0], hex(id(student_names[0])))
print(student_names[1], hex(id(student_names[1])))
print(student_names[2], hex(id(student_names[2])))
print(student_names[3], hex(id(student_names[3])))
print(student_names[4], hex(id(student_names[4])))

actor_name = "john"
print(actor_name, hex(id(actor_name)))

# actor_name is the reference variable which refers to the String object : john