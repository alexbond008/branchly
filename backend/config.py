from typing import Optional
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Database
    SUPABASE_URL: str
    SUPABASE_KEY: str
    
    # OpenAI
    OPENAI_API_KEY: str
    
    # Server
    PORT: int = 8000
    HOST: str = "0.0.0.0"
    
    class Config:
        env_file = ".env"

settings = Settings()