from app import db
from datetime import datetime

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))    
    last_name = db.Column(db.String(50))
    username = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    password_hash = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<USER: {self.username}'

class Post(db.Model):
    post_id = db.Column(db.String, primary_key=True)
    body = db.Column(db.String(), nullable = False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)