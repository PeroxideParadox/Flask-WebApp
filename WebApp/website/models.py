#from . specified that anything from the current directory which is websites import this db 
from . import db
from flask_login import UserMixin
from sqlalchemy import func

#using func for automatically get the current time 
#Defining the schema for the database 

#Databse model is a layout or blueprint for an object that needs to be stored , so all user must look like this to ensure consistency
class Note(db.Model):
    id=db.Column(db.Integer(150),primary_key=True)
    data=db.Column(db.String(1000))
    date=db.Column(db.DateTime(timezone=True),default=func.now())
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))


class User(db.Model,UserMixin):
    id=db.column(db.Integer,primary_key=True)
    email=db.column(db.String(100),unique=True)
    password=db.column(db.String(50))
    first_name=db.column(db.String(50))
    notes=db.relationship('Note')