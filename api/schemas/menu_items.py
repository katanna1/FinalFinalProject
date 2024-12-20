from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .sandwiches import Sandwich


class MenuItemBase(BaseModel):
    name: str
    ingredients: str
    price: float
    calories: Optional[int] = None
    food_category: Optional[str] = None


class MenuItemCreate(MenuItemBase):
    pass


class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    ingredients: Optional[str] = None
    price: Optional[float] = None
    calories: Optional[int] = None
    food_category: Optional[str] = None


class MenuItem(MenuItemBase):
    id: int

    class ConfigDict:
        from_attributes = True