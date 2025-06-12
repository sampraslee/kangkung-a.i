# Tolong susah sngtt
# app/main.py or app/core/dependencies.py (for get_db dependency)
from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey, Text, create_engine, Interval
from sqlalchemy.dialects.postgresql import NUMRANGE
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from psycopg2.extras import NumericRange
# Import datetime for timestamp fields
from datetime import datetime, timedelta, date
# app/main.py (FastAPI app instance and middleware)
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
# app/schemas/book_schemas.py
from pydantic import BaseModel, Field
from typing import Optional, Tuple, List

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app/core/config.py (these variables should ideally come from environment variables)
# Database URL (adjust username/password as needed)
DB_USER = "postgres"
DB_PASSWORD = "ayam"
DB_HOST = "localhost"
DB_NAME = "kangkung_ai_db"
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"

# app/core/database.py
engine = create_engine(DATABASE_URL)
Base = declarative_base()
# In a real app, 'session' would be passed as a dependency for each request, not a global instance.
# This global 'session' is okay for a simple example but not scalable.
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    user_vegetable_progress = relationship(
        "UserVegetableProgress", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"


class Vegetable(Base):
    __tablename__ = "vegetables"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    estimated_harvest_time = Column(Interval, nullable=True)
    water_needs = Column(Interval, nullable=True)
    sunlight_needs = Column(NUMRANGE(), nullable=True)
    image_url = Column(String, nullable=True)
    instruction = Column(Text, nullable=True)
    user_vegetable_progress = relationship(
        "UserVegetableProgress", back_populates="vegetable"
    )

    def __repr__(self):
        return f"<Vegetable(id={self.id}, name='{self.name}')>"


class UserVegetableProgress(Base):
    __tablename__ = "user_vegetable_progress"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    vegetable_id = Column(Integer, ForeignKey("vegetables.id"), nullable=False)
    vegeNickname = Column(String, nullable=True)
    lastWatered = Column(DateTime, nullable=True)
    startDate = Column(DateTime, default=datetime.utcnow)
    lastFertilized = Column(DateTime, nullable=True)
    expectedHarvestDate = Column(Date, nullable=True)
    lastCheckup = Column(Date, nullable=True)
    checkUpNotes = Column(Text, nullable=True)
    user = relationship("User", back_populates="user_vegetable_progress")
    vegetable = relationship(
        "Vegetable", back_populates="user_vegetable_progress")

    def __repr__(self):
        return (
            f"<UserVegetableProgress(id={self.id}, user_id={self.user_id}, "
            f"vegetable_id={self.vegetable_id}, nickname='{self.vegeNickname}')>"
        )


Base.metadata.create_all(engine)


class VegetableModel(BaseModel):
    name: str = Field(..., example="Kangkung")  # `...` means required
    estimated_harvest_time: Optional[timedelta] = Field(None, example="P6W")
    water_needs: Optional[timedelta] = Field(None, example="P2D")
    sunlight_needs: Optional[Tuple[Optional[int],
                                   Optional[int]]] = Field(None, example=(6, 8))
    image_url: Optional[str] = Field(
        None, example="http://example.com/kangkung.jpg")
    instruction: Optional[str] = Field(
        None, example="Plant in fertile soil, water regularly.")


class UserModel(BaseModel):
    username: str = Field(..., example="Aina")  # `...` means required


class UserVegetableProgressModel(BaseModel):
    user_id: int = Field(..., example=1)
    vegetable_id: int = Field(..., example=1)
    vegeNickname: Optional[str] = Field(None, example="My Special Kangkung")
    lastWatered: Optional[datetime] = Field(
        None, example="2024-06-09T10:00:00")
    startDate: Optional[datetime] = Field(
        None, example="2024-06-01T12:00:00")  # Has default in DB model
    lastFertilized: Optional[datetime] = Field(
        None, example="2024-06-05T15:00:00")
    expectedHarvestDate: Optional[date] = Field(None, example="2024-07-15")
    lastCheckup: Optional[date] = Field(None, example="2024-06-08")
    checkUpNotes: Optional[str] = Field(
        None, example="Plant looks healthy, new leaves growing.")


@app.get("/")
def read_root():
    return {"message": "Hello this is the birth of kangkung AI"}


@app.post("/user-add")
def add_user(user_data: UserModel):
    try:
        new_user = User(
            username=user_data.username,
        )
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user
    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=500, detail=f"Error creating user: {str(e)}"
        )


@app.get("/user-get-all")
def list_user():
    try:
        users = session.query(User).order_by(
            User.id.desc()).all()
        return users
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error getting users: {str(e)}"
        )


@app.post("/vegetable-add")
def add_vegetable(vegetable_data: VegetableModel):
    try:
        sunlight_range = None
        if vegetable_data.sunlight_needs:
            lower, upper = vegetable_data.sunlight_needs
            # '[]' indicates an inclusive range
            sunlight_range = NumericRange(lower, upper, '[]')

        new_vegetable = Vegetable(
            name=vegetable_data.name,
            estimated_harvest_time=vegetable_data.estimated_harvest_time,
            water_needs=vegetable_data.water_needs,
            sunlight_needs=sunlight_range,  # Assign the NumericRange object here
            image_url=vegetable_data.image_url,
            instruction=vegetable_data.instruction
        )
        session.add(new_vegetable)
        session.commit()
        session.refresh(new_vegetable)

        return new_vegetable

    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=500, detail=f"Error creating vegetable: {str(e)}"
        )


@app.get("/vegetable-get-all")
def list_vegetable():
    try:
        vegetables = session.query(Vegetable).order_by(
            Vegetable.id.desc()).all()
        return vegetables
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error getting vegetables: {str(e)}"
        )


@app.get("/vegetable-get/{vegetable_id}")
def get_vegetable(vegetable_id: int):
    try:
        vegetable = session.query(Vegetable).filter_by(
            id=vegetable_id).order_by(Vegetable.id.desc()).first()
        if not vegetable:
            raise HTTPException(status_code=404, detail="Vegetable not found")
        return vegetable
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error getting vegetable: {str(e)}")

# USER_VEGETABLE_PROGRESS##########################################3


@app.get("/user-vegetable-get-all/{user_id}", response_model=List[UserVegetableProgressModel])
def get_user_vegetable_progress_entries(user_id: int):
    """
    Retrieves all User Vegetable Progress entries for a specific user.
    """
    try:
        user_progress_entries = session.query(UserVegetableProgress).filter(
            UserVegetableProgress.user_id == user_id
        ).all()

        if not user_progress_entries:
            return []

        return user_progress_entries
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error retrieving user vegetable progress: {str(e)}"
        )


@app.post("/user-vegetable-add/")
def create_user_vegetable_progress_entry(progress_input: UserVegetableProgressModel):
    """
    Creates a new User Vegetable Progress entry.
    - `expectedHarvestDate` is automatically calculated if `estimated_harvest_time`
      is available for the selected vegetable.
    - `startDate` is automatically set to current UTC if not provided.
    """

    # 1. Validate user_id and vegetable_id and fetch vegetable details
    user = session.query(User).filter(
        User.id == progress_input.user_id).first()
    if not user:
        raise HTTPException(
            status_code=500, detail=f"Error getting users: {str(e)}"
        )

    vegetable = session.query(Vegetable).filter(
        Vegetable.id == progress_input.vegetable_id).first()
    if not vegetable:
        raise HTTPException(
            status_code=500, detail=f"Error getting vegetable: {str(e)}"
        )

    # 2. Calculate expectedHarvestDate based on current date + estimated_harvest_time
    calculated_expected_harvest_date: Optional[date] = None
    current_date = datetime.utcnow().date()

    if vegetable.estimated_harvest_time is not None:
        calculated_expected_harvest_date = current_date + vegetable.estimated_harvest_time
    else:
        print(
            f"WARNING: Vegetable ID {vegetable.id} ({vegetable.name}) has no estimated_harvest_time. expectedHarvestDate will be None.")
        calculated_expected_harvest_date = None

    # 3. Create the SQLAlchemy model instance
    session_progress = UserVegetableProgress(
        user_id=progress_input.user_id,
        vegetable_id=progress_input.vegetable_id,
        vegeNickname=progress_input.vegeNickname,
        lastWatered=progress_input.lastWatered,
        startDate=progress_input.startDate,  # If None, DB default will apply
        lastFertilized=progress_input.lastFertilized,
        expectedHarvestDate=calculated_expected_harvest_date,  # Use the calculated date
        lastCheckup=progress_input.lastCheckup,
        checkUpNotes=progress_input.checkUpNotes
    )

    # 4. Add to session, commit, and refresh to get the ID
    try:
        session.add(session_progress)
        session.commit()
        session.refresh(session_progress)  # This populates the ID
    except Exception as e:
        session.rollback()  # Rollback on error
        raise HTTPException(
            status_code=500, detail=f"Error getting users Progress: {str(e)}"
        )

    return session_progress
