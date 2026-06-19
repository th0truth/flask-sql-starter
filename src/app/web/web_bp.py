from flask import Blueprint

from .auth.routes import bp as auth_bp 
from .main.routes import bp as main_bp

# Initialize the /v1
web_bp = Blueprint("Web", __name__)


# Include blueprints to the /v1
web_bp.register_blueprint(auth_bp)
web_bp.register_blueprint(main_bp)
