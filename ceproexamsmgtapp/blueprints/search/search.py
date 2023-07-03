from forms import SearchForm

@bp.route('/search', methods=['POST'])
@login_required
def search():
  form = SearchForm()
  if not form.validate_on_submit():
    return redirect(url_for('index'))
  return redirect((url_for('search_results', query=form.search.data)))
