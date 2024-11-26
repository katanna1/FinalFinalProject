# routers/promotions.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import promotions as controller
from ..schemas import promotions as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=["Promotions"],
    prefix="/promotions"
)


@router.post("/", response_model=schema.Promotion)
def create_promotion(request: schema.PromotionCreate, db: Session = Depends(get_db)):
    return controller.create_promotion(db, request)


@router.get("/", response_model=list[schema.Promotion])
def read_all_promotions(db: Session = Depends(get_db)):
    return controller.read_all_promotions(db)


@router.get("/{promotion_id}", response_model=schema.Promotion)
def read_promotion(promotion_id: int, db: Session = Depends(get_db)):
    return controller.read_promotion(db, promotion_id)


@router.put("/{promotion_id}", response_model=schema.Promotion)
def update_promotion(promotion_id: int, request: schema.PromotionUpdate, db: Session = Depends(get_db)):
    return controller.update_promotion(db, promotion_id, request)


@router.delete("/{promotion_id}")
def delete_promotion(promotion_id: int, db: Session = Depends(get_db)):
    return controller.delete_promotion(db, promotion_id)
