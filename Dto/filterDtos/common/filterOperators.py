from enum import Enum


class OPERATORS(str, Enum):
    """
    Class to enumerate each possible operators.
    
    This enum defines all available operators that can be used in filters.
    Each operator has a specific meaning and use case.
    """

    EQUAL = "eq"        # exactly this value
    GT = "gt"           # greater than this value (excluded)
    LT = "lt"           # lesser than this value (excluded)
    IN = "in"           # exactly one of these values
    BETWEEN = "between" # between two bounds (included)

    def __repr__(self):
        return f"{self.value}"
