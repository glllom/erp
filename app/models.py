from app import db
from flask_login import UserMixin


class Product(db.Models):
    product_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column("Name", db.String)
    active = db.Column("active", db.Boolean, default=True)

