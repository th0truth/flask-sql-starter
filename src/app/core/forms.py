from flask_wtf import FlaskForm
from wtforms import (
    PasswordField, StringField, SubmitField
)
from wtforms.validators import (
    DataRequired, Email, EqualTo, ValidationError
)

import sqlalchemy as sa

from app.core.schema import UserBase
from app.main import db


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    password_repeat = PasswordField(
        "Repeat Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Register")

    def validate_username(self, username):
        user = db.session.scalar(
            sa.select(UserBase).where(UserBase.username == username.data)
        )
        if user is not None:
            raise ValidationError("Please use a different username.")

    def validate_email(self, email):
        user = db.session.scalar(
            sa.select(UserBase).where(UserBase.email == email.data)
        )
        if user is not None:
            raise ValidationError("Please use a different email address.")
