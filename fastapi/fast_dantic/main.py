from fastapi import FastAPI, Body
from typing import List
from pydantic_ai import Agent

# We import the schemas from our dedicated models file
# Note: adjusted import path to match the current directory structure
from schemas import CustomerOrder, OrderProcessSummary

app = FastAPI(title="Real-World Order Processor API")

# A simple in-memory "database" to store our orders
fake_orders_db: List[CustomerOrder] = []

@app.get("/orders", response_model=List[CustomerOrder])
async def get_orders():
    """
    Retrieve all orders from our in-memory database.
    """
    return fake_orders_db

# Notice how we also define the type of the data we are returning using response_model!
# This makes FastAPI validate the data WE send out, not just the data coming in.
@app.post("/process-orders/", response_model=OrderProcessSummary)
def process_multiple_orders(orders: List[CustomerOrder]):
    # In a real app, you might do things here like:
    # 1. Save valid orders to a database
    fake_orders_db.extend(orders)
    
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
    
    # Save the order to our fake database so we can retrieve it with our GET route
    fake_orders_db.append(order)
    
    return {
        "status": "success",
        "message": f"Order {order.order_id} for {order.customer_name} is perfectly structured and saved.",
        "clean_data": order
    }

# 3. Create a batch endpoint to handle lists of data
@app.post("/clean-batch")
async def clean_order_batch(orders: List[CustomerOrder]):
    fake_orders_db.extend(orders)
    return {
        "status": "success",
        "message": f"Successfully validated and cleaned {len(orders)} orders!",
        "clean_data": orders
    }

# 4. Create an endpoint that uses Pydantic AI to extract orders from raw text
# Initialize the Pydantic AI Agent.
# 'openai:gpt-4o' is the default model; the agent will return data matching the CustomerOrder schema.
order_agent = Agent(
    'openai:gpt-4o',
    output_type=CustomerOrder,
    system_prompt="You are an order extraction assistant. Extract the customer's order details from the provided text into the structured format required."
)

@app.post("/extract-order", response_model=CustomerOrder)
async def extract_order(order_text: str = Body(..., embed=True)):
    # Run the agent asynchronously to pass the raw text to the LLM
    result = await order_agent.run(order_text)
    fake_orders_db.append(result.output)
    # Return the structured data from the agent run.
    return result.output
