# Functions can be copied as Reference

def fun1():
    print("Hello from fun1")


print("fun1 is:", fun1)

# Reference Copy
fun2 = fun1
print("fun2 is:", fun2)

fun2()

del fun2
fun1()