# Filter System Documentation

## Overview

This documentation explains how to create and use filters in the system. The filter system is designed to be type-safe and flexible, allowing for easy validation of filter values.

## Creating a New Filter Type

### 1. Define a Filter Dictionary

First, create a dictionary that defines the allowed fields, operators, and their corresponding value check methods:

```python
from typing import Callable

from Dto.filterDtos.common.filterOperators import OPERATORS
from Dto.filterDtos.common.filterMethodCheckValue import FilterMethodCheckValue

user_filter_dictionary: dict[str, dict[OPERATORS, Callable]] = {
    "name": {
        OPERATORS.EQUAL: FilterMethodCheckValue.is_value_str,
        OPERATORS.IN: FilterMethodCheckValue.is_value_list_str
    },
    "age": {
        OPERATORS.EQUAL: FilterMethodCheckValue.is_value_int,
        OPERATORS.GREATER_THAN: FilterMethodCheckValue.is_value_int,
        OPERATORS.BETWEEN: FilterMethodCheckValue.is_value_list_int
    },
    "created_at": {
        OPERATORS.EQUAL: FilterMethodCheckValue.is_value_datetime_iso,
        OPERATORS.BETWEEN: FilterMethodCheckValue.is_value_list_str
    }
}
```

### 2. Create a Filter Class

Create a class that inherits from `FilterBase` and set the filter dictionary:

```python
from pydantic import PrivateAttr

from Dto.filterDtos.common.filterBase import FilterBase
from Dto.filterDtos.common.filterDictionary import FilterDictionary


class UserFilter(FilterBase):
    _filter_dictionary: FilterDictionary = PrivateAttr(default=FilterDictionary(user_filter_dictionary))
```

### 3. Create a Filter List Class

Create a class to handle multiple filters:

```python
from Dto.filterDtos.common.filterBaseList import FilterBaseList


class UserFilterList(FilterBaseList):
    filters: list[UserFilter]
```

### 4. Resume

```python
from typing import Callable

from pydantic import PrivateAttr

from Dto.filterDtos.common.filterBase import FilterBase
from Dto.filterDtos.common.filterBaseList import FilterBaseList
from Dto.filterDtos.common.filterMethodCheckValue import FilterMethodCheckValue
from Dto.filterDtos.common.filterDictionary import FilterDictionary
from Dto.filterDtos.common.filterOperators import OPERATORS

user_filter_dictionary: dict[str, dict[OPERATORS, Callable]] = {
    "name": {
        OPERATORS.EQUAL: FilterMethodCheckValue.is_value_str,
        OPERATORS.IN: FilterMethodCheckValue.is_value_list_str
    },
    "age": {
        OPERATORS.EQUAL: FilterMethodCheckValue.is_value_int,
        OPERATORS.GREATER_THAN: FilterMethodCheckValue.is_value_int,
        OPERATORS.BETWEEN: FilterMethodCheckValue.is_value_list_int
    },
    "created_at": {
        OPERATORS.EQUAL: FilterMethodCheckValue.is_value_datetime_iso,
        OPERATORS.BETWEEN: FilterMethodCheckValue.is_value_list_str
    }


class UserFilter(FilterBase):
    _filter_dictionary: FilterDictionary = PrivateAttr(default=FilterDictionary(user_filter_dictionary))


class UserFilterList(FilterBaseList):
    filters: list[UserFilter]
```

## Go Further

This section will explain every classes involved in the filter system

### 1. FilterDictionary

Class to define the dictionary needed to check if the filter validity.

This class provides methods to:
- Get all allowed fields for filtering
- Get allowed operators for a specific field
- Get the value check function for a specific field and operator combination

### 2. FilterOperators

Class to enumerate each possible operators.

This enum defines all available operators that can be used in filters.
Each operator has a specific meaning and use case.

### 3. FilterCheckValueMethods

Class containing static methods to check value types in filters.

### 4. FilterBase

Base class for all filters.

This class provides the basic structure for all filter implementations.
It includes validation to ensure the filter is properly configured and valid.

### 5. FilterBaseList

Class to handle a list of filters (mainly the unicity of filter on each Field key).

This class ensures that there are no duplicate filters on the same field.
It provides validation to maintain filter uniqueness across the list.


## Extend the filter system

There is three ways to extend the filter system:

- Create a new XXXFilter et a new XXXFilterList (see 'Creating a New Filter Type' section) that will create a new filter usable with current operators and checkValueMethods.
- Create a new operators.
- Create a new checkValueMethod

### 1. Creating a New Filter Type

The main and most procedure, see 'Creating a New Filter Type' section.

### 2. Creating a New Operator

As reminder Operators are used to check is the operator field correspond to one of the allowed one in the filterDictionary of a Filter.

To create a new operator you have to add a value in the Enum and explain (please) the utility for this.

```python
LTE = "lte" # lower or equal than (<=)
```

### 3. Creating a New CheckValueMethod

As reminder checkValueMethods are used to check if the value field correspond to a certain criteria. 

For exemple I want a filter on a brand, in the database the brand is stored as VARCHAR, that correspond to a str value in python. 

So if we want each database occurrences with the brand column equal to value we use in the filter we have to check it and use the following function:

```python
@staticmethod
def is_value_str(value_entry: Any) -> bool:
    return isinstance(value_entry, str)
```

if we want each database occurrences with the brand column value in a list of brands we have to use the following function:

```python
@staticmethod
def is_value_list_str(value_entry: Any) -> bool:
    return isinstance(value_entry, list) and all(isinstance(elem, str) for elem in value_entry)
```

To create a new checkValueMethod we just have to create a new function, For example we want to check if the value entry is an email we could create:

```python
import re

def is_value_email(value_entry: Any) -> bool:
    
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, value_entry):
        return True
    else:
        return False
```

This new function can now being used in a filterDictionary and this function will be triggered in the __check_filter_value_entry Filter check method.