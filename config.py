from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv()


class UvicornConfig(BaseSettings):
    PORT: int = 8080
    HOST: str = "0.0.0.0"

    WORKERS: int = 4
    RELOAD_ON_CHANGE: bool = False

    class Config:
        env_prefix = "UVICORN_"


class APPSecrets(BaseSettings):
    JWT_SECRET_KEY: str
    ENCRYPTION_KEY: str

    class Config:
        env_prefix = "SECRETS_"


class DBConfig(BaseSettings):
    HOST: str
    POOL_SIZE: str

    class Config:
        env_prefix = "DB_"


class FrontendConfig(BaseSettings):
    FRONTEND_BASE_URL: str


class CONFIG:
    UVICORN = UvicornConfig()
    SECRETS = APPSecrets()
    DB = DBConfig()
    FRONTEND = FrontendConfig()
