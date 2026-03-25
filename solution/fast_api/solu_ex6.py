"""
## Exercice 6: Configuration Avec Pydantic Settings

**Énoncé**:
Créez un modèle `Settings` pour configurer l'API:
- `app_name`: nom de l'app
- `debug`: mode debug (défaut False)
- `database_url`: URL de connexion à la base
- `secret_key`: clé secrète
- `api_v1_prefix`: préfixe des routes (défaut "/api/v1")

Chargez les valeurs depuis des variables d'environnement.

**Indices**:
- Héritez de `BaseSettings` (Pydantic v2) ou `Settings` (Pydantic v1)
- Utilisez `Field(..., env='VAR_NAME')` pour mapper les variables
- Créez une instance singleton au démarrage
"""

from pathlib import Path
import sys

from fastapi import FastAPI
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent

# print("BASE_DIR =", BASE_DIR)
# sys.exit(0)

class Settings(BaseSettings):
    app_name: str = Field(..., alias="APP_NAME")
    debug: bool = Field(False, alias="DEBUG")
    database_url: str = Field(..., alias="DATABASE_URL")
    secret_key: str = Field(..., alias="SECRET_KEY")
    api_v1_prefix: str = Field("/api/v1", alias="API_V1_PREFIX")

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()

print(settings.model_dump())



app = FastAPI(
    title=settings.app_name,
    debug=settings.debug
)


@app.get(f"{settings.api_v1_prefix}/info")
def get_info():
    return {
        "app_name": settings.app_name,
        "debug": settings.debug,
        "database_url": settings.database_url,
        "api_v1_prefix": settings.api_v1_prefix
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8000)