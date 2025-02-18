from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField
from wtforms.validators import DataRequired
class Postform (FlaskForm):
    title= StringField(validators=[DataRequired()])
    summary = StringField()
    content=TextAreaField(validators=[DataRequired()])
    slug=StringField(validators=[DataRequired()])

