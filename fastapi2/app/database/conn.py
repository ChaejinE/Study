from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import logging


class SQLAlchemy:
    def __init__(self, app: FastAPI = None, **kwargs) -> None:
        self._engine = None
        self._session = None
        if app is not None:
            self.init_app(app, **kwargs)

    def init_app(self, app: FastAPI, **kwargs):
        database_url = kwargs.get("DB_URL")
        pool_recycle = kwargs.setdefault("DB_POOL_RECYCLE", 900)
        echo = kwargs.setdefault("DB_ECHO", True)

        self._engine = create_engine(
            database_url, echo=echo, pool_recycle=pool_recycle, pool_pre_ping=True
        )
        self._session = sessionmaker(
            autoflush=False, autocommit=False, bind=self._engine
        )

        @app.on_event("startup")
        def startup(self):
            self._engine.connect()
            logging.info("DB connected")

        @app.on_event("shutdonw")
        def shutdown(self):
            self._session.close_all()
            self._engine.dispose()
            logging.info("DB disconnected")

    def get_db(self):
        if self._session is None:
            raise Exception("must be called 'init_app'")
        db_session = None
        try:
            db_session = self._session()
            yield db_session
        finally:
            db_session.close()

    @property
    def session(self):
        return self.get_db

    @property
    def engine(self):
        return self._engine


db = SQLAlchemy()
Base = declarative_base()
