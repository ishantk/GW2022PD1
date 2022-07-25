"""

    Object Oriented Programming Structure
        Real World:
        1. Object: Anything which exists
        2. Class:  Drawing of an Object

        Computer Science
        1. Object: STORAGE CONTAINER [MULTI VALUE] -> HOMO|HETRO
        2. Class: A program which describes what object will contain
                  or how it will look in memory


        Principle of OOPS:
            1. Think of Object
                An Object is the one which has lot of data associated (attributes) to it
            2. Create its class
                its a programmatical way of defining the object
            3. From the class create Real Object in memory
                class_name()


        Client Requirements:
            Mr. John wants to create a food delivery app
            He want users to login with mobile phone numbers
            and choose dishes from restaurant and add them to cart
            Further place an order which is reflected to the restaurant
            And PickUp Person picks and delivers the order to user
            User can pay by several means

            User is an Object
            name, phone, email, gender, address

            Order is an Object
            id, amount, dishes, user, date, time ......

            Dish
            name, price, description, ratings, category

            Restaurant
            name, phone, email, address, price_per_person, review, operating_hours, dining


            MMT.com
            Object: OneWayFlight
            Attributes: from_location, to_location, departure_date, num_of_travellers, travel_class

            Objects are related to each other
            1. One to One
            2. One to Many
            3. Many to Many

"""


class OneWayFlight:
    pass


flight1 = OneWayFlight()
flight2 = OneWayFlight()
flight3 = flight1

print("flight1 is:", flight1, flight1.__dict__)
print("flight2 is:", flight2, flight2.__dict__)
print("flight3 is:", flight3, flight3.__dict__)

# Operations on Object
# 1. Add Data to Object
flight1.from_location = "New Delhi"
flight1.to_location = "Bangalore"
flight3.departure_date = "30th July, 2022"
flight1.num_of_travellers = 2
flight3.travel_class = "economy"

flight2.from_location = "New Delhi"
flight2.to_location = "Goa"
flight2.departure_date = "15th August, 2022"
flight2.num_of_travellers = 1
flight2.travel_class = "business"
flight2.meals_pref = "veg"

print("flight1 is:", flight1, flight1.__dict__)
print("flight2 is:", flight2, flight2.__dict__)
print("flight3 is:", flight3, flight3.__dict__)


# 2. Update Data into Object
flight2.departure_date = "10th August, 2022"
flight2.meals_pref = "italian"

# 3. Read Operation
print("flight2 is:", flight2, flight2.__dict__)

# Delete Data from Object
del flight3.travel_class
del flight3.departure_date

print("flight1 is:", flight1, flight1.__dict__)
print("flight3 is:", flight3, flight3.__dict__)

# Delete Object from memory
del flight2
# print("flight2 is:", flight2, flight2.__dict__) # ERROR


# Assignment: Code your Object which should be really unique :)