from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='mysql+pymysql://root:@localhost:3306/blog'
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False
app.config["SECRET_KEY"]="SECRET"
db= SQLAlchemy(app)
migrate = Migrate(app=app,db=db)
from mod_admin import admin
from mod_user import user
app.register_blueprint(admin)
app.register_blueprint(user)
if __name__ == '__main__':
    app.run(debug=True)