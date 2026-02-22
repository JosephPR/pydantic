from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

# ==========================================
# SQLModel Database Tables
# ==========================================
# SQLModel combines SQLAlchemy (for databases) and Pydantic (for data validation).
# By adding `table=True`, we tell SQLModel that this class isn't just a data validator,
# it is an actual Table in our SQLite database!

class Product(SQLModel, table=True):
    # Field(primary_key=True) tells the database this is the unique ID for the row.
    # Optional[int] means it can be None before it's saved, but the DB will auto-generate an integer.
    id: Optional[int] = Field(default=None, primary_key=True)
    item_name: str
    
    # index=True makes searching by SKU faster. unique=True means no two products can have the same SKU.
    sku: str = Field(index=True, unique=True)
    price: float
    stock: int
    image_url: str

class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    # This is a custom mock order ID we generate, separate from the database's internal PK
    order_id: int = Field(index=True) 
    customer_name: str
    email: str
    price: float
    is_priority: bool = Field(default=False)
    
    # Relationships 🤝:
    # A single order can have multiple items. `back_populates` links this list to the 
    # `order` property in the OrderItem table below.
    items: List["OrderItem"] = Relationship(back_populates="order")

class OrderItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    
    # foreign_key links this specific item to a specific Order row by its ID
    order_id: int = Field(default=None, foreign_key="order.id")
    order: Optional[Order] = Relationship(back_populates="items")
    
    # We store the item details here. Why not just a relationship to Product?
    # Because if a product's price changes *tomorrow*, we don't want it to change 
    # the receipt of the order from *yesterday*.
    item_name: str
    sku: str
    quantity: int
