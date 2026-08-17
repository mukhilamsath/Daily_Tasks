# FastAPI with PostgreSQL Backend

A simple FastAPI web application with a PostgreSQL database backend, using asynchronous SQLAlchemy with the `asyncpg` driver.

## Project Structure

```text
├── app/
│   ├── config.py      # Environment variables & configuration validation
│   ├── database.py    # Database connection logic (SQLAlchemy async)
│   ├── models.py      # SQLAlchemy DB models (Item table definition)
│   ├── schemas.py     # Pydantic validation & response schemas
│   ├── crud.py        # Database CRUD query operations
│   └── main.py        # Main entrypoint, endpoints, and lifespan hook
├── .env               # Environment configuration file
├── docker-compose.yml # PostgreSQL database container runner
├── requirements.txt   # Python dependency list
└── README.md          # Project instructions
```

## Running the Application

### 1. Database Setup

If you have Docker installed, you can spin up the PostgreSQL database in the background:

```bash
docker-compose up -d
```

*Note: If you have an existing PostgreSQL database, you can update the `DATABASE_URL` value inside the `.env` file to point to it.*

### 2. Virtual Environment & Dependencies

If you haven't already activated the virtual environment and installed the dependencies:

```powershell
# Create venv (if not done already)
python -m venv venv

# Activate venv (Windows)
.\venv\Scripts\Activate.ps1

# Install requirements
pip install -r requirements.txt
```

### 3. Run FastAPI

Start the Uvicorn development server:

```bash
uvicorn app.main:app --reload
```

The application will automatically connect to the database and create the tables if they don't exist.

## API Documentation

Once the server is running, navigate to:
- Interactive Swagger UI Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc API Docs: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## CRUD Endpoints

The API includes the following endpoints under `/items/` for managing database entries:
- **`POST /items/`**: Create a new item.
- **`GET /items/`**: Retrieve a list of items (supports pagination query parameters `skip` and `limit`).
- **`GET /items/{item_id}`**: Retrieve a specific item by ID.
- **`PATCH /items/{item_id}`**: Update specific fields of an item.
- **`DELETE /items/{item_id}`**: Delete an item by ID.
