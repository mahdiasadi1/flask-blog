from flask_wtf import FlaskForm
from wtforms.fields import EmailField,PasswordField
from wtforms.validators import DataRequired 
class Loginform(FlaskForm):
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])