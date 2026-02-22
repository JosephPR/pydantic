from typing import List
from pydantic import BaseModel, EmailStr, Field, field_validator

# ==========================================
# Pydantic Schemas (Data Validation)
# ==========================================
# This is where all your Pydantic schemas go in a real API.
# It keeps them separated from the actual routing logic and the database models.
# Schemas are purely for VALIDATING the data coming in from the user and going out to the user.

class Product(BaseModel):
    item_name: str
    sku: str
    quantity: int


class CustomerOrder(BaseModel):
    order_id: int
    customer_name: str
    
    # EmailStr automatically validates that the string contains a valid email format (@ and .)
    email: EmailStr
    
    # Field() allows us to add strict validation rules. 
    # gt=0 means "greater than zero". If a user tries to submit an order with a price of -5, 
    # FastAPI will automatically block the request and return a 422 Unprocessable Entity error.
    price: float = Field(gt=0, description="Price must be strictly greater than 0")
    
    # Default values mean the user doesn't have to provide this in their JSON payload
    is_priority: bool = False
    
    # This expects a list of dictionaries that match the `Product` schema above
    items: List[Product]
    
    # Note: Although your price field already has Field(gt=0)
    # which theoretically prevents it from being zero or negative,
    # keeping the custom validator is still a great way to learn
    # how manual control works in Pydantic!
    @field_validator('price')
    @classmethod
    def price_not_negative(cls, value: float) -> float:
        """
        A custom validator function.
        This runs automatically whenever a new CustomerOrder is instantiated or received by the API.
        """
        if value < 0:
            raise ValueError("Total price cannot be a negative number")
        return value

# We can also add schemas for the responses we send back!
# This is great for documentation (Swagger UI) and ensures we don't accidentally leak sensitive data.
class OrderProcessSummary(BaseModel):
    message: str
    total_revenue: float
    priority_orders: int
