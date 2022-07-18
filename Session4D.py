def welcome():
    message = "Welcome to Auribises"
    print(message)
    quote = "Search the Candle, Rather Than Cursing The Darkness"
    print(quote)


def add(num1, num2):
    result = num1 + num2
    print("Result is:", result)


def max(num1, num2):
    result = 0
    if num1 > num2:
        result = num1
    else:
        result = num2

    return result


welcome()
add(10, 20)
max_number = max(30, 50)
print("max_number out of 30 and 50 is:", max_number)