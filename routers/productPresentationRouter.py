from fastapi import APIRouter
from fastapi.params import Depends, Body
from sqlalchemy import Select
from sqlalchemy.orm import Session

from Dto.responseDtos.productDto import GetProductFiltered
from controller import productController
from database.initialiser import get_connection
from database.tables.productBdd import ProductBdd

productPresentationRouter = APIRouter(
    prefix="/products/presentation",
    tags=["products/presentation"]
)


@productPresentationRouter.post("/without-filters")
def without_filters(product_filter: GetProductFiltered = Body(
        example={}
    ), db: Session = Depends(get_connection), select_stmt: Select[ProductBdd] = Depends(ProductBdd.get_select_stmt)):
    return productController.get_filtered_products(product_filter, db, select_stmt)


@productPresentationRouter.post("/empty-filters")
def empty_filters(product_filter: GetProductFiltered = Body(
        example={
            "filters": [],
        }
    ), db: Session = Depends(get_connection), select_stmt: Select[ProductBdd] = Depends(ProductBdd.get_select_stmt)):
    return productController.get_filtered_products(product_filter, db, select_stmt)


@productPresentationRouter.post("/wrong-field")
def wrong_field(product_filter: GetProductFiltered = Body(
        example={
            "filters": [
                {
                    "field": "name",
                    "operator": "string",
                    "value": "string"
                }
            ],
        }
    ), db: Session = Depends(get_connection), select_stmt: Select[ProductBdd] = Depends(ProductBdd.get_select_stmt)):
    return productController.get_filtered_products(product_filter, db, select_stmt)


@productPresentationRouter.post("/wrong-operator")
def wrong_operator(product_filter: GetProductFiltered = Body(
        example={
            "filters": [
                {
                    "field": "brand",
                    "operator": "string",
                    "value": "string"
                }
            ],
        }
    ), db: Session = Depends(get_connection), select_stmt: Select[ProductBdd] = Depends(ProductBdd.get_select_stmt)):
    return productController.get_filtered_products(product_filter, db, select_stmt)


@productPresentationRouter.post("/wrong-value")
def wrong_value(product_filter: GetProductFiltered = Body(
        example={
            "filters": [
                {
                    "field": "brand",
                    "operator": "IN",
                    "value": "Apple"
                }
            ],
        }
    ), db: Session = Depends(get_connection), select_stmt: Select[ProductBdd] = Depends(ProductBdd.get_select_stmt)):
    return productController.get_filtered_products(product_filter, db, select_stmt)


@productPresentationRouter.post("/simple-filter")
def simple_filter(product_filter: GetProductFiltered = Body(
        example={
            "filters": [
                {
                    "field": "brand",
                    "operator": "IIN",
                    "value": ["SAMsung", "Apple", "Brand"]
                }
            ],
        }
    ), db: Session = Depends(get_connection), select_stmt: Select[ProductBdd] = Depends(ProductBdd.get_select_stmt)):
    return productController.get_filtered_products(product_filter, db, select_stmt)

@productPresentationRouter.post("/duplicate-filters")
def duplicate_filters(product_filter: GetProductFiltered = Body(
        example={
            "filters": [
                {
                    "field": "brand",
                    "operator": "EQ",
                    "value": "Samsung"
                },
                {
                    "field": "brand",
                    "operator": "EQ",
                    "value": "Apple"
                },
            ],
        }
    ), db: Session = Depends(get_connection), select_stmt: Select[ProductBdd] = Depends(ProductBdd.get_select_stmt)):
    return productController.get_filtered_products(product_filter, db, select_stmt)

@productPresentationRouter.post("/multiple-filters")
def multiple_filters(product_filter: GetProductFiltered = Body(
        example={
            "filters": [
                {
                    "field": "brand",
                    "operator": "IN",
                    "value": ["Samsung", "Apple"]
                },
                {
                    "field": "price",
                    "operator": "GT",
                    "value": 400
                },
            ],
        }
    ), db: Session = Depends(get_connection), select_stmt: Select[ProductBdd] = Depends(ProductBdd.get_select_stmt)):
    return productController.get_filtered_products(product_filter, db, select_stmt)