from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    review_text = Column(String(255), nullable=True)
    score = Column(Integer, nullable=False)
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))

    sandwich = relationship("Sandwich", back_populates="reviews")