from werkzeug.security import generate_password_hash,check_password_hash
# from flask_wtf import FlaskForm
# from wtforms import EmailField,PasswordField,SubmitField
# from wtforms.validators import DataRequired,Email,Length

from app import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(120),nullable=False,unique=True)
    password = db.Column(db.String(120),nullable=False)
    role = db.Column(db.Integer)
    def set_password(self,password):
        self.password=generate_password_hash(password)
    def check_password(self,password):
       
        # return check_password_hash(self.password,password)    
        if self.password == password:
            return True
        else:
            return False