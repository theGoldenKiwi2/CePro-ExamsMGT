from flask import  Blueprint, render_template
from flask_login import login_required, current_user
from ceproexamsmgtapp.models import db

bp = Blueprint('main', __name__)



@bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.firstname)