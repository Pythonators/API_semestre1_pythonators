from flask import Flask

#Função para criar webserver
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'A1B2C3'

    from .views import views
    #from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    return app