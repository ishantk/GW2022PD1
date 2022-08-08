"""
    DataBase Interactions !!
    Persist :)
        To Save :)
         1. Files
         2. DataBases
                Objects Data :)
                SQL (Tables)
                    MySQL
                    Oracle
                NoSQL (Dictionary)
                    MongoDB
                    FirebaseFirestore
                    Amazon
                    ....
                Graph
                    Neo4J

        Application Development
        MEAN STACK
        MERN STACK

        MySQL:
        mysql -u root -p (To Login into MySQL)
        show databases;  (To check list of databases)
        create database gw2022pd1; (To create a new database)
        use gw2022pd1; (To select the database in which we wish to work)


        DataBase is a Collection of Tables
        Table is a Collection of Rows and Columns

        ORM -> Object Relational Mapping

        create table Customer(
            cid int primary key auto_increment,
            name varchar(256),
            phone varchar(24),
            email varchar(256),
            points int
        );

        select * from Customer;
        insert into Customer values(null, "John", "+91 99999 11111", "john@example.com", 0);
        update Customer set name = "John Watson", email ="john.watson@example.com" where cid = 1;
        delete from Customer where cid = 2;
    """

class Customer:

    def __init__(self, name, phone, email):
        self.cid = 0
        self.name = name
        self.phone = phone
        self.email = email
        self.points = 0

    def show(self):
        print("Name: {name}, Phone: {phone}, Email: {email}, Points:{points}".format_map(vars(self)))


c1 = Customer("John", "+91 99999 11111", "john@example.com")
c1.show()