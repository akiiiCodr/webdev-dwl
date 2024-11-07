from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'TESTWEBDWL'

    from website.templates.views import views_bp
    from website.templates.auth import auth_bp

    app.register_blueprint(views_bp, url_prefix = '/')
    app.register_blueprint(auth_bp, url_prefix = '/')

    return app