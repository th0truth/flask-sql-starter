from flask import Blueprint, render_template, flash, redirect, url_for
from .forms import LoginForm


bp = Blueprint("Auth", __name__)


@bp.route("/login", methods=["GET", "POST"])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    flash("Login requested for user {}, remember_me={}".format(
      form.username.data,
      form.remember_me.data
    ))
    return redirect(url_for("Web.Main.index"))
  return render_template("login.html", title="Sign In", form=form)
