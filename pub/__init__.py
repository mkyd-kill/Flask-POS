from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path, environ
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sslify import SSLify
from .validators import secretKey
from .middleware import MethodRewriteMiddleware
from flask_login import LoginManager
from .database import db_session, init_db

db = SQLAlchemy()
moment = Moment()
migrate = Migrate()
DB_NAME = "posDatabase.db"

def create_app():
    app = Flask(
        __name__,
        instance_relative_config=True,
        static_url_path='/static'
    )
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = secretKey()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    UPLOAD_FOLDER = 'static/images/icons'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    moment.init_app(app)
    migrate.init_app(app, db)
    db.init_app(app)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    with app.app_context():
        sslify = SSLify(app)

        # middleware for the application
        MethodRewriteMiddleware(app)

        # blueprint registration
        from .dashboard import dash
        from .pwa import progressive
        from .view import view
        from .super_user import super_usr
        from .errors import error

        app.register_blueprint(dash)
        app.register_blueprint(progressive)
        app.register_blueprint(view)
        app.register_blueprint(super_usr)
        app.register_blueprint(error)

        if 'DYNO' in environ:
            sslify = SSLify(app)

        # after request handler
        @app.after_request
        def after_request(response):
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE')
            return response

        # database creation
        create_database()

        login_manager = LoginManager()
        login_manager.login_view = 'view.login'
        login_manager.init_app(app)

        from .models import Admin, Super_Admin
        @login_manager.user_loader
        def load_user(id):
            return Admin.query.get(int(id))

        # saving super admin credentials
        #Super_Admin.constantUser()

        return app
    

def create_database():
    if not path.exists('pub/' + DB_NAME):
        init_db()
        print('Database Created Successfully!!!')