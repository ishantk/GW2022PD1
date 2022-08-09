"""
    Principle of OOPS

        Crossing
            name, latitude, longitude, status, personInCharge

        HealthLogger
            phone, weight, bp, sugar, logTimeStamp

        VegetableSeller
            name, phone, amount, logTimeStamp, description, frequency


        create table HealthLogger(
            id int primary key auto_increment,
            phone varchar(10),
            weight int,
            bp_high int,
            bp_low int,
            sugar int,
            log_time_stamp datetime
        );
"""

import datetime
import mysql.connector as db


class DBHelper:

    def __init__(self):
        self.connection = db.connect(user='root', password='',
                                     host='127.0.0.1',
                                     database='gw2022pd1')
        print("DB CONNECTED :)")
        self.cursor = self.connection.cursor()
        print("CURSOR CREATED :)")

    def write(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()
        print("SQL QUERY EXECUTED :)")

    def read(self):
        pass


class HealthLogger:

    db_helper = DBHelper()

    def __init__(self):
        self.id = None
        self.phone = input("Enter Phone Number: ")
        self.weight = int(input("Enter Weight: "))
        self.bp_high = int(input("Enter BP High: "))
        self.bp_low = int(input("Enter BP Low: "))
        self.sugar = int(input("Enter Diabetes: "))
        dt = str(datetime.datetime.today())
        idx = dt.rindex(".")
        self.log_time_stamp = dt[0: idx]

    def show(self):
        print(vars(self))

    def save_log(self):
        sql = "insert into HealthLogger values(null, '{phone}', {weight}, {bp_high}, {bp_low}, {sugar}, '{log_time_stamp}')".format_map(vars(self))
        print(sql)
        self.db_helper.write(sql)


print("~~~~~~~~~~~~~~~~~~~~")
print("WELCOME")
print("HEALTH LOGGER APP")
print("~~~~~~~~~~~~~~~~~~~~")


while True:

    print("Create a New Health Log")

    logger = HealthLogger()
    logger.show()

    save = input("Do you wish to Save the Record (yes/no)")
    if save == "yes":
        logger.save_log()

    choice = input("Would You Like to add another Health Log... (yes/no)")
    if choice == "no":
        break

