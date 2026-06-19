from flask import Blueprint


bp = Blueprint("Authentication", __name__)


@bp.route("/login", methods=["GET", "POST"])
def login():
  return "Auth"