# Lambda Expressions :)
# Computation :)

def area_of_circle(radius):
    return 3.14 * radius * radius


func = area_of_circle

print(area_of_circle(2.5))
print(area_of_circle(5.7))
print(func(2.11))


ref = lambda radius: 3.14 * radius * radius
print(ref)
print(ref(2.11))