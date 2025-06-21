
from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy import Select
from sqlalchemy.orm import Session

from Dto.responseDtos.commandeDtoS import GetCommandeFiltered
from Dto.responseDtos.productDto import ProductDto, GetProductFiltered
from controller import productController
from database.initialiser import get_connection
from database.tables.productBdd import ProductBdd

app = FastAPI()

bdd_products: list[ProductDto] = [
    ProductDto(id=1, name="Smartphone Galaxy S22", price=799, brand="Samsung"),
    ProductDto(id=2, name="Laptop XPS 13", price=999, brand="Dell"),
    ProductDto(id=3, name="Smartwatch Series 7", price=399, brand="Apple"),
    ProductDto(id=4, name="Tablet Galaxy Tab S7", price=649, brand="Samsung"),
    ProductDto(id=5, name="Wireless Earbuds Pro", price=129, brand="Sony"),
]


@app.post("/create")
def create_products(db: Session = Depends(get_connection)):
    for p in bdd_products:
        db.add(ProductBdd(id=p.id, name=p.name, price=p.price, brand=p.brand))

    db.commit()


@app.get("/all_products", response_model=list[ProductDto])
def get_all_products(db: Session = Depends(get_connection)) -> list[ProductDto]:
    return productController.get_all_products(db)


@app.post("/products")
def get_products(product_filter: GetProductFiltered, db: Session = Depends(get_connection),select_stmt: Select[ProductBdd] = Depends(ProductBdd.get_select_stmt) ):
    return productController.get_filtered_products(product_filter, db, select_stmt)

@app.post("/commandes")
def get_commandes(commande_filter: GetCommandeFiltered, db: Session = Depends(get_connection)):
    return None