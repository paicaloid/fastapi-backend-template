from pydantic import BaseSettings, BaseModel

class Settings(BaseSettings):
    DB_USR: str
    DB_PWD: str
    DB_IP: str
    DB_PORT: str
    DB_SCHEME: str
    
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTE: int
    
    authjwt_cookie_access_expires_second: int
    authjwt_algorithm: str
    authjwt_secret_key: str
    authjwt_cookie_secure: bool
    authjwt_cookie_csrf_protect: bool

    MLFLOW_URL: str
    S3_URL: str
    S3_ACCESS_KEY: str
    S3_SECRET_KEY: str
    S3_REGION: str
    
    class Config:
        env_file = '.env.local'
        env_file_encoding = 'utf-8'