from db import mysql_db
class User(mysql_db.Model):
    id = mysql_db.Column(mysql_db.Integer, primary_key=True)
    first_name = mysql_db.Column(mysql_db.String(30))
    last_name = mysql_db.Column(mysql_db.String(30))
    email = mysql_db.Column(mysql_db.String(50), unique=True)
    password = mysql_db.Column(mysql_db.String(50))
    confirm_password = mysql_db.Column(mysql_db.String(50))