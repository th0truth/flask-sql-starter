from flask import Blueprint


users = Blueprint("Users", __name__)


@users.route("/", methods=["GET"])
def get_users():
  return ["user_1", "user_2"]
