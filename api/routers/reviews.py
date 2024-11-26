from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import reviews as controller
from ..schemas import reviews as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=["Reviews"],
    prefix="/reviews"
)


@router.post("/", response_model=schema.Review)
def create_review(request: schema.ReviewCreate, db: Session = Depends(get_db)):
    return controller.create_review(db, request)


@router.get("/", response_model=list[schema.Review])
def read_all_reviews(db: Session = Depends(get_db)):
    return controller.read_all_reviews(db)


@router.get("/{review_id}", response_model=schema.Review)
def read_review(review_id: int, db: Session = Depends(get_db)):
    return controller.read_review(db, review_id)


@router.put("/{review_id}", response_model=schema.Review)
def update_review(review_id: int, request: schema.ReviewUpdate, db: Session = Depends(get_db)):
    return controller.update_review(db, review_id, request)


@router.delete("/{review_id}")
def delete_review(review_id: int, db: Session = Depends(get_db)):
    return controller.delete_review(db, review_id)
