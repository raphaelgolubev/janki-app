from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from src.database import Base


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    hashed_password: Mapped[str]


class Profile(Base):
    __tablename__ = 'profiles'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    score: Mapped[int]
