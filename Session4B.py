# Functions
# f(x) = y | y = x*x + 1
# f(1) -> 1*1 + 1 -> 2

# def -> define i.e. create a function in memory
# f -> name of function, which can be any name of your choice
# after the : wih tab space, we have instructions which a function will execute in a sequence
def f(x):
    y = x*x + 1
    print("y is:", y)

print("f is:", f)

# execute the function f or call the function f or run the function f
f(1)
f(2)
f(5)


"""
ac_power = False
def power():
    global ac_power

    if ac_power:
        print("Currently AC is Turned ON")
        ac_power = False
    else:
        print("Currently AC is Turned OFF")
        ac_power = True

power()
power()
"""