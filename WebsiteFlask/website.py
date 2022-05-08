from flask import Flask, render_template

webApp = Flask(__name__) 

@webApp.route('/')

def home():
    # html should be inside a folder called templates
    return render_template("home.html")

@webApp.route('/about/')
def about():
    return render_template("about.html")

# Calling directly the script does that Python anmes it as __main__, if it called from other it will calle it as the file name
if __name__== "__main__":
    webApp.run(debug=True)
