"""
## Exercice 1: Modèle Utilisateur Basique

**Énoncé**:
Créez un modèle Pydantic `User` avec:
- `id`: entier (non modifiable)
- `username`: chaîne (2-50 caractères)
- `email`: email valide
- `age`: entier optionnel (0-150 si fourn
- `is_active`: booléen (par défaut True)

Testez avec une route POST `/users` qui accepte le modèle.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime

app = FastAPI(
    title="FastAPI Pydantic Models",
    description="eX 1",
    version="1.0.0"
)

users = []
next_id = 1


# ============================================================================
# Pydantic Models
# ============================================================================

# Input (POST)
class UserCreate(BaseModel):
    username: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    age: Optional[int] = Field(None, ge=0, le=150)
    is_active: bool = True

# Output
class UserResponse(UserCreate):
    id: int


# ============================================================================
# Endpoints
# ============================================================================

@app.get("/", tags=["Root"])
def root():
    """Root endpoint"""
    return {"message": "FastAPI Pydantic Models Exercices"}


@app.post("/users", response_model=UserResponse, status_code=201, tags=["Users"])
def create_user(user: UserCreate):
    global next_id

    new_user = user.dict()
    new_user["id"] = next_id

    users.append(new_user)
    next_id += 1

    return new_user


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
