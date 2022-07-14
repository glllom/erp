from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import process_app


@process_app.route('/')
def index():
    return render_template('index.html')


@process_app.route('/<int:height>/<int:width>')
def dimensions(height, width):
    dim = [('', height)]
    return render_template('dimensions.html', height=height, width=width)
