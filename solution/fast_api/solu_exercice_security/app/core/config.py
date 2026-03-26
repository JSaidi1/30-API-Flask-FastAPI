# SECRET_KEY = "change-me-in-real-life-super-secret-key-v5"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30
# DATABASE_PATH = "data/app.db"


from pathlib import Path
import sys
from typing import Optional
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

CURRENT_DIR = Path(__file__).resolve().parent
ENV_FILE_PATH = CURRENT_DIR.parent.parent / ".env.example"

# print("ENV_FILE_PATH :", ENV_FILE_PATH)
# sys.exit()

class Settings(BaseSettings):
    app_name: str = Field(..., alias="APP_NAME")                                # obligatoire
    debug: bool = Field(False, alias="DEBUG")
    database_url: Optional[str] = Field(None, alias="DATABASE_URL")
    database_path: str = Field(..., alias="DATABASE_PATH")                      # obligatoire       
    secret_key: str = Field(..., alias="SECRET_KEY") 
    access_token_exp_mn: int = Field(..., alias="ACCESS_TOKEN_EXPIRE_MINUTES")  # obligatoire
    algorithm: str = Field(..., alias="ALGORITHM")                              # obligatoire
    api_v1_prefix: str = Field("/api/v1", alias="API_V1_PREFIX")
    log_level: str = Field("INFO", alias="LOG_LEVEL")

    model_config = SettingsConfigDict(
        env_file=ENV_FILE_PATH,
        case_sensitive=False,
        extra="ignore"
    )


settings = Settings()

if __name__ == "__main__":
    print(settings.app_name)
    print(settings.debug)
    print(settings.database_url)
    print(settings.database_path)
    print(settings.secret_key)
    print(settings.access_token_exp_mn)
    print(settings.api_v1_prefix)
    print(settings.log_level)