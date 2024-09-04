from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from src.database import Base


class Card(Base):
    __tablename__ = 'cards'
    id: Mapped[int] = mapped_column(primary_key=True)
    question: Mapped[str]
    answer: Mapped[str]
