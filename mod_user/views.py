from flask import session, request,render_template,flash
from . import user
from .form import Register
from .models import User
from app import db
from sqlalchemy.exc import IntegrityError
@user.route('/')
def index():
    return "hello user"
@user.route('/register/',methods=["POST","GET"])
def register():
    form = Register(request.form)
    if request.method == "POST":
        if  not form.validate_on_submit():
            render_template('user/register.html',form=form)
        if   not form.password.data == form.confirm_password.data :
            message=" password and confirm password are not equal"
            form.password.errors.append(message)
            form.confirm_password.errors.append(message)   
            return render_template('user/register.html' ,form=form)
        newuser = User()
        newuser.fullname=form.fullname.data
        newuser.email = form.email.data
        newuser.set_password(form.password.data)
        try:
            db.session.add(newuser)
            db.session.commit()
            flash("new user added successfully ","bg-success")
        except IntegrityError:
            db.session.rollback()
            flash("email is in use","bg-danger")
            return render_template('user/register.html' ,form=form)
    
        return render_template('user/register.html' ,form=form)

        
        

    return render_template('user/register.html' ,form=form)


