# Import all the Built in Classes/Functions from the flask module :)
from flask import *

from Session18A import DBHelper
from Session18B import HealthLogger


app = Flask("HealthLogger")
db_helper = DBHelper()

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add")
def add_health_log():
    return render_template("add-health-log.html")


@app.route("/logs")
def view_all_health_logs():

    health_logger_object = HealthLogger()
    sql = health_logger_object.fetch_sql_command()

    rows = db_helper.read(sql)

    return render_template("logs.html", result=rows)


@app.route("/save", methods=["POST"])
def save_health_data():
    print("Save health Data Executed...")

    """
    health_data = {
        "phone": request.form['txtPhone'],
        "weight": request.form['weight'],
        "bphigh": request.form['bphigh'],
        "bplow": request.form['bplow'],
        "sugar": request.form['sugar'],
    }

    print("health_data dictionary:", health_data)
    """

    health_data_object = HealthLogger(phone=request.form['txtPhone'],
                                      weight=int(request.form['weight']),
                                      bp_high=int(request.form['bphigh']),
                                      bp_low=int(request.form['bplow']),
                                      sugar=int(request.form['sugar']),
                                      )

    print(health_data_object)
    sql = health_data_object.insert_sql_command()
    print("SQL IS:", sql)
    db_helper.write(sql)

    return "Health Record Added :)"

def main():
    app.run()


if __name__ == "__main__":
    main()
