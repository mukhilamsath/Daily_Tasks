from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import Base, engine, get_db
from models import Note
from schemas import NoteCreate, NoteUpdate, NoteResponse


app = FastAPI(
    title="Notes API",
    description="Async FastAPI CRUD API using SQLite and SQLAlchemy",
    version="1.0.0"
)


@app.on_event("startup")
async def create_tables():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)


@app.post("/notes/", response_model=NoteResponse, status_code=201)
async def create_note(note_data: NoteCreate, db: AsyncSession = Depends(get_db)):

    new_note = Note(
        title=note_data.title,
        content=note_data.content
    )

    db.add(new_note)
    await db.commit()
    await db.refresh(new_note)

    return new_note


@app.get("/notes/", response_model=list[NoteResponse])
async def get_notes(db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(Note))

    notes = result.scalars().all()

    return notes


@app.get("/notes/{note_id}", response_model=NoteResponse)
async def get_note(note_id: int, db: AsyncSession = Depends(get_db)):

    result = await db.execute(
        select(Note).where(Note.id == note_id)
    )

    note = result.scalar_one_or_none()

    if note is None:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    return note


@app.put("/notes/{note_id}", response_model=NoteResponse)
async def update_note(note_id: int, note_data: NoteUpdate, db: AsyncSession = Depends(get_db)):

    result = await db.execute(
        select(Note).where(Note.id == note_id)
    )

    note = result.scalar_one_or_none()

    if note is None:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    note.content = note_data.content

    await db.commit()
    await db.refresh(note)

    return note


@app.delete("/notes/{note_id}")
async def delete_note(note_id: int, db: AsyncSession = Depends(get_db)):

    result = await db.execute(
        select(Note).where(Note.id == note_id)
    )

    note = result.scalar_one_or_none()

    if note is None:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    await db.delete(note)
    await db.commit()

    return {
        "message": "Note deleted successfully"
    }