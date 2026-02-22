# logfire: A modern observability tool by the creators of Pydantic. It automatically tracks API requests and LLM calls.
import logfire

# asynccontextmanager: A Python utility that lets us run setup code *before* the server starts and teardown code *after* it stops.
from contextlib import asynccontextmanager

# FastAPI core tools. FastAPI is the web framework, Body lets us extract JSON from requests, and Depends handles dependency injection (like DB sessions).
from fastapi import FastAPI, Body, Depends

# CORSMiddleware: Tells the backend which frontends (like localhost:3000) are allowed to securely talk to it.
from fastapi.middleware.cors import CORSMiddleware

# List: Lets us strictly define Python arrays (e.g., List[Product]) for type hinting and validation.
from typing import List

# pydantic_ai.Agent: The core class that wraps LLMs (like GPT-4) and strictly enforces that their output matches our Pydantic schemas.
from pydantic_ai import Agent

# SQLModel components. Session represents an active connection to the database, select is used to write SQL queries in pure Python.
from sqlmodel import Session, select

# Local imports
from database import engine, get_session, create_db_and_tables
from models import Product, Order, OrderItem
from schemas import CustomerOrder, OrderProcessSummary
from dummy_data import fake_products_db

# ==========================================
# FastAPI Application & Lifespan
# ==========================================
# The strict order of startup/shutdown operations for the server
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Setup the DB tables (creates them if they don't exist yet)
    create_db_and_tables()
    
    # Seed the mock products for our storefront if the database is currently empty
    with Session(engine) as session:
        existing_products = session.exec(select(Product)).first()
        if not existing_products:
            for p in fake_products_db:
                # `**p` unpacks the dictionary into keyword arguments to instantiate the Product
                db_product = Product(**p)
                session.add(db_product)
            session.commit()
            print("Database seeded with mock B2B enterprise AI agents!")
            
    yield
    # Any shutdown logic would go here, after the 'yield'

app = FastAPI(title="Real-World Order Processor API", lifespan=lifespan)

# Configure Logfire for full stack observability
# This gives you an amazing dashboard to see all incoming requests and LLM traces
logfire.configure()
logfire.instrument_fastapi(app)
logfire.instrument_pydantic()

# Configure CORS so the Next.js frontend can communicate with this API
origins = [
    "http://localhost:3000",
    "http://localhost:3001" 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================
# API Routes
# ==========================================
# Each function decorated with @app.get, @app.post, etc. becomes an API endpoint.

@app.get("/products")
async def get_products(session: Session = Depends(get_session)):
    """
    Retrieve all available products from the database for the frontend storefront grid.
    
    The pattern `session: Session = Depends(get_session)` is called Dependency Injection.
    FastAPI will automatically call `get_session()`, open a database connection, pass it in 
    as the `session` argument, and handle closing it when the router returns!
    """
    products = session.exec(select(Product)).all()
    return products

@app.get("/orders")
async def get_orders(session: Session = Depends(get_session)):
    """
    Retrieve all orders from the database.
    Useful for an admin dashboard to see all successfully processed sales.
    """
    orders = session.exec(select(Order)).all()
    return orders

# Notice how we also define the type of the data we are returning using response_model!
# This makes FastAPI validate the data WE send out, not just the data coming in.
@app.post("/process-orders/", response_model=OrderProcessSummary)
def process_multiple_orders(orders: List[CustomerOrder], session: Session = Depends(get_session)):
    """
    Process an array of multiple orders at once.
    FastAPI expects the JSON body payload to be a List (Array) containing valid CustomerOrder objects.
    """
    # 1. Save valid orders to a database
    for order_data in orders:
        db_order = Order(
            order_id=order_data.order_id,
            customer_name=order_data.customer_name,
            email=order_data.email,
            price=order_data.price,
            is_priority=order_data.is_priority
        )
        session.add(db_order)
        session.commit()
        session.refresh(db_order)
        
        for item in order_data.items:
            db_item = OrderItem(
                order_id=db_order.id, # Map back to the primary key of the new Order row
                item_name=item.item_name,
                sku=item.sku,
                quantity=item.quantity
            )
            session.add(db_item)
        session.commit()
    
    # Calculate metrics
    total_revenue = sum(order.price for order in orders)
    priority_count = sum(1 for order in orders if order.is_priority)
    
    # We return a dictionary that matches the OrderProcessSummary schema.
    # FastAPI will validate it before sending it.
    return {
        "message": f"Successfully processed {len(orders)} clean orders.",
        "total_revenue": total_revenue,
        "priority_orders": priority_count
    }


# Notice how we use `order: CustomerOrder`. This tells FastAPI to strictly enforce the schema!
@app.post("/clean-order")
async def clean_single_order(order: CustomerOrder, session: Session = Depends(get_session)):
    """
    Process a single manual checkout order from the React frontend cart.
    """
    # If the code execution reaches this line, FastAPI has ALREADY validated the data!
    # It automatically coerced strings to ints/floats, checked email formats, etc.
    
    # Save the order parent to our database
    db_order = Order(
        order_id=order.order_id,
        customer_name=order.customer_name,
        email=order.email,
        price=order.price,
        is_priority=order.is_priority
    )
    session.add(db_order)
    session.commit()
    session.refresh(db_order) # Reload the object to grab its new auto-generated ID from SQLite
    
    # Save child line-items linking to the parent order
    for item in order.items:
        db_item = OrderItem(
            order_id=db_order.id,
            item_name=item.item_name,
            sku=item.sku,
            quantity=item.quantity
        )
        session.add(db_item)
    session.commit()
    
    return {
        "status": "success",
        "message": f"Order {order.order_id} for {order.customer_name} is perfectly structured and saved to the database.",
        "clean_data": order # We return the exact parsed Pydantic schema data back to the frontend
    }


# ==========================================
# Pydantic AI Integration
# ==========================================
# Build a dynamic string of our product catalog for the AI so it knows current prices
catalog_prompt = "\n".join([f"- {p['item_name']} (SKU: {p['sku']}): ${p['price']} each" for p in fake_products_db])

# Initialize the Pydantic AI Agent.
# 'openai:gpt-4o' is the default model.
# By setting `output_type=CustomerOrder`, the agent is restricted to ONLY return perfectly formatted JSON
# matching that exact Pydantic schema.
order_agent = Agent(
    'openai:gpt-4o',
    output_type=CustomerOrder,
    system_prompt=(
        "You are an order extraction assistant. Extract the customer's order details from the provided text into the structured format required.\n\n"
        "IMPORTANT PRICING RULES:\n"
        "You MUST calculate the `price` field strictly using the following product catalog for all items ordered:\n"
        f"{catalog_prompt}\n\n"
        "If the customer doesn't specify an ID, name, or email, use a random integer order_id, 'Guest User' for customer_name, and 'guest@example.com' for email."
    )
)

@app.post("/extract-order", response_model=CustomerOrder)
async def extract_order(order_text: str = Body(..., embed=True)):
    """
    Uses Pydantic AI to turn natural language ("I'll take 3 routers") into a structured CustomerOrder JSON.
    The frontend calls this magic box, gets the JSON back, and immediately posts it to /clean-order.
    """
    # Run the agent asynchronously to pass the raw text to the LLM
    result = await order_agent.run(order_text)
    
    # Return the perfectly structured data from the agent run!
    return result.output
