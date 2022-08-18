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

    def read(self, sql):
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows