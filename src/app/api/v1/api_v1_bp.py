from flask import Blueprint

from .routes import users, auth


# Initialize the /v1
api_v1_bp = Blueprint("v1", __name__)


# Include blueprints to the /v1
api_v1_bp.register_blueprint(users.bp, url_prefix="/users")
api_v1_bp.register_blueprint(auth.bp, url_prefix="/auth")
