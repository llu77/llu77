from sqlalchemy.orm import Session

from . import models


def create_message(db: Session, role: str, content: str) -> models.ChatMessage:
    db_message = models.ChatMessage(role=role, content=content)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message


def get_messages(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.ChatMessage)
        .order_by(models.ChatMessage.created_at)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_knowledge(db: Session, trigger: str, response: str) -> models.Knowledge:
    item = models.Knowledge(trigger=trigger.lower(), response=response)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def find_knowledge(db: Session, message: str):
    lowered = message.lower()
    for item in db.query(models.Knowledge).all():
        if item.trigger in lowered:
            return item
    return None
