from fastapi import APIRouter, Body, Depends
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


@productPresentationRouter.post(
    "/without-filters",
    summary="Get all products",
    description="Retrieves a full list of all products with no filters applied."
)
def without_filters(product_filter: GetProductFiltered = Body(
        example={}
    ), db: Session = Depends(get_connection), select_stmt: Select[ProductBdd] = Depends(ProductBdd.get_select_stmt)):
    return productController.get_filtered_products(product_filter, db, select_stmt)


@productPresentationRouter.post(
    "/empty-filters",
    summary="Get all products with an empty filter array",
    description="Retrieves all products by passing an empty filter array in the request body. This is another way to request all products without applying any filters."
)
def empty_filters(product_filter: GetProductFiltered = Body(
        example={
            "filters": [],
        }
    ), db: Session = Depends(get_connection), select_stmt: Select[ProductBdd] = Depends(ProductBdd.get_select_stmt)):
    return productController.get_filtered_products(product_filter, db, select_stmt)


@productPresentationRouter.post(
    "/wrong-field",
    summary="Attempt to filter by a non-existent field",
    description="Tests the API's validation by attempting to filter products using a field name that does not exist in the product table. The validation successfully returned an error."
)
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


@productPresentationRouter.post(
    "/wrong-operator",
    summary="Attempt to filter with an incorrect operator",
    description="Tests the API's validation by using an operator that is not supported for the specified field. The validation successfully returned an error."
)
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


@productPresentationRouter.post(
    "/wrong-value",
    summary="Attempt to filter with a value of the wrong type",
    description="Tests the API's validation by using a value that is not supported for the specified field and operator. In this case using a str when a list is expected. The validation successfully returned an error."
)
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


@productPresentationRouter.post(
    "/simple-filter",
    summary="Apply a single filter",
    description="Filters products based on a single condition, such as filtering by brand using the 'IN' operator with a list of brands."
)
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


@productPresentationRouter.post(
    "/duplicate-filters",
    summary="Filter using duplicate fields",
    description="This endpoint demonstrates how the system handles multiple filters on the same field. The validation successfully returned an error."
)
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


@productPresentationRouter.post(
    "/multiple-filters",
    summary="Apply multiple distinct filters simultaneously",
    description="Combines multiple filters on different fields to narrow down the product selection. This example filters by both 'brand' and 'price' at the same time."
)
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