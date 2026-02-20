from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, ValidationError, field_validator


# --- 1. Basic Model ---
# Pydantic models inherit from `BaseModel`. 
# Type hints (int, str, bool) define the schema and are strictly enforced.
class User(BaseModel):
    id: int                     # Required field (no default value)
    username: str               # Required field
    email: str                  # Required field
    is_active: bool = True      # Optional field (has a default value)
    tags: List[str] = []        # Optional list with a default empty list


# --- 2. Advanced Validation using `Field` ---
# `Field` allows you to add constraints, descriptions, and extra metadata.
class Product(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    price: float = Field(gt=0, description="Price must be strictly greater than 0")
    stock: int = Field(default=0, ge=0)  # ge=0 means Greater than or Equal to 0


# --- 3. Custom Validators ---
# You can define custom logic that runs when a field is set.
class Account(BaseModel):
    username: str
    signup_date: Optional[datetime] = None

    @field_validator('username')
    @classmethod
    def username_must_be_alphanumeric(cls, value: str) -> str:
        if not value.isalnum():
            raise ValueError('Username must be alphanumeric (letters and numbers only)')
        return value


# --- 4. Nested Models ---
# You can use Pydantic models as types inside other models.
class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class Employee(BaseModel):
    name: str
    # Here we nest the Address model
    address: Address


# --- 5. Model Configuration (`ConfigDict`) ---
# `ConfigDict` allows you to change the behavior of the model itself.
from pydantic import ConfigDict

class Settings(BaseModel):
    # This configuration tells Pydantic to strictly forbid any extra fields
    # passed during instantiation that aren't defined in the model.
    model_config = ConfigDict(extra='forbid')
    
    app_name: str
    debug_mode: bool


# --- 6. Computed Fields ---
# Sometimes you want a field that is calculated from other fields,
# but you still want it to be included when you dump the model to a dictionary/JSON.
from pydantic import computed_field

class Rectangle(BaseModel):
    width: float
    height: float

    # The @computed_field decorator makes this property act like a regular field
    @computed_field
    def area(self) -> float:
        return self.width * self.height


def run_tutorial():
    print("=== 1. Basic Model Creation ===")
    # Pydantic automatically parses types if it can (e.g., if you passed id="1", it becomes int 1)
    user1 = User(id=1, username="john_doe", email="john@example.com")
    
    # model_dump() converts the model instance into a standard Python dictionary
    print("Success! Created User:", user1.model_dump())
    print(f"Is user active? {user1.is_active}\n")


    print("=== 2. Handling Validation Errors ===")
    try:
        # This will fail because 'abc' cannot be converted to an integer
        bad_user = User(id="abc", username="jane", email="jane@example.com")
    except ValidationError as e:
        print("Caught a ValidationError!")
        # Errors are detailed and tell you exactly what went wrong and where
        print(e.json(indent=2))
    print()


    print("=== 3. Working with Field Constraints ===")
    try:
        # This will fail two constraints: name is too short, price is negative
        bad_product = Product(name="Tv", price=-5.0)
    except ValidationError as e:
        print("Product Validation Errors:")
        for err in e.errors():
            print(f" - Field '{err['loc'][0]}': {err['msg']}")
    print()


    print("=== 4. Custom Validators in Action ===")
    try:
        # Fails the custom `@field_validator` we wrote
        Account(username="invalid username!")
    except ValidationError as e:
        print("Account Validation Error:")
        print(f" - {e.errors()[0]['msg']}")
    print()


    print("=== 5. JSON Parsing (Deserialization) ===")
    # You can easily load data directly from JSON strings
    json_data = '{"id": 2, "username": "alice", "email": "alice@examples.com", "is_active": false}'
    
    # model_validate_json safely parses the JSON text and validates it against the User schema
    parsed_user = User.model_validate_json(json_data)
    print("Parsed from JSON successfully:")
    print(repr(parsed_user))
    print()


    print("=== 6. Nested Models ===")
    emp = Employee(
        name="Bob",
        # We pass a dictionary for the nested model, and Pydantic converts it to an Address object
        address={"street": "123 Main St", "city": "Anytown", "zip_code": "12345"}
    )
    print("Created Employee with nested Address:")
    print(emp.model_dump())
    print(f"Employee lives in: {emp.address.city}\n")


    print("=== 7. Model Configuration (Extra Fields) ===")
    try:
        # Fails because 'version' is not a defined field in the Settings model,
        # and we set `extra='forbid'` in its ConfigDict.
        Settings(app_name="MyApp", debug_mode=True, version="1.0")
    except ValidationError as e:
        print("Settings Validation Error for Extra Fields:")
        print(f" - {e.errors()[0]['msg']}")
    print()


    print("=== 8. Computed Fields ===")
    rect = Rectangle(width=5.0, height=10.0)
    print("Rectangle Data (Notice 'area' is included!):")
    # model_dump() automatically includes computed fields
    print(rect.model_dump())


if __name__ == "__main__":
    # If you run this script directly, it will execute the tutorial.
    run_tutorial()
