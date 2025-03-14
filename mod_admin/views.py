from flask import flash, session , render_template,request,abort,redirect,url_for
from werkzeug.security import check_password_hash
from  mod_user.form import Loginform
# from models import User
from mod_user.models import User
from . import admin
from .utils import protected_view
from mod_blog.forms import Postform,Categoryform
from mod_blog.models import Post ,Category
from app import db
from sqlalchemy.exc import IntegrityError
from mod_uploads.forms import Fileform
from mod_uploads.models import uploads
from werkzeug.utils import secure_filename
import uuid
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
    form.categories.choices = [(category.id, category.name) for category in Category.query.all()]

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
        newpost.categories = Category.query.filter(Category.id.in_(form.categories.data)).all()

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
@admin.route('post/modify/<int:id>',methods=["GET","POST"])
@protected_view
def modify_post(id):
        
    post=Post.query.get_or_404(id)
    
    form = Postform(obj=post)
    form.categories.choices = [(category.id, category.name) for category in Category.query.all()]
    if request.method=="GET":
        form.categories.data = [category.id for category in post.categories]  # مقداردهی اولیه چک‌باکس‌ها
    

    if request.method =="POST":
        if not form.validate_on_submit():
            return render_template('admin/modify_post.html',form = form,post=post) 
        post.title = form.title.data
        post.summary = form.summary.data
        post.slug = form.slug.data
        post.content = form.content.data
        post.categories = Category.query.filter(Category.id.in_(form.categories.data)).all()
        # post.categories = Category.query.filter(Category.id.in_(form.categories.data)).all()  # تنظیم دسته‌های انتخابی


        try:
            db.session.commit()
            flash("update successfully",'text-success')
            return redirect(url_for('admin.list_post'))
        except IntegrityError:
            db.session.rollback()
            flash("your slug is already taken")
            return render_template('admin/modify_post.html',form = form,post=post)    
    return render_template('admin/modify_post.html',form = form,post=post) 
############################ 
@admin.route('/category/new',methods=["POST","GET"])
@protected_view
def create_category():
    form = Categoryform(request.form)
    if request.method == 'POST':
        print ("fuck")
        if not form.validate_on_submit():
            return 1
        
        newcategory  = Category()
        newcategory.name = form.name.data
        newcategory.slug = form.slug.data
        newcategory.description=form.description.data
        try:
            db.session.add(newcategory)
            db.session.commit()
            flash("new category created successfully " , "success")
            return redirect(url_for('admin.admin_index'))
        except  IntegrityError: 
            db.session.rollback()   
    else: 
        print("no fuck")      
        return render_template('admin/create_category.html',form=form)
@admin.route('/list_category/',methods=["GET","POST"])
@protected_view
def list_category():
    categories = Category.query.all()
    return render_template('admin/list_category.html',categories = categories)
@admin.route('categoriy/delete/<int:id>')
@protected_view
def delete_category(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    flash("category deleted successfully", "bg-danger text-white")
    return redirect(url_for('admin.list_category'))
@admin.route('category/modify/<int:id>',methods=["GET","POST"])
@protected_view

def modify_category(id):
        
    category=Category.query.get_or_404(id)
    form = Categoryform(obj=category)
    if request.method =="POST":
        if not form.validate_on_submit():
            return render_template('admin/modify_category.html',form = form,category=category) 
        category.name = form.name.data
        category.description = form.description.data
        category.slug = form.slug.data
        try:
            db.session.commit()
            flash("update successfully",'text-success')
            return redirect(url_for('admin.list_category'))
        except IntegrityError:
            db.session.rollback()
            flash("your slug is already taken")
            return render_template('admin/modify_category.html',form = form,category=category)    
    return render_template('admin/modify_category.html',form = form,category=category)   

@admin.route('/library/upload',methods=["GET","POST"])  
@protected_view
def upload_file():
    form = Fileform()
    if request.method =="POST":
        if not form.validate_on_submit():
            return 5
        newfile= uploads()
        filename =f'{uuid.uuid1()} {secure_filename(form.file.data.filename)}'
        newfile.filename=filename
        db.session.add(newfile)
        db.session.commit()
        form.file.data.save(f'static/uploads/{filename}')
        flash('file uploaded','text-success')
    return render_template('admin/upload_file.html',form=form)