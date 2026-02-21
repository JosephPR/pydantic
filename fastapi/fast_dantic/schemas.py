from typing import List
from pydantic import BaseModel, EmailStr, Field, field_validator


# This is where all your Pydantic schemas go in a real API.
# It keeps them separated from the actual routing logic.
class Product(BaseModel):
    item_name: str
    sku: str
    quantity: int


class CustomerOrder(BaseModel):
    order_id: int
    customer_name: str
    email: EmailStr
    price: float = Field(gt=0, description="Price must be strictly greater than 0")
    is_priority: bool = False
    items: List[Product]
    
# Note: Although your price field already has Field(gt=0)
# which theoretically prevents it from being zero or negative,
# keeping the custom validator is still a great way to learn
# how manual control works in Pydantic!
    @field_validator('price')
    @classmethod
    def price_not_negative(cls, value: float) -> float:
        if value < 0:
            raise ValueError("Total price cannot be a negative number")
        return value
# We can also add schemas for the responses we send back!
class OrderProcessSummary(BaseModel):
    message: str
    total_revenue: float
    priority_orders: int
