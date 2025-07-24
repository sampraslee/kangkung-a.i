from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers import users, vegetables, materials, AItool
from app.core.database import create_db_and_tables

# This line is for development, it creates the tables if they don't exist.
# For production, you should use a migration tool like Alembic.
create_db_and_tables()

app = FastAPI(title="Kangkung AI API")

# Add CORS middleware
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",  # Make sure your Vue dev server port is here
    "http://127.0.0.1:5173",
    "*",  # The wildcard allows all origins
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)
# Include routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(vegetables.router, tags=["Vegetables & Progress"])
app.include_router(materials.router, prefix="/materials", tags=["Materials"])
app.include_router(AItool.router, prefix="/AItool", tags=["AI Tools"])


@app.get("/")
def read_root():
    return {"message": "Hello, this is the birth of Kangkung AI"}
