import os

#ici on importe flask
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from ceproexamsmgtapp.models import db, Exam

basedir = os.path.abspath(os.path.dirname(__file__))

#on crée l’application
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:Mic99099.-.@localhost:3306/ceproexamsmgt"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    #remplacer la configuration
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)


    db.init_app(app)

    #s’assure que l’instance existe
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #petit test pour voir si la page s’affiche bien 
    @app.route('/hello')
    def hello():

        exams = Exam.query.all()
        for exam in exams:
            print("Examen :"+ str(exam.id)+" / "+exam.code+" / "+exam.name)
        
        return 'Hello, World!'

    return app