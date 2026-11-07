from typing import TYPE_CHECKING

import sqlalchemy as sa
import sqlalchemy.orm as so
from flask_login import UserMixin

from app.core.security import Hash
from app.main import db

if TYPE_CHECKING:
    from .post import PostBase


class UserBase(UserMixin, db.Model):
    __tablename__ = "users"

    id: so.Mapped[int] = so.mapped_column(primary_key=True)

    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(50), index=True, unique=True)

    password_hash: so.Mapped[str] = so.mapped_column(sa.String(128))

    posts: so.Mapped[list["PostBase"]] = so.relationship(back_populates="author")

    def set_password(self, password: str) -> None:
        self.password_hash = Hash.hash(password)

    def check_password(self, password: str) -> bool:
        return Hash.verify(password, self.password_hash)

    def __repr__(self):
        return f"<User {self.username}>"
