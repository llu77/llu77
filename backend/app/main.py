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
    reply = chatbot.generate_response(req.message, db)
    crud.create_message(db, role="bot", content=reply)
    return {"reply": reply}


@app.post("/teach", response_model=schemas.Knowledge)
def teach(req: schemas.KnowledgeCreate, db: Session = Depends(get_db)):
    return crud.create_knowledge(db, trigger=req.trigger, response=req.response)


@app.get("/history", response_model=list[schemas.Message])
def history(db: Session = Depends(get_db)):
    return crud.get_messages(db)
