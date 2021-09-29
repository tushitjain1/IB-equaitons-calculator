from flask import Flask


def createApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'computerscienceIA'

    from .views import views
    app.register_blueprint(views, url_prefix='/')
    return app
