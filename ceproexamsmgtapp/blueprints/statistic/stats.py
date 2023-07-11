from flask import Blueprint, render_template
from flask_login import login_required

bp = Blueprint('stats', __name__)


@bp.route('/stats', methods=['GET', 'POST'])
@login_required
def stats():
    return render_template('stats.html')
