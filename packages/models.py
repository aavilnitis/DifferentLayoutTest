from flask_sqlalchemy import SQLAlchemy
from .extensions import db


class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(300))
    type = db.Column(
        db.Enum('food', 'drink', name='menuItem_type'), nullable=False)

    def __init__(self, name, price, description, type):
        self.name = name
        self.price = price
        self.description = description
        self.type = type
