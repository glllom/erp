from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config
from flask_login import LoginManager

process_app = Flask(__name__)
process_app.config.from_object(Config)

db = SQLAlchemy()


class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column("Name", db.String)
    active = db.Column("active", db.Boolean, default=True)




db.init_app(process_app)

from app import routes

db.create_all(app=process_app)

migrate = Migrate(process_app, db)



