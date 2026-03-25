"""
## Exercice 7: Validation Conditionnelle

**Énoncé**:
Créez un modèle `Événement` avec:
- `type`: "online" ou "offline"
- `title`: titre (requis)
- `location`: obligatoire si type="offline", sinon facultatif
- `url`: obligatoire si type="online", sinon facultatif
- `max_participants`: entier (>= 1)

**Indices**:
- Utilisez `model_validator` pour la logique conditionnelle
- Accédez à `self.type` pour vérifier le type
- Levez `ValueError` si la validation échoue
"""
from fastapi import FastAPI
from pydantic import BaseModel, Field, model_validator
from typing import Literal

app = FastAPI(
    title="FastAPI Ex 7",
    description="Solu ex 7",
    version="1.0.0"
)

class Event(BaseModel):
    type: Literal["online", "offline"]
    title: str
    location: str | None = None
    url: str | None = None
    max_participants: int = Field(..., ge=1)

    @model_validator(mode="after")
    def check_fields(self):
        if self.type == "online":
            if not self.url:
                raise ValueError("url is required for online events")

        if self.type == "offline":
            if not self.location:
                raise ValueError("location is required for offline events")

        return self
    
@app.post("/events")
def create_event(event: Event):
    return event


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8000)