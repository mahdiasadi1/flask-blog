from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
from mod_admin import admin
app.register_blueprint(admin)
if __name__ == '__main__':
    app.run(debug=True)