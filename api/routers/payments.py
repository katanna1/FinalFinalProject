from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import payments as controller
from ..schemas import payments as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=["Payments"],
    prefix="/payments"
)


@router.post("/", response_model=schema.Payment)
def create_payment(request: schema.PaymentCreate, db: Session = Depends(get_db)):
    return controller.create_payment(db, request)


@router.get("/", response_model=list[schema.Payment])
def read_all_payments(db: Session = Depends(get_db)):
    return controller.read_all_payments(db)


@router.get("/{payment_id}", response_model=schema.Payment)
def read_payment(payment_id: int, db: Session = Depends(get_db)):
    return controller.read_payment(db, payment_id)


@router.put("/{payment_id}", response_model=schema.Payment)
def update_payment(payment_id: int, request: schema.PaymentUpdate, db: Session = Depends(get_db)):
    return controller.update_payment(db, payment_id, request)


@router.delete("/{payment_id}")
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    return controller.delete_payment(db, payment_id)
