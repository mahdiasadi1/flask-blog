from flask import session, request,render_template
from . import user
@user.route('/')
def index():
    return "hello user"
# @user.route('/login',methods=["POST","GET"])
# def login():
#     # session['user']="mahdi"
#     if request.method =="GET" :
#         form = Form()   
#         return render_template('admin/login.html',form=form)
     

#     return session['user']
