import json
import os
from pydantic import BaseModel, EmailStr, ValidationError, Field


# This is your strict data contract
class CustomerOrder(BaseModel):
    order_id: int
    customer_name: str
    email: EmailStr  # Pydantic has built-in email validation
    
    # We can add a Field constraint to ensure price is positive
    price: float = Field(gt=0, description="Price must be strictly greater than 0")
    
    is_priority: bool = False  # If missing, it defaults to False


def validate_orders(filepath: str):
    """Reads a JSON file of orders and validates each one."""
    print(f"Loading orders from: {filepath}\n")
    
    try:
        with open(filepath, 'r') as file:
            orders_data = json.load(file)
    except FileNotFoundError:
        print(f"Error: Could not find file {filepath}")
        return
        
    valid_orders = []
    invalid_orders = []

    # Loop through the raw dictionary data
    for raw_order in orders_data:
        try:
            # We use **raw_order to unpack the dictionary into keyword arguments
            # e.g., CustomerOrder(order_id=101, customer_name="Alice...")
            validated_order = CustomerOrder(**raw_order)
            
            # If we get here, the data was valid!
            valid_orders.append(validated_order)
            
            print(f"✅ {raw_order['order_id']} SUCCESS:")
            # Printing the repr() shows how Pydantic coerced the data (e.g., string "102" -> int 102)
            print(f"   Input: {raw_order}")
            print(f"   Clean: {repr(validated_order)}\n")
            
        except ValidationError as e:
            # If validation fails, Pydantic raises this exception
            invalid_orders.append((raw_order, e))
            
            print(f"❌ {raw_order['order_id']} FAILED:")
            print(f"    Input: {raw_order}")
            print("   Errors:")
            # e.errors() returns a list of dictionaries detailing every error found
            for error in e.errors():
                field_name = error['loc'][0]
                error_msg = error['msg']
                print(f"      - Field '{field_name}': {error_msg}")
            print()

    print("-" * 40)
    print(f"Validation Complete: {len(valid_orders)} valid, {len(invalid_orders)} invalid.")


if __name__ == "__main__":
    # Get the absolute path to the json file, assuming it's in the same directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, "messy_orders.json")
    
    validate_orders(json_path)
