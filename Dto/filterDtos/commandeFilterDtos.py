from typing import Callable

from pydantic import PrivateAttr
from sqlalchemy import Select

from Dto.filterDtos.common.filterBase import FilterBase
from Dto.filterDtos.common.filterDictionary import FilterDictionary
from Dto.filterDtos.common.filterMethodCheckValue import FilterMethodCheckValue
from Dto.filterDtos.common.filterOperators import OPERATORS
from database.tables.base import Base

commande_filter_dictionary: dict[str, dict[OPERATORS, Callable]] = {
    "date_commande": {
        OPERATORS.GT: FilterMethodCheckValue.is_value_datetime_iso
    },
}


class CommandeFilter(FilterBase):
    _filter_dictionary: FilterDictionary = PrivateAttr(default=FilterDictionary(commande_filter_dictionary))

    def update_query(self, stmt: Select[Base]) -> Select[Base]:
        pass