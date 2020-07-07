from project import db, login_manager
from flask_login import UserMixin
from sqlalchemy.orm import relationship, backref

#get user by id (login manager requires this function)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    found_email_sent = db.Column(db.Integer, default=0)
    #The backref will be a column in the Item table
    subscribed_items = db.relationship('Item', secondary='subscribes', backref=db.backref('subscribed_users'), lazy='dynamic')
    
    def __repr__(self):
        return f"User('{self.email}'"

#helper table
subscribes = db.Table('subscribes',
        db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
        db.Column('item_id', db.Integer, db.ForeignKey('items.id')),
        db.Column('email_sent', db.Integer, default=0))



class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(30), nullable=False)
    country = db.Column(db.String(15), nullable=False)
    sku = db.Column(db.String(30), nullable=False)
    is_available = db.Column(db.Boolean, default=False)
    #last_time = db.Column(db.DateTime, default=datetime.utcnow)
    #users = db.relationship("User", secondary="subscribes")

    def now_available(self):
        self.is_available = True
    
    def now_unavailable(self):
        self.is_available = False
    
    def __repr__(self):
        return f"Item('{self.sku}')"