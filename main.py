from typing import Optional
from fastapi import FastAPI
import models

app = FastAPI()

items = []

@app.get("/")
def read_root():
    return {"message": "Hello this is root directory!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: models.Item):
    items.append(item)
    return {"item_name": item.name, "item_id": item_id}


@app.get("/items/find-all/")
def get_item():
    return items
