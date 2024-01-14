import datetime

from pydantic import BaseModel, validator
from domain.answer.answer_schema import Answer
from domain.user.user_schema import User
from typing import Optional


class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    answers: list[Answer] = []
    user: Optional[User]

    class Config:
        orm_mode = True


class QuestionCreate(BaseModel):
    subject: str
    content: str

    @validator("subject", "content")
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("빈 값 허용 안됨")
        return v


class QuestionList(BaseModel):
    total: int = 0
    question_list: list[Question] = []
