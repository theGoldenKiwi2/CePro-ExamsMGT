
bp = Blueprint('stats', __name__)


@bp.route('/stats', methods=['GET', 'POST'])
@login_requiered
def stats():
    return render_template('stats.html')
