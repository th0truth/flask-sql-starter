from datetime import UTC, datetime

import sqlalchemy as sa
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from app.core.schema import PostBase, UserBase
from app.main import db
from app.web.forms import EditProfileForm

bp = Blueprint("Main", __name__)


@bp.route("/", methods=["GET", "POST"])
@bp.route("/index", methods=["GET", "POST"])
@login_required
def index():
    return render_template("index.html", title="Home")


@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now(UTC)
        db.session.commit()


@bp.route("/user/<username>")
@login_required
def get_user(username):
    user = db.first_or_404(sa.select(UserBase).where(UserBase.username == username))

    posts = db.session.scalars(
        sa.select(PostBase)
        .where(PostBase.author == user)
        .order_by(PostBase.timestamp.desc())
    ).all()

    return render_template("user.html", user=user, posts=posts)


@bp.route("/edit/profile", methods=["GET", "POST"])
@login_required
def edit_profile():
    form = EditProfileForm()

    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()

        flash("Your changes have been saved.")

        return redirect(url_for("Web.Main.edit_profile"))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me

    return render_template("edit_profile.html", title="Edit Profile", form=form)
