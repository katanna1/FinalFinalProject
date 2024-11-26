from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models.reviews import Review as ReviewModel
from ..schemas.reviews import ReviewCreate, ReviewUpdate


def create_review(db: Session, request: ReviewCreate):
    new_review = ReviewModel(**request.dict())
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review


def read_all_reviews(db: Session):
    return db.query(ReviewModel).all()


def read_review(db: Session, review_id: int):
    review = db.query(ReviewModel).filter(ReviewModel.id == review_id).first()
    if not review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found!")
    return review


def update_review(db: Session, review_id: int, request: ReviewUpdate):
    review = db.query(ReviewModel).filter(ReviewModel.id == review_id).first()
    if not review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found!")
    for key, value in request.dict(exclude_unset=True).items():
        setattr(review, key, value)
    db.commit()
    db.refresh(review)
    return review


def delete_review(db: Session, review_id: int):
    review = db.query(ReviewModel).filter(ReviewModel.id == review_id).first()
    if not review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found!")
    db.delete(review)
    db.commit()
    return review
