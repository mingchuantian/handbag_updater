om frproject import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    want_item = db.relationship('Item', backref='wanter', lazy=True)
    
    def __repr__(self):
        return f"User('{self.email}', '{self.}'"

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)