
class MovieTicket:

    def __init__(self, name, seat_num, row_num, price, time):
        self.name = name
        self.seat_num = seat_num
        self.row_num = row_num
        self.price = price
        self.time = time
        self.is_booked = False
        self.user_email = ""

    def show(self):
        empty_seat = '\u2B1C'
        booked_seat = '\u2B1B'

        if self.is_booked:
            print(booked_seat, end=" ")
        else:
            print(empty_seat, end=" ")

    def show_details(self):
        print("~~~~~~~~~~~~~~~")
        print(self.name)
        print(self.seat_num)
        print(self.row_num)
        print(self.price)
        print(self.time)
        print(self.is_booked)
        print(self.user_email)
        print("~~~~~~~~~~~~~~~")


class CinemaHall:

    def __init__(self, name, audi, num_of_seats, seating_plan):
        self.name = name
        self.audi = audi
        self.num_of_seats = num_of_seats
        self.seating_plan = seating_plan

    def print_cinema_hall(self):
        # Assignment: Display the Rows and Seat Numbers
        for row in range(len(self.seating_plan)):
            for seat in range(len(self.seating_plan[row])):
                self.seating_plan[row][seat].show()
            print()

    def book_ticket(self):
        rows = ['A', 'B', 'C', 'D', 'E']
        row = input("Enter the Row (A-E): ")
        idx = -1
        email = input("Enter your Email: ")
        for i in range(len(rows)):
            if row == rows[i]:
                idx = i
                break
        seat_number = int(input("Enter the Seat Number [1-5]: "))

        self.seating_plan[idx][seat_number-1].is_booked = True
        self.seating_plan[idx][seat_number - 1].user_email = email

        print("Thank You for Booking...")
        self.seating_plan[idx][seat_number - 1].show_details()

# Empty List
tickets = []
rows = ['A', 'B', 'C', 'D', 'E']
total_tickets = 0

# rowIdx: 0, 1, 2, 3, 4
for rowIdx in range(0, len(rows)):
    row = []
    for idx in range(1, 6):
        row.append(MovieTicket("Avengers", idx, rows[rowIdx], 200, '13:45'))

    tickets.append(row)
    total_tickets += len(row)


cinema_hall = CinemaHall(name="PVR", audi=3, num_of_seats=total_tickets, seating_plan=tickets)

# cinema_hall.seating_plan[0][1].is_booked = True
cinema_hall.book_ticket()

print("Cinema Hall :)")
cinema_hall.print_cinema_hall()
