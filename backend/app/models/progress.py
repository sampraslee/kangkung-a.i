from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime


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
    vegetable = relationship("Vegetable", back_populates="user_vegetable_progress")

    def __repr__(self):
        return (
            f"<UserVegetableProgress(id={self.id}, user_id={self.user_id}, "
            f"vegetable_id={self.vegetable_id}, nickname='{self.vegeNickname}')>"
        )
