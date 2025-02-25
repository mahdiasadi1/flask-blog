from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField,SelectMultipleField
from wtforms.validators import DataRequired
from mod_blog.models import Category
from wtforms.widgets import ListWidget, CheckboxInput


class Postform (FlaskForm):
    title= StringField(validators=[DataRequired()])
    summary = StringField()
    content=TextAreaField(validators=[DataRequired()])
    categories = SelectMultipleField('Categories', coerce=int, option_widget=CheckboxInput(), widget=ListWidget(prefix_label=False))
    slug=StringField(validators=[DataRequired()])
class Categoryform(FlaskForm):
    name = StringField(validators=[DataRequired()])
    description=TextAreaField()
    slug=StringField(validators=[DataRequired()])    

