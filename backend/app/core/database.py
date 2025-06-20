from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from .config import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# This function will create all tables.
# It's better to run this once manually or use a migration tool like Alembic.


def create_db_and_tables():
    Base.metadata.create_all(bind=engine)
