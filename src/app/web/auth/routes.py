from urllib.parse import urlsplit

from flask import (
    Blueprint, flash, redirect,
    render_template, request, url_for,
)
from flask_login import (
    current_user, login_user, logout_user
)

from app.core.forms import RegistrationForm
from app.core.schema import UserBase
from app.core.security import Hash
from app.main import db

from .forms import LoginForm


bp = Blueprint("Auth", __name__)


@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("Web.Main.index"))

    form = LoginForm()

    if form.validate_on_submit():
        user = db.session.scalar(
            db.select(UserBase).where(
                UserBase.username == form.username.data
            )
        )

        if not user or not Hash.verify(
            form.password.data, user.password_hash
        ):
            flash("Invalid username or password")

            return redirect(url_for("Web.Auth.login"))

        login_user(user, remember=form.remember_me.data)

        next_page = request.args.get("next")

        if not next_page or urlsplit(next_page).netloc != "":
            next_page = url_for("Web.Main.index")

        return redirect(next_page)

    return render_template("login.html", title="Sign In", form=form)


@bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("Web.Main.index"))

    form = RegistrationForm()

    if form.validate_on_submit():
        user = UserBase(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash("User has been created successfully.")

        return redirect(url_for("Web.Auth.login"))

    return render_template("register.html", title="Register", form=form)


@bp.route("/logout")
def logout():
    logout_user()

    return redirect(url_for("Web.Main.index"))
