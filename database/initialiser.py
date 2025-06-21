from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.tables.base import Base

# Import des modèles pour qu'ils soient enregistrés
import database.tables.productBdd
import database.tables.commandeBdd

DATABASE_URL = f"sqlite:///ma_base.db"

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)

# Création de toutes les tables
Base.metadata.create_all(engine)


def get_connection():
    db = Session()
    try:
        yield db
    finally:
        db.close()
