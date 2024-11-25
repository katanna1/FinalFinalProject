from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .sandwiches import Sandwich

class ReviewBase(BaseModel):
    review_text: Optional[str] = None
    score: int


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    review_text: Optional[str] = None
    score: Optional[int] = None


class Review(ReviewBase):
    id: int
    sandwich_id: int

    class ConfigDict:
        from_attributes = True
