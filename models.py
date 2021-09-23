from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    name: str
    price: float
    is_deleted: Optional[bool] = None
