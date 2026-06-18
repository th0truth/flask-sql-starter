from flask import Blueprint

from .routes import users


# Initialize the /v1
api_v1_bp = Blueprint("v1", __name__)


# Include blueprints to the /v1
api_v1_bp.register_blueprint(users, url_prefix="/users")
