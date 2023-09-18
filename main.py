from flask import Flask, render_template, request
## import pymongo
## from pymongo import MongoClient
## client = MongoClient
## import mysql.connector

app = Flask(__name__)

## conn = mysql.connector.connect(host='localhost', user='root', password='admin', database="expenceapp")
## cursor = conn.cursor()

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/registration')
def about():
    return render_template('registration.html')

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/login_validation', methods = ['POST'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')
##    cursor.execute("""select * from expenceapp.users u where u.email LIKE {} and u.password LIKE {}""".format(email, password))
##    user = cursor.fetchall()
##    return user
    return "Login validation: Your email: {} and passwored is {}".format(email, password)

if __name__ == '__main__':
    app.run(debug=True)

