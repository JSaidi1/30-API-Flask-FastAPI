"""
## Exercice 2: Validateurs Personnalisés

**Énoncé**:
Créez un modèle `Password` avec validation:
- `password`: au moins 8 caractères, doit contenir minuscule, majuscule, chiffre, symbole
- `confirm_password`: doit égaler `password`

Retournez des erreurs détaillées si la validation échoue.

Exemple:
```bash
# Valide
{"password": "SecurePass123!", "confirm_password": "SecurePass123!"}

# Invalide
{"password": "weak", "confirm_password": "weak"}
# Erreur: "password too short"
```
"""
import re
from fastapi import FastAPI
from pydantic import BaseModel, field_validator, model_validator

app = FastAPI(title="FastAPI Pydantic Models",
            description="ex 2",
            version="1.0.0"
        )


class Password(BaseModel):
    password: str
    confirm_password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str) -> str:
        errors = []

        if len(value) < 8:
            errors.append("password too short (minimum 8 characters)")
        if not re.search(r"[a-z]", value):
            errors.append("password must contain at least one lowercase letter")
        if not re.search(r"[A-Z]", value):
            errors.append("password must contain at least one uppercase letter")
        if not re.search(r"\d", value):
            errors.append("password must contain at least one digit")
        if not re.search(r"[^\w\s]", value):
            errors.append("password must contain at least one symbol")

        if errors:
            raise ValueError(", ".join(errors))

        return value

    @model_validator(mode="after")
    def passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError("confirm_password must match password")
        return self


@app.post("/passwords")
def validate_password(data: Password):
    return {
        "success": True,
        "message": "Password is valid"
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)