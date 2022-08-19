"""
1. Create a Class in Python using OOPS
    Customer
        id, name, phone, email, createdOn, remarks, points, type

2. Create a Table in MySQL using the attributes of your Object

3. Create a Class DataBaseHelper where you will create write and read operations for the table

4. Create a Flask Web App
    4.1 Create a Web Page which has fields to insert data
        Here, fileds will be as per the number of attributes
        As per our project, id and createdOn is automatic
        Hence, 6 UI Web Elements must be thr

    4.2 Create a Web Page which has a table to display records

"""

from flask import *
from S19Customer import Customer
from S19DataBaseHelper import DataBaseHelper

app = Flask("CustomerManagementApp", template_folder="cms")
db_helper = DataBaseHelper()

@app.route("/")
def index():
    # return "Welcome to CMS App"
    return render_template("index.html")


@app.route("/add")
def add():
    # return "Welcome to CMS App"
    return render_template("add-customer.html")


@app.route("/view")
def view():
    # return "Welcome to CMS App"
    return render_template("view-customers.html")


@app.route("/save-customer", methods=["POST"])
def save_customer_in_db():
    cref = Customer(name=request.form["name"],
                    phone=request.form["phone"],
                    email=request.form["email"],
                    remarks=request.form["remarks"])
    print(vars(cref))
    sql = cref.insert_sql()
    db_helper.write(sql)
    return cref.name+" Inserted Successfully..."


def main():
    app.run()


if __name__ == "__main__":
    main()