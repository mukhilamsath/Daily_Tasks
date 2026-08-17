from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from app.config import settings

# Create database engine
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Configure session maker
SessionLocal = async_sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)

# Base class for database models
Base = declarative_base()

# Dependency to get db session
async def get_db():
    async with SessionLocal() as session:
        try:
            yield session
        finally:
            pass  # context manager closes the session automatically
