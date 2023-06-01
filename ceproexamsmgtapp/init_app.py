import os

# ici on importe flask
from flask import Flask, render_template
from flask_login import current_user, LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from ceproexamsmgtapp.models import db, Exam, User, UserType, ServiceLevel
from ceproexamsmgtapp.views import UserView

basedir = os.path.abspath(os.path.dirname(__file__))


# on crée l’application
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:MOTdepasse2023!@localhost:3306/ceproexamsmgt"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['BASIC_AUTH_FORCE'] = True
    db.init_app(app)

    # remplacer la configuration
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    from .blueprints.auth import auth
    app.register_blueprint(auth.bp)


        # Import admin model views

    #if __name__ == '__main__':
    admin = Admin(app)
    admin.add_view(UserView(User, db.session))
    admin.add_view(ModelView(UserType, db.session))
    admin.add_view(ModelView(ServiceLevel, db.session))

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)


    # s’assure que l’instance existe
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # petit test pour voir si la page s’affiche bien

    # exams = Exam.query.all()
    # for exam in exams:
    #     print("Examen :"+ str(exam.id)+" / "+exam.code+" / "+exam.name)
    @app.route('/')
    def index():

        if current_user.is_authenticated:
            return render_template('login.html')
        else:
            return render_template('index.html')

    @app.route('/login', methods=('GET', 'POST'))
    def login():
        return render_template('login.html')

    #@app.route('/logout/', methods=('GET', 'POST'))
    #def logout():
     #   return render_template('logout.html')

    return app

