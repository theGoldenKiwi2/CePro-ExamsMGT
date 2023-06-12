import os

#ici on importe flask
from flask import Flask, render_template
from flask_login import LoginManager, current_user
from flask_login import login_required
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy, model
from ceproexamsmgtapp.models import db, Exam, User, UserType

basedir = os.path.abspath(os.path.dirname(__file__))


#on crée l’application
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:Mic99099.-.@localhost:3306/ceproexamsmgt"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = basedir+'/blueprints/data_import/upload'
    print(app.config['UPLOAD_FOLDER'])
    db.init_app(app)



    #remplacer la configuration
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    from .blueprints.auth import auth
    app.register_blueprint(auth.bp)
    from .blueprints.data_import import data_import
    app.register_blueprint(data_import.bp)

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(user_id):

        return User.query.get(user_id)

    admin = Admin(app)
    admin.add_view(ModelView(User, db.session))

     #s’assure que l’instance existe
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    #petit test pour voir si la page s’affiche bien
    @app.route('/')
    def index():

        # exams = Exam.query.all()
        # for exam in exams:
        #     print("Examen :"+ str(exam.id)+" / "+exam.code+" / "+exam.name)

        if current_user.is_authenticated:
            return render_template('login.html')
        else:
            return render_template('index.html')

    return app