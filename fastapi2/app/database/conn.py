from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from common.config import conf_dict

engine = create_async_engine(
    url=conf_dict.get("DB_URL"),
    echo=conf_dict.setdefault("DB_ECHO", True),
    pool_recycle=conf_dict.setdefault("DB_POOL_RECYCLE", 900),
    pool_pre_ping=True,
)


async def get_async_session() -> AsyncSession:
    engine = create_async_engine(
        url=conf_dict.get("DB_URL"),
        echo=conf_dict.setdefault("DB_ECHO", True),
        pool_recycle=conf_dict.setdefault("DB_POOL_RECYCLE", 900),
        pool_pre_ping=True,
    )

    async_session = async_sessionmaker(engine)

    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()
