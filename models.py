#from flask.ext.sqlalchemy import SQLAlchemy
#from werkzeug import generate_password_hash, check_password_hash

#db = SQLAlchemy()

#class User(db.Model):
#    __tablename__ = 'Users'
#    UserID = db.Column(db.Integer, primary_key = True)
#    First_Name = db.Column(db.String(64))
#    Last_Name = db.Column(db.String(64))
#    Email = db.Column(db.String(128), unique = True)
#    Pass = db.Column(db.String(64))
#
#    def __init__(self, First_Name, Last_Name, Email, Pass):
#        self.First_Name = First_Name.title()
#        self.Last_Name = Last_Name.title()
#        self.Email = Email.lower()
#        self.set_password(Pass)
#
#    def set_password(self, Pass):
#        self.Pass = generate_password_hash(Pass)
#
#    def check_password(self, Pass):
#        return check_password_hash(self.Pass, Pass)
