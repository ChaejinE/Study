from dataclasses import dataclass, asdict
from os import path, environ

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))


@dataclass
class Config:
    BASE_DIR: str = base_dir
    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True
    DEBUG: bool = False
    TEST_MODE: bool = False
    DB_URL: str = environ.get(
        "DB_URL", "postgresql+asyncpg://postgres:1234@db:5432/postgres"
    )


@dataclass
class LocalConfig(Config):
    TRUSTED_HOSTS = ["*"]
    ALLOW_SITE = ["*"]
    DEBUG: bool = True


@dataclass
class ProdConfig(Config):
    TRUSTED_HOSTS = ["*"]
    ALLOW_SITE = ["*"]


def conf():
    """
    사용할 Config를 설정할 수 있게한다.
    """
    config = dict(prod=ProdConfig, local=LocalConfig)
    return config[environ.get("API_ENV", "local")]()


config = conf()
conf_dict = asdict(config)
