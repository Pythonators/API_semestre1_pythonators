<<<<<<< HEAD
from flask import Flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'A1B2C3'

    from Website.rotas import app


=======
from flask import Flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'A1B2C3'

    from Website.rotas import app


>>>>>>> 6165261cd08a060cae6648c8024d20a8d333b3dc
    return app