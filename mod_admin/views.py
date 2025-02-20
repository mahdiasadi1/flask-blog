from flask import flash, session , render_template,request,abort,redirect,url_for
from werkzeug.security import check_password_hash
from  mod_user.form import Loginform
# from models import User
from mod_user.models import User
from . import admin
from .utils import protected_view
from mod_blog.forms import Postform
from mod_blog.models import Post
from app import db
from sqlalchemy.exc import IntegrityError
@admin.route('/')
@protected_view
def admin_index():
    # print(session['user_id'])    
    # return "sdfdgeh"
    return render_template('admin/index.html')
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
        if not check_password_hash(user.password, password.data):
            breakpoint()
            flash("incorrect credential")
            return render_template('admin/login.html',form=form)
        session["email"]= user.email
        session["user_id"] = user.id
        session['role']=user.role
        print (session)
        return redirect (url_for('admin.admin_index'))
        
    if session.get('email') is not None:
        return "you are already logged in"
    return render_template('admin/login.html',form = form)
@admin.route('/logout/')
@protected_view
def logout():
    session.clear()
    flash(" you 're successfully logged out ","warning")
    return redirect (url_for('admin.login'))
@admin.route('/post/new',methods=["POST","GET"])
@protected_view
def create_post():
    form = Postform(request.form)
    if request.method == 'POST':
        print ("fuck")
        if not form.validate_on_submit():
            return 1
        title = form.title.data
        summary=form.title.data
        slug=form.slug.data
        content = form.content.data
        newpost  = Post()
        newpost.title = title
        newpost.summary = summary
        newpost.slug=slug
        newpost.content = content
        try:
            db.session.add(newpost)
            db.session.commit()
            flash("new post created successfully " , "success")
            return redirect(url_for('admin.admin_index'))
        except  IntegrityError: 
            db.session.rollback()   
    else: 
        print("no fuck")      
        return render_template('admin/create_post.html',form=form)
@admin.route('/list_post/',methods=["GET","POST"])
@protected_view
def list_post():
    posts = Post.query.all()
    return render_template('admin/list_post.html',posts = posts)
@admin.route('post/delete/<int:id>')
@protected_view
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash("post deleted successfully", "bg-danger text-white")
    return redirect(url_for('admin.list_post'))
 