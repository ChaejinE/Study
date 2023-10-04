from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import logging

Base = declarative_base()


class SQLAlchemy:
    def __init__(self, app: FastAPI = None, **kwargs) -> None:
        self._engine = None
        self._session = None
        if app is not None:
            self.init_app(app, **kwargs)

    async def init_app(self, app: FastAPI, **kwargs):
        database_url = kwargs.get("DB_URL")
        pool_recycle = kwargs.setdefault("DB_POOL_RECYCLE", 900)
        echo = kwargs.setdefault("DB_ECHO", True)

        self._engine = create_async_engine(
            database_url, echo=echo, pool_recycle=pool_recycle, pool_pre_ping=True
        )

        self._session = sessionmaker(
            autoflush=False, autocommit=False, bind=self._engine, class_=AsyncSession
        )

        @app.on_event("startup")
        async def startup():
            async with self._engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
                logging.info("DB connected")

        @app.on_event("shutdown")
        def shutdown():
            self._session.close_all()
            self._engine.dispose()
            logging.info("DB disconnected")

    async def get_db(self):
        if self._session is None:
            raise Exception("must be called 'init_app'")

        async with self._session() as db_session:
            try:
                yield db_session
            finally:
                await db_session.close()

    @property
    def session(self):
        return self.get_db

    @property
    def engine(self):
        return self._engine


db = SQLAlchemy()
