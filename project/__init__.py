from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Dont think about it'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
#pass in the funciton name of the route
#when go to login_required page but not logged in,
#it will automatically redirect to login route
login_manager.login_view = 'login'


from project import routes