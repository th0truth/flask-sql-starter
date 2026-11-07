from flask import Blueprint, render_template
from flask_login import login_required


bp = Blueprint("Main", __name__)


@bp.route("/", methods=["GET", "POST"])
@bp.route("/index", methods=["GET", "POST"])
@login_required
def index():
    return render_template("index.html", title="Home")
