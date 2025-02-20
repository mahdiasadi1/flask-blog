from flask import render_template,request
from . import blog 
from .models import Post
@blog.route('index')
def index():
    posts = Post.query.all()
    return render_template('blog/index.html',posts=posts)
@blog.route('/post/<string:slug>')
def single_post(slug):
    post = Post.query.filter(Post.slug == slug).first()
    return render_template('blog/single.html',post=post)
