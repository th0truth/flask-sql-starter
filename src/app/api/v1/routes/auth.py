from flask import (
    Blueprint, flash,
    redirect, render_template
)

from app.web.auth import LoginForm 


bp = Blueprint("Authentication", __name__)


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash(
            f"Login requested from user {form.username.data}, {form.remember_me.data}"
        )

        return redirect("/")

    return render_template("login.html", title="Sign In", form=form)
