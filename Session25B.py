# A function can be created inside another function

def outer():
    print("This is outer function")

    def inner():
        print("This is inner function defined inside outer function")

    inner()


outer()
