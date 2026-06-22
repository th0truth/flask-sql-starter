import sqlalchemy as sa
import sqlalchemy.orm as so
from app.main import db


class UserBase(db.Model):
  __tablename__ = "users"

  id: so.Mapped[int] = so.mapped_column(
          primary_key=True)

  username: so.Mapped[str] = so.mapped_column(
          sa.String(64), index=True, unique=True)
  email: so.Mapped[str] = so.mapped_column(
          sa.String(50), index=True, unique=True)
  
  password_hash: so.Mapped[str] = so.mapped_column(
          sa.String(128))

  posts: so.Mapped["PostBase"] = so.relationship(
          back_populates="author")

  def __repr__(self):
    return f"<User {self.username}>"
