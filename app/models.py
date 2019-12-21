# models of your database tabels
from app import db

class Example(db.Model):
    primary_key = db.Column(db.Integer, primary_key=True)
    int_row = db.Column(db.String())
    str_row = db.Column(db.Integer())
