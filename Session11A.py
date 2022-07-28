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


# List of Objects
row = []
for idx in range(1, 11):
    row.append(MovieTicket("Avengers", idx, 'A', 200, '13:45'))

for idx in range(len(row)):
    row[idx].show_details()


def sort_movie_tickets():
    n = len(row)
    for idx1 in range(0, len(row)): # 0, 1, 2, 3, 4
        for idx2 in range(0, n-idx1-1):

            if row[idx2].seat_num < row[idx2+1].seat_num:
                row[idx2], row[idx2+1] = row[idx2+1], row[idx2]


sort_movie_tickets()
print("AFTER SORTING")
for idx in range(len(row)):
    row[idx].show_details()
