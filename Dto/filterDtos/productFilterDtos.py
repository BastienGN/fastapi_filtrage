from typing import Callable

from fastapi import HTTPException
from pydantic import PrivateAttr, Field
from sqlalchemy import Select

from Dto.filterDtos.common.filterBase import FilterBase
from Dto.filterDtos.common.filterBaseList import FilterBaseList
from Dto.filterDtos.common.filterDictionary import FilterDictionary
from Dto.filterDtos.common.filterMethodCheckValue import FilterMethodCheckValue
from Dto.filterDtos.common.filterOperators import OPERATORS
from database.tables.productBdd import ProductBdd

product_filter_dictionary: dict[str, dict[OPERATORS, Callable]] = {
    "brand": {
        OPERATORS.EQUAL: FilterMethodCheckValue.is_value_str,
        OPERATORS.IN: FilterMethodCheckValue.is_value_list_str
    },
    "price": {
        OPERATORS.EQUAL: FilterMethodCheckValue.is_value_int,
        OPERATORS.GT: FilterMethodCheckValue.is_value_int,
        OPERATORS.LT: FilterMethodCheckValue.is_value_int
    },
}

def update_query_product(product_filter: 'ProductFilter', stmt: Select[ProductBdd]) -> Select[ProductBdd]:
    match (product_filter.field, product_filter.operator):
        case ("brand", OPERATORS.EQUAL):
            stmt = stmt.where(ProductBdd.brand == product_filter.value)
        case ("brand", OPERATORS.IN):
            stmt = stmt.where(ProductBdd.brand.in_(product_filter.value))
        case ("price", OPERATORS.EQUAL):
            stmt = stmt.where(ProductBdd.price == product_filter.value)
        case ("price", OPERATORS.GT):
            stmt = stmt.where(ProductBdd.price > product_filter.value)
        case ("price", OPERATORS.LT):
            stmt = stmt.where(ProductBdd.price < product_filter.value)
        case _:
            raise HTTPException(
                500,
                f"You have to implement every possibilities found in the associated dictionary. Field '{product_filter.field}' and Operator '{product_filter.operator}' possibility occurred."
            )

    return stmt

class ProductFilter(FilterBase):
    _filter_dictionary: FilterDictionary = PrivateAttr(default=FilterDictionary(product_filter_dictionary))

    def update_query(self, stmt: Select[ProductBdd]) -> Select[ProductBdd]:
        return update_query_product(self, stmt)


class ListProductFilter(FilterBaseList):
    filters: list[ProductFilter] = Field(default_factory=list)