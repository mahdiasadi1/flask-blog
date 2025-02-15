from flask import flash, session , render_template,request,abort
from  mod_user.form import Loginform
# from models import User
from mod_user.models import User
from . import admin
from .utils import protected_view
@admin.route('/')
@protected_view
def admin_index():
    print(session['user_id'])    
    return "hello admin "
@admin.route('/login/',methods=["POST","GET"])
def login():
    form = Loginform(request.form)
    if request.method == "POST":
        email = form.email
        password = form.password
        if  not  form.validate_on_submit():
            abort(400)
        user =User.query.filter(User.email == email.data).first()
        if not user:
            flash("incorrect credential")
            return render_template('admin/login.html',form=form)
        if  not user.check_password(password.data):
            flash("incorrect credential")
            return render_template('admin/login.html',form=form)
        session["email"]= user.email
        session["user_id"] = user.id
        session['role']=user.role
        print (session)
        return "logged in successfuly"
        
    if session.get('email') is not None:
        return "you are already logged in"
    return render_template('admin/login.html',form = form)