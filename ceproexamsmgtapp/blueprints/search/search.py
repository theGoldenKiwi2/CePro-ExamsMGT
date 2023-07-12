from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, request, render_template
from flask_login import login_required
from ceproexamsmgtapp.models import User


bp = Blueprint('search', __name__)

@bp.route('/search', methods=['POST'])
@login_required
def search():
    search_str = request.form.get('search')
    results = User.query.filter(User.firstname.like('%'+search_str+'%')).all()
    if not results:
        msg = 'No search found'
        return render_template('search.html', users=results, message=msg)

    return render_template('search.html', users=results)

# @bp.route('/search/filter/year', methods=['POST'])
# @login_required
# def year():
#     year_str = request.form.get('year')
#     results = Exam.query.filter(Exam.exam_date.like('%'+year_str+'%')).all()
#
#     return render_template('searchYear.html', exams=results)
