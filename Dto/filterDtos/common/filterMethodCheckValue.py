from datetime import datetime
from typing import Any

class FilterMethodCheckValue:
    """
    Class containing static methods to check value types in filters.
    """

    @staticmethod
    def is_value_str(value_entry: Any) -> bool:
        return isinstance(value_entry, str)

    @staticmethod
    def is_value_int(value_entry: Any) -> bool:
        return isinstance(value_entry, int)

    @staticmethod
    def is_value_list_str(value_entry: Any) -> bool:
        return isinstance(value_entry, list) and all(isinstance(elem, str) for elem in value_entry)

    @staticmethod
    def is_value_list_int(value_entry: Any) -> bool:
        return isinstance(value_entry, list) and all(isinstance(elem, int) for elem in value_entry)

    @staticmethod
    def is_value_datetime_iso(value_entry: Any) -> bool:
        if isinstance(value_entry, str):
            try:
                datetime.strptime(value_entry, "%Y-%m-%dT%H:%M:%S")
                return True
            except ValueError:
                return False
        return False