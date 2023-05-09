import os

#ici on importe flask
from flask import Flask

#on crée l’application
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    
    #remplacer la configuration
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    #s’assure que l’instance existe
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #petit test pour voir si la page s’affiche bien 
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app