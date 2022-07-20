# args and kwargs
# Arguments and KeyWord Arguments

def add(*args):
    print(args)
    print(len(args))
    print(type(args))
    print(max(args))
    print(min(args))
    print(sum(args))


add(10, 20, 30, 40, 50, 60)
# add(10, 20, 'john', 30, 40, 50, 60) -> Crash the Program

# add = 20
# add(10, 20, 30)

def fun(*kuchBhi):
    print(kuchBhi)
    print(len(kuchBhi))
    print(type(kuchBhi))
    print(min(kuchBhi))
    print("~~~~~~~~~~")


fun(10, 20)
fun(10.22, 20.22)
fun("John", "JEnnie", "Jim", "Jack", "Joe")


def book_flight(**kwargs):
    print(kwargs)
    print(type(kwargs))


book_flight(source='delhi', destinition='Bangalore', travellers=2)


def demo(*args, **kwargs):
    print(args)
    print(kwargs)

demo(10, 20, 30, a=1, b=2, c=3)


