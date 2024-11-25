from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    ingredients = Column(String(255), nullable=False)
    price = Column(DECIMAL, nullable=False)
    calories = Column(Integer, nullable=True)
    food_category = Column(String(50), nullable=True)