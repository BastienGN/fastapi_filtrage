from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from database.tables.base import Base


class ProductBdd(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    brand: Mapped[str] = mapped_column(String, nullable=False)

