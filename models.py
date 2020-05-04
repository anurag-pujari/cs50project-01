from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "userstable"
    userid = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, nullable = False, unique = True)
    userpassword = db.Column(db.String, nullable = False)


"""
    def __init__(self, userId, userName, userPassword):
        self.userId=userId
        self.userName = userName
        self.userPassword = userPassword


    def addUserInput(self, userId, uName, uPassword):
        name = User(name = uname, id = userId, pw = uPassword)
        db.session.add(name)
        db.session.commit()
"""

    