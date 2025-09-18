from typing import Callable

from pydantic import PrivateAttr

from Dto.filterDtos.common.filterBase import FilterBase
from Dto.filterDtos.common.filterDictionary import FilterDictionary
from Dto.filterDtos.common.filterMethodCheckValue import FilterMethodCheckValue
from Dto.filterDtos.common.filterOperators import OPERATORS

commande_filter_dictionary: dict[str, dict[OPERATORS, Callable]] = {
    "date_commande": {
        OPERATORS.GREATER_THAN: FilterMethodCheckValue.is_value_datetime_iso
    },
}


class CommandeFilter(FilterBase):
    _filter_dictionary: FilterDictionary = PrivateAttr(default=FilterDictionary(commande_filter_dictionary))