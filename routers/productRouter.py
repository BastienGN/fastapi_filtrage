from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy import Select
from sqlalchemy.orm import Session

from Dto.responseDtos.productDto import GetProductFiltered, ProductDto
from controller import productController
from database.initialiser import get_connection
from database.tables.productBdd import ProductBdd

productRouter = APIRouter(
    prefix="/products",
    tags=["products"]
)


@productRouter.post("")
def get_products(product_filter: GetProductFiltered, db: Session = Depends(get_connection),select_stmt: Select[ProductBdd] = Depends(ProductBdd.get_select_stmt) ):
    return productController.get_filtered_products(product_filter, db, select_stmt)


@productRouter.get("/all_products", response_model=list[ProductDto])
def get_all_products(db: Session = Depends(get_connection)) -> list[ProductDto]:
    return productController.get_all_products(db)
