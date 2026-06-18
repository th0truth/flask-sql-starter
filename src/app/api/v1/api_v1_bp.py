from flask import Blueprint

from .routes import users


# Initialize the /v1 router
api_v1_bp = Blueprint("v1", __name__)


# Include routes
api_v1_bp.register_blueprint(users, url_prefix="/users")
