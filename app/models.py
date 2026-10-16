from app import db


class Kid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    points = db.Column(db.Integer, default=0)
    photo = db.Column(db.String(120), default='default_kid.svg')


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    icon = db.Column(db.String(120), nullable=False)


class Reward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    icon = db.Column(db.String(120), nullable=False)
