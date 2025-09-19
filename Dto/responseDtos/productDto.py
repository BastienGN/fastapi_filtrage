from pydantic import BaseModel

from Dto.filterDtos.productFilterDtos import ListProductFilter


class ProductDto(BaseModel):
    id: int
    name: str
    price: int
    brand: str

    class Config:
        from_attributes = True


class GetProductFiltered(ListProductFilter):
    pass

