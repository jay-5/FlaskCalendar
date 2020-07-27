from flask import Flask, render_template
 
app = Flask(__name__)

if  __name__  ==  "__main__":
    app.run(debug=True)

@app.route("/home") # this route goes to the home page
def home():
    return render_template("home.html")

@app.route("/cal") # this route goes to the calendar page
def cal():
    return render_template("cal.html")
