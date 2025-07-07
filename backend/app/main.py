from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers import users, vegetables, materials
from app.core.database import create_db_and_tables

# This line is for development, it creates the tables if they don't exist.
# For production, you should use a migration tool like Alembic.
create_db_and_tables()

app = FastAPI(title="Kangkung AI API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(vegetables.router, tags=["Vegetables & Progress"])
app.include_router(materials.router, prefix="/materials", tags=["Materials"])


@app.get("/")
def read_root():
    return {"message": "Hello, this is the birth of Kangkung AI"}
