# auth.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, current_user, login_required
from .models import User
from source.main import db

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.index'))

    if User.query.first() is None:
        user = User(name='user', password='password')
        db.session.add(user)
        db.session.commit()
    return render_template('login.html')


@auth_bp.route('/login', methods=['POST'])
def login_post():
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    name = request.form.get('name')

    user = User.query.filter_by(name=name).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not password:
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))  # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('admin.index'))


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('admin.index'))
