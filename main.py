from flask import Flask, render_template
 
app = Flask(__name__)

@app.route("/") # this route is the default one
def home():
    return render_template("home.html")

if  __name__  ==  "__main__":
    app.run(debug=True)

@app.route("/cal")
def cal():
    return render_template("cal.html")
