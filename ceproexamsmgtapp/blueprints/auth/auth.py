import bcrypt as bcrypt
from flask import render_template, Blueprint, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user
from ceproexamsmgtapp.blueprints.auth.Froms_auth import LoginForm
from ceproexamsmgtapp.models import db, User

bp = Blueprint('auth', __name__, url_prefix='/auth')



@bp.route('/login', methods=['GET', 'POST'])
@login_required
def login():
    print(db)
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.get(form.email.data)
        if user:
           if bcrypt.check_password_hash(user.password, form.password.data):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return redirect(url_for("bp.reports"))
    return render_template("login.html", form=form)

    return render_template('login.html')

@bp.route("/logout", methods=["GET"])

@login_required
def logout():
    """Logout the current user."""
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return render_template("logout.html")