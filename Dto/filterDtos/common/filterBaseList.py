from fastapi import HTTPException
from pydantic import BaseModel, model_validator
from sqlalchemy import Select

from Dto.filterDtos.common.filterBase import FilterBase
from database.tables.base import Base


class FilterBaseList(BaseModel):
    """
    Class to handle a list of filters (mainly the unicity of filter on each Field key).
    
    This class ensures that there are no duplicate filters on the same field.
    It provides validation to maintain filter uniqueness across the list.
    
    Attributes:
        filters (list[FilterBase]): List of filters to apply
    """

    filters: list[FilterBase]

    @model_validator(mode="after")
    def check_unicity_filter(self) -> 'FilterBaseList':
        if self.filters:
            encountered_filters: set[str] = set()
            for current_filter in self.filters:
                if current_filter.field in encountered_filters:
                    raise HTTPException(
                        400,
                        f"You can only have one filter apply on one of each available field. Too much filters on '{current_filter.field}' field.",
                    )
                else:
                    encountered_filters.update([current_filter.field])
        return self

    def update_query(self, stmt: Select[Base]) -> Select[Base]:
        for current_filter in self.filters:
            stmt = current_filter.update_query(stmt)
        return stmt
