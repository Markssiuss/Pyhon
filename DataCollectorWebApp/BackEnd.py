from flask import Flask, render_template, request
from Database import Database

app = Flask(__name__)
database = Database("DataCollectorWebApp\\Height.db")

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form["email_name"]
        height = request.form["height_name"]
        if database.checkUniqueEmail(email) == True:
            database.insert(email, height)
            return render_template("success.html")
        else:
            return render_template("index.html", text = "This email has taken the survey before!!")

if __name__ == '__main__':
    app.debug = True
    app.run()