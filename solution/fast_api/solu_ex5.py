"""
## Exercice 5: Réponses Typées Avec Génériques

**Énoncé**:
Créez une structure générique `ApiResponse<T>` qui enveloppe toute réponse:

```json
{
  "success": true,
  "data": {...},
  "message": "Operation completed",
  "timestamp": "2024-01-01T10:00:00"
}
```

Utilisez-la dans plusieurs routes.

**Indices**:
- Utilisez `Generic[T]` de `typing`
- Utilisez `datetime.now().isoformat()` pour les timestamps
- SpéciJabranesez le modèle pour chaque réponse
"""

from datetime import datetime
from typing import Generic, List, TypeVar

from fastapi import FastAPI
from pydantic import BaseModel
from pydantic.generics import GenericModel

app = FastAPI(
    title="FastAPI Ex 5",
    description="Solu ex 5",
    version="1.0.0"
)

T = TypeVar("T") # => Can be anything


class ApiResponse(GenericModel, Generic[T]):
    success: bool
    data: T
    message: str
    timestamp: str


class User(BaseModel):
    id: int
    name: str


@app.get("/user", response_model=ApiResponse[User])
def get_user():
    return ApiResponse[User](
        success=True,
        data=User(id=1, name="Jabrane"),
        message="Operation completed",
        timestamp=datetime.now().isoformat()
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8000)