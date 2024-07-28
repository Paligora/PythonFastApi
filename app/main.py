from typing import List
from fastapi import FastAPI, HTTPException, status, Response
from app.models import ProductPrice, Product, ProductInfo

app = FastAPI()

productsList: List[Product]  = [
    Product(id= 1, description='Skoda Octavia IV 2.0 TDI', length=4702, engine_type='diesel', price_in_eur= 28000),
    Product(id= 2, description='Volkswagen Golf 1.5 TSI', length=4650, engine_type='petrol', price_in_eur= 31500),
    Product(id= 3, description='Tesla model s', length=4720, engine_type='electric', price_in_eur= 45000)
]

@app.get("/get_products")
def get_products():
    products: List[ProductInfo] = []
    for product in productsList:
        products.append(ProductInfo(id=product.id, description=product.description))

    return products

@app.get("/get_products/{id}")
def get_product(id: int):
    product = find_product(id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Product with ID {id} not found")
    return product

@app.post("/set_price")
def set_price(price: ProductPrice):
    product = find_product(price.id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Product with ID {id} not found")
    
    product.price_in_eur = price.price_in_eur
    return Response(status_code=200)


def find_product(id: int):
    for p in productsList:
        if p.id == id:
            return p