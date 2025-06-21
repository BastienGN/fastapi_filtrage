from datetime import datetime

from pydantic import BaseModel

from Dto.filterDtos.commandeFilterDtos import CommandeFilter


class CommandeDto(BaseModel):
    id: int
    client_id: int
    date_commande: datetime
    statut: str
    total: float

    class Config:
        from_attributes = True


class GetCommandeFiltered(BaseModel):
    filters: list[CommandeFilter] | None
