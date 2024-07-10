from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # secret key for the app, as it relates to cookies/sessions
    app.config['SECRET_KEY'] = 'akjgkrskdb'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")


    return app


