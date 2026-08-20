from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import engine, get_db
from models import Base, Note
from schemas import NoteCreate, NoteUpdate, NoteResponse



Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Notes API",
    description="Day 5 FastAPI CRUD API using SQLite and SQLAlchemy",
    version="1.0.0"
)




@app.post("/notes/", response_model=NoteResponse, status_code=201)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):

    new_note = Note(
        title=note.title,
        content=note.content
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note




@app.get("/notes/", response_model=list[NoteResponse])
def get_notes(db: Session = Depends(get_db)):

    notes = db.query(Note).all()

    return notes




@app.get("/notes/{note_id}", response_model=NoteResponse)
def get_note(note_id: int, db: Session = Depends(get_db)):

    note = db.query(Note).filter(Note.id == note_id).first()

    if note is None:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    return note




@app.put("/notes/{note_id}", response_model=NoteResponse)
def update_note(
    note_id: int,
    note_data: NoteUpdate,
    db: Session = Depends(get_db)
):

    note = db.query(Note).filter(Note.id == note_id).first()

    if note is None:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    note.content = note_data.content

    db.commit()
    db.refresh(note)

    return note



@app.delete("/notes/{note_id}")
def delete_note(
    note_id: int,
    db: Session = Depends(get_db)
):

    note = db.query(Note).filter(Note.id == note_id).first()

    if note is None:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    db.delete(note)
    db.commit()

    return {
        "message": "Note deleted successfully"
    }