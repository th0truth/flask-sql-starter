from flask import Flask

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager

from .core.config import BASE_DIR, settings


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_mapping(settings.model_dump())

    # Ensure instance directory exists for SQLite
    (BASE_DIR / "instance").mkdir(parents=True, exist_ok=True)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    login.init_app(app)
    login.login_view = "Web.Auth.login"

    from .core.schema import UserBase

    @login.user_loader
    def load_user(user_id: str):
        return db.session.get(UserBase, int(user_id))

    with app.app_context():
        from .api.api import api_main_bp
        from .web.web_bp import web_bp

        app.register_blueprint(web_bp)
        app.register_blueprint(api_main_bp)

        return app


# Create an app instance at module level
app = create_app()
