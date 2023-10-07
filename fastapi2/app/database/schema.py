from sqlalchemy import Integer, DateTime, Enum, String, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column

from database.conn import Base

from datetime import datetime


class BaseMixin:
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=datetime.utcnow
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
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


class User(Base, BaseMixin):
    __tablename__ = "users"

    # status: Mapped[Enum] = mapped_column(
    #     Enum("active", "deleted", "blocked"), default="active", name="user_status"
    # )
    email: Mapped[str] = mapped_column(String(length=255), nullable=True)
    pw: Mapped[str] = mapped_column(String(length=2000), nullable=True)
    name: Mapped[str] = mapped_column(String(length=255), nullable=True)
    phone_number: Mapped[str] = mapped_column(
        String(length=20), nullable=True, unique=True
    )
    profile_img: Mapped[str] = mapped_column(String(length=1000), nullable=True)
    # sns_type: Mapped[Enum] = mapped_column(
    #     Enum("FB", "G", "K"), nullable=True, name="sns_platform"
    # )
    marketing_agree: Mapped[bool] = mapped_column(Boolean, nullable=True, default=True)
