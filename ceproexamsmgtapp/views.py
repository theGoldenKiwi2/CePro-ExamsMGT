from flask import current_app as app, render_template

@app.route('/login')
def login():
    return render_template('login.html')