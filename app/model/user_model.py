from app import db
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

class User(db.Model):
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    user_name: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    token: Mapped[str] = mapped_column(String, nullable=False)
