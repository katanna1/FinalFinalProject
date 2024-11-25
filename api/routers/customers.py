from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import customers as controller
from ..schemas import customers as schema
from ..dependencies.database import get_db


router = APIRouter(
    tags=['Customers'],
    prefix="/customers"
)

@router.post("/", response_model=schema.Customer)
def create_customer(request: schema.CustomerCreate, db: Session = Depends(get_db)):
    return controller.create_customer(db=db, request=request)


@router.get("/", response_model=list[schema.Customer])
def read_all_customers(db: Session = Depends(get_db)):
    return controller.read_all_customers(db)


@router.get("/{customer_id}", response_model=schema.Customer)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    return controller.read_customer(db, customer_id=customer_id)


@router.put("/{customer_id}", response_model=schema.Customer)
def update_customer(customer_id: int, request: schema.CustomerUpdate, db: Session = Depends(get_db)):
    return controller.update_customer(db=db, request=request, customer_id=customer_id)


@router.delete("/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    return controller.delete_customer(db=db, customer_id=customer_id)