from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str
    is_done: bool = False

items = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/about")
async def about():
    return {"message": "About Page"}

@app.get("/items", response_model=list[Item])
async def list_items(limit: int = 10):
    return items[0:limit]

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int) -> Item:
    if item_id not in items:
        raise HTTPException(status_code=404, detail="suck an egg!!")
    return items[item_id]

@app.post("/items")
async def create_item(item: Item):
    items.append(item)
    return items

