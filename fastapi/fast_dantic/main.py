from fastapi import FastAPI
from typing import List

# We import the schemas from our dedicated models file
from app.schemas import CustomerOrder, OrderProcessSummary


app = FastAPI(title="Real-World Order Processor API")

# Notice how we also define the type of the data we are returning using response_model!
# This makes FastAPI validate the data WE send out, not just the data coming in.
@app.post("/api/v1/process-orders/", response_model=OrderProcessSummary)
def process_multiple_orders(orders: List[CustomerOrder]):
    # In a real app, you might do things here like:
    # 1. Save valid orders to a database
    # 2. Send emails
    # 3. Calculate metrics
    
    total_revenue = sum(order.price for order in orders)
    priority_count = sum(1 for order in orders if order.is_priority)
    
    # We return a dictionary that matches the OrderProcessSummary schema.
    # FastAPI will validate it before sending it.
    return {
        "message": f"Successfully processed {len(orders)} clean orders.",
        "total_revenue": total_revenue,
        "priority_orders": priority_count
    }

    # 2. Create a POST endpoint
# Notice how we use `order: CustomerOrder`. This tells FastAPI to strictly enforce the schema.
@app.post("/clean-order")
async def clean_single_order(order: CustomerOrder):
    # If the code execution reaches this line, FastAPI has ALREADY validated the data!
    # It automatically coerces strings to ints/floats just like your script did.
    return {
        "status": "success",
        "message": f"Order {order.order_id} for {order.customer_name} is perfectly structured.",
        "clean_data": order
    }

# 3. Create a batch endpoint to handle lists of data
@app.post("/clean-batch")
async def clean_order_batch(orders: List[CustomerOrder]):
    return {
        "status": "success",
        "message": f"Successfully validated and cleaned {len(orders)} orders!",
        "clean_data": orders
    }
