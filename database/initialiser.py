from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.tables.base import Base

# Needed for tables création
import database.tables.productBdd

DATABASE_URL = f"sqlite:///ma_base.db"

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)

# Tables creation
Base.metadata.create_all(engine)


def get_connection():
    db = Session()
    try:
        yield db
    finally:
        db.close()
