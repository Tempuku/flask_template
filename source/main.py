from flask import Flask, redirect, url_for
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, current_user
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from . import settings

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
login_manager = LoginManager()
csrf = CSRFProtect()


class ModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for("auth.login"))


class AdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('auth.login'))
        return super(AdminIndexView, self).index()


def create_app():
    app = Flask(__name__, template_folder='templates')

    # load default configuration
    app.config.from_object(settings.Config)

    # init apps
    db.init_app(app)
    migrate.init_app(app, db, directory=settings.MIGRATION_DIR)
    ma.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    csrf.init_app(app)

    # admin
    from .auth.models import User
    admin = Admin(app, name='Page admin', index_view=AdminIndexView(
                    name='Home',
                    template='admin.html',
                    url='/admin/'
                ), base_template='base.html')

    admin.add_view(ModelView(User, db.session))

    # api
    from .api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    # auth
    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth.auth import auth_bp
    app.register_blueprint(auth_bp)

    return app
