from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail


class OrderBase(BaseModel):
    order_date: datetime
    tracking_number: Optional[str] = None
    order_status: str
    total_price: float


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    order_date: Optional[datetime] = None
    tracking_number: Optional[str] = None
    order_status: Optional[str] = None
    total_price: Optional[float] = None


class Order(OrderBase):
    id: int
    customer_id: int

    class ConfigDict:
        from_attributes = True