import os

#ici on importe flask
from flask import Flask, render_template
from flask_login import LoginManager
from flask_login import login_required

from flask_sqlalchemy import SQLAlchemy
from ceproexamsmgtapp.models import db, Exam, User

basedir = os.path.abspath(os.path.dirname(__file__))

#on crée l’application
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:MOTdepasse2023!@localhost:3306/ceproexamsmgt"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    #remplacer la configuration
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(user_id):
        """Given *user_id*, return the associated User object.

        :param unicode user_id: user_id (email) user to retrieve

        """
        return User.query.get(user_id)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    #s’assure que l’instance existe
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #petit test pour voir si la page s’affiche bien 
    @app.route('/hello')
    @login_required
    def hello():

        # exams = Exam.query.all()
        # for exam in exams:
        #     print("Examen :"+ str(exam.id)+" / "+exam.code+" / "+exam.name)
        
        return 'Hello, World!'

    @app.route('/')
    def login():
        return render_template('login.html')

    return app