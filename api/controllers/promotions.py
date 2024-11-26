from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models.promotions import Promotion as PromotionModel
from ..schemas.promotions import PromotionCreate, PromotionUpdate


def create_promotion(db: Session, request: PromotionCreate):
    new_promotion = PromotionModel(**request.dict())
    db.add(new_promotion)
    db.commit()
    db.refresh(new_promotion)
    return new_promotion


def read_all_promotions(db: Session):
    return db.query(PromotionModel).all()


def read_promotion(db: Session, promotion_id: int):
    promotion = db.query(PromotionModel).filter(PromotionModel.id == promotion_id).first()
    if not promotion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found!")
    return promotion


def update_promotion(db: Session, promotion_id: int, request: PromotionUpdate):
    promotion = db.query(PromotionModel).filter(PromotionModel.id == promotion_id).first()
    if not promotion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found!")
    for key, value in request.dict(exclude_unset=True).items():
        setattr(promotion, key, value)
    db.commit()
    db.refresh(promotion)
    return promotion


def delete_promotion(db: Session, promotion_id: int):
    promotion = db.query(PromotionModel).filter(PromotionModel.id == promotion_id).first()
    if not promotion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found!")
    db.delete(promotion)
    db.commit()
    return promotion
