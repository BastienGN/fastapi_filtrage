from enum import Enum
from typing import Callable


class OPERATORS(str, Enum):
    """
    Class to enumerate each possible operators.
    
    This enum defines all available operators that can be used in filters.
    Each operator has a specific meaning and use case.
    """

    EQUAL = "EQ"        # exactly this value
    GREATER_THAN = "GT" # greater than this value (excluded)
    LESSER_THAN = "LT"  # lesser than this value (excluded)
    IN = "IN"           # exactly one of these values
    BETWEEN = "BETWEEN" # between two bounds (included)

    def __repr__(self):
            return f"{self.value}"


# Maps each operator to its corresponding SQLAlchemy filtering function
operator_functions: dict[str, Callable] = {
    OPERATORS.EQUAL: lambda col, val: col == val,
    OPERATORS.GREATER_THAN: lambda col, val: col > val,
    OPERATORS.LESSER_THAN: lambda col, val: col < val,
    OPERATORS.IN: lambda col, val: col.in_(val),
    OPERATORS.BETWEEN: lambda col, val: col.between(val[0], val[1]),
}
