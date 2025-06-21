from typing import Type

from sqlalchemy.orm import Session

from database.tables.productBdd import ProductBdd


def get_all_products(db: Session) -> list[Type[ProductBdd]]:
    products: list[Type[ProductBdd]] = db.query(ProductBdd).all()
    return products
