from pydantic import BaseModel

class Product(BaseModel):
    id: int
    description: str
    length: int
    engine_type: str
    price_in_eur: float

class ProductInfo(BaseModel):
    id: int
    description: str

class ProductPrice(BaseModel):
    id: int
    price_in_eur: float