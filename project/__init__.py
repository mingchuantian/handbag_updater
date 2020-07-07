from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail, Message
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
'''
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Dont think about it'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
'''
#for db session
some_engine = create_engine('postgresql://scott:tiger@localhost/')
# create a configured "Session" class
Session = sessionmaker(bind=some_engine)
# create a Session
session = Session()
'''
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
#pass in the funciton name of the route
#when go to login_required page but not logged in,
#it will automatically redirect to login route
login_manager.login_view = 'login'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'mingchuantian1@gmail.com'
app.config['MAIL_PASSWORD'] = 'tianmingchuan123'

#setting up mail
mail=Mail()
mail.init_app(app)



from project import routes