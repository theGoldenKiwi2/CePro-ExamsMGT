# from forms import SearchForm
# @bp.route('/search', methods=['GET', 'POST'])
# @login_required
# def search():
#     form = SearchForm()
#     if request.method == 'POST' and form.validate_on_submit():
#         return redirect((url_for('search_results', query=form.search.data)))  # or what you want
#     return render_template('search.html', form=form)
# @bp.route('/search_results/<query>')
# @login_required
# def search_results(query):
#   results = User.query.whoosh_search(query).all()
#   return render_template('search_results.html', query=query, results=results)