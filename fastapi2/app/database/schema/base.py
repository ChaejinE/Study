from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession

from datetime import datetime

from database.conn import async_session


class Base(DeclarativeBase):
    pass


class BaseMixin:
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    created_at: Mapped[datetime] = mapped_column(
        nullable=False, default=datetime.utcnow
    )
    updated_at: Mapped[datetime] = mapped_column(
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    def __init__(self):
        self._q = None
        self._session = None
        self.served = None

    def all_columns(self):
        return [
            c
            for c in self.__table__.columns
            if c.primary_key is False and c.name != "created_at"
        ]

    def __hash__(self):
        return hash(self.id)

    @classmethod
    async def create(cls, session: AsyncSession, auto_commit: bool = False, **kwargs):
        obj = cls()

        col_name = None
        for col in obj.all_columns():
            col_name = col.name
            if col_name in kwargs:
                setattr(obj, col_name, kwargs.get(col.name))

        session.add(obj)
        await session.flush()
        if auto_commit:
            await session.commit()
            await session.refresh(obj)

        return obj

    @classmethod
    async def get(cls, session: AsyncSession = None, **kwargs):
        query = select(cls)

        if not session:
            session = async_session()

        for key, val in kwargs.items():
            col = getattr(cls, key)
            query = query.filter(col == val)

        result = await session.execute(query)
        result = result.all()

        if len(result) > 1:
            raise Exception(
                "Only one row is supposed to be returned, but got more than one."
            )

        return result[0] if result else result
