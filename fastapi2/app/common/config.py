from dataclasses import dataclass
from os import path, environ
from typing import List

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))

class Config:
    BASE_DIR: str = base_dir
    DB_POOL_RECYCLE: int = 900