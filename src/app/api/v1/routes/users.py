from flask import Blueprint


bp = Blueprint("Users", __name__)


@bp.route("/", methods=["GET"])
def get_users():
  return ["user_1", "user_2"]
