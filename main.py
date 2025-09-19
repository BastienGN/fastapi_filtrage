from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.orm import Session

from Dto.responseDtos.productDto import ProductDto
from database.initialiser import get_connection
from database.tables.productBdd import ProductBdd
from routers.productPresentationRouter import productPresentationRouter
from routers.productRouter import productRouter

app = FastAPI()

bdd_products: list[ProductDto] = [
    ProductDto(id=1, name="Smartphone Galaxy S22", price=799, brand="Samsung"),
    ProductDto(id=2, name="Laptop XPS 13", price=999, brand="Dell"),
    ProductDto(id=3, name="Smartwatch Series 7", price=399, brand="Apple"),
    ProductDto(id=4, name="Tablet Galaxy Tab S7", price=649, brand="Samsung"),
    ProductDto(id=5, name="Wireless Earbuds Pro", price=129, brand="Sony"),
]

app.include_router(productRouter)
app.include_router(productPresentationRouter)

@app.post("/create")
def create_products(db: Session = Depends(get_connection)):
    for p in bdd_products:
        db.add(ProductBdd(id=p.id, name=p.name, price=p.price, brand=p.brand))

    db.commit()