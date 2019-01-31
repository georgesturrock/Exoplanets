#!/usr/bin/python3

from flask import Flask
#Create instance of flask and pass in the name variable
app = Flask(__name__)

#decorator telling flask what URL should trigger the hello function
@app.route("/")
def hello():
    return "Welcome to machine learning model APIs!"
    return redirect("http://35.202.91.11", code=302)


if __name__ == '__main__':
    app.run(debug=True)