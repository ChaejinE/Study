from pydantic import BaseModel
from enum import Enum
from typing import List, Optional


class UserRegister(BaseModel):
    email: str = None
    pw: str = None


class SnsType(str, Enum):
    email: str = "email"
    facebook: str = "facebook"
    google: str = "google"
    kakao: str = "kakao"


class Token(BaseModel):
    Authorization: str = None


class EmailRecipients(BaseModel):
    name: str
    email: str


class SendEmail(BaseModel):
    email_to: List[EmailRecipients] = None


class UserToken(BaseModel):
    id: int
    email: Optional[str] = None
    name: Optional[str] = None
    phone_number: Optional[str] = None
    profile_img: Optional[str] = None
    sns_type: Optional[str] = None

    class Config:
        from_attributes = True


class UserMe(BaseModel):
    id: int
    email: Optional[str] = None
    name: Optional[str] = None
    phone_number: Optional[str] = None
    profile_img: Optional[str] = None
    sns_type: Optional[str] = None

    class Config:
        from_attributes = True
