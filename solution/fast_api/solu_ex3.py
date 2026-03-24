"""
## Exercice 3: Modèles Imbriqués

**Énoncé**:
Créez une structure pour un `Produit` contenant:
- `name`: nom du produit
- `price`: prix (> 0)
- `category`: catégorie (énumération: ELECTRONICS, CLOTHING, FOOD, OTHER)
- `stock`: entier (>= 0)
- `supplier`: objet Pydantic avec:
  - `name`: nom du fournisseur
  - `email`: email du fournisseur
  - `phone`: téléphone (optionnel)
"""
from enum import Enum
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field

app = FastAPI(title="FastAPI Pydantic Models",
            description="ex 3",
            version="1.0.0"
        )

class Category(str, Enum):
    ELECTRONICS = "ELECTRONICS"
    CLOTHING = "CLOTHING"
    FOOD = "FOOD"
    OTHER = "OTHER"

class Supplier(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None

class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0)
    category: Category
    stock: int = Field(..., ge=0)
    supplier: Supplier


@app.post("/products")
def create_product(product: Product):
    return {
        "message": "Product created",
        "product": product
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)


