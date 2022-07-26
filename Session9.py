class OneWayFlight:

    # Constructor
    """
    def __init__(self):
        print("self is:", self, "type is:", type(self))
        self.from_location = "New Delhi"
        self.to_location = "Bangalore"
        self.departure_date = "30th July, 2022"
        self.num_of_travellers = 2
        self.travel_class = "economy"
    """

    # Now, the previous constructor is no more available to be used
    # Further, we do not have Constructor or Function Overloading in Python OOPS
    def __init__(self, from_location="New Delhi", to_location="Bangalore", departure_date="26th July, 2022", num_of_travellers=1, travel_class="economy"):
        print("self is:", self, "type is:", type(self))
        self.from_location = from_location
        self.to_location = to_location
        self.departure_date = departure_date
        self.num_of_travellers = num_of_travellers
        self.travel_class = travel_class


print("Class Dictionary")
print(OneWayFlight.__dict__)

flight1 = OneWayFlight() #OneWayFlight() -> executes __init__
# flight1.from_location = "New Delhi"
# flight1.to_location = "Bangalore"

print("flight1 is:", flight1, "type is:", type(flight1))

flight2 = OneWayFlight()
print("flight2 is:", flight2, "type is:", type(flight2))

flight3 = OneWayFlight(departure_date="30th Aug, 2022", num_of_travellers=5)
flight4 = OneWayFlight("Goa", "Chennai", "27th July, 2022", 5, "economy")

print("flight1 dictionary:", flight1.__dict__)
print("flight2 dictionary:", flight2.__dict__)
print("flight3 dictionary:", flight3.__dict__)
print("flight4 dictionary:", flight4.__dict__)

