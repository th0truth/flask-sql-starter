from flask import Blueprint, render_template


bp = Blueprint("Main", __name__)


@bp.route("/", methods=["GET", "POST"])
@bp.route("/index", methods=["GET", "POST"])
def index():
  return render_template("index.html", title="Home")
