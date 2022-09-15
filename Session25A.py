# A function can take another function as input :)
def fun1(f):
    # execution of function
    f()


def hello():
    print("This is hello")


def bye():
    print("This is bye")


fun1(hello)
fun1(bye)