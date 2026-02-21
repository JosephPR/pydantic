from pydantic import BaseModel, EmailStr, Field


# This is where all your Pydantic schemas go in a real API.
# It keeps them separated from the actual routing logic.
class CustomerOrder(BaseModel):
    order_id: int
    customer_name: str
    email: EmailStr
    price: float = Field(gt=0, description="Price must be strictly greater than 0")
    is_priority: bool = False

# We can also add schemas for the responses we send back!
class OrderProcessSummary(BaseModel):
    message: str
    total_revenue: float
    priority_orders: int
