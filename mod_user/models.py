from werkzeug.security import generate_password_hash
from app import db
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(120),nullable=False,unique=True)
    password = db.Column(db.String(120),nullable=False)
    role = db.Column(db.Integer)
    def set_password(self,password):
        self.password=generate_password_hash(password)