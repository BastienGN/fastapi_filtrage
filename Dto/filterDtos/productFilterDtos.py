from typing import Callable

from pydantic import PrivateAttr, Field
from sqlalchemy.orm import DeclarativeBase

from Dto.filterDtos.common.filterBase import FilterBase
from Dto.filterDtos.common.filterBaseList import FilterBaseList
from Dto.filterDtos.common.filterDictionary import FilterDictionary
from Dto.filterDtos.common.filterMethodCheckValue import FilterMethodCheckValue
from Dto.filterDtos.common.filterOperators import OPERATORS
from database.tables.productBdd import ProductBdd

product_filter_dictionary: dict[str, dict[OPERATORS, Callable]] = {
    "brand": {
        OPERATORS.EQUAL: FilterMethodCheckValue.is_value_str,
        OPERATORS.IEQUAL: FilterMethodCheckValue.is_value_str,
        OPERATORS.IN: FilterMethodCheckValue.is_value_list_str,
        OPERATORS.IIN: FilterMethodCheckValue.is_value_list_str,
    },
    "price": {
        OPERATORS.BETWEEN: FilterMethodCheckValue.is_value_between_operator_suitable,
        OPERATORS.EQUAL: FilterMethodCheckValue.is_value_int,
        OPERATORS.IN: FilterMethodCheckValue.is_value_list_int,
        OPERATORS.GREATER_THAN: FilterMethodCheckValue.is_value_int,
        OPERATORS.LESSER_THAN: FilterMethodCheckValue.is_value_int
    },
}

class ProductFilter(FilterBase):
    _filter_dictionary: FilterDictionary = PrivateAttr(default=FilterDictionary(product_filter_dictionary))
    _table: DeclarativeBase = PrivateAttr(default=ProductBdd)

class ListProductFilter(FilterBaseList):
    filters: list[ProductFilter] = Field(default_factory=list)