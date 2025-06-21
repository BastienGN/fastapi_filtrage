from sqlalchemy import Select, select
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):

    @classmethod
    def get_select_stmt(cls) -> Select:
        return select(cls)

