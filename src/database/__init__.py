from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import DeclarativeBase

from src.config import db_settings


engine = create_engine(
    db_settings.postgres_dsn,
    echo=True,
    pool_size=5,
    max_overflow=10
)


class Base(DeclarativeBase):
    metadata = MetaData()
