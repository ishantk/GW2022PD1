# A function can return another function

def outer():
    print("This is outer function")

    def inner():
        print("This is inner function defined inside outer function")

    print("inner is:", inner)
    return inner


result = outer()
print("result is:", result)
result()
