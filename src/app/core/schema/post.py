from datetime import datetime, timezone
import sqlalchemy as sa
import sqlalchemy.orm as so
from app.main import db


class PostBase(db.Model):
  __tablename__ = "posts"
  
  id: so.Mapped[int] = so.mapped_column(primary_key=True)

  title: so.Mapped[str] = so.mapped_column(sa.String(64))
  body: so.Mapped[str] = so.mapped_column(sa.String(256)) 
  
  timestamp: so.Mapped[datetime] = so.mapped_column(
            index=True, default=lambda: datetime.now(timezone.utc))
  user_id: so.Mapped[int] = so.mapped_column(
            sa.ForeignKey("users.id"), index=True)
  author: so.Mapped["UserBase"] = so.relationship(back_populates="posts")

  def __repr__(self):
    return f"<Post {self.title}"
