from flask import Flask, render_template, request, session
from models import *
from sqlalchemy import exc

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://postgres:anurag123@localhost:5432/cs50wbooks'
db.init_app(app)

loggedin_username = ''

loggedInUser = []

@app.route("/")
@app.route("/index")
def index():
    username = ''.join(loggedInUser)
    message = "Welcome to Book Review"
    return render_template("index.html", username = username, message = message) 

@app.route("/register", methods = ["GET" , "POST"])
def register():
    return render_template("registration.html")# Sumit should call Save route


@app.route("/save", methods = ["GET" , "POST"])
def save():
   # print('\nThe request',request)
    username = request.form.get("username")
    password = request.form.get("password")

    user_in_db = User.query.filter_by(username=username).first()
    if user_in_db != None:
        return render_template("success.html", message="username already exists", username = username)
    

    user = User(username = username, userpassword = password)
    db.session.add(user)
    db.session.commit()
    message = "Submitted the recoreds"
    return render_template("success.html", message = message, username = username) # Saves to database and renders to success.html

@app.route("/log_in", methods = ["GET","POST"])
def log_in():
    username = request.form.get("username")
    print(username)
    user_In_Db = User.query.filter_by(username = username).first()
    if user_In_Db == None:
        message = "Userid not found"
        return render_template("success.html", message = message)
    
    if user_In_Db:
        loggedInUser.append(username)
        username = ''.join(loggedInUser)
        
        message = "Welcome to Book Review"
        return render_template("home.html", message = message , username = username)

    
        
    return render_template("home.html", message = message)
@app.route("/log_out", methods = ["GET","POST"])
def log_out():
    loggedInUser[:] = []
    #message = ""
    return render_template("index.html")
   
    
if (__name__)==('__main__'):
    app.run(debug = True)
