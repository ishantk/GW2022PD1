# We can give default values to arguments
# initializing arguments follows rule which is Right to Left
def add(num1=1, num2=2, num3=0):
    result = num1 + num2 + num3
    print("Result is:", result)


def compute_taxes(amount, taxes):
    return amount * taxes

add()
add(10, 20, 30)
add(num2=30)
add(num3=30, num1=5, num2=1)
print(compute_taxes(taxes=0.18, amount=200))


def book_one_way_flight(source='Delhi', to='Bangalore', departure_date='21st July, 2022', num_of_traverllers=1):
    print("Booking Flight....")
    print(source, to, departure_date, num_of_traverllers)

book_one_way_flight()