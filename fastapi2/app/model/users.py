from pydantic import BaseModel


class UserRegister(BaseModel):
    email: str = None
    pw: str = None
