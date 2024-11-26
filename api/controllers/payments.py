from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models.payments import Payment as PaymentModel
from ..schemas.payments import PaymentCreate, PaymentUpdate


def create_payment(db: Session, request: PaymentCreate):
    new_payment = PaymentModel(**request.dict())
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return new_payment


def read_all_payments(db: Session):
    return db.query(PaymentModel).all()


def read_payment(db: Session, payment_id: int):
    payment = db.query(PaymentModel).filter(PaymentModel.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found!")
    return payment


def update_payment(db: Session, payment_id: int, request: PaymentUpdate):
    payment = db.query(PaymentModel).filter(PaymentModel.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found!")
    for key, value in request.dict(exclude_unset=True).items():
        setattr(payment, key, value)
    db.commit()
    db.refresh(payment)
    return payment


def delete_payment(db: Session, payment_id: int):
    payment = db.query(PaymentModel).filter(PaymentModel.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found!")
    db.delete(payment)
    db.commit()
    return payment
