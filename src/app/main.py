from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .core.config import settings


db = SQLAlchemy()
migrate = Migrate() 


def create_app() -> Flask: 
  app = Flask(__name__)
  app.config.from_mapping(settings.model_dump())

  # Initialize the db instance
  db.init_app(app)
  migrate.init_app(app, db)

  from .core.schema import UserBase, PostBase

  from .api.api import api_main_bp
  app.register_blueprint(api_main_bp)

  from .web.web_bp import web_bp
  app.register_blueprint(web_bp)

  return app


# Create an app instance at module level
app = create_app()
