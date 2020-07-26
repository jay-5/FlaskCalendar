from flask import Flask
 
app = Flask(__name__)

@app.route("/") # this route is the default one
def home():
    return "My name is Max!"

if  __name__  ==  "__main__":
    app.run(debug=True)

    