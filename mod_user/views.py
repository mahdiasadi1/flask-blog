from flask import session
from . import user
@user.route('/')
def index():
    return "hello user"
@user.route('/login')
def login():
    session['user']="mahdi"
    
    return session['user']
