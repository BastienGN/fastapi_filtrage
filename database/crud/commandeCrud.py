from typing import Type

from sqlalchemy.orm import Session

from database.tables.commandeBdd import CommandeBdd


def get_all_products(db: Session) -> list[Type[CommandeBdd]]:
    commandes: list[Type[CommandeBdd]] = db.query(CommandeBdd).all()
    return commandes
