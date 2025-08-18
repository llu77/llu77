from datetime import datetime
from pydantic import BaseModel


class MessageCreate(BaseModel):
    message: str


class Message(BaseModel):
    id: int
    role: str
    content: str
    created_at: datetime

    class Config:
        orm_mode = True
