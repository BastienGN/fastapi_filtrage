from typing import Callable

from Dto.filterDtos.common.filterOperators import OPERATORS


class FilterDictionary:
    """
    Class to define the dictionary needed to check if the filter validity.
    
    This class provides methods to:
    - Get all allowed fields for filtering
    - Get allowed operators for a specific field
    - Get the value check function for a specific field and operator combination
    
    Attributes:
        dictionary (dict[str, dict[OPERATORS, Callable]]): Dictionary defining allowed fields, their associated operators 
                                                          and the function used to check the value.
    """
    dictionary: dict[str, dict[OPERATORS, Callable]]

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def get_allowed_fields(self) -> list[str]:
        return list(self.dictionary.keys())

    def get_allowed_operators_by_field(self, field_entry: str) -> list[OPERATORS]:
        return list(self.dictionary[field_entry].keys())

    def get_value_check_function_by_field_and_operator(self, field_entry: str, operator_entry: OPERATORS) -> Callable:
        return self.dictionary[field_entry][operator_entry]

