"""

## Exercice 4: Validation Avec Listes

**Énoncé**:
Créez un modèle `Commande` (Order) contenant:
- `order_id`: identifiant unique (généralement UUID)
- `customer_email`: email valide
- `items`: liste de produits avec:
  - `product_id`: entier
  - `quantity`: entier (>= 1)
  - `price`: float (> 0)
- `total`: float (calculé ou fourni)

Validez que la liste n'est pas vide.

**Indices**:
- Utilisez `List[ItemModel]` pour la liste
- Validez la longueur minimale: `min_length=1`
- Optionnel: calculez le total automatiquement
"""

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field, UUID4, computed_field
from typing import List

app = FastAPI()


#--- Item
class Item(BaseModel):
    product_id: int
    quantity: int = Field(..., ge=1)
    price: float = Field(..., gt=0)


#--- Base
class OrderBase(BaseModel):
    order_id: UUID4
    customer_email: EmailStr
    items: List[Item] = Field(..., min_length=1)


#--- Create DTO
class OrderCreate(OrderBase):
    pass


#--- Read DTO (avec total calculé)
class OrderRead(OrderBase):

    @computed_field
    @property
    def total(self) -> float:
        return sum(item.quantity * item.price for item in self.items)


#--- Route
@app.post("/orders", response_model=OrderRead)
def create_order(order: OrderCreate):
    return OrderRead(**order.model_dump())


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8000)

