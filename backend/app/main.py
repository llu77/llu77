from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import models, schemas, crud, database, chatbot

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/chat")
def chat(req: schemas.MessageCreate, db: Session = Depends(get_db)):
    crud.create_message(db, role="user", content=req.message)
    reply = chatbot.generate_response(req.message)
    crud.create_message(db, role="bot", content=reply)
    return {"reply": reply}


@app.get("/history", response_model=list[schemas.Message])
def history(db: Session = Depends(get_db)):
    return crud.get_messages(db)
