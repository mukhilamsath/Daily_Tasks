from contextlib import asynccontextmanager
from typing import List
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud, models, schemas
from app.database import engine, Base, get_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Automatically create the database tables on startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title="FastAPI PostgreSQL App",
    description="A simple FastAPI application with a PostgreSQL backend using async SQLAlchemy",
    version="1.0.0",
    lifespan=lifespan
)

@app.get("/", tags=["General"])
def read_root():
    return {"message": "Welcome to the FastAPI + PostgreSQL application!"}

@app.post("/items/", response_model=schemas.ItemResponse, status_code=status.HTTP_201_CREATED, tags=["Items"])
async def create_item(item: schemas.ItemCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_item(db=db, item=item)

@app.get("/items/", response_model=List[schemas.ItemResponse], tags=["Items"])
async def read_items(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    items = await crud.get_items(db=db, skip=skip, limit=limit)
    return items

@app.get("/items/{item_id}", response_model=schemas.ItemResponse, tags=["Items"])
async def read_item(item_id: int, db: AsyncSession = Depends(get_db)):
    db_item = await crud.get_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.patch("/items/{item_id}", response_model=schemas.ItemResponse, tags=["Items"])
async def update_item(item_id: int, item_update: schemas.ItemUpdate, db: AsyncSession = Depends(get_db)):
    db_item = await crud.update_item(db=db, item_id=item_id, item_update=item_update)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.delete("/items/{item_id}", response_model=schemas.ItemResponse, tags=["Items"])
async def delete_item(item_id: int, db: AsyncSession = Depends(get_db)):
    db_item = await crud.delete_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
