from flask_wtf import FlaskForm
from wtforms.fields import EmailField,PasswordField,StringField
from wtforms.validators import DataRequired 
class Loginform(FlaskForm):
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
class Register(FlaskForm):
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    confirm_password = PasswordField(validators=[DataRequired()])
    fullname = StringField()

    