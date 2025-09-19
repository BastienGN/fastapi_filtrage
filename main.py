from fastapi import FastAPI

from Dto.responseDtos.productDto import ProductDto
from routers.productPresentationRouter import productPresentationRouter
from routers.productRouter import productRouter

app = FastAPI()

# Just as a reminder
bdd_products: list[ProductDto] = [
    ProductDto(id=1, name="Smartphone Galaxy S22", price=799, brand="Samsung"),
    ProductDto(id=2, name="Laptop XPS 13", price=999, brand="Dell"),
    ProductDto(id=3, name="Smartwatch Series 7", price=399, brand="Apple"),
    ProductDto(id=4, name="Tablet Galaxy Tab S7", price=649, brand="Samsung"),
    ProductDto(id=5, name="Wireless Earbuds Pro", price=129, brand="Sony"),
]

app.include_router(productRouter)
app.include_router(productPresentationRouter)