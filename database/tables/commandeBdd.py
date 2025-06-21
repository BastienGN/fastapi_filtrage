from datetime import datetime

from sqlalchemy import String, Float, func
from sqlalchemy.orm import Mapped, mapped_column

from database.tables.base import Base


class CommandeBdd(Base):
    __tablename__ = "commande"

    id: Mapped[int] = mapped_column(primary_key=True)
    client_id: Mapped[int] = mapped_column(nullable=False)
    date_commande: Mapped[datetime] = mapped_column(default=func.now())
    statut: Mapped[str] = mapped_column(String(50))
    total: Mapped[float] = mapped_column(Float)

