from typing import Type

from sqlalchemy import Select
from sqlalchemy.orm import Session

from Dto.responseDtos.productDto import GetProductFiltered, ProductDto
from database.crud import productCrud
from database.tables.productBdd import ProductBdd


def get_all_products(db: Session) -> list[ProductDto]:
    product_bdds: list[Type[ProductBdd]] = productCrud.get_all_products(db)
    return [ProductDto.model_validate(prod) for prod in product_bdds]



def get_filtered_products(product_filters: GetProductFiltered, db: Session, select_stmt: Select[ProductBdd] ) -> list[ProductDto] | None:
    select_stmt = product_filters.update_query(select_stmt)
    return [ProductDto.model_validate(product) for product in db.execute(select_stmt).scalars().all()]
