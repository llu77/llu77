from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from .database import Base


class ChatMessage(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Knowledge(Base):
    """Stores user-taught trigger/response pairs for lightweight learning."""

    __tablename__ = "knowledge"

    id = Column(Integer, primary_key=True, index=True)
    trigger = Column(String, nullable=False, unique=True)
    response = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
