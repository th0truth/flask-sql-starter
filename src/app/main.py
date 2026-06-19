from flask import Flask
from .core.config import settings

def create_app() -> Flask: 
  app = Flask(__name__)
  app.config.from_mapping(settings.model_dump())

  from .api.api import api_main_bp
  app.register_blueprint(api_main_bp)

  return app


# Create an app instance at module level
app = create_app()
