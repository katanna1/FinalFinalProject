from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .sandwiches import Sandwich

class PaymentBase(BaseModel):
    card_info: str
    transaction_status: str
    payment_type: str


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    card_info: Optional[str] = None
    transaction_status: Optional[str] = None
    payment_type: Optional[str] = None


class Payment(PaymentBase):
    id: int
    order_id: int

    class ConfigDict:
        from_attributes = True
