from flask import Flask


def create_app() -> Flask: 
  app = Flask(__name__)

  from .api.api import api_main_bp
  app.register_blueprint(api_main_bp, url_prefix="/api")

  return app


# Create an app instance at module level
app = create_app()
