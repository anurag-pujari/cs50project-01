import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import *

app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://postgres:anurag123@localhost:5432/cs50wbooks'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)
db = SQLAlchemy()


def main():
    #db.create_all()
    user = User(username = "Anurag", userpassword = "password")
    db.session.add(user)
    db.session.commit()
    print(user.username)


if __name__ == "__main__":
    with app.app_context():
        main()
