from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    sqlite_database_url: str
    secret_key: str

    class Config:
        env_file = ".env" 
        case_sensitive = False  

settings = Settings()