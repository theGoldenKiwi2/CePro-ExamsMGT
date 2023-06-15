from flask_login import login_user, login_required, logout_user
from flask import Blueprint, render_template, flash, redirect, url_for, request
from login import check_password_hash
from sqlalchemy.sql.functions import user
from .Froms_auth import LoginForm
#from . import db
from ...models import User
bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    error_msg = request.form.get('error')
    if request.method == 'POST':
        error_msg = None
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        user = User.query.filter_by(email=email).first()
        # check if the user actually exists
        # take the user-supplied password, hash it, and compare it to the hashed password in the database

        if not user or user.password != password:
            error_msg = 'Please check your login details and try again.'
            print(error_msg)
            return redirect(url_for('auth.login', error=error_msg))

        login_user(user, remember=remember)
        return redirect(url_for('main.profile'))

    return render_template('login.html', error=None)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))