from sqlalchemy import String, Boolean
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import Mapped, mapped_column

from schema.base import Base, BaseMixin


class User(Base, BaseMixin):
    __tablename__ = "users"

    user_status: Mapped[ENUM] = mapped_column(
        ENUM("active", "deleted", "blocked", name="user_status"),
        default="active",
    )
    email: Mapped[str] = mapped_column(String(length=255), nullable=True)
    pw: Mapped[str] = mapped_column(String(length=2000), nullable=True)
    name: Mapped[str] = mapped_column(String(length=255), nullable=True)
    phone_number: Mapped[str] = mapped_column(
        String(length=20), nullable=True, unique=True
    )
    profile_img: Mapped[str] = mapped_column(String(length=1000), nullable=True)
    sns_type: Mapped[ENUM] = mapped_column(
        ENUM("FB", "G", "K", name="sns_type"),
        nullable=True,
    )
    marketing_agree: Mapped[bool] = mapped_column(Boolean, nullable=True, default=True)
