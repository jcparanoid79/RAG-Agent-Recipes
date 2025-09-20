import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_env: str = os.getenv("APP_ENV", "development")
    debug: bool = os.getenv("DEBUG", "False").lower() == "true"
    log_level: str = os.getenv("LOG_LEVEL", "info")
    google_api_key: str = os.getenv("GOOGLE_API_KEY", "")
    host: str = os.getenv("HOST", "0.0.0.0")
    port: int = int(os.getenv("PORT", 8000))
    workers: int = int(os.getenv("WORKERS", 1))
    
    class Config:
        env_file = ".env"

settings = Settings()