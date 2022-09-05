"""
 OOPS
 Class -> Customer
        id, name, phone, email, createdOn, remarks, points, type

 ORM
 MySQL
 table -> Customer
 create table Customer(
    id int primary key auto_increment,
    name varchar(256),
    phone varchar(10),
    email varchar(256),
    createdOn datetime DEFAULT CURRENT_TIMESTAMP,
    remarks varchar(1024),
    points int DEFAULT 100,
    type int DEFAULT 1
 );

"""
class Customer:

    # Constructor
    def __init__(self, id=None, name=None, phone=None, email=None, created_on=None, remarks=None, points=100, type=1):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.created_on = created_on
        self.remarks = remarks
        self.points = points
        self.type = type

    def insert_sql(self):
        return "insert into Customer (name, phone, email, remarks) " \
               "values " \
               "('{name}', '{phone}', '{email}', '{remarks}');".format_map(vars(self))

    def update_sql(self):
        return ""

    def delete_sql(self):
        return "delete from Customer where id = {}".format(self.id)

    def select_sql(self):
        return "select * from Customer"

    def select_sql_where(self):
        return "select * from Customer where id = {}".format(self.id)


c1 = Customer()
print(vars(c1))