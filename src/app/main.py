from flask import Flask

def create_app() -> Flask: 
  app = Flask(__name__)

  return app

# Create an app instance at module level
app = create_app()

from .api.routes import users