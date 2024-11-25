from sqlalchemy.orm import Session
from ..models.customers import Customer as CustomerModel
from ..schemas.customers import CustomerCreate, CustomerUpdate



def create_customer(db: Session, request: CustomerCreate):
    db_customer = CustomerModel(**request.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def read_all_customers(db: Session):
    return db.query(CustomerModel).all()

def read_customer(db: Session, customer_id: int):
    return db.query(CustomerModel).filter(CustomerModel.id == customer_id).first()

def update_customer(db: Session, request: CustomerUpdate, customer_id: int):
    db_customer = db.query(CustomerModel).filter(CustomerModel.id == customer_id).first()
    if not db_customer:
        return None
    for key, value in request.items():
        setattr(db_customer, key, value)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def delete_customer(db: Session, customer_id: int):
    db_customer = db.query(CustomerModel).filter(CustomerModel.id == customer_id).first()
    if db_customer:
        db.delete(db_customer)
        db.commit()
    return db_customer