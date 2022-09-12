from pydantic import BaseSettings

class Settings(BaseSettings):
    DB_USR: str
    DB_PWD: str
    DB_IP: str
    DB_PORT: str
    DB_SCHEME: str
    
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTE: int
    
    class Config:
        env_file = '.env', '.env.local'
        env_file_encoding = 'utf-8'