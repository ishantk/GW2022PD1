"""
    Think of Object
    1. MovieTicket : name, seatNum, rowNum, price .....
    2. CinemaHall : audi, numOfSeats, seatingPlan

    CinemaHall HAS MovieTickets
    1 to many
"""


class MovieTicket:

    def __init__(self, name, seat_num, row_num, price, time):
        self.name = name
        self.seat_num = seat_num
        self.row_num = row_num
        self.price = price
        self.time = time


class CinemaHall:

    def __init__(self, name, audi, num_of_seats, seating_plan):
        self.name = name
        self.audi = audi
        self.num_of_seats = num_of_seats
        self.seating_plan = seating_plan

    def print_cinema_hall(self):
        pass


ticket1 = MovieTicket("Avengers", 1, 'A', 200, '13:45')
ticket2 = MovieTicket("Avengers", 2, 'A', 200, '13:45')
ticket3 = MovieTicket("Avengers", 3, 'A', 200, '13:45')
ticket4 = MovieTicket("Avengers", 4, 'A', 200, '13:45')
ticket5 = MovieTicket("Avengers", 5, 'A', 200, '13:45')

ticket6 = MovieTicket("Avengers", 1, 'B', 200, '13:45')
ticket7 = MovieTicket("Avengers", 2, 'B', 200, '13:45')
ticket8 = MovieTicket("Avengers", 3, 'B', 200, '13:45')
ticket9 = MovieTicket("Avengers", 4, 'B', 200, '13:45')
ticket10 = MovieTicket("Avengers", 5, 'B', 200, '13:45')

row_a = [ticket1, ticket2, ticket3, ticket4, ticket5]
row_b = [ticket6, ticket7, ticket8, ticket9, ticket10]

tickets = [
    row_a,
    [
        MovieTicket("Avengers", 1, 'B', 200, '13:45'),
        MovieTicket("Avengers", 2, 'B', 200, '13:45'),
        MovieTicket("Avengers", 3, 'B', 200, '13:45'),
        MovieTicket("Avengers", 4, 'B', 200, '13:45'),
        MovieTicket("Avengers", 5, 'B', 200, '13:45')
     ]
]

total_tickets = len(tickets[0]) + len(tickets[1])

cinema_hall = CinemaHall(name="PVR", audi=3, num_of_seats=total_tickets, seating_plan=tickets)
cinema_hall.print_cinema_hall()