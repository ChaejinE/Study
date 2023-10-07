from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

from common.config import conf_dict

Base = declarative_base()

engine = create_async_engine(
    url=conf_dict.get("DB_URL"),
    echo=conf_dict.setdefault("DB_ECHO", True),
    pool_recycle=conf_dict.setdefault("DB_POOL_RECYCLE", 900),
    pool_pre_ping=True,
)

session = async_sessionmaker(engine)


async def get_db() -> AsyncSession:
    async with engine.connect() as conn:
        await conn.run_sync(Base.metadata.create_all)

    db = session()
    try:
        yield db
    finally:
        await db.close()
