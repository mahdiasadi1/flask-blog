from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv  # Import load_dotenv
load_dotenv()


app = Flask(__name__)

# Corrected SMTP settings (TLS on Port 587)
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 587,
    "MAIL_USE_TLS": True,
    "MAIL_USE_SSL": False,
   "MAIL_USERNAME": os.getenv("MAIL_USERNAME"),  # Access from .env
    "MAIL_PASSWORD": os.getenv("MAIL_PASSWORD")   # Access from .env
}

app.config.update(mail_settings)
mail = Mail(app)

# Rest of your code...
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
db = SQLAlchemy(app)
migrate = Migrate(app=app, db=db)

# Register blueprints...
from mod_admin import admin
from mod_user import user
from mod_blog import blog
from mod_uploads import upload
app.register_blueprint(admin)
app.register_blueprint(user)
app.register_blueprint(blog)
app.register_blueprint(upload)

@app.route('/send-email')
def send_email():
    try:
        msg = Message(
            subject='Hello from Flask-Mail',
            sender='asadi.mahdi@gmail.com',
            recipients=['mahdi_asadi@yahoo.com']
        )
        msg.body = 'This is a test email sent via Flask-Mail with Gmail.'
        mail.send(msg)
        return 'Email sent!'
    except Exception as e:
        return f'Error: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)