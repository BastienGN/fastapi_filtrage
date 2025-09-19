from enum import Enum
from typing import Callable

from sqlalchemy.sql.functions import func


class OPERATORS(str, Enum):
    """
    Class to enumerate each possible operators.
    
    This enum defines all available operators that can be used in filters.
    Each operator has a specific meaning and use case.
    """

    EQUAL = "EQ"        # exactly this value
                        # Accepted values: int | str
    IEQUAL = "IEQ"      # exactly this value without case sensitivity
                        # Accepted values: str
    GREATER_THAN = "GT" # greater than this value (excluded)
                        # Accepted values: int
    LESSER_THAN = "LT"  # lesser than this value (excluded)
                        # Accepted values: int
    IN = "IN"           # exactly one of these values
                        # Accepted values: str
    IIN = "IIN"         # exactly one of these values without case sensitivity
                        # Accepted values: str
    BETWEEN = "BETWEEN" # between two bounds (included)
                        # Accepted values: int

    def __repr__(self):
            return f"{self.value}"


# Maps each operator to its corresponding SQLAlchemy filtering function
operator_functions: dict[str, Callable] = {
    OPERATORS.EQUAL: lambda col, val: col == val,
    OPERATORS.IEQUAL: lambda col, val: func.lower(col) == val.lower(),
    OPERATORS.GREATER_THAN: lambda col, val: col > val,
    OPERATORS.LESSER_THAN: lambda col, val: col < val,
    OPERATORS.IN: lambda col, val: col.in_(val),
    OPERATORS.IIN: lambda col, val: func.lower(col).in_([v.lower() for v in val]),
    OPERATORS.BETWEEN: lambda col, val: col.between(val[0], val[1]),
}
