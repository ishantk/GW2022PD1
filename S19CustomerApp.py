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
from Session21 import MongoDBHelper

app = Flask("CustomerManagementApp", template_folder="cms")
db_helper = DataBaseHelper()
mongodb_helper = MongoDBHelper()

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
    # cref = Customer()
    # sql = cref.select_sql()
    # rows = db_helper.read(sql)

    rows = mongodb_helper.fetch()
    print(rows, len(rows), type(rows))

    return render_template("view-customers.html", result=rows)

"""
@app.route("/delete/<id>")
def delete_customer_from_db(id):
    cref = Customer(id=id)
    sql = cref.delete_sql()
    db_helper.write(sql)

    return render_template("success.html", message="Customer with ID "+id+" Deleted Successfully..")
"""

@app.route("/delete/<phone>")
def delete_customer_from_db(phone):

    query = {"phone": phone}
    mongodb_helper.delete(query)
    return render_template("success.html", message="Customer with Phone {} Deleted Successfully..".format(phone))


@app.route("/save-customer", methods=["POST"])
def save_customer_in_db():
    cref = Customer(name=request.form["name"],
                    phone=request.form["phone"],
                    email=request.form["email"],
                    remarks=request.form["remarks"])

    if len(cref.name) == 0:
        return render_template("error.html", message="Name cannot be Empty...")

    print(vars(cref))
    # Get the Dictionary of Object
    customer_to_save = vars(cref)
    mongodb_helper.insert(document=customer_to_save)

    # sql = cref.insert_sql()
    # db_helper.write(sql)

    # return cref.name+" Inserted Successfully..."
    return render_template("success.html", message=cref.name+" Inserted Successfully...")

"""
@app.route("/update-customer/<id>")
def update_customer(id):
    cref = Customer(id=id)
    sql = cref.select_sql_where()
    rows = db_helper.read(sql)
    return render_template("update-customer.html", row=rows[0])
"""

@app.route("/update-customer/<phone>")
def update_customer(phone):
    query = {"phone": phone}
    document = mongodb_helper.fetch_selected(query)
    return render_template("update-customer.html", row=document)


@app.route("/update-customer-in-db", methods=["POST"])
def update_customer_in_db():
    cref = Customer(name=request.form["name"],
                    phone=request.form["phone"],
                    email=request.form["email"],
                    remarks=request.form["remarks"])

    if len(cref.name) == 0:
        return render_template("error.html", message="Name cannot be Empty...")

    print(vars(cref))
    # Get the Dictionary of Object
    query = {"phone": cref.phone}
    customer_to_update = vars(cref)
    mongodb_helper.update(customer_to_update, query)

    return render_template("success.html", message=cref.name + " Updated Successfully...")


def main():
    app.run()


if __name__ == "__main__":
    main()