from typing import Any, Callable

from fastapi import HTTPException
from pydantic import BaseModel, PrivateAttr, model_validator
from sqlalchemy import Select
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm.attributes import InstrumentedAttribute

from Dto.filterDtos.common.filterDictionary import FilterDictionary
from Dto.filterDtos.common.filterOperators import OPERATORS, operator_functions
from database.tables.base import Base


def __check_field_type(field_entry: Any) -> None:
    if not isinstance(field_entry, str):
        raise HTTPException(
            400,
            f"Field key type '{type(field_entry).__name__}' is not allowed. Allowed Field key type: 'str'",
        )


def __check_filter_field_entry(field_entry: str, allowed_fields: list[str]) -> None:
    if field_entry not in allowed_fields:
        raise HTTPException(
            400,
            f"Field key '{field_entry}' is not allowed for filtering. Allowed keys: {allowed_fields}",
        )


def __check_operator_type(operator_entry: Any) -> None:
    if not isinstance(operator_entry, str):
        raise HTTPException(400, f"Operator key type '{type(operator_entry).__name__}' is not allowed. Allowed Operator key type: str")


def __check_filter_operator_value(field_entry: str, operator_entry: OPERATORS, allowed_operators: list[OPERATORS]) -> None:
    if operator_entry not in allowed_operators:
        raise HTTPException(400, f"Operator key '{operator_entry}' is not allowed for the field '{field_entry}'. Allowed keys: {allowed_operators}")


def __check_filter_value_entry(field_entry: str, operator_entry: OPERATORS, value_entry: Any, value_check_function: Callable) -> None:
    if not value_check_function(value_entry):
        raise HTTPException(
            400, f"Value key '{value_entry}' doesn't match the check_function '{value_check_function.__name__}' for the operator '{operator_entry}' and the field '{field_entry}'."
        )


def check_filter_entries(field_entry: Any, operator_entry: Any, value_entry: Any, filter_dictionnary: FilterDictionary) -> None:

    # 1 - Check Field key
    __check_field_type(field_entry)
    __check_filter_field_entry(field_entry, filter_dictionnary.get_allowed_fields())

    # 2 - Check Operator key
    __check_operator_type(operator_entry)
    __check_filter_operator_value(field_entry, operator_entry, filter_dictionnary.get_allowed_operators_by_field(field_entry))

    # 3 - Check Value key
    __check_filter_value_entry(field_entry, operator_entry, value_entry, filter_dictionnary.get_value_check_function_by_field_and_operator(field_entry, operator_entry))


class FilterBase(BaseModel):
    """
    Base class for all filters.
    
    This class provides the basic structure for all filter implementations.
    It includes validation to ensure the filter is properly configured and valid.
    
    Attributes:
        field (Any): The field to apply the filter on
        operator (Any): The operator to use
        value (Any): The value to use
        _filter_dictionary (FilterDictionary | None): Filter dictionary (private)
    """

    field: Any          # each attribute is tagged to Any to allow personalized type checking error message.
    operator: Any       # each attribute is tagged to Any to allow personalized type checking error message.
    value: Any          # each attribute is tagged to Any to allow personalized type checking error message.

    _filter_dictionary: FilterDictionary | None = PrivateAttr(default=None) # private attribute hidden in the request params and instanced in every derived classes.
    _table: DeclarativeBase | None = PrivateAttr(default=None)

    @model_validator(mode="after")
    def check_filter(self) -> 'FilterBase':
        if not self._filter_dictionary:
            raise HTTPException(
                500,
                "To initialize a filter you have to specify a filterDictionary."
            )

        if not self._table:
            raise HTTPException(
                500,
                "To initialize a filter you have to specify a table."
            )

        check_filter_entries(
            self.field, self.operator, self.value, self._filter_dictionary
        )

        return self

    def update_query(self, stmt: Select[Base]) -> Select[Base]:
        field_column: InstrumentedAttribute = getattr(self._table, self.field)
        return stmt.where(operator_functions[self.operator](field_column, self.value))