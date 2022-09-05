class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Restaurant:

    def __init__(self, name, phone, email, operatingHours, ratings, menu):
        self.name = name
        self.phone = phone
        self.email = email
        self.operatingHours = operatingHours
        self.ratings = ratings
        self.menu = menu

